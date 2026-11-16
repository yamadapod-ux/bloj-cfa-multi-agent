import urllib.request as u, json, os, datetime as dt
UA={'User-Agent':'CFA research yamadapod@gmail.com'}
def get(url,fn):
    if os.path.exists(fn): return json.load(open(fn))
    d=json.loads(u.urlopen(u.Request(url,headers=UA),timeout=60).read()); json.dump(d,open(fn,'w')); return d
TK=get('https://www.sec.gov/files/company_tickers.json','tickers.json')
CIK={v['ticker']:v['cik_str'] for v in TK.values()}
def facts(t):
    return get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK[t]:010d}.json',f'cf_{t}.json')
D=lambda s: dt.date.fromisoformat(s)
def series(f,concepts,tax='us-gaap'):
    "return list of facts (dedup by start,end keep latest filed) for first concept with data, merged across concepts"
    res={}
    for c in concepts:
        node=f['facts'].get(tax,{}).get(c)
        if not node: continue
        for unit,arr in node['units'].items():
            for x in arr:
                if x.get('form') not in ('10-K','10-Q','10-K/A','10-Q/A','20-F','40-F'): continue
                k=(x.get('start'),x['end'])
                if k not in res or x['filed']>res[k]['filed']: res[k]=dict(x,concept=c)
    return list(res.values())
def dur(x): return (D(x['end'])-D(x['start'])).days
def ttm_at(f,concepts,end=None):
    s=[x for x in series(f,concepts) if x.get('start')]
    if not s: return None
    if end is None: end=max(x['end'] for x in s)
    cand=[x for x in s if x['end']==end]
    for x in cand:
        if 350<=dur(x)<=380: return x['val']
    ytd=sorted(cand,key=dur,reverse=True)
    if not ytd: return None
    y=ytd[0]; L=dur(y); e=D(end)
    # prior FY ending before start of y... FY that ends at y.start-1
    fy=[x for x in s if 350<=dur(x)<=380 and abs((D(x['end'])-(D(y['start'])-dt.timedelta(1))).days)<=7]
    py=[x for x in s if abs(dur(x)-L)<=7 and abs((D(x['end'])-(e-dt.timedelta(365))).days)<=7]
    if fy and py: return fy[0]['val']+y['val']-py[0]['val']
    return None
def inst(f,concepts,end=None):
    tot=0;found=False
    for c in concepts if isinstance(concepts[0],tuple) else [(c,) for c in concepts]:
        pass
def inst1(f,concepts,end):
    for c in concepts:
        s=[x for x in series(f,[c]) if not x.get('start') and x['end']==end]
        if s: return s[0]['val']
    return None
def inst_latest(f,c):
    s=[x for x in series(f,[c]) if not x.get('start')]
    return max(s,key=lambda x:x['end']) if s else None
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueNet']
CFO=['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations']
CAPEX=['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','PaymentsForProceedsFromProductiveAssets','PaymentsToAcquireOtherPropertyPlantAndEquipment']
OPI=['OperatingIncomeLoss']
DA=['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet','Depreciation']
TAX=['IncomeTaxExpenseBenefit']
PTI=['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments']
EQ=['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest']
CASH=['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents']
MKT=['MarketableSecuritiesCurrent','ShortTermInvestments','AvailableForSaleSecuritiesDebtSecuritiesCurrent','MarketableSecurities']
DEBTS=[['LongTermDebt'],['LongTermDebtNoncurrent','LongTermDebtAndCapitalLeaseObligations'],['LongTermDebtCurrent','LongTermDebtAndCapitalLeaseObligationsCurrent'],['CommercialPaper','ShortTermBorrowings','DebtCurrent']]
def bs(f,end):
    cash=inst1(f,CASH,end) or 0; mkt=inst1(f,MKT,end) or 0
    ltd=inst1(f,['LongTermDebt'],end)
    if ltd is None: ltd=(inst1(f,DEBTS[1],end) or 0)+(inst1(f,DEBTS[2],end) or 0)
    std=inst1(f,['CommercialPaper','ShortTermBorrowings'],end) or 0
    return dict(cash=cash,mkt=mkt,debt=ltd+std,eq=inst1(f,EQ,end))
def shares_cover(f):
    s=f['facts'].get('dei',{}).get('EntityCommonStockSharesOutstanding')
    arr=[x for u_ in s['units'].values() for x in u_]
    last=max(x['end'] for x in arr); acc=max(x['accn'] for x in arr if x['end']==last)
    return sum(x['val'] for x in arr if x['end']==last and x['accn']==acc), last
