# Scout Round 87: B-Zero/B/C/D for Filter A survivors. Inputs come from 8-K/XBRL cited in the report ($M unless noted).
RF,ERP=4.837,4.41
def wacc(beta,E,D,kd,t): 
    k=RF+beta*ERP; return k, (E*k+D*100*kd*(1-t))/(E+D)  # kd passed as a fraction, k in percent
def fv(f,w,nd,sh): return (f/(w/100)-nd)/sh
def row(n,px,f,nd,sh,ws):
    print(f" {n:30} FCF {f:6.1f} yield-on-cap {100*f/(px*sh):5.1f}% | "+' '.join(f"{w:.2f}%: ${fv(f,w,nd,sh):6.2f} ({px/fv(f,w,nd,sh):.2f}x)" for w in ws))
# CXW
px,sh,debt,cash=28.23,86.498,629.6,547.2; nd=debt-cash; cap=px*sh; ebitda=444.0
fy={'21':(263.231,81.494,85.542),'22':(153.583,83.444,84.974),'23':(231.901,67.749,72.960),'24':(269.153,70.422,67.415),'25':(194.595,141.809,62.229)}
t=.26; lev=sum(a-b for a,b,_ in fy.values())/5; ai=sum(c for *_,c in fy.values())/5; thru=lev+ai*(1-t)
q4=444-337.339; rr=q4*4; ebit=rr-33.917*4; run=rr-70-ebit*t
k,w=wacc(.80,cap,debt,62.229/1205.037,t)
print(f"CXW cap {cap:.0f} nd {nd:.1f} EV {cap+nd:.0f} EV/EBITDA {(cap+nd)/ebitda:.2f} ND/EBITDA {nd/ebitda:.2f} P/B {cap/2278.11:.2f} 5Y lev FCF {lev:.1f} ({100*lev/cap:.1f}%) Q4impl {q4:.1f} rr {rr:.0f} CoE {k:.2f} WACC {w:.2f}")
row('through-cycle',px,thru,nd,sh,[w,10,11.5]); row('run-rate Q4x4',px,run,nd,sh,[w,10,11.5])
for lab,e,ic in [('Q1',52.31+17.681,1395.61+1380.955-209.686),('Q2',47.512+22.279,1438.477+1231.77-108.934),('Q3',1849.436+7.017-1770.7,2278.11+629.6-547.2)]:
    print(f"  ROIC {lab}: EBIT {e:.1f} IC {ic:.0f} = {100*e*4*(1-t)/ic:.1f}%")
pti={'21':86.103,'22':165.302,'23':95.823,'24':91.963,'25':157.176}
print('  5Y EBIT avg',round(sum(pti[y]+fy[y][2] for y in pti)/5,1),' FY25 ROIC',round(100*(157.176+62.229)*(1-t)/(1405.249+1205.037-97.929),1))
print(f"  sale $/bed {2200/7187*1000:.0f}k  ASR residual if $100M at $30: {100/30:.1f}M sh -> {sh-100/30:.1f}M; 11-04 close off high {100*(30.52/36.55-1):.1f}% low-to-now {100*(px/15.74-1):.0f}%")
# GEO
px,sh=25.17,132.0; nd=537.5; cap=px*sh; ebitda=570.5
gy={'21':(282.635,69.394,129.460),'22':(296.412,90.026,164.550),'23':(284.933,73.002,218.292),'24':(242.236,78.691,190.624),'25':(72.611,197.512,160.521)}
t=.28; f=lambda ys:(sum(gy[y][0]-gy[y][1] for y in ys)/len(ys), sum(gy[y][2] for y in ys)/len(ys))
l5,i5=f(gy); l4,i4=f(['21','22','23','24']); thru=l5+i5*(1-t); thru4=l4+i4*(1-t)
rr=151.5*4; ebit=rr-34.182*4; run=rr-(85.75+35)-ebit*t
k,w=wacc(.89,cap,625,160.521/1670.869,t)
print(f"GEO cap {cap:.0f} EV {cap+nd:.0f} EV/EBITDA {(cap+nd)/ebitda:.2f} ND/EBITDA {nd/ebitda:.2f} 5Y lev FCF {l5:.1f} ({100*l5/cap:.1f}%) ex25 {l4:.1f} ({100*l4/cap:.1f}%) rr {rr:.0f} CoE {k:.2f} WACC {w:.2f}")
row('through-cycle 5Y',px,thru,nd,sh,[w,10,11.5]); row('through-cycle ex-2025',px,thru4,nd,sh,[w,10,11.5]); row('run-rate Q4x4',px,run,nd,sh,[w,10,11.5])
for lab,e,ic in [('Q1',89.299,1497.237+1588.917-80.217),('Q2',101.703,1516.435+1511.53-54.992),('Q3*IC Q2',102.389,1516.435+1511.53-54.992)]:
    print(f"  ROIC {lab}: {100*e*4*(1-t)/ic:.1f}%")
oi=[288.083,383.102,352.389,309.975,257.49]; print('  5Y EBIT avg',sum(oi)/5,'on FY25 IC',round(100*sum(oi)/5*(1-t)/(1505.806+1670.869-68.995),1),' 11-04 off high',round(100*(27.53/33.17-1),1),'low-to-now',round(100*(px/12.51-1)))
# NHI
px,sh=71.58,48.498; fad=(240.6+243.7)/2; ffo=(4.74+4.79)/2; cap=px*sh
k,w=wacc(.63,cap,1288,57.368/1179,0)
print(f"NHI cap {cap:.0f} NFFO {ffo:.3f} P/FFO {px/ffo:.1f} yld {100*ffo/px:.2f}% FAD/sh {fad/sh:.2f} P/FAD {px/(fad/sh):.1f} yld {100*fad/sh/px:.2f}% div yld {100*.94*4/px:.2f}% CoE {k:.2f} WACC {w:.2f}")
for c in (k,8,9,10): print(f"  FAD/CoE {c:.2f}%: ${fad/sh/(c/100):.2f} ({px/(fad/sh/(c/100)):.2f}x)")
print('  ROIC FY25',round(100*(142.177+57.368)/(1521.543+1179-19.624),1))
print('A-fail info')
for n,p,h,fo in [('SUI',122.08,137.85,7.01),('ELS',62.98,69.00,3.18),('UMH',15.13,16.77,1.01),('OUT',32.00,34.96,102.9*4/177.6),('LAMR',157.30,166.33,8.92),('OHI',47.99,52.39,3.29)]:
    print(f"  {n}: off {100*(p/h-1):.1f}% A-price {.8*h:.2f} need {100*(.8*h/p-1):.1f}% P/x {p/fo:.1f} yld {100*fo/p:.2f}%")
for n,p,h in [('CTRE',37.18,43.62),('VTR',89.04,101.60),('SBRA',20.89,22.77),('WELL',245.43,255.20),('LTC',45.65,46.92)]:
    print(f"  {n}: off {100*(p/h-1):.1f}% A-price {.8*h:.2f}")
