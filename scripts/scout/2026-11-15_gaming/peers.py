import json,urllib.request,time
UA={'User-Agent':'CFA-scout research research@example.com'}
def g(u): return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
for t,c in [('SRAD',1836470),('GENI',1834489),('DKNG',1883685),('RSI',1793659),('BRSL',1619762),('INSE',1615063)]:
    s=g(f'https://data.sec.gov/submissions/CIK{c:010d}.json'); print(t,s.get('sic'),s.get('sicDescription'),[f for f in s['filings']['recent']['form'][:12]])
    time.sleep(0.3)
def q(c,tags,cur='USD'):
    F=g(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json')['facts']['us-gaap']
    out={}
    for tg in tags:
        if tg in F:
            dd={}
            for x in F[tg]['units'].get(cur,F[tg]['units'].get('shares',[])):
                k=(x.get('start'),x['end'])
                if k not in dd or x['filed']>dd[k]['filed']: dd[k]=x
            out[tg]=[(x.get('start','')[:10],x['end'],round(x['val']/1e6,1)) for x in sorted(dd.values(),key=lambda x:x['end'])][-10:]
    return out
for t,c in [('DKNG',1883685),('RSI',1793659)]:
    print('==',t); r=q(c,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','LongTermDebt','LongTermDebtNoncurrent','ConvertibleNotesPayable','CashAndCashEquivalentsAtCarryingValue','WeightedAverageNumberOfDilutedSharesOutstanding'])
    for k,v in r.items(): print(' ',k,v)
    time.sleep(0.3)
