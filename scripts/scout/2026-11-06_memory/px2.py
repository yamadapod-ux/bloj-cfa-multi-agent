# Additional market data for scout: KRX SK hynix + FX, B-V1 peers (pre-registered before computing multiples).
import urllib.request as u, json, time
HY={'User-Agent':'Mozilla/5.0'}; H2={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
for t in ['000660.KS','KRW=X','NTAP','PSTG','005930.KS','SSNLF']:
    try:
        d=json.loads(u.urlopen(u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1y&interval=1d',headers=HY),timeout=30).read())['chart']['result'][0]
        q=d['indicators']['quote'][0]; days=[time.strftime('%Y-%m-%d',time.gmtime(x)) for x in d['timestamp']]; cc=dict(zip(days,q['close'])); vol=q['volume'][-10:]
        hi=max((x,i) for i,x in enumerate(q['high']) if x)
        print(t,'last',d['meta']['regularMarketPrice'],'cl1105',cc.get('2026-11-05'),'cl1106',cc.get('2026-11-06'),'hi',round(hi[0],2),days[hi[1]],'vol10d',vol[-5:])
    except Exception as e: print(t,'ERR',repr(e)[:90])
