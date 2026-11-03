from hist import *
import json,sys
H2={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
for t in sys.argv[1:]:
    try:
        y=ych(t,'1y','1d'); q=y['indicators']['quote'][0]
        p=y['meta']['regularMarketPrice']; hi=max(x for x in q['high'] if x); lo=min(x for x in q['low'] if x)
        ts=time_.strftime('%Y-%m-%d',time_.gmtime(y['meta']['regularMarketTime']))
    except Exception as e: p=hi=None; ts=repr(e)
    try:
        d=json.loads(u.urlopen(u.Request(f'https://api.nasdaq.com/api/quote/{t}/info?assetclass=stocks',headers=H2),timeout=20).read())['data']
        np_=d['primaryData']['lastSalePrice']; nts=d['primaryData']['lastTradeTimestamp']; rng=d['keyStats']['fiftyTwoWeekHighLow']['value']
    except Exception as e: np_=nts=rng=repr(e)[:60]
    print(f"{t:5} Y {p} ({ts}) hi {hi} off {100*(p/hi-1) if p else 0:.1f}% | N {np_} {nts} 52W {rng}")
