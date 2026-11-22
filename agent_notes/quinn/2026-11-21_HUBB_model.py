import math, json
P0=403.66; SH=53.1; DEBT=5120.2; CASH=334.5; NONOP=121.0; MIN=12.2
TAX=0.225; KD=0.0453; WACC0=0.0864
ND0=DEBT-CASH-NONOP+MIN   # net claims ex-leases (op lease in EBIT) 
Y=list(range(2027,2037))
SC={
 'Bull':dict(p=0.25,rev27=7850,g=[.11,.10,.09,.08,.07,.06,.05,.045,.04],m=[.230,.240,.248,.255,.255,.255,.255,.255,.255,.255],tm=.245,tgr=.030,ronic=.14,capex=.030),
 'Base':dict(p=0.45,rev27=7680,g=[.08,.07,.065,.06,.055,.05,.045,.04],m=[.230,.233,.235,.235,.235,.235,.235,.235,.235,.235],tm=.230,tgr=.030,ronic=.12,capex=.030),
 'Bear':dict(p=0.30,rev27=7250,g=[.00,.02,.04,.04,.035,.035,.03,.03,.03],m=[.215,.200,.200,.205,.210,.212,.214,.215,.215,.215],tm=.215,tgr=.025,ronic=.095,capex=.028),
}
# base g list length fix: 9 entries
SC['Base']['g']=[.08,.07,.065,.06,.055,.05,.045,.04,.04]
def run(s,wacc=WACC0,gshift=0.0,tm_override=None,tgr=None,full=False):
    rev=[s['rev27']]
    for g in s['g']: rev.append(rev[-1]*(1+g+gshift))
    prev=6920.0
    m=list(s['m']); tm=tm_override if tm_override is not None else s['tm']
    if tm_override is not None:  # glide last years to override
        m=[x+(tm-s['m'][-1])*min(1,(i)/9) for i,x in enumerate(m)]
    fc=[]; nopat=[]
    for i,r in enumerate(rev):
        e=r*m[i]*(1-TAX); nopat.append(e)
        dep=r*(0.023+0.0004*i); cx=r*s['capex']
        nwc=0.15*(r-prev); prev=r
        fc.append(e+dep-cx-nwc)
    tg=tgr if tgr is not None else s['tgr']
    nT1=rev[-1]*(1+tg)*tm*(1-TAX)
    tvf=nT1*(1-tg/s['ronic'])
    # FY26 stub Q4: 0.25*FY26 FCFF approx (rev 6920, margin .226)
    fy26=6920*.226*(1-TAX)+6920*.023-6920*.03-0.15*(6920-6593.7*1.0)
    stub=0.25*fy26
    t0=0.11  # Q4 stub timing mid ~0.11
    t=[0.61+i for i in range(10)]
    pv=stub/(1+wacc)**0.06+sum(f/(1+wacc)**tt for f,tt in zip(fc,t))
    tv=tvf/(wacc-tg); pvtv=tv/(1+wacc)**t[-1]
    ev=pv+pvtv
    eq=ev+NONOP+CASH-DEBT-MIN
    fv=eq/SH
    out=dict(fv=fv,ev=ev,tv_share=pvtv/ev,rev=rev,fc=fc,m=m,nopat=nopat)
    if full:
        # FV5 at end 2031: flows 2032-2036 (idx5..9), times 0.5..4.5 ; TV at 4.5
        tt=[0.5+i for i in range(5)]
        ev5=sum(fc[5+i]/(1+wacc)**tt[i] for i in range(5))+tv/(1+wacc)**4.5
        nd=ND0; div=SH*6.08; ints=[]
        # Q4'26 stub + 2027..2031
        flows=[stub]+fc[:5]
        for k,f in enumerate(flows):
            dd=div*(1.07**max(0,k))*(0.25 if k==0 else 1)
            intr=nd*KD*(1-TAX)*(0.25 if k==0 else 1)
            nd=nd-(f-intr-dd)
        eq5=ev5-nd
        out.update(ev5=ev5,nd5=nd,fv5=eq5/SH,eq5=eq5)
        ke=0.0995
        out['chk']=eq5/ (eq*(1+ke)**5.11)  # ratio (before dividends)
        out['irr_implied_rev_cagr']=(rev[-1]/6920)**(1/10)-1
        # implied ROIC increment
        out['inc_roic']= (nopat[-1]-nopat[0])/sum(max(0,0.0) for _ in [0]) if False else None
    return out
res={}
for k,s in SC.items():
    r=run(s,full=True); res[k]=r
    print(k,'FV %.2f EV %.0f TV%% %.1f FV5 %.2f nd5 %.0f chk %.3f revCAGR27-36 %.3f rev36 %.0f m36 %.3f'%(r['fv'],r['ev'],100*r['tv_share'],r['fv5'],r['nd5'],r['chk'],r['irr_implied_rev_cagr'],r['rev'][-1],r['m'][-1]))
    print('  FCFF',[round(x) for x in r['fc']])
pw=sum(SC[k]['p']*res[k]['fv'] for k in SC); pw5=sum(SC[k]['p']*res[k]['fv5'] for k in SC)
print('PW FV %.2f MOS %.1f%%  PW FV5 %.2f ER %.2f%%'%(pw,100*(pw/P0-1),pw5,100*((pw5/P0)**(1/5.11)-1)))
mos=(pw-P0)/pw; print('MOS (FV-P)/FV',mos)
# prob-weighted std
sd=math.sqrt(sum(SC[k]['p']*(res[k]['fv']-pw)**2 for k in SC)); print('sd',sd)
# no-growth floor
nop=1309.9*(1-TAX); ng=(nop/WACC0+NONOP+CASH-DEBT-MIN)/SH; print('no-growth FV',ng)
# sensitivity tables on Base
W=[0.0764,0.0814,0.0864,0.0914,0.0964]
G=[-.03,-.015,0,.015,.03]
print('WACC x growth shift (Base)')
for g in G: print(g,[round(run(SC['Base'],w,g)['fv'],0) for w in W])
TM=[.21,.22,.23,.24,.25]
print('WACC x terminal margin (Base)')
for t in TM: print(t,[round(run(SC['Base'],w,0,t)['fv'],0) for w in W])
# PW across matrix (all scenarios shift): PW FV vs WACC x gshift
print('PW matrix')
for g in G: print(g,[round(sum(SC[k]['p']*run(SC[k],w,g)['fv'] for k in SC),0) for w in W])
# stress WACC ~9.95
print('stress WACC 9.95 base/pw',run(SC['Base'],0.0995)['fv'],sum(SC[k]['p']*run(SC[k],0.0995)['fv'] for k in SC))
# reverse: implied gshift base to hit price
lo,hi=-0.1,0.05
for _ in range(60):
    mid=(lo+hi)/2
    if run(SC['Base'],WACC0,mid)['fv']>P0: hi=mid
    else: lo=mid
print('implied growth shift base',mid)
lo,hi=0.08,0.2
for _ in range(60):
    mid=(lo+hi)/2
    if run(SC['Base'],mid)['fv']>P0: lo=mid
    else: hi=mid
print('implied WACC base',mid)
lo,hi=0.08,0.3
for _ in range(60):
    mid=(lo+hi)/2
    if run(SC['Base'],WACC0,0,mid)['fv']>P0: hi=mid
    else: lo=mid
print('implied terminal margin base',mid)
lo,hi=0.0,0.03
for _ in range(60):
    mid=(lo+hi)/2
    if run(SC['Base'],WACC0,0,None,mid)['fv']>P0: hi=mid
    else: lo=mid
print('implied TGR base',mid)
# TGR & RONIC single-var for 1.6 table
for tg in (0.025,0.035): print('tgr',tg,run(SC['Base'],tgr=tg)['fv'])
print('Method A WACC 7.84',run(SC['Base'],0.0784)['fv'],'B 9.44',run(SC['Base'],0.0944)['fv'])
b=SC['Base'];import copy
for r in (0.10,0.15):
    c=copy.deepcopy(b);c['ronic']=r;print('ronic',r,run(c)['fv'])
# implied multiples of base FV
print('implied P/E27 on base FV',res['Base']['fv']/23.07, 'PW',pw/23.07)
# base revenue/ margin check, implied incremental ROIC
r=res['Base']; print([round(x) for x in r['rev']]); print([round(x,3) for x in r['m']]); print([round(x) for x in r['nopat']])
