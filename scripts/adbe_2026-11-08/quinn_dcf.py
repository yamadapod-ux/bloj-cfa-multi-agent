# Quinn ADBE VS2 DCF — 2026-11-08
# PROBABILITIES PRE-SET (written before any FV computed): Bull 25% / Base 45% / Bear 30%
# Inputs (Atlas Data Package 2026-11-08): WACC 10.10% (9.98/10.23/10.62), FV/sh = EV/391.5 - 1.85,
# FY26 revenue guide $26.576-26.626B (8-K Q3 FY26), GAAP op margin ~35% FY26 guide, Q4 revenue guide $6.80-6.85B
PROBS={'Bull':0.25,'Base':0.45,'Bear':0.30}
WACC=0.1010; SH=391.5; NETDEBT=724.0; PRICE=239.30
REV26=26600.0; Q4REV=6825.0; Q4MARGIN=0.35
KE=(0.1039+0.1066)/2; KD_AT=0.05*(1-0.226); DEBT=6363.0
def lin(a,b,n):  # n points from a (exclusive) to b (inclusive)
    return [a+(b-a)*(i+1)/n for i in range(n)]
S={
 'Bull':dict(g=[.100,.100,.095,.090,.085]+lin(.085,.055,5), m=[.355]+lin(.355,.39,4)+[.39]*5, tax=.215, ronic=.50, tronic=.30, tgr=.030),
 'Base':dict(g=[.085,.075,.070,.065,.060]+lin(.060,.045,5), m=[.345]+lin(.345,.355,4)+[.355]*5, tax=.215, ronic=.40, tronic=.20, tgr=.025),
 'Bear':dict(g=[.060,.045,.040,.035,.030]+[.025]*5, m=[.33,.31,.30]+lin(.30,.29,2)+[.29]*5, tax=.226, ronic=.25, tronic=.12, tgr=.020),
}
def run(p,wacc=WACC,midyear=True,detail=False,stub=True):
    g=list(p['g']); m=list(p['m']); tgr=p['tgr']
    # VS2 1.3 fade: if final growth > TGR+3pp add linear fade (<=10y) to TGR
    fade=[]
    if g[-1]>tgr+0.03:
        n=min(10,max(1,round((g[-1]-tgr)/0.005)))
        fade=lin(g[-1],tgr,n)[:-1] if n>1 else []
    gg=g+fade; mm=m+[m[-1]]*len(fade)
    N=len(gg)
    rev=REV26; rows=[]; pv=0
    # stub Q4 FY26 (Aug29-Nov27): NOPAT less base reinvestment, ~0.06y
    if stub:
        nq=Q4REV*Q4MARGIN*(1-p['tax']); fq=nq*(1-gg[0]/p['ronic'])
        pv+=fq/(1+wacc)**0.03
    for i in range(N):
        rev*=1+gg[i]; ebit=rev*mm[i]; nopat=ebit*(1-p['tax'])
        gnext=gg[i+1] if i+1<N else tgr
        # explicit years: RONIC transitions linearly to terminal RONIC over fade years
        r=p['ronic'] if i<10 else p['ronic']+(p['tronic']-p['ronic'])*(i-9)/max(1,N-10)
        if i==N-1: r=p['tronic']
        reinv=nopat*gnext/r; fcff=nopat-reinv
        t=(i+1-0.5+0.06) if midyear else (i+1+0.06)
        df=(1+wacc)**t; pv+=fcff/df
        rows.append((2027+i,rev,gg[i],mm[i],nopat,reinv,fcff,df))
    # terminal (Gordon on year N+1 NOPAT, reinvestment = TGR/terminal RONIC)
    nopatN1=rows[-1][4]*(1+tgr); fcffN1=nopatN1*(1-tgr/p['tronic'])
    tv=fcffN1/(wacc-tgr); tN=(N+0.06) if not midyear else (N-0.5+0.06)
    pvtv=tv/(1+wacc)**tN
    ev=pv+pvtv; fv=ev/SH-NETDEBT/SH
    if detail: return dict(ev=ev,fv=fv,pvtv=pvtv,tvshare=pvtv/ev,rows=rows,tv=tv,N=N,fade=len(fade))
    return fv
if __name__=='__main__':
    pw=0
    for k,p in S.items():
        d=run(p,detail=True); pw+=PROBS[k]*d['fv']
        print(f"\n== {k} (p={PROBS[k]:.0%}) EV ${d['ev']:,.0f}M  FV/sh ${d['fv']:.2f}  PV(TV)/EV {d['tvshare']:.1%}  fade yrs {d['fade']}  N={d['N']}")
        print(" FY   Rev$M   g     OpM   NOPAT  Reinv  FCFF")
        for r in d['rows']: print(f" {r[0]} {r[1]:8,.0f} {r[2]:5.1%} {r[3]:5.1%} {r[4]:6,.0f} {r[5]:6,.0f} {r[6]:6,.0f}")
        for w in (0.0998,0.1023,0.1062,0.086): print(f"   WACC {w:.2%}: ${run(p,wacc=w):.2f}")
        print(f"   end-year convention: ${run(p,midyear=False):.2f}; no stub: ${run(p,stub=False):.2f}")
        nog=d['rows'][0][4]/WACC/SH-NETDEBT/SH
        print(f"   no-growth value (FY27 NOPAT/WACC): ${nog:.2f}")
    print(f"\nP-W FV ${pw:.2f}  MOS {pw/PRICE-1:+.1%} (MOS def = FV/Price-1) ; (FV-P)/FV {1-PRICE/pw:+.1%}")
    for w in (0.0998,0.1023,0.1062,0.086):
        print(f" P-W @WACC {w:.2%}: ${sum(PROBS[k]*run(p,wacc=w) for k,p in S.items()):.2f}")
