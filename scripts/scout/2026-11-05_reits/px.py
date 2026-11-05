# Scout Round 86 — price + 52W high from 2 sources (Yahoo chart, Nasdaq.com quote), no SEC dependency.
import urllib.request as u, json, sys, time, statistics as st
H={'User-Agent':'Mozilla/5.0'}; H2={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
def ych(t,rng='1y',iv='1d'):
    return json.loads(u.urlopen(u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range={rng}&interval={iv}',headers=H),timeout=30).read())['chart']['result'][0]
for t in sys.argv[1:]:
    try:
        y=ych(t); q=y['indicators']['quote'][0]; p=y['meta']['regularMarketPrice']
        hi=max(x for x in q['high'] if x); lo=min(x for x in q['low'] if x)
        ts=time.strftime('%Y-%m-%d',time.gmtime(y['meta']['regularMarketTime']))
        ysum=f"Y {p} ({ts}) hi {hi:.2f} lo {lo:.2f} off {100*(p/hi-1):.1f}%"
    except Exception as e: ysum='Y ERR '+repr(e)[:70]
    try:
        d=json.loads(u.urlopen(u.Request(f'https://api.nasdaq.com/api/quote/{t}/info?assetclass=stocks',headers=H2),timeout=20).read())['data']
        nsum=f"N {d['primaryData']['lastSalePrice']} {d['primaryData']['lastTradeTimestamp']} 52W {d['keyStats']['fiftyTwoWeekHighLow']['value']}"
    except Exception as e: nsum='N ERR '+repr(e)[:70]
    print(f"{t:6} {ysum} | {nsum}")
