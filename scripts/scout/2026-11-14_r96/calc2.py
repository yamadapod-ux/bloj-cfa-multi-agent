import json
s=json.load(open('sec.json')); p=json.load(open('prices.json'))
M=1e6
SH={'BELFB':None}
def g(r,k,f='ttm'):
    x=r.get(k)
    if not x: return 0
    return (x.get(f) if f in x else x.get('last')) or 0
def fyd(r,k):
    x=r.get(k); return {e[:4]:v for e,v in x['fy']} if x else {}
rows=[]
for t,r in s.items():
    pr=p[t]['y_close']
    sh=(r['shs'] or {}).get('last') if (r.get('shs') and r['shs'].get('end','')>='2026') else None
    if not sh and r.get('dil') and r['dil']['fy']: sh=r['dil']['fy'][-1][1]
    if t=='BELFB': sh=12.7e6  # placeholder replaced below
    rev=g(r,'rev');oi=g(r,'oi');ocf=g(r,'ocf');cap=g(r,'capex');sbc=g(r,'sbc');da=g(r,'da')
    eq=g(r,'eq','last');debt=g(r,'ltd','last')+g(r,'std','last');cash=g(r,'cash','last')+g(r,'sti','last')
    mc=pr*sh; nd=debt-cash; ev=mc+nd
    fcf=ocf-cap
    # 5Y FCF
    o=fyd(r,'ocf'); c=fyd(r,'capex'); yrs=sorted(set(o)&set(c))[-5:]
    f5=[o[y]-c[y] for y in yrs]; a5=sum(f5)/len(f5) if f5 else 0
    revfy=r['rev']['fy']; g1=(rev/revfy[-2][1]-1) if r['rev']['ytd_m']==12 else (rev/revfy[-1][1]-1)
    nopat=oi*0.79; ic=eq+debt; ic_x=eq+debt-cash
    ebitda=oi+da
    print(f"{t:6} px {pr:8.2f} sh {sh/M:7.1f} mc {mc/M:8.0f} nd {nd/M:7.0f} ev {ev/M:8.0f} | rev {rev/M:7.0f} g {g1*100:5.1f}% | FCF {fcf/M:6.0f} y {fcf/mc*100:5.1f}% sbc/rev {sbc/rev*100:4.1f}% | 5yFCF {[round(x/M) for x in f5]} avg {a5/M:6.0f} | EV/EBITDA {ev/ebitda:5.1f} ND/EBITDA {nd/ebitda:4.1f} | ROIC {nopat/ic*100:5.1f}% xcash {nopat/ic_x*100:5.1f}% eq {eq/M:.0f}")
    for w in (0.10,0.12,0.13):
        fv=(a5/w - nd)/sh
        print(f"        naiveFV@{w:.0%} 5Yavg ${fv:7.2f} P/FV {pr/fv if fv>0 else float('nan'):5.2f}x   |  TTM-FCF FV ${(fcf/w-nd)/sh:7.2f} P/FV {pr/((fcf/w-nd)/sh):5.2f}x")
