import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from quinn_dcf import run,S,PROBS,WACC,SH,NETDEBT,PRICE,KE,KD_AT,DEBT
# VS2 1.4: FV at end of FY31 (year 5). Equity5 = PV@yr5 of FCFF FY32+ (incl. terminal) - net debt5
# Assumption: FCFF after after-tax interest fully distributed via buyback -> net debt5 = net debt0 ($724M)
# Shares5 = 391.5 x (1-3.2%)^5 (Atlas: FY22->FY25 net dilution -3.2%/yr, SEC XBRL); sensitivity -5%/yr
def fv5(p,dil=-0.032):
    d=run(p,detail=True); rows=d['rows']; N=d['N']; tgr=p['tgr']
    # PV at end-yr5 (t=5.06 from valuation date ~ mid-year cash flows), use same mid-year convention
    pv=0
    for i in range(5,N):
        t=(i+1-0.5+0.06)-5.06
        pv+=rows[i][6]/(1+WACC)**t
    nopatN1=rows[-1][4]*(1+tgr); fcffN1=nopatN1*(1-tgr/p['tronic'])
    tv=fcffN1/(WACC-tgr); pv+=tv/(1+WACC)**((N-0.5+0.06)-5.06)
    eq5=pv-NETDEBT; sh5=SH*(1+dil)**5
    dist=[rows[i][6]-DEBT*KD_AT for i in range(5)]
    fvdist=sum(x*(1+KE)**(5-(i+0.5)) for i,x in enumerate(dist))
    eq0=d['ev']-NETDEBT
    chk=eq0*(1+KE)**5-fvdist; chkw=eq0*(1+WACC)**5-sum(x*(1+WACC)**(5-(i+0.5)) for i,x in enumerate(dist))
    return eq5/sh5, eq5, sh5, chk, chkw, sum(dist)
tot=0;tot5b=0
for k,p in S.items():
    f,eq5,sh5,chk,chkw,dist=fv5(p); f2=fv5(p,-0.05)[0]; tot+=PROBS[k]*f; tot5b+=PROBS[k]*f2
    print(f"{k}: FV5/sh ${f:.2f} (dil -5%/yr: ${f2:.2f}) Equity5 ${eq5:,.0f}M shares5 {sh5:.1f}M | sum_dist ${dist:,.0f}M | check Eq0(1+Ke)^5-FVdist ${chk:,.0f}M ({eq5/chk-1:+.1%}); @WACC ${chkw:,.0f}M ({eq5/chkw-1:+.1%})")
print(f"P-W FV5 ${tot:.2f} -> exp return/yr {(tot/PRICE)**0.2-1:.2%} ; (dil -5%: ${tot5b:.2f} -> {(tot5b/PRICE)**0.2-1:.2%})")
print(f"S&P implied expected return = Rf 4.86% + ERP 4.41% = 9.27% (Atlas DP sec F, Damodaran)")
