import json, urllib.request, datetime, sys
UA={'User-Agent':'Mozilla/5.0'}
def get(u):
    return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read())
out={}
for t in sys.argv[1:]:
    r={}
    try:
        d=get(f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1y&interval=1d")['chart']['result'][0]
        ts=d['timestamp']; q=d['indicators']['quote'][0]
        cl=q['close']; hi=q['high']; lo=q['low']
        idx=[i for i,c in enumerate(cl) if c is not None]
        last=idx[-1]
        hmax=max((h,i) for i,h in enumerate(hi) if h is not None)
        lmin=min((l,i) for i,l in enumerate(lo) if l is not None)
        r.update(y_close=round(cl[last],2), y_date=str(datetime.date.fromtimestamp(ts[last])),
                 y_hi=round(hmax[0],2), hi_date=str(datetime.date.fromtimestamp(ts[hmax[1]])),
                 y_lo=round(lmin[0],2), lo_date=str(datetime.date.fromtimestamp(ts[lmin[1]])))
    except Exception as e: r['y_err']=str(e)[:80]
    try:
        n=get(f"https://api.nasdaq.com/api/quote/{t}/info?assetclass=stocks")['data']
        r['n_last']=n['primaryData']['lastSalePrice']; r['n_52w']=n.get('keyStats',{}).get('fiftyTwoWeekHighLow',{}).get('value')
    except Exception as e: r['n_err']=str(e)[:80]
    if 'y_close' in r: r['pct_from_hi']=round((r['y_close']/r['y_hi']-1)*100,1)
    out[t]=r; print(t, r)
json.dump(out,open('prices.json','w'),indent=1)
