# Memory selloff scout + MU re-analysis: SEC companyfacts (annual + every quarter), Yahoo/Nasdaq price, 5Y beta.
import urllib.request as u, json, os, time, statistics as st, sys
H={'User-Agent':'bljcfa research'}; HY={'User-Agent':'Mozilla/5.0'}; H2={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'data')
CIK={'MU':723125,'WDC':106040,'STX':1137789,'SNDK':2023554}
def get(url,path,hdr):
    p=os.path.join(D,path)
    if not os.path.exists(p):
        open(p,'wb').write(u.urlopen(u.Request(url,headers=hdr),timeout=90).read()); time.sleep(.3)
    return json.load(open(p,'rb'))
TAGS={'Rev':['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','RevenueFromContractWithCustomerIncludingAssessedTax'],'COGS':['CostOfGoodsAndServicesSold','CostOfRevenue'],'OpInc':['OperatingIncomeLoss'],'NI':['NetIncomeLoss'],'PTI':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],'Tax':['IncomeTaxExpenseBenefit'],
'OCF':['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],'Capex':['PaymentsToAcquireProductiveAssets','PaymentsToAcquirePropertyPlantAndEquipment'],'DA':['DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet','DepreciationAndAmortization'],'SBC':['ShareBasedCompensation'],'DilSh':['WeightedAverageNumberOfDilutedSharesOutstanding'],
'Eq':['StockholdersEquity'],'TA':['Assets'],'Cash':['CashAndCashEquivalentsAtCarryingValue'],'STInv':['ShortTermInvestments','MarketableSecuritiesCurrent','AvailableForSaleSecuritiesDebtSecuritiesCurrent'],'LTInv':['LongTermInvestments','MarketableSecuritiesNoncurrent','AvailableForSaleSecuritiesDebtSecuritiesNoncurrent'],'EqInv':['EquityMethodInvestments','EquitySecuritiesFvNiCurrentAndNoncurrent','OtherLongTermInvestments'],'Debt':['LongTermDebt','DebtLongtermAndShorttermCombinedAmount'],'DebtCur':['LongTermDebtCurrent','DebtCurrent'],'DebtNC':['LongTermDebtNoncurrent'],'Lease':['OperatingLeaseLiability','FinanceLeaseLiability'],'CIP':['ConstructionInProgressGross'],'PPE':['PropertyPlantAndEquipmentNet'],'Sh':['EntityCommonStockSharesOutstanding','CommonStockSharesOutstanding'],'Div':['PaymentsOfDividendsCommonStock','PaymentsOfDividends'],'Buyback':['PaymentsForRepurchaseOfCommonStock']}
out={}
for t,c in CIK.items():
    f=get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json',f'cf_{t}.json',H)
    print('=====',t,f['entityName'])
    g=dict(f['facts'].get('us-gaap',{})); g.update(f['facts'].get('dei',{}))
    for k,tags in TAGS.items():
        ann={}; q={}; inst={}
        for tg in tags:
            for un,rows in g.get(tg,{}).get('units',{}).items():
                for r in rows:
                    if not r.get('form','').startswith('10-') or r['end']<'2015': continue
                    if 'start' in r:
                        days=(time.mktime(time.strptime(r['end'],'%Y-%m-%d'))-time.mktime(time.strptime(r['start'],'%Y-%m-%d')))/86400
                        if days>340 and days<380: ann.setdefault(r['end'],r['val'])
                        elif 80<days<100: q.setdefault(r['end'],r['val'])
                        elif r['end']>='2025': q.setdefault(r['end']+f'~{int(days)}d',r['val'])
                    else: inst.setdefault(r['end'],r['val'])
        fmt=lambda d,n:{a:(round(b/1e6) if abs(b)>1e5 else b) for a,b in sorted(d.items())[-n:]}
        if ann: print(k,'ANN',fmt(ann,11))
        if q: print(k,'QTR',fmt(q,8))
        if inst: print(k,'BAL',fmt(inst,6))
    fl=[r for rows in g.get('Assets',{}).get('units',{}).values() for r in rows]
    print('latest filing',max(((r['filed'],r['form'],r['accn'],r['end']) for r in fl))) if fl else None
def rets(t):
    y=get(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=5y&interval=1mo',f'y_{t.replace("^","")}_5y.json',HY)['chart']['result'][0]
    c=y['indicators']['adjclose'][0]['adjclose'] if 'adjclose' in y['indicators'] else y['indicators']['quote'][0]['close']
    return dict(zip(y['timestamp'],c))
m=rets('^GSPC')
for t in ['MU','WDC','STX','SNDK','SKHY']:
    try:
        a=rets(t); ks=[k for k in sorted(set(a)&set(m)) if a[k] and m[k]]
        ra=[a[ks[i]]/a[ks[i-1]]-1 for i in range(1,len(ks))]; rm=[m[ks[i]]/m[ks[i-1]]-1 for i in range(1,len(ks))]
        b=st.covariance(ra,rm)/st.variance(rm); print(t,'raw beta',round(b,2),'Blume',round(.67*b+.33,2),'n',len(ra))
    except Exception as e: print(t,'beta ERR',repr(e)[:80])
for t in ['MU','WDC','STX','SNDK','SKHY','SSNLF','^GSPC','^TNX','^VIX']:
    try:
        d=json.loads(u.urlopen(u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1y&interval=1d',headers=HY),timeout=30).read())['chart']['result'][0]
        q=d['indicators']['quote'][0]; days=[time.strftime('%Y-%m-%d',time.gmtime(x)) for x in d['timestamp']]
        hi=max((x,i) for i,x in enumerate(q['high']) if x); lo=min((x,i) for i,x in enumerate(q['low']) if x)
        cc=dict(zip(days,q['close']))
        print(t,'Y last',d['meta']['regularMarketPrice'],'cl1104',cc.get('2026-11-04'),'cl1105',cc.get('2026-11-05'),'hi',round(hi[0],2),days[hi[1]],'lo',round(lo[0],2),days[lo[1]],d['meta'].get('exchangeName'))
    except Exception as e: print(t,'Y ERR',repr(e)[:80])
    if t.startswith('^'): continue
    try:
        r=json.loads(u.urlopen(u.Request(f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass=stocks&fromdate=2026-11-03&todate=2026-11-06&limit=5',headers=H2),timeout=25).read())['data']['tradesTable']['rows']
        print('  Nasdaq',{x['date']:x['close'] for x in r})
    except Exception as e: print('  Nasdaq ERR',repr(e)[:80])
