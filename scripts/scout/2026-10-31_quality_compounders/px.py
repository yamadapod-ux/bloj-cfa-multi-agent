import urllib.request as u, json, sys, time
H={'User-Agent':'Mozilla/5.0'}
def chart(t,rng='1y',iv='1d'):
    r=u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range={rng}&interval={iv}',headers=H)
    return json.loads(u.urlopen(r,timeout=20).read())['chart']['result'][0]
out={}
for t in sys.argv[1:]:
    try:
        c=chart(t); q=c['indicators']['quote'][0]; ts=c['timestamp']
        cl=[x for x in q['close'] if x]; hi=max(x for x in q['high'] if x)
        last=c['meta']['regularMarketPrice']; d=time.strftime('%Y-%m-%d',time.gmtime(ts[-1]))
        out[t]=(last,hi,d); print(f"{t:6} {d} last {last:9.2f} 52wHi {hi:9.2f} off {100*(last/hi-1):6.1f}%")
    except Exception as e: print(t,'ERR',e)
json.dump(out,open('px_'+sys.argv[1]+'.json','w'))
