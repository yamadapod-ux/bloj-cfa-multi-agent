# Scout Round 86 — STWD: GAAP ROE, leverage, share growth from SEC companyfacts. Also NLY/AGNC TTM econ-return inputs. Run: python -I stwdfund.py
import json, datetime as dt
f=json.load(open('data/cf_STWD.json'))['facts']['us-gaap']
def fy(c,unit='USD'):
    o={}
    for x in f.get(c,{}).get('units',{}).get(unit,[]):
        if 'start' in x and 350<=(dt.date.fromisoformat(x['end'])-dt.date.fromisoformat(x['start'])).days<=380:
            if x['end'] not in o or x['filed']>o[x['end']][1]: o[x['end']]=(x['val'],x['filed'])
    return {k:v[0] for k,v in o.items()}
def inst(c,unit='USD'):
    o={}
    for x in f.get(c,{}).get('units',{}).get(unit,[]):
        if 'start' not in x and x.get('form') in('10-K','10-Q'):
            if x['end'] not in o or x['filed']>o[x['end']][1]: o[x['end']]=(x['val'],x['filed'])
    return {k:v[0] for k,v in o.items()}
ni=fy('NetIncomeLoss'); eq=inst('StockholdersEquity'); sh=inst('CommonStockSharesOutstanding','shares'); eps=fy('EarningsPerShareDiluted','USD/shares')
print('year NI eq ROE EPS sh')
ks=sorted(ni)[-6:]; rs=[]
for k in ks:
    e=eq.get(k); r=ni[k]/e if e else None; rs.append(r)
    print(k,round(ni[k]/1e6),round(e/1e6) if e else None,round(100*r,1) if r else None,eps.get(k),round(sh.get(k,0)/1e6,1))
print('5Y avg GAAP ROE',round(100*sum(rs[-5:])/5,2))
for k in sorted(eq)[-6:]: print('Q',k,round(eq[k]/1e6),round(sh.get(k,0)/1e6,1))
for c in ['DebtInstrumentCarryingAmount','SecuredDebt','UnsecuredDebt','LongTermDebt','DebtLongtermAndShorttermCombinedAmount','Liabilities','Assets']:
    v=inst(c)
    if v:
        k=max(v); print(c,k,round(v[k]/1e6))
