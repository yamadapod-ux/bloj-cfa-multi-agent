# Scout Round 87: 2-source close check via Yahoo daily close and Nasdaq historical on the same date.
import urllib.request as u, json, sys
H={'User-Agent':'Mozilla/5.0'}; H2={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
D='2026-11-05'; DN='11/05/2026'
for t in sys.argv[1:]:
    try:
        y=json.loads(u.urlopen(u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=5d&interval=1d',headers=H),timeout=30).read())['chart']['result'][0]
        c=y['indicators']['quote'][0]['close']; yc=c[-1] if y['meta']['regularMarketTime'] else None
        import time
        days=[time.strftime('%Y-%m-%d',time.gmtime(x)) for x in y['timestamp']]
        yc=dict(zip(days,c)).get(D)
    except Exception as e: yc='ERR '+repr(e)[:50]
    try:
        d=json.loads(u.urlopen(u.Request(f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass=stocks&fromdate=2026-11-03&todate=2026-11-06&limit=5',headers=H2),timeout=25).read())['data']['tradesTable']['rows']
        nc={r['date']:r['close'] for r in d}
    except Exception as e: nc='ERR '+repr(e)[:50]
    print(t,'Yahoo',yc,'| Nasdaq',nc)
