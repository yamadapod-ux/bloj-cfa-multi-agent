# Scout Round 87: SEC XBRL companyfacts + Yahoo beta for the Filter A survivors (CXW, GEO, NHI).
import urllib.request as u, json, os, time
H={'User-Agent':'bljcfa research yamadapod@gmail.com'}; HY={'User-Agent':'Mozilla/5.0'}
CIK={'CXW':1070985,'GEO':923796,'NHI':877860}
def get(url,path,hdr):
    if not os.path.exists(path):
        open(path,'wb').write(u.urlopen(u.Request(url,headers=hdr),timeout=60).read()); time.sleep(.3)
    return json.load(open(path,'rb'))
def annual(f,tags,n=7):
    g=f['facts'].get('us-gaap',{})
    out={}
    for t in tags:
        for un,rows in g.get(t,{}).get('units',{}).items():
            for r in rows:
                if r.get('fp')=='FY' and r.get('form','').startswith('10-K'):
                    d=(int(r['end'][:4]),)
                    s=r.get('start')
                    if s and (int(r['end'][:4])-int(s[:4])>1 or int(r['end'][5:7])-int(s[5:7]) not in(11,-1,0)): continue
                    out.setdefault(r['end'],{})[t]=r['val']
    return dict(sorted(out.items())[-n:])
TAGS={'OCF':['NetCashProvidedByUsedInOperatingActivities'],'Capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','PaymentsToAcquireRealEstate','PaymentsToAcquireAndDevelopRealEstate'],
'OpInc':['OperatingIncomeLoss'],'Rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'],'DA':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet'],
'Int':['InterestExpense','InterestExpenseNonoperating','InterestIncomeExpenseNet'],'Tax':['IncomeTaxExpenseBenefit'],'PTI':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],'NI':['NetIncomeLoss'],
'Eq':['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],'Debt':['LongTermDebt','LongTermDebtNoncurrent','DebtInstrumentCarryingAmount','SeniorLongTermNotes'],'Cash':['CashAndCashEquivalentsAtCarryingValue','CashAndCashEquivalentsAtCarryingValueIncludingRestrictedCash'],'TA':['Assets'],'TaxPay':['AccruedIncomeTaxesCurrent','AccruedIncomeTaxes','TaxesPayableCurrent'],'Sh':['CommonStockSharesOutstanding']}
for t,c in CIK.items():
    f=get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json',f'data/cf_{t}.json',H)
    print('=====',t,f['entityName'])
    g=f['facts'].get('us-gaap',{})
    for k,tags in TAGS.items():
        best={}
        for tg in tags:
            for un,rows in g.get(tg,{}).get('units',{}).items():
                for r in rows:
                    if not r.get('form','').startswith('10-'): continue
                    if 'start' in r:
                        days=(time.mktime(time.strptime(r['end'],'%Y-%m-%d'))-time.mktime(time.strptime(r['start'],'%Y-%m-%d')))/86400
                        lab=r['end'] if days>340 else (r['end']+f"~{int(days)}d" if r['end']>='2026' else None)
                        if lab is None: continue
                    else: lab=r['end']
                    if lab[:4]>='2020': best.setdefault(lab,(tg,r['val']))
        print(k,{a:b[1] for a,b in sorted(best.items())[-11:]}, set(b[0] for b in best.values()))
# beta 5y monthly
def rets(t):
    y=get(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=5y&interval=1mo',f'data/y_{t.replace("^","")}_5y.json',HY)['chart']['result'][0]
    c=y['indicators']['adjclose'][0]['adjclose'] if 'adjclose' in y['indicators'] else y['indicators']['quote'][0]['close']
    return dict(zip(y['timestamp'],c))
m=rets('^GSPC')
import statistics as st
for t in ['CXW','GEO','NHI']:
    a=rets(t); ks=sorted(set(a)&set(m)); ks=[k for k in ks if a[k] and m[k]]
    ra=[a[ks[i]]/a[ks[i-1]]-1 for i in range(1,len(ks))]; rm=[m[ks[i]]/m[ks[i-1]]-1 for i in range(1,len(ks))]
    b=st.covariance(ra,rm)/st.variance(rm); print(t,'raw beta',round(b,2),'Blume',round(.67*b+.33,2),'n',len(ra))
    d=get(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1y&interval=1d',f'data/y_{t}_1y.json',HY)['chart']['result'][0]
    q=d['indicators']['quote'][0]; hi=max((x,i) for i,x in enumerate(q['high']) if x)
    print('  52W high',round(hi[0],2),time.strftime('%Y-%m-%d',time.gmtime(d['timestamp'][hi[1]])))
