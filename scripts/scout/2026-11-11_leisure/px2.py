# Round 92 -- 2nd price source: Yahoo meta (regularMarketPrice/time) + Nasdaq historical API with browser headers + stooq
import urllib.request as u, json, sys, time
H={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36','Accept':'application/json, text/plain, */*','Accept-Language':'en-US,en;q=0.9','Origin':'https://www.nasdaq.com','Referer':'https://www.nasdaq.com/'}
out={}
for t in sys.argv[1:]:
    r={}
    try:
        m=json.loads(u.urlopen(u.Request(f'https://query2.finance.yahoo.com/v8/finance/chart/{t}?range=5d&interval=1d',headers=H),timeout=30).read())['chart']['result'][0]['meta']
        r['ymeta']=(m.get('regularMarketPrice'),time.strftime('%Y-%m-%d %H:%M',time.gmtime(m.get('regularMarketTime',0))),m.get('fiftyTwoWeekHigh'))
    except Exception as e: r['ymeta']=f'ERR {e}'
    try:
        n=json.loads(u.urlopen(u.Request(f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass=stocks&fromdate=2025-11-10&limit=400',headers=H),timeout=30).read())['data']['tradesTable']['rows']
        hi=max(n,key=lambda x:float(x['high'].strip('$').replace(',','')))
        r['nasdaq']=(n[0]['date'],n[0]['close'],'hi',hi['high'],hi['date'])
    except Exception as e: r['nasdaq']=f'ERR {e}'
    try:
        s=u.urlopen(u.Request(f'https://stooq.com/q/l/?s={t.lower()}.us&f=sd2t2ohlc&h&e=csv',headers=H),timeout=30).read().decode()
        r['stooq']=s.strip().splitlines()[-1]
    except Exception as e: r['stooq']=f'ERR {e}'
    out[t]=r; print(t,r)
json.dump(out,open('data/px2.json','w'),indent=1)
