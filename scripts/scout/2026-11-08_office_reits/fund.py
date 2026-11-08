# Scout Round 89 -- beta (5Y monthly vs ^GSPC, Blume), trailing dividend yield history, latest market quote cross-check.
import urllib.request as u, json, statistics as st, sys
H={'User-Agent':'Mozilla/5.0'}
def ch(t,rng,iv,ev=''):
    return json.loads(u.urlopen(u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range={rng}&interval={iv}{ev}',headers=H),timeout=30).read())['chart']['result'][0]
g=ch('%5EGSPC','5y','1mo'); gm=dict(zip(g['timestamp'],g['indicators']['quote'][0]['close']))
tn=ch('%5ETNX','5d','1d'); print('TNX',list(zip(tn['timestamp'],tn['indicators']['quote'][0]['close']))[-2:],tn['meta']['regularMarketPrice'])
for t in sys.argv[1:]:
    y=ch(t,'5y','1mo','&events=div'); ts=y['timestamp']; c=y['indicators']['adjclose'][0]['adjclose'] if 'adjclose' in y['indicators'] else y['indicators']['quote'][0]['close']; raw=y['indicators']['quote'][0]['close']
    gs=[gm.get(x) for x in ts]
    rs=[];rg=[]
    for i in range(1,len(ts)):
        if c[i] and c[i-1] and gs[i] and gs[i-1]:
            rs.append(c[i]/c[i-1]-1); rg.append(gs[i]/gs[i-1]-1)
    mg=st.mean(rg); ms=st.mean(rs)
    beta=sum((a-ms)*(b-mg) for a,b in zip(rs,rg))/sum((b-mg)**2 for b in rg)
    divs=sorted((int(v['date']),v['amount']) for v in y.get('events',{}).get('dividends',{}).values())
    ys=[]
    for x,p in zip(ts,raw):
        if p:
            tot=sum(a for d,a in divs if x-365*86400<d<=x)
            if x-ts[0]>=330*86400: ys.append(100*tot/p)
    # price range (raw monthly closes) for rough 5Y context
    q=ch(t,'5d','1d'); qp=q['meta']['regularMarketPrice']
    print(f"{t:5} n={len(rs)} rawbeta {beta:.2f} blume {0.67*beta+0.33:.2f} | div12m last {sum(a for d,a in divs if ts[-1]-365*86400<d<=ts[-1]):.3f} yldnow {(ys or [0])[-1]:.2f}% med {st.median(ys or [0]):.2f}% n={len(ys)} | Yquote {qp} last-divs {[round(a,3) for d,a in divs[-5:]]}",flush=True)
