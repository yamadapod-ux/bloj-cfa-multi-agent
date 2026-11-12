# Round 93 Asset Managers / Trust Banks -- price + 52W high: Yahoo chart API (1y daily); 2nd source stockanalysis.com page scrape.
import urllib.request as u, json, time, sys, re
H={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36','Accept':'*/*'}
T=sys.argv[1:]
out={}
for t in T:
    r={}
    try:
        y=json.loads(u.urlopen(u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1y&interval=1d',headers=H),timeout=30).read())['chart']['result'][0]
        q=y['indicators']['quote'][0]; rows=[(time.strftime('%Y-%m-%d',time.gmtime(a)),c,h,l) for a,c,h,l in zip(y['timestamp'],q['close'],q['high'],q['low']) if c]
        hi=max(rows,key=lambda x:x[2]); hc=max(rows,key=lambda x:x[1])
        r['y']=dict(last=rows[-1][0],close=round(rows[-1][1],2),hi=round(hi[2],2),hid=hi[0],hiclose=round(hc[1],2),hcd=hc[0],name=y['meta'].get('longName'))
    except Exception as e: r['y']=f'ERR {e}'
    try:
        h=u.urlopen(u.Request(f'https://stockanalysis.com/stocks/{t.lower()}/',headers=H),timeout=30).read().decode('utf8','ignore')
        m=re.search(r'"52-Week Range"\s*,\s*"?value"?\s*:\s*"([^"]+)"',h) or re.search(r'52-Week Range[^0-9]{0,200}?([\d,.]+\s*-\s*[\d,.]+)',h)
        p=re.search(r'quote:\{[^}]*?p:([\d.]+)',h) or re.search(r'"p":([\d.]+)',h)
        r['sa']=dict(range52=m.group(1) if m else None,price=p.group(1) if p else None)
    except Exception as e: r['sa']=f'ERR {e}'
    out[t]=r; print(t,json.dumps(r))
json.dump(out,open('data/px.json','w'),indent=1)
