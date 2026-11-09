# Round 91 Airlines -- price + 52W high/low: Yahoo chart API (1y daily) and Nasdaq.com quote/info API as 2nd source.
import urllib.request as u, json, time, sys
H={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
T=sys.argv[1:] or ['DAL','UAL','AAL','LUV','ALK','JBLU','ALGT','SKYW','RYAAY','CPA','ULCC','SNCY','SAVE','MESA']
out={}
for t in T:
    r={}
    try:
        y=json.loads(u.urlopen(u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1y&interval=1d',headers=H),timeout=30).read())['chart']['result'][0]
        q=y['indicators']['quote'][0]; rows=[(time.strftime('%Y-%m-%d',time.gmtime(a)),c,h,l) for a,c,h,l in zip(y['timestamp'],q['close'],q['high'],q['low']) if c]
        hi=max(rows,key=lambda x:x[2]); lo=min(rows,key=lambda x:x[3])
        r['y']=dict(last=rows[-1][0],close=round(rows[-1][1],2),hi=round(hi[2],2),hid=hi[0],lo=round(lo[3],2),lod=lo[0],prev=[(a,round(c,2)) for a,c,_,_ in rows[-3:]],ex=y['meta'].get('exchangeName'),name=y['meta'].get('longName'))
    except Exception as e: r['y']=f'ERR {e}'
    for cls in ('stocks',):
        try:
            n=json.loads(u.urlopen(u.Request(f'https://api.nasdaq.com/api/quote/{t}/info?assetclass={cls}',headers={**H,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}),timeout=30).read())['data']
            k=n.get('keyStats') or {}; p=n.get('primaryData') or {}
            r['n']=dict(price=p.get('lastSalePrice'),time=p.get('lastTradeTimestamp'),range52=(k.get('fiftyTwoWeekHighLow') or {}).get('value'),status=n.get('marketStatus'))
        except Exception as e: r['n']=f'ERR {e}'
    out[t]=r; print(t,json.dumps(r))
json.dump(out,open('data/px.json','w'),indent=1)
