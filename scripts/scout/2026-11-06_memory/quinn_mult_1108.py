# Quinn MU multiple percentile 2026-11-08: monthly EV/TTM Sales, EV/TTM EBITDA, trailing P/E, ex-post NTM P/E
# Sources: SEC XBRL companyfacts (data/cf_MU.json), Yahoo daily close (data/q1108/d_MU.json). Balance sheet = latest period end <= month end (ignores ~5wk filing lag).
import json,os,datetime as dt,statistics as st
B=os.path.dirname(os.path.abspath(__file__))
g=json.load(open(f'{B}/data/cf_MU.json','rb'))['facts']['us-gaap']
D=dt.date.fromisoformat
def flows(tags):
    # cumulative YTD values grouped by fiscal-year start -> difference to get each quarter
    cum={}
    for t in tags:
        for rows in g.get(t,{}).get('units',{}).values():
            for r in rows:
                if 'start' not in r or not r.get('form','').startswith('10-'): continue
                d=(D(r['end'])-D(r['start'])).days
                if d<80 or d>380: continue
                cum.setdefault(r['start'],{}).setdefault(r['end'],r['val'])
    q={}
    for s0,ser in cum.items():
        prev=0
        for e in sorted(ser):
            if (D(e)-D(s0)).days<105 or prev or e==min(ser):
                pass
            q.setdefault(e,ser[e]-prev) if (D(e)-D(s0)).days<105 or prev else None
            prev=ser[e]
    return dict(sorted(q.items()))
def stock(tags):
    o={}
    for t in tags:
        for rows in g.get(t,{}).get('units',{}).values():
            for r in rows:
                if 'start' in r: continue
                o.setdefault(r['end'],0); o[r['end']]=r['val'] if t==tags[0] else o[r['end']]
    return o
def bs(t):
    o={}
    for rows in g.get(t,{}).get('units',{}).values():
        for r in rows:
            if 'start' not in r: o[r['end']]=r['val']
    return o
rev=flows(['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet']); oi=flows(['OperatingIncomeLoss']); da=flows(['DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet']); ni=flows(['NetIncomeLoss'])
sh={}
for rows in g['WeightedAverageNumberOfDilutedSharesOutstanding']['units'].values():
    for r in rows:
        if 'start' in r and (D(r['end'])-D(r['start'])).days<105: sh[r['end']]=r['val']   # 3-month diluted weighted avg (shares, not differenced)
for rows in g['WeightedAverageNumberOfDilutedSharesOutstanding']['units'].values():
    for r in rows:
        if 'start' in r: sh.setdefault(r['end'],r['val'])
cash=bs('CashAndCashEquivalentsAtCarryingValue'); afc=bs('AvailableForSaleSecuritiesDebtSecuritiesCurrent'); afn=bs('AvailableForSaleSecuritiesDebtSecuritiesNoncurrent')
debt=bs('LongTermDebt') or {}; dc=bs('DebtCurrent'); dl=bs('LongTermDebtNoncurrent')
ends=sorted(rev)
def ttm(f,e):
    k=[x for x in sorted(f) if x<=e][-4:]
    return sum(f[x] for x in k) if len(k)==4 and (D(k[-1])-D(k[0])).days<300 else None
def last(dct,e):
    k=[x for x in dct if x<=e]; return dct[max(k)] if k else 0
r=json.load(open(f'{B}/data/q1108/d_MU.json'))['chart']['result'][0]
px={}
for ts,c in zip(r['timestamp'],r['indicators']['quote'][0]['close']):
    if c: d=dt.datetime.utcfromtimestamp(ts).date(); px[(d.year,d.month)]=(d,c)
px[(2026,11)]=(dt.date(2026,11,5),656.39)
rows=[]
for (y,m),(d,p) in sorted(px.items()):
    if d<dt.date(2016,10,1): continue
    e=max(x for x in ends if x<=d.isoformat()); s=last(sh,e) or sh[max(sh)]
    mc=p*s; nd=last(debt,e) if debt else last(dc,e)+last(dl,e)
    netc=last(cash,e)+last(afc,e)+last(afn,e)-nd
    ev=mc-netc; R=ttm(rev,e); O=ttm(oi,e); A=ttm(da,e); N=ttm(ni,e)
    if not R: continue
    # ex-post NTM net income (perfect-foresight forward P/E) where available
    fut=[x for x in sorted(ni) if x>e][:4]; NTM=sum(ni[x] for x in fut) if len(fut)==4 else None
    rows.append(dict(d=d,p=p,evs=ev/R,eve=ev/(O+A) if A and O+A>0 else None,pe=mc/N if N>0 else None,fpe=mc/NTM if NTM and NTM>0 else None,opm=O/R))
cur=rows[-1]; print('current',cur['d'],'EV/S %.2f EV/EBITDA %.2f P/E %.2f TTM opm %.1f%%'%(cur['evs'],cur['eve'],cur['pe'],cur['opm']*100))
def pct(vals,x): v=[a for a in vals if a is not None]; return 100*sum(1 for a in v if a<x)/len(v),len(v),st.median(v),sorted(v)[int(.7*len(v))]
for lab,start in [('5Y',dt.date(2021,11,1)),('10Y',dt.date(2016,11,1))]:
    R=[x for x in rows if x['d']>=start][:-1]
    for k in ['evs','eve','pe']:
        p,n,md,p70=pct([x[k] for x in R],cur[k]); print('%s %-4s pctile %.0f%% (n=%d, median %.2f, p70 %.2f)'%(lab,k,p,n,md,p70))
    f=[x['fpe'] for x in R if x['fpe']]; print('%s ex-post NTM P/E n=%d median %.1f min %.1f max %.1f'%(lab,len(f),st.median(f),min(f),max(f)))
# peak-margin context: EV/S at past margin peaks
for x in rows:
    if x['d'].month in (8,) or x['d']>=dt.date(2026,6,1): print(x['d'],'EV/S %.2f EV/EBITDA %s P/E %s TTM opm %.1f%% NTM-PE %s'%(x['evs'],None if not x['eve'] else round(x['eve'],2),None if not x['pe'] else round(x['pe'],1),x['opm']*100,None if not x['fpe'] else round(x['fpe'],1)))
