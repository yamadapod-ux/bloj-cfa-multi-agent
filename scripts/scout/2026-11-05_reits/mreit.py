# Scout Round 86 — mREIT framework: P/B history, economic return, CoE. SEC companyfacts + Yahoo chart. Run with: python -I mreit.py
import urllib.request as u, json, os, time, statistics as st, datetime as dt, re
os.makedirs('data',exist_ok=True)
UA={'User-Agent':'CFA-Fund-Scout research-script'}; H={'User-Agent':'Mozilla/5.0'}
Rf=0.0489; ERP=0.0441  # ^TNX 4.894 close 11-04; Damodaran implied ERP 4.41% (R85 source, 2026-11-01)
CIK={'NLY':1043219,'AGNC':1423689,'STWD':1465128}
def cache(url,fn,h):
    fn='data/'+fn
    if not os.path.exists(fn): open(fn,'wb').write(u.urlopen(u.Request(url,headers=h),timeout=60).read())
    return json.load(open(fn))
def facts(t): return cache(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK[t]:010d}.json',f'cf_{t}.json',UA)
def ych(t,r,i): return cache(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range={r}&interval={i}&events=div%7Csplit',f'y_{t.strip("^")}_{r}_{i}.json',H)['chart']['result'][0]
def inst(f,cs,unit='USD'):
    out={}
    for c in cs:
        for x in f['facts']['us-gaap'].get(c,{}).get('units',{}).get(unit,[]):
            if x.get('form') in('10-K','10-Q') and 'start' not in x:
                k=x['end']
                if k not in out or x['filed']>out[k][1]: out[k]=(x['val'],x['filed'])
    return {k:v[0] for k,v in out.items()}
def beta(t):
    a=ych(t,'5y','1mo'); b=ych('^GSPC','5y','1mo')
    A=dict(zip(a['timestamp'],a['indicators']['adjclose'][0]['adjclose'])); B=dict(zip(b['timestamp'],b['indicators']['adjclose'][0]['adjclose']))
    k=[x for x in sorted(A) if x in B and A[x] and B[x]]
    ra=[A[k[i]]/A[k[i-1]]-1 for i in range(1,len(k))]; rb=[B[k[i]]/B[k[i-1]]-1 for i in range(1,len(k))]
    ma,mb=st.mean(ra),st.mean(rb)
    return sum((x-ma)*(y-mb) for x,y in zip(ra,rb))/(len(ra)-1)/st.variance(rb)
for t in CIK:
    f=facts(t)
    eq=inst(f,['StockholdersEquity']); pref=inst(f,['PreferredStockValue','PreferredStockValueOutstanding','PreferredStockLiquidationPreferenceValue'])
    sh=inst(f,['CommonStockSharesOutstanding','EntityCommonStockSharesOutstanding'],'shares')
    y=ych(t,'6y','1d'); ts=y['timestamp']; cl=y['indicators']['quote'][0]['close']
    dates=[time.strftime('%Y-%m-%d',time.gmtime(z)) for z in ts]
    splits=[(time.strftime('%Y-%m-%d',time.gmtime(int(k))),v['numerator']/v['denominator']) for k,v in y.get('events',{}).get('splits',{}).items()]
    divs=sorted((time.strftime('%Y-%m-%d',time.gmtime(int(k))),v['amount']) for k,v in y.get('events',{}).get('dividends',{}).items())
    rows=[]
    for e in sorted(eq):
        if e<'2020-12-01' or e not in sh: continue
        s=sh[e]
        for sd,r in splits:
            if e<sd: s*=r  # restate pre-split shares (yahoo closes are split-adjusted)
        px=[c for d,c in zip(dates,cl) if d<=e and c]
        p=px[-1] if px else None
        bv=(eq[e]-(pref.get(e) or 0))/s
        rows.append((e,round(bv,2),round(p,2),round(p/bv,2),pref.get(e)))
    print('\n==',t,'splits',splits,'latest XBRL',rows[-1][0] if rows else None)
    for r in rows[-24:]: print(r)
    pbs=[r[3] for r in rows[-20:]]
    print('P/B 5Y (20q) min/med/max',min(pbs),st.median(pbs),max(pbs))
    print('dividends last 5Y sum',round(sum(a for d,a in divs if d>='2021-09-30'),2),'TTM',round(sum(a for d,a in divs if d>='2025-11-05'),2),'last',divs[-5:])
    # economic return from 2021-09-30 BV (or nearest) to latest
    r0=min(rows,key=lambda r:abs((dt.date.fromisoformat(r[0])-dt.date(2021,9,30)).days)); r1=rows[-1]
    dv=sum(a for d,a in divs if r0[0]<d<=r1[0]); yrs=(dt.date.fromisoformat(r1[0])-dt.date.fromisoformat(r0[0])).days/365.25
    er=((r1[1]+dv)/r0[1])-1
    print(f'Econ return {r0[0]} BV {r0[1]} -> {r1[0]} BV {r1[1]} + div {dv:.2f}: total {er*100:.1f}% simple/yr {er/yrs*100:.1f}% ; BV CAGR {((r1[1]/r0[1])**(1/yrs)-1)*100:.1f}%')
    b=beta(t); bb=.67*b+.33
    print(f'beta raw {b:.2f} blume {bb:.2f} CoE {100*(Rf+bb*ERP):.2f}%')
