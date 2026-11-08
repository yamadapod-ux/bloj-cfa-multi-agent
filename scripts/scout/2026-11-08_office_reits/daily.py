# Round 89 -- daily closes for selected tickers (Yahoo) to check post-event highs / one-day moves.
import urllib.request as u, json, sys, time
H={'User-Agent':'Mozilla/5.0'}
t=sys.argv[1]; start=sys.argv[2]
y=json.loads(u.urlopen(u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1y&interval=1d&events=split',headers=H),timeout=30).read())['chart']['result'][0]
q=y['indicators']['quote'][0]
rows=[(time.strftime('%Y-%m-%d',time.gmtime(a)),c,h,v) for a,c,h,v in zip(y['timestamp'],q['close'],q['high'],q['volume']) if c]
print(t,'splits',y.get('events',{}).get('splits'))
sub=[r for r in rows if r[0]>=start]
hi=max(sub,key=lambda r:r[2]); hc=max(sub,key=lambda r:r[1])
print(f"since {start}: max high {hi[2]:.2f} on {hi[0]} | max close {hc[1]:.2f} on {hc[0]} | last {sub[-1][0]} {sub[-1][1]:.2f} -> off high {100*(sub[-1][1]/hi[2]-1):.1f}%")
for r in sub[-int(sys.argv[3]) if len(sys.argv)>3 else -8:]: print(r[0],round(r[1],2))
