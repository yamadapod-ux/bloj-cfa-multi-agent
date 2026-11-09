# Round 91 Airlines -- Filter A/B-Zero/B/C/D + Tier 1 math. Prices: Yahoo chart = Nasdaq.com, close 2026-11-06.
# Financials: SEC EDGAR companyfacts (data/cf_*.json via sec.py/tags.py), $M. RYAAY in EUR (20-F IFRS, FY Mar).
# FCF = OCF - all capex (incl. flight equipment). WACC = CLAUDE.md Filter D sector proxy by cap size (+/-1pp shown).
PX={'DAL':(87.20,95.68),'UAL':(112.74,138.77),'AAL':(13.18,18.79),'LUV':(44.45,55.11),'ALK':(38.94,60.63),'JBLU':(3.67,6.62),
    'ALGT':(91.97,123.63),'SKYW':(79.38,117.72),'RYAAY':(59.30,74.24),'CPA':(142.80,160.47)}
for t,(p,h) in PX.items(): print(f"A {t:5s} {p:8.2f} / {h:8.2f} = {100*(p/h-1):6.1f}%  {'PASS' if p/h-1<=-0.20 else 'fail'}")
D={ # sh(M), debt, cash+STI, op lease, equity, TTM op, TTM D&A, TTM OCF, TTM capex, FY FCF dict (OCF-capex), tax, wacc
 'AAL':dict(sh=661.97,debt=25395+933,cash=1124+7163,opl=6639,eq=-4224,op=973,da=2200,ocf=4267,cap=4358,
            fy={2022:2173-2546,2023:3803-2596,2024:3983-2683,2025:3099-3779},w=0.10),
 'ALK':dict(sh=112.78,debt=5976,cash=835+1396,opl=1360,eq=3530,op=-290,da=826,ocf=940,cap=(1063+790-744)+(309+175-219),
            fy={2021:1030-166,2022:1418-1463,2023:1050-1297,2024:1464-1110,2025:1249-1372},w=0.105),
 'JBLU':dict(sh=377.35,debt=8393,cash=1258+251,opl=953,eq=1337,op=-609,da=724,ocf=-224,cap=911,
            fy={2021:1642-907,2022:379-767,2023:400-1128,2024:144-1478,2025:-94-1078},w=0.13),
 'ALGT':dict(sh=27.31,debt=2938+636,cash=339+515,opl=69,eq=1765,op=180,da=268,ocf=215,cap=241,
            fy={2021:538-244,2022:303-435,2023:423-528,2024:338-300,2025:390-315},w=0.115),
 'SKYW':dict(sh=38.03,debt=2365,cash=72+497,opl=84,eq=2810,op=590,da=351,ocf=799,cap=(546+357-339)+(32+29-25),
            fy={2021:832-538-18,2022:480-632-13,2023:736-238-13,2024:692-266-45,2025:940-546-32},w=0.10),
}
for t,x in D.items():
    p=PX[t][0]; mc=p*x['sh']; nd=x['debt']-x['cash']; ev=mc+nd; ebitda=x['op']+x['da']; fcf=x['ocf']-x['cap']
    avg=sum(x['fy'].values())/len(x['fy']); ic=x['eq']+nd; nopat=x['op']*0.77
    print(f"\n{t}: mcap {mc:,.0f} ND {nd:,.0f} (+op lease {x['opl']:,}) EV {ev:,.0f} eq {x['eq']:,} | TTM EBITDA {ebitda:,} ND/EBITDA {nd/ebitda if ebitda>0 else float('nan'):.1f}x (lease-adj {(nd+x['opl'])/ebitda if ebitda>0 else float('nan'):.1f}x) EV/EBITDA {ev/ebitda if ebitda>0 else float('nan'):.1f}x")
    print(f"   FCF TTM {fcf:,} yield {100*fcf/mc:.1f}% | FY FCF {x['fy']} avg {avg:,.0f} yield {100*avg/mc:.1f}% | ROIC TTM (op*0.77/(eq+ND)) {100*nopat/ic if ic>0 else float('nan'):.1f}% vs WACC {100*x['w']:.1f}%")
    for w in (x['w']-0.01,x['w'],x['w']+0.01):
        for lab,f in (('avg',avg),('TTM',fcf),('OCF-D&A',x['ocf']-x['da'])):
            fv=(f/w-nd)/x['sh']; print(f"   WACC {100*w:4.1f}% {lab:8s} naive FV ${fv:8.2f}  P/FV {p/fv if fv>0 else float('inf'):.2f}")
# RYAAY: EUR. ADS = 2 ordinary; ADS-equivalent shares 526.23M (ChartMill 2026-01-06). EURUSD 1.1228 (Yahoo 11-06).
fx=1.1228; sh=526.23; mc=59.30*sh/fx; netcash=2700  # Jun-30-2026 net cash EUR (Ryanair Q1 FY27)
fy={2018:2233-1471,2019:1759-1288,2020:1327-579,2023:3891-1915,2024:3158-2392,2025:3416-1552}
avg=sum(fy.values())/len(fy); avg3=(fy[2023]+fy[2024]+fy[2025])/3
print(f"\nRYAAY mcap EUR {mc:,.0f}M net cash {netcash} EV {mc-netcash:,.0f} | FY FCF {fy} avg6 {avg:,.0f} avg3 {avg3:,.0f} | FY26 PAT 2,260 P/E {mc/2260:.1f}x | ROE FY25 {1612/7037:.1%}")
for w in (0.075,0.085,0.095):
    for lab,f in (('avg6',avg),('avg3',avg3),('PAT FY26',2260)):
        fv=f/w+netcash; print(f"   WACC {100*w:.1f}% {lab:9s} naive equity EUR {fv:,.0f}M  P/FV {mc/fv:.2f}")
