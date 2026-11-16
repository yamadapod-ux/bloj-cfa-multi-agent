# Quinn MU 2026-11-08: P-W, WACC/TGR sensitivity, 5x5 matrix, FV5 (VS2 1.4), reverse DCF, no-growth floor. Imports quinn_dcf_1108.
import copy,math,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from quinn_dcf_1108 import *
def fv(s,mshift=0.,aspx=None,**kw):
    s2=copy.deepcopy(s); r=path(s2,mshift=mshift,aspx=aspx); mT=s2['mT']+mshift
    return value(s2,r,mT=mT,**kw)['fv']
def pw(**kw): return sum(s['p']*fv(s,**kw) for s in SC.values())
P=pw(); print('P-W FV $%.2f | MOS @656.39 %.1f%% | @696 %.1f%%'%(P,(P/PX-1)*100,(P/PXI-1)*100))
for k,s in SC.items(): print(' %s %.0f%% FV $%.2f'%(k,s['p']*100,fv(s)))
print('\nWACC sensitivity (P-W / Bull / Base / Bear):')
for w in [.1144,.1175,.125,.13,.1356,.1328]:
    print(' WACC %.2f%%: P-W $%.2f | %s'%(w*100,pw(wacc=w),' / '.join('$%.2f'%fv(s,wacc=w) for s in SC.values())))
for g in [.01,.03]: print(' TGR %.0f%%: P-W $%.2f'%(g*100,pw(g=g)))
print(' end-year discounting (t0=0.83): P-W $%.2f'%pw(t0=.83))

# probability sensitivity
for pb in [(.2,.5,.3),(.25,.5,.25),(.3,.45,.25),(.15,.45,.4),(1/3,1/3,1/3)]:
    print(' probs Bull/Base/Bear %s -> P-W $%.2f'%(pb,sum(p*fv(s) for p,s in zip(pb,SC.values()))))
# Base at consensus FY27/FY28 revenue (275.5 / 320.06 [StockAnalysis])
b=SC['Base']; a27=275500/(REV0*1.18)-1; a28=320060/(REV0*1.18*1.20)/(1+a27)-1
print('\nBase w/ consensus FY27-28 revenue: ASP FY27 %+.0f%%, FY28 %+.0f%% -> FV $%.2f'%(a27*100,a28*100,fv(b,aspx={2027:a27*100-62,2028:a28*100+8})))
# ---- 5x5: mid-cycle margin (terminal + FY31-36 path shift) x WACC, Base scenario; plus P-W row-equivalent
W=[.1144,.1175,.125,.13,.1356]; M=[.18,.24,.30,.36,.42]
print('\n5x5 BASE: mid-cycle margin x WACC'); print(' m/W '+' '.join('%7.2f%%'%(w*100) for w in W))
for m in M: print(' %4.0f%% '%(m*100)+' '.join('%8.0f'%fv(b,mshift=m-.30,wacc=w) for w in W))
print('\n5x5 P-W (all scenario mid-cycle margins shifted by same delta vs base 30%)'); 
for m in M: print(' %+4.0fpp '%((m-.30)*100)+' '.join('%8.0f'%pw(mshift=m-.30,wacc=w) for w in W))
# supplementary: peak ASP (FY27 ASP change, Base) x WACC
print('\nSupp 5x5 BASE: FY27 ASP YoY x WACC (FY28 -8% after)')
for a in [32,47,62,77,92]:
    r27=REV0*1.18*(1+a/100); print(' %+3d%% (FY27 rev $%3.0fB) '%(a,r27/1e3)+' '.join('%8.0f'%fv(b,aspx={2027:a-62},wacc=w) for w in W))
# ---- Reverse DCF
def solve(f,lo,hi,target,n=80):
    for _ in range(n):
        mid=(lo+hi)/2
        if f(mid)<target: lo=mid
        else: hi=mid
    return (lo+hi)/2
for price in [PX,PXI]:
    # (a) uniform FY26->FY28 revenue CAGR, Base bits; FY29+ base margin path unchanged
    def fa(gg):
        a27=(1+gg)/1.18-1; a28=(1+gg)/1.20-1
        return fv(b,aspx={2027:a27*100-62,2028:a28*100+8})
    gi=solve(fa,0,2.5,price); print('\nReverse DCF @$%.2f: implied FY26-28 revenue CAGR %.1f%% vs consensus 55.0%% -> ratio %.2fx (pass <=1.20x) | FY28 rev $%.0fB vs cons $320B'%(price,gi*100,gi/.55,REV0*(1+gi)**2/1e3))
    # (b) implied mid-cycle margin (FY31-36 path + terminal shifted), base FY27-30
    mi=solve(lambda d: fv(b,mshift=d),-.25,.6,price); print('   implied mid-cycle/terminal op margin %.1f%% (base 30%%; FY16-25 avg 17.4%%, rev-wtd 21.6%%, prior peak FY18 49.3%%, FY26 74.6%%)'%((.30+mi)*100))
    # (c) P-W implied mid-cycle margin shift
    pi=solve(lambda d: pw(mshift=d),-.25,.6,price); print('   P-W implied: all scenario mid-cycle margins +%.1fpp (Base becomes %.1f%%)'%(pi*100,(.30+pi)*100))
    # (d) how many years must FY28-level margin persist? extend base peak: replace FY29.. margins with 79%
    for yrs in range(1,8):
        s2=copy.deepcopy(b); ys=list(range(2029,2029+yrs))
        for y in ys: s2['m'][y]=79
        if fv(s2)>=price: print('   implied: peak-level margin (79%%) must persist through FY%d (%d extra yrs) before base downturn path'%(ys[-1],yrs)); break
# ---- No-growth floor (Multi-Segment Rule 5 / VS2)
nopat26=OI0*(1-.148); ng=(nopat26/WACC+BR)/SH
print('\nNo-growth value on FY26 (peak) NOPAT $%.0fB: $%.2f/share'%(nopat26/1e3,ng))
C26=REV0-OI0
for k,s in SC.items():
    r=path(s); v=value(s,r); mT=s['mT']; rn=C26/(1-mT/(1-s['ps'])); n_norm=rn*mT*(1-TAX)
    ngm=(n_norm/WACC+BR)/SH; dN=v['nT']/(1+G)**(FADE+1)-n_norm; dK=r[-1]['ppe']-PPE0
    capn=[x['y'] for x in r if x['y'] not in s['capex']][0]
    print(' %s: FY26 cost base at mid-cycle %.0f%% -> NOPAT $%.1fB, no-growth $%.2f | FV $%.2f | incremental NOPAT (FY36N-FY26N) $%.1fB on +PP&E $%.0fB -> incr. ROIC %.1f%% vs WACC 12.5%% | terminal RONIC %.1f%% | capex normalises FY%d'%(k,mT*100,n_norm/1e3,ngm,v['fv'],dN/1e3,dK/1e3,dN/dK*100,s['ronic']*100,capn))
# ---- FV5 (VS2 1.4): value at end FY31 (~Nov 2031 ~ 5y)
RI=.0484*(1-TAX)   # after-tax yield on retained cash (Rf 4.84%)
dil=(1143/1118)**.5-1   # diluted shares FY24 1,118M -> FY26 1,143M [S4]
def fv5(s,wacc=WACC):
    r=path(s); v=value(s,r,wacc=wacc); n=5
    # value at end FY31 (t=4.83y from today; treat as 5y): PV of FCFF FY32-36 + fade + TV, discounted to end FY31
    pv=sum(x['fcff']/(1+wacc)**(i+.5) for i,x in enumerate(r[n:]))
    # fade+TV: reuse value() with r[n:] by rebasing: discount factor from today to end-FY31 = (1+w)^(T0+n-.5)
    df=(1+wacc)**(T0+n-.5); rest=(v['fadepv']+v['pvtv'])*df
    cash=BR
    for x in r[:n]: cash=cash*(1+RI)+x['fcff']
    eq5=pv+rest+cash; sh5=SH*(1+dil)**5
    return eq5/sh5,eq5,v['ev']+BR,cash
out=[];print('\nFV5 (end FY31):')
ke=.0484+1.99*.0441
for k,s in SC.items():
    f5,e5,e0,c5=fv5(s); out.append(s['p']*f5)
    print(' %s FV5 $%.2f | Equity5 $%.0fB (net cash5 $%.0fB) vs Equity0 x (1+WACC)^5 = $%.0fB (gap %.0f%%)'%(k,f5,e5/1e3,c5/1e3,e0*1.125**5/1e3,(e5/(e0*1.125**5)-1)*100))
F5=sum(out); print(' P-W FV5 $%.2f | exp. annual return @656.39 %.1f%%/yr, @696 %.1f%%/yr | shares5 %.0fM'%(F5,((F5/PX)**.2-1)*100,((F5/PXI)**.2-1)*100,SH*(1+dil)**5))
print(' S&P 500 expected return = Rf 4.84%% + ERP 4.41%% = 9.25%%/yr')
