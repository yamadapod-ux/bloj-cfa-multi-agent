from sec import *
import urllib.request as u, json, bisect, statistics as st
H={'User-Agent':'Mozilla/5.0'}
def ych(t,rng='6y',iv='1d'):
    fn=f'y_{t}_{rng}_{iv}.json'
    if os.path.exists(fn): return json.load(open(fn))
    r=u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range={rng}&interval={iv}&events=split',headers=H)
    d=json.loads(u.urlopen(r,timeout=30).read())['chart']['result'][0]; json.dump(d,open(fn,'w')); return d
def mkt(f,end):
    for c in ['CashCashEquivalentsAndShortTermInvestments']:
        v=inst1(f,[c],end)
        if v: return v
    cash=inst1(f,['CashAndCashEquivalentsAtCarryingValue'],end) or 0
    m=inst1(f,['MarketableSecuritiesCurrent','ShortTermInvestments'],end)
    if m is None: m=inst1(f,['AvailableForSaleSecuritiesDebtSecurities'],end) or 0
    return cash+m
def debt(f,end):
    a=inst1(f,['LongTermDebtNoncurrent'],end); b=inst1(f,['LongTermDebtCurrent','DebtCurrent'],end)
    if a is not None: d=a+(b or 0)
    else: d=inst1(f,['LongTermDebt'],end) or 0
    return d+(inst1(f,['CommercialPaper','ShortTermBorrowings'],end) or 0)
def shares(f,end,splits):
    s=[x for x in series(f,['WeightedAverageNumberOfDilutedSharesOutstanding']) if x.get('start') and x['end']==end]
    if not s:
        node=f['facts']['us-gaap'].get('CommonStockSharesOutstanding',{}).get('units',{}).get('shares',[])
        c=[x for x in node if x['end']==end]
        if not c: return None
        x=max(c,key=lambda x:x['filed']); fac=1
        for sd,r in splits:
            if x['filed']<sd: fac*=r
        return x['val']*fac
    # all versions, not dedup: pick via facts raw latest filed
    node=f['facts']['us-gaap']['WeightedAverageNumberOfDilutedSharesOutstanding']['units']['shares']
    c=[x for x in node if x['end']==end and x.get('start') and 80<=dur(x)<=100] or [x for x in node if x['end']==end and x.get('start')]
    x=max(c,key=lambda x:(x['filed'], -dur(x)))
    fac=1
    for sd,r in splits:
        if x['filed']<sd<=str(dt.date.today()): fac*=r
    return x['val']*fac
def run(t):
    f=facts(t); y=ych(t)
    ts=[time_.strftime('%Y-%m-%d',time_.gmtime(z)) for z in y['timestamp']]; cl=y['indicators']['quote'][0]['close']
    splits=[(time_.strftime('%Y-%m-%d',time_.gmtime(int(k))),v['numerator']/v['denominator']) for k,v in y.get('events',{}).get('splits',{}).items()]
    ends=sorted({x['end'] for x in series(f,REV) if x.get('start') and x['end']>='2021-06-01'})
    rows=[]
    for e in ends:
        r=ttm_at(f,REV,e); sh=shares(f,e,splits)
        if not r or not sh: continue
        i=bisect.bisect_right(ts,e)-1
        while cl[i] is None: i-=1
        p=cl[i]; nd=debt(f,e)-mkt(f,e); ev=p*sh+nd
        rows.append((e,p,sh,r,nd,ev/r))
    return rows,splits
import time as time_
if __name__=='__main__':
    import sys
    for t in sys.argv[1:]:
        rows,sp=run(t); print(t,'splits',sp)
        for e,p,sh,r,nd,m in rows: print(f'  {e} px {p:8.2f} sh {sh/1e9:7.3f}B revTTM {r/1e9:7.1f} netdebt {nd/1e9:7.1f} EV/Rev {m:5.2f}')
