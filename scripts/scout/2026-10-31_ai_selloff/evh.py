from hist import *
import sys,math
def ttm2(f,c,e):
    v=ttm_at(f,c,e)
    if v is not None: return v
    s=[x for x in series(f,c) if x.get('start') and 350<=dur(x)<=380 and x['end']<=e]
    return max(s,key=lambda x:x['end'])['val'] if s else None
def ebit(f,e):
    v=ttm2(f,OPI,e)
    if v is None:
        p=ttm2(f,PTI+['IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],e); i=ttm2(f,['InterestExpense','InterestExpenseNonoperating','InterestExpenseDebt'],e) or 0
        v=p+i if p is not None else None
    return v
for t in sys.argv[1:]:
    f=facts(t); y=ych(t)
    ts=[time_.strftime('%Y-%m-%d',time_.gmtime(z)) for z in y['timestamp']]; cl=y['indicators']['quote'][0]['close']
    sp=[(time_.strftime('%Y-%m-%d',time_.gmtime(int(k))),v['numerator']/v['denominator']) for k,v in y.get('events',{}).get('splits',{}).items()]
    ends=sorted({x['end'] for x in series(f,REV) if x.get('start') and x['end']>='2021-09-01'})
    rows=[]
    for e in ends:
        eb=ebit(f,e); da=ttm2(f,DA,e) or 0; sh=shares(f,e,sp)
        if eb is None or not sh: continue
        i=bisect.bisect_right(ts,e)-1
        while cl[i] is None:i-=1
        ev=cl[i]*sh+debt(f,e)-mkt(f,e); E=eb+da
        if E>0: rows.append((e,ev/E,E))
    e=ends[-1]; eb=ebit(f,e); da=ttm2(f,DA,e) or 0; sh=shares(f,e,sp)
    p=y['meta']['regularMarketPrice']; ev=p*sh+debt(f,e)-mkt(f,e); cur=ev/(eb+da)
    h=sorted(m for _,m,_ in rows)
    pct=sum(1 for m in h if m<=cur)/len(h)*100 if h else float('nan')
    q33=h[int(len(h)/3)] if h else float('nan')
    print(f"{t:5} cur EV/EBITDA {cur:5.1f} (EBITDA {(eb+da)/1e9:.2f}B) 5Y n={len(h)} min {h[0]:.1f} p33 {q33:.1f} med {h[len(h)//2]:.1f} max {h[-1]:.1f} pctile {pct:.0f} -> {'B PASS' if cur<=q33 else 'B fail'}")
