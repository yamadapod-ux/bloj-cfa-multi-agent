# Emma MTZ FCFF model (VS2). Inputs: Atlas 2026-11-21 Data Package + 8-K Q3-26. Judgment calls fixed BEFORE run.
import copy
BASE=dict(wacc=0.0984, ke=0.1166, tgr=0.03, ronic=0.12, tax=0.24, mid=0.040, norm_years=5,
  growth=[None,0.176,0.10,0.08,0.065,0.055,0.05,0.045,0.04,0.035], # 2026 = guide, 2027 = consensus
  nwc=0.09, capex=[0.032,0.032,0.032,0.031,0.030,0.029,0.028,0.028,0.028,0.028], da=[0.0304,0.030,0.029,0.028,0.028,0.027,0.027,0.027,0.027,0.027],
  m26=0.051, rev26=18300.0, rev25=14299.2, q4_fcff=560.0,
  net_debt=3686.7, nci_mult=10.0, nci_inc=47.0, aff_inc=19.6, aff_mult=12.0, shares=80.30, days=52, kd_at=0.0677*0.76)
def run(p):
    n=10; rev=[p['rev26']]
    g=[None,p['growth'][1]]+p['growth'][2:]
    rev.append(rev[0]*(1+g[1]))
    for i in range(2,n): rev.append(rev[-1]*(1+g[i]))
    # margin
    m=[p['m26']]
    for i in range(1,n):
        if i<=p['norm_years']: m.append(p['m26']+(p['mid']-p['m26'])*i/p['norm_years'])
        else: m.append(p['mid'])
    prev=[p['rev25']*(1.0)]; 
    fc=[];nop=[]
    for i in range(n):
        r=rev[i]; rp=(p['rev26'] if i==1 else rev[i-1]) if i>0 else p['rev25']
        rp=rev[i-1] if i>0 else p['rev25']
        ebit=r*m[i]; nopat=ebit*(1-p['tax'])
        f=nopat+r*p['da'][i]-r*p['capex'][i]-p['nwc']*(r-rp)
        fc.append(f);nop.append(nopat)
    # stub: Q4'26 guided
    pv=0; t=0.125; pv+=p['q4_fcff']/(1+p['wacc'])**t
    for i in range(1,n): pv+=fc[i]/(1+p['wacc'])**(0.25+i-0.5)
    nopat_T=nop[-1]*(1+p['tgr']); fcff_T=nopat_T*(1-p['tgr']/p['ronic'])
    tv=fcff_T/(p['wacc']-p['tgr']); pvtv=tv/(1+p['wacc'])**(0.25+n-1)
    ev=pv+pvtv
    nci=p['nci_inc']*p['nci_mult']; aff=p['aff_inc']*p['aff_mult']
    eq=ev-p['net_debt']-nci+aff
    eq*= (1+p['ke'])**(p['days']/365)
    fv=eq/p['shares']
    return dict(fv=fv,ev=ev,pvtv=pvtv,tvpct=pvtv/ev,rev=rev,m=m,fc=fc,nop=nop,tv=tv,nci=nci,aff=aff,eq=eq,fcff_T=fcff_T)
def fv5(p,r):
    # equity at 2031-12-31: PV of FCFF 2032-35 + TV, + aff - NCI (mult*grown nci) - net debt5
    w=p['wacc'];n=10
    # time from end-2031: year idx 6..9 (2032..2035) mid-year
    pv=sum(r['fc'][i]/(1+w)**(i-6+0.5) for i in range(6,10)); pvtv=r['tv']/(1+w)**4
    ev5=pv+pvtv
    nd=p['net_debt']; 
    cum=p['q4_fcff']
    nd-=p['q4_fcff']
    nci_inc=p['nci_inc']
    for i in range(1,6):
        interest=nd*p['kd_at']
        nci_inc*= (r['rev'][i]/r['rev'][i-1])
        nd=nd-r['fc'][i]+interest+nci_inc  # NCI distributions = NCI income
    nci5=nci_inc*p['nci_mult']
    eq5=ev5+r['aff']-nci5-nd
    return eq5/p['shares'],nd,eq5,ev5
if __name__=='__main__':
    b=run(BASE); f5=fv5(BASE,b)
    print('BASE FV %.2f EV %.0f TV%% %.1f%% PVTV %.0f eq %.0f'%(b['fv'],b['ev'],b['tvpct']*100,b['pvtv'],b['eq']))
    print('rev',[round(x) for x in b['rev']]);print('m',[round(x*100,2) for x in b['m']]);print('fcff',[round(x) for x in b['fc']])
    print('FV5 %.2f nd5 %.0f eq5 %.0f ev5 %.0f'%f5)
    ke=BASE['ke']; eq0=b['eq']; 
    print('consistency eq5/(eq0*(1+ke)^5.1)=',f5[2]/(eq0*(1+ke)**5.1))
    P=144.71
    print('MOS',b['fv']/P-1,'ER5',(f5[0]/P)**(1/5.11)-1)
    def s(name,**kw):
        q=copy.deepcopy(BASE);q.update(kw);r=run(q);f=fv5(q,r);print('%-28s FV %.2f d%% %.1f FV5 %.2f TV%% %.0f'%(name,r['fv'],(r['fv']/b['fv']-1)*100,f[0],r['tvpct']*100));return r['fv']
    s('mid 3.4 (5Y avg)',mid=0.0337);s('mid 3.6',mid=0.036);s('mid 4.5',mid=0.045);s('mid 5.0',mid=0.05);s('mid 5.1 TTM',mid=0.051)
    s('WACC blume 10.12',wacc=0.1012,ke=0.1205);s('WACC bu 9.56',wacc=0.0956,ke=0.1127)
    s('ERP+100',wacc=0.0984+0.0071,ke=0.1166+0.01*1.527);s('ERP-100',wacc=0.0984-0.0071,ke=0.1166-0.01527)
    s('Rf+50&ERP+100',wacc=0.0984+0.0071+0.0036,ke=0.1166+0.0153+0.0076)
    s('Rf-50',wacc=0.0984-0.0036,ke=0.1166-0.0076)
    for d in (-0.03,0.03):
        g=BASE['growth'][:];g=[g[0],g[1]]+[x+d for x in g[2:]];s('growth28+ %+.0fpp'%(d*100),growth=g)
    s('RONIC=WACC',ronic=0.0984);s('RONIC 15',ronic=0.15);s('TGR2.5',tgr=0.025);s('TGR3.5',tgr=0.035)
    s('NWC 12%',nwc=0.12);s('NWC 5%',nwc=0.05)
    s('norm 2y',norm_years=2);s('norm 8y',norm_years=8)
    s('stub=0.25*normal (100)',q4_fcff=100);s('stub 0.5*guide',q4_fcff=280)
    s('net debt all-in 4223',net_debt=4223.2)
    s('NCI BS 147',nci_mult=147.2/47.0);s('NCI 15x',nci_mult=15)
    s('no aff',aff_mult=0)
    s('shares 79.8',shares=79.8)
    s('capex +0.5pp all',capex=[c+0.005 for c in BASE['capex']])
    # scenarios
    bull=copy.deepcopy(BASE);bull.update(mid=0.05,wacc=0.0930,ke=0.1100,ronic=0.15,growth=[None,0.176]+[x+0.02 for x in BASE['growth'][2:]]);rb=run(bull);print('BULL',rb['fv'],fv5(bull,rb)[0],rb['tvpct'])
    bear=copy.deepcopy(BASE);bear.update(mid=0.0337,wacc=0.1050,ke=0.1250,ronic=0.10,growth=[None,0.12]+[x-0.02 for x in BASE['growth'][2:]]);rr=run(bear);print('BEAR',rr['fv'],fv5(bear,rr)[0],rr['tvpct'])
    # gap-closing
    def solve(key,lo,hi,fn=None):
        for _ in range(80):
            mid=(lo+hi)/2;q=copy.deepcopy(BASE)
            if fn: fn(q,mid)
            else: q[key]=mid
            v=run(q)['fv']
            if v<P: lo=mid
            else: hi=mid
        return mid
    print('mid margin to close',solve('mid',0.03,0.20))
    def gw(q,x): q['wacc']=x; q['ke']=x+0.0182
    print('wacc to close',solve(None,0.04,0.0984,gw))
    def gt(q,x): q['tgr']=x
    print('tgr to close (cap 9.5%)',solve('tgr',0.03,0.095))
    def gg(q,x): q['growth']=[None,BASE['growth'][1]]+[BASE['growth'][i]+x for i in range(2,10)]
    print('growth 28+ add pp to close',solve(None,0,0.4,gg))
    def gg2(q,x):
        q['growth']=[None,x]+[BASE['growth'][i]+x-0.176 for i in range(2,10)]
    # revenue 2035 under uniform pp
    q=copy.deepcopy(BASE);gg(q,solve(None,0,0.4,gg));rq=run(q);print('rev2035 close',rq['rev'][-1],'vs',b['rev'][-1])
    # both margin & growth
    q=copy.deepcopy(BASE);q['mid']=0.051;q['growth']=[None,0.176]+[x+0.0 for x in BASE['growth'][2:]]
    def gg3(q,x): q['mid']=0.051;q['growth']=[None,0.176]+[BASE['growth'][i]+x for i in range(2,10)]
    print('growth add w/ margin 5.1 to close',solve(None,0,0.4,gg3))
    # multiples cross-check
    print('rev27',b['rev'][1],'ebit27 mid',b['rev'][1]*b['m'][1],'ebit TTM 881.5')
