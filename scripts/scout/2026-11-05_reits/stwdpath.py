# Scout Round 86 — STWD daily path since Aug + largest moves; peer comparison for mREIT selloff. Run: python -I stwdpath.py
import json, time, urllib.request as u
H={'User-Agent':'Mozilla/5.0'}
def y(t):
    d=json.loads(u.urlopen(u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=6mo&interval=1d',headers=H),timeout=30).read())['chart']['result'][0]
    return [(time.strftime('%Y-%m-%d',time.gmtime(a)),c) for a,c in zip(d['timestamp'],d['indicators']['quote'][0]['close']) if c]
s=y('STWD'); print('monthly',[x for i,x in enumerate(s) if i%21==0],s[-1])
mv=sorted(((s[i][1]/s[i-1][1]-1,s[i][0],round(s[i][1],2)) for i in range(1,len(s))),key=lambda x:x[0])[:6]
print('worst days',[(round(a*100,1),b,c) for a,b,c in mv]); lo=min(s,key=lambda x:x[1]); print('low',lo)
for t in ['BXMT','ARI','KREF','RITM','RC','LADR','ABR','TRTX']:
    p=y(t); print(t,'6mo',round(100*(p[-1][1]/p[0][1]-1),1),'last',round(p[-1][1],2),'hi6m',round(max(c for _,c in p),2),'off',round(100*(p[-1][1]/max(c for _,c in p)-1),1))
