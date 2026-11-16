# Quinn MU VS2 re-analysis 2026-11-08 -- 3-scenario FCFF (bits x ASP x cost/bit), P-W EV, FV5, reverse DCF, sensitivity
# Inputs: agent_notes/charlie/2026-11-06_MU_verified_inputs.md [S1]-[S4]; Atlas locks (WACC 12.50%, bridge EV/1150 + 48.35, net capex, 10y FY27-36, TGR 1-3%)
# Run: python -I quinn_dcf_1108.py [--mask]
import sys,statistics as st,math
MASK='--mask' in sys.argv
PX=656.39; PXI=696.0; SH=1150.; BR=55601.; WACC=.125; TAX=.155; G=.025
# FY26 anchors ($M) [S1][S4]
REV0=133188.; COGS0=25684.; OI0=99340.; DA0=9503.; PPE0=63310.; OPEX0=REV0-COGS0-OI0   # 8,164
VAR0=COGS0-.9*DA0            # cash COGS (assume 90% of D&A sits in COGS) = 17,131
FIX0=OPEX0-.1*DA0            # cash opex incl. SBC = 7,214
FIX27=FIX0+2500              # FY27 opex +~$2.5B [S2][S3]
DAR=.16                      # D&A / avg PP&E (FY26 actual 0.173; new shells longer-lived)
NWC=.15                      # NWC build per $ revenue increase; no release on decline (FY23 evidence: AR -2.8B vs inventory +3.6B)
T0=1/3                       # years from 2026-11-05 to FY27 mid-point (~Mar 2027); mid-year convention
YRS=list(range(2027,2037))
SC={
 'Bull':dict(p=.20,bits=[20,22,20,16,15,14,13,12,11,10],cost=[0]+[-7]*9,fixg=.08,ps=.01,
             asp={2027:78,2028:-5},m={2029:75,2030:55,2031:38,2032:45,2033:50,2034:36,2035:38,2036:40},mT=.40,
             capex={2027:60000,2028:75000,2029:70000},cxk=1.45,ronic=.16),
 'Base':dict(p=.50,bits=[18,20,17,15,15,14,13,12,11,10],cost=[0]+[-6]*9,fixg=.07,ps=.02,
             asp={2027:62,2028:-8},m={2029:55,2030:32,2031:24,2032:34,2033:38,2034:24,2035:28,2036:32},mT=.30,
             capex={2027:57000,2028:65000,2029:50000},cxk=1.35,ronic=.125),
 'Bear':dict(p=.30,bits=[10,14,12,8,10,12,12,11,10,10],cost=[5,0]+[-5]*8,fixg=.04,ps=.06,
             asp={2027:40},m={2028:35,2029:0,2030:-20,2031:5,2032:20,2033:25,2034:8,2035:15,2036:20},mT=.175,
             capex={2027:55000,2028:48000,2029:30000},cxk=1.10,ronic=.09),
}
def path(s,mshift=0.,aspx=None):
    out=[];rev=REV0;ppe=PPE0;bi=1.;ci=1.;asp=1.;fix=FIX27
    for i,y in enumerate(YRS):
        bi*=1+s['bits'][i]/100; ci*=1+s['cost'][i]/100
        if i>0: fix*=1+s['fixg']
        var=VAR0*bi*ci
        # capex: explicit early years, else k x D&A (solve D&A on avg PP&E jointly)
        if y in s['capex']:
            cx=s['capex'][y]; da=DAR*(ppe+cx/2)/(1+DAR/2)
        else:
            k=s['cxk']; da=DAR*ppe/(1+DAR/2-DAR*k/2); cx=k*da
        C=var+fix+da; prev=rev
        if y in s['asp']:
            a=s['asp'][y]+(aspx.get(y,0) if aspx else 0); asp*=1+a/100; rev=REV0*bi*asp
            pre=rev-C; ebit=pre-s['ps']*max(0,pre)
        else:
            m=s['m'][y]/100+mshift
            rev=C/(1-m/(1-s['ps'])) if m>0 else C/(1-m); ebit=m*rev; asp=rev/(REV0*bi)
        ppe0=ppe; ppe=ppe+cx-da
        nopat=ebit-TAX*max(0,ebit); dn=NWC*max(0,rev-prev)
        fcff=nopat-(cx-da)-dn
        out.append(dict(y=y,rev=rev,g=rev/prev-1,bi=bi,ci=ci,asp=asp,ebit=ebit,m=ebit/rev,da=da,cx=cx,ppe=ppe,nopat=nopat,dn=dn,fcff=fcff,
                        roic=nopat/((ppe0+ppe)/2+.10*rev),C=C))
    return out
FADE=5   # VS2 1.3: linear fade FY37-FY41 from FY36 underlying cost-base growth to TGR (Quinn judgment, recorded)
def value(s,r,wacc=WACC,g=G,mT=None,ronic=None,t0=T0,fade=FADE):
    mT=s['mT'] if mT is None else mT; ronic=s['ronic'] if ronic is None else ronic
    last=r[-1]; prevC=r[-2]['C']; g0=last['C']/prevC-1          # underlying growth = cost-base growth FY36 (strips cycle-margin swing)
    rev36N=last['C']/(1-mT/(1-s['ps'])) if mT>0 else last['C']/(1-mT)   # FY36 revenue normalised to mid-cycle margin
    pv=[x['fcff']/(1+wacc)**(t0+i) for i,x in enumerate(r)]
    rv=rev36N; fpv=[]; n=len(r)
    for j in range(1,fade+1):
        gj=g0+(g-g0)*j/fade; rv*=1+gj; nop=rv*mT*(1-TAX); f=nop*(1-gj/ronic)   # reinvestment = g/RONIC (no free growth)
        fpv.append(f/(1+wacc)**(t0+n-1+j))
    revT=rv*(1+g); nT=revT*mT*(1-TAX); fT=nT*(1-g/ronic); tv=fT/(wacc-g)
    tT=t0+n-1+fade+.5; pvtv=tv/(1+wacc)**tT          # TV at end of last fade year (mid-year flows -> +0.5)
    ev=sum(pv)+sum(fpv)+pvtv
    return dict(ev=ev,fv=ev/SH+BR/SH,pvtv=pvtv,tv=tv,revT=revT,nT=nT,fT=fT,pv=pv,sumpv=sum(pv),fadepv=sum(fpv),g0=g0,rev36N=rev36N)
if __name__=='__main__':
    for k,s in SC.items():
        r=path(s); print('\n==',k,'p=%.0f%%'%(s['p']*100))
        print(' FY   Rev$B  g%   bitsIdx costIdx ASPidx(FY26=1) EBIT$B  m%   D&A  Capex  PPE   NOPAT  dNWC  FCFF  ROIC%')
        for x in r: print(' %d %6.1f %5.1f  %5.2f  %5.2f  %5.2f  %6.1f %5.1f %5.1f %5.1f %6.1f %6.1f %5.1f %6.1f %5.1f'%(x['y'],x['rev']/1e3,x['g']*100,x['bi'],x['ci'],x['asp'],x['ebit']/1e3,x['m']*100,x['da']/1e3,x['cx']/1e3,x['ppe']/1e3,x['nopat']/1e3,x['dn']/1e3,x['fcff']/1e3,x['roic']*100))
        print(' avg m FY31-36 %.1f%% | sum FCFF FY27-36 $%.0fB | FY36 growth %.1f%% (fade needed if > TGR+3pp=%.1f%%)'%(st.mean(x['m'] for x in r[4:])*100,sum(x['fcff'] for x in r)/1e3,r[-1]['g']*100,(G+.03)*100))
        if not MASK:
            v=value(s,r); print(' g0 %.1f%% | EV $%.0fB = explicit $%.0fB + fade $%.0fB + PV TV $%.0fB (TV+fade %.0f%% of EV) | TV rev $%.0fB NOPAT $%.0fB | FV/share $%.2f'%(v['g0']*100,v['ev']/1e3,v['sumpv']/1e3,v['fadepv']/1e3,v['pvtv']/1e3,100*(v['pvtv']+v['fadepv'])/v['ev'],v['revT']/1e3,v['nT']/1e3,v['fv']))
