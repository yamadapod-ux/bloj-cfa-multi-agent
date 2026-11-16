import json,urllib.request,datetime
UA={'User-Agent':'Mozilla/5.0'}
def ch(t): 
    d=json.loads(urllib.request.urlopen(urllib.request.Request(f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=6y&interval=1mo",headers=UA)).read())['chart']['result'][0]
    return {datetime.date.fromtimestamp(x).strftime('%Y-%m'):c for x,c in zip(d['timestamp'],d['indicators']['quote'][0]['close']) if c}
p=ch('SRAD'); fx=ch('EURUSD=X')
# FY rev EUR M, net cash EUR M (cash - borrowings) from SEC XBRL
REV={'2022-12':730.2,'2023-12':877.6,'2024-12':1106.6,'2025-12':1290.0}
NC={'2022-12':243.8-22.8,'2023-12':277.2-50.1,'2024-12':348.4-46.7,'2025-12':365.3-62.9}
SH=300.0  # econ shares approx (Class A + Class B/10), flagged
for k in REV:
    m=k; pr=p.get(m) or p.get(m[:5]+'11'); f=fx.get(m)
    mc=pr*SH/f; ev=mc-NC[k]; print(k,'px',round(pr,2),'fx',round(f,4),'EV/Rev',round(ev/REV[k],2))
cur_ev=12.81*296.1/1.1028-(190.1-59.2); print('now EV EURm',round(cur_ev),'EV/Rev TTM',round(cur_ev/1456.0,2),'fwd',round(cur_ev/1525.5,2))
