# usage: python -I quinn_multiples.py <cf_ADBE.json> <yahoo_dir>
import json,sys,statistics as st
from datetime import date,datetime,timezone
# StockAnalysis quarterly ratios (https://stockanalysis.com/stocks/adbe/financials/ratios/?p=quarterly, fetched 2026-11-08)
SA={ # period: (fwdPE, EV/Sales, EV/EBITDA, PE)
'Q4-21':(45.17,18.49,44.29,60.84),'Q1-22':(32.79,13.14,31.51,44.18),'Q2-22':(30.41,12.16,29.54,41.53),'Q3-22':(25.35,9.99,24.73,35.80),
'Q4-22':(23.09,8.96,22.67,33.39),'Q1-23':(22.52,8.68,22.46,33.31),'Q2-23':(27.39,10.78,28.13,41.24),'Q3-23':(33.83,13.46,34.94,50.13),
'Q4-23':(35.27,14.19,36.62,51.37),'Q1-24':(31.86,12.77,32.46,53.82),'Q2-24':(24.17,9.62,24.27,39.23),'Q3-24':(29.84,12.07,30.13,47.52),
'Q4-24':(25.95,10.49,26.01,40.85),'Q1-25':(21.50,8.57,21.14,28.25),'Q2-25':(19.88,7.79,19.23,25.76),'Q3-25':(16.31,6.57,16.31,21.75),
'Q4-25':(14.03,5.67,14.15,18.80),'Q1-26':(11.17,4.38,10.92,14.84),'Q2-26':(10.76,4.15,10.44,14.49),'Q3-26':(11.24,4.52,11.50,15.91)}
CUR=(8.91,3.63,9.51,13.36)
def pct(v,arr): return sum(1 for a in arr if a<v)/len(arr)
names=['Fwd P/E','EV/Sales','EV/EBITDA','P/E TTM']
for i,n in enumerate(names):
    arr=[x[i] for x in SA.values()]
    print(f"{n}: current {CUR[i]} | 5Y min {min(arr)} median {st.median(arr):.2f} max {max(arr)} | percentile {pct(CUR[i],arr):.0%} (n={len(arr)}) | z={(CUR[i]-st.mean(arr))/st.stdev(arr):.2f}")
# independent monthly EV/TTM revenue from SEC XBRL + Yahoo
d=json.load(open(sys.argv[1],encoding='utf-8'))['facts']['us-gaap']
def dur(tag,lo,hi):
    o={}
    for u in d[tag]['units'].values():
        for x in u:
            if 'start' in x and lo<=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<=hi: o[x['end']]=x['val']
    return o
qa=dur('Revenues',80,100); an=dur('Revenues',350,380)
# derive Q4s
q=dict(qa)
ends=sorted(an)
for e in ends:
    ed=date.fromisoformat(e)
    prior=[k for k in qa if 0<(ed-date.fromisoformat(k)).days<300]
    if len(prior)==3: q[e]=an[e]-sum(qa[k] for k in prior)
qs=sorted(q)
ttm={qs[i]:sum(q[qs[j]] for j in range(i-3,i+1)) for i in range(3,len(qs))}
sh=dur('WeightedAverageNumberOfDilutedSharesOutstanding',80,100)
r=json.load(open(sys.argv[2]+'/ADBE.json'))['chart']['result'][0]
px=[(datetime.fromtimestamp(t,timezone.utc).date(),c) for t,c in zip(r['timestamp'],r['indicators']['quote'][0]['close']) if c]
mon={}
for dt,c in px: mon[(dt.year,dt.month)]=(dt,c)
vals=[]
for k,(dt,c) in sorted(mon.items()):
    if dt<date(2021,11,1): continue
    fin=[e for e in ttm if date.fromisoformat(e)<=dt]
    if not fin: continue
    e=max(fin); se=[x for x in sh if x<=e]
    s=sh[max(se)] if se else None
    if s is None: continue
    vals.append((dt,c*s/ttm[e]))  # mcap/TTM rev (net debt small, ~1% of EV)
cur=vals[-1][1]; arr=[v for _,v in vals[:-1]]
print(f"Monthly Mcap/TTM Rev (SEC+Yahoo, n={len(arr)}): current {cur:.2f} | min {min(arr):.2f} median {st.median(arr):.2f} max {max(arr):.2f} | percentile {pct(cur,arr):.0%}")
print('first',vals[0],'last',vals[-1])
