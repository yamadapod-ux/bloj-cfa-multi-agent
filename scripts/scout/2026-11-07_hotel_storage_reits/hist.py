# Scout Round 88 -- close 11-06, 11-05 + 52W high/low from 2 sources: Yahoo chart + Nasdaq historical.
import urllib.request as u, json, sys, time, datetime as dt
H={'User-Agent':'Mozilla/5.0'}; H2={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
for t in sys.argv[1:]:
    ys=ns=''
    try:
        y=json.loads(u.urlopen(u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1y&interval=1d',headers=H),timeout=30).read())['chart']['result'][0]
        q=y['indicators']['quote'][0]; c=[(time.strftime('%m-%d',time.gmtime(a)),b) for a,b in zip(y['timestamp'],q['close']) if b]
        hi=max(x for x in q['high'] if x); lo=min(x for x in q['low'] if x); hic=max(b for a,b in c)
        p=c[-1][1]
        ys=f"Y {c[-1][0]} {p:.2f} prev {c[-2][1]:.2f} hi {hi:.2f} hiclose {hic:.2f} lo {lo:.2f} off {100*(p/hi-1):.1f}%"
    except Exception as e: ys='Y ERR '+repr(e)[:80]
    try:
        d=json.loads(u.urlopen(u.Request(f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass=stocks&fromdate=2026-11-02&limit=5&todate=2026-11-07',headers=H2),timeout=25).read())
        r=d['data']['tradesTable']['rows']; ns='N '+' '.join(f"{x['date'][:5]} {x['close']}" for x in r[:2])
    except Exception as e: ns='N ERR '+repr(e)[:80]
    print(f"{t:5} {ys} | {ns}",flush=True)
