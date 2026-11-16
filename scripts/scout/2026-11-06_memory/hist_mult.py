# 5-10Y multiples history for MU/WDC/STX: month-end price x diluted shares vs annual SEC financials (EV/Revenue, EV/EBITDA, P/E approx.).
import json, os, time, statistics as st
D='data'; 
def cf(t): return json.load(open(f'{D}/cf_{t}.json','rb'))['facts']['us-gaap']
def ann(g,tags):
    o={}
    for tg in tags:
        for rows in g.get(tg,{}).get('units',{}).values():
            for r in rows:
                if r.get('form','').startswith('10-') and 'start' in r:
                    d=(time.mktime(time.strptime(r['end'],'%Y-%m-%d'))-time.mktime(time.strptime(r['start'],'%Y-%m-%d')))/86400
                    if 340<d<380: o.setdefault(r['end'],r['val'])
    return dict(sorted(o.items()))
for t in ['MU','WDC','STX']:
    g=cf(t); y=json.load(open(f'{D}/y_{t}_5y.json','rb'))['chart']['result'][0]; px=dict(zip(y['timestamp'],y['indicators']['quote'][0]['close']))
    rev=ann(g,['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues']); op=ann(g,['OperatingIncomeLoss']); da=ann(g,['DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet','DepreciationAndAmortization']); sh=ann(g,['WeightedAverageNumberOfDilutedSharesOutstanding'])
    ev=[];ee=[]
    for ts,p in sorted(px.items()):
        if not p: continue
        ds=time.strftime('%Y-%m-%d',time.gmtime(ts)); fy=[k for k in rev if k<=ds]
        if not fy: continue
        k=fy[-1]; mc=p*sh.get(k,list(sh.values())[-1])/1e6; r=rev[k]/1e6; e=(op.get(k,0)+da.get(k,0))/1e6
        ev.append((ds,mc/r)); 
        if e>0: ee.append((ds,mc/e))
    v=sorted(x for _,x in ev); w=sorted(x for _,x in ee)
    print(t,'P/S(mktcap/last-FY rev) n',len(v),'min %.2f p33 %.2f med %.2f p70 %.2f max %.2f'%(v[0],v[len(v)//3],st.median(v),v[int(len(v)*.7)],v[-1]),'| mcap/EBITDA n',len(w),'min %.2f p33 %.2f med %.2f p70 %.2f max %.2f'%(w[0],w[len(w)//3],st.median(w),w[int(len(w)*.7)],w[-1]))
    print('  rev',{k:round(a/1e6) for k,a in list(rev.items())[-11:]})
    print('  opm',{k:round(100*op[k]/rev[k],1) for k in list(rev)[-11:] if k in op})
