# Round 92 Leisure & Recreation -- SEC EDGAR companyfacts: annual FY + TTM (YTD 2026 + FY25 - YTD 2025) for flows, latest balance for stocks.
import urllib.request as u, json, sys, os
H={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'}
def get(url):
    return json.loads(u.urlopen(u.Request(url,headers=H),timeout=60).read())
cik={'FUN':1999001,'PLNT':1637207,'XPOF':1802156,'PTON':1639825,'GOLF':1672013,'LUCK':1840572}  # entityName printed below verifies each CIK
FLOW={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'],'op':['OperatingIncomeLoss'],'ni':['NetIncomeLoss'],
 'ocf':['NetCashProvidedByUsedInOperatingActivities'],'capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','PaymentsForFlightEquipment','PaymentsToAcquireFlightEquipment'],
 'capex2':['PaymentsToAcquireOtherPropertyPlantAndEquipment','PaymentsForProceedsFromOtherPropertyPlantAndEquipment','PaymentsToAcquireOtherProductiveAssets'],
 'da':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet'],'int':['InterestExpense','InterestExpenseNonoperating','InterestExpenseDebt'],
 'tax':['IncomeTaxExpenseBenefit'],'pretax':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],
 'buyback':['PaymentsForRepurchaseOfCommonStock'],'div':['PaymentsOfDividendsCommonStock','PaymentsOfDividends']}
STOCK={'eq':['StockholdersEquity'],'cash':['CashAndCashEquivalentsAtCarryingValue'],'sti':['ShortTermInvestments','AvailableForSaleSecuritiesDebtSecuritiesCurrent','MarketableSecuritiesCurrent'],
 'ltd':['LongTermDebtNoncurrent','LongTermDebtAndCapitalLeaseObligations','LongTermDebtAndFinanceLeasesNoncurrent'],'cltd':['LongTermDebtCurrent','LongTermDebtAndCapitalLeaseObligationsCurrent','DebtAndFinanceLeasesCurrent','LongTermDebtAndFinanceLeasesCurrent'],
 'ltdtot':['LongTermDebt'],'opl':['OperatingLeaseLiability'],'oplnc':['OperatingLeaseLiabilityNoncurrent'],'oplc':['OperatingLeaseLiabilityCurrent'],'finl':['FinanceLeaseLiability'],'assets':['Assets']}
def series(f,tags):
    for tag in tags:
        for ns in ('us-gaap',):
            if tag in f['facts'].get(ns,{}):
                us=[x for x in list(f['facts'][ns][tag]['units'].values())[0] if x.get('form') in ('10-K','10-Q','10-K/A')]
                if us: return tag,us
    return None,[]
def dur(x): 
    from datetime import date
    s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end']); return (e-s).days
for t in sys.argv[1:]:
    f=get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik[t]:010d}.json'); json.dump(f,open(f'data/cf_{t}.json','w'))
    print(f'===== {t} CIK {cik[t]} {f.get("entityName")}')
    sh=f['facts'].get('dei',{}).get('EntityCommonStockSharesOutstanding')
    if sh:
        s=list(sh['units'].values())[0]; l=max(s,key=lambda x:(x['end'],x.get('filed',''))); print(f"  shares {l['val']/1e6:.2f}M as of {l['end']} ({l['form']})")
    for k,tags in FLOW.items():
        tag,us=series(f,tags)
        if not tag: continue
        ann={};fyend={}
        for x in us:
            if 'start' in x and 350<dur(x)<380 and x['form'].startswith('10-K'): ann[x['end'][:4]]=x['val'];fyend[x['end'][:4]]=x['end']   # later filings overwrite -> latest restated
        ytd=sorted([x for x in us if 'start' in x and x['form']=='10-Q' and 80<dur(x)<290],key=lambda x:(x['end'],dur(x)))
        ttm=''
        if ytd:
            cur=ytd[-1]; prior=[x for x in us if 'start' in x and abs(dur(x)-dur(cur))<8 and x['end'][:4]==str(int(cur['end'][:4])-1) and abs(int(x['end'][5:7])-int(cur['end'][5:7]))<1]
            fyk=[k for k in ann if k<cur['end'][:4] or (k==cur['end'][:4])]; fyk=[k for k in sorted(ann) if fyend.get(k,'9')<cur['end']]
            fy=ann[fyk[-1]] if fyk else None
            if prior and fy is not None: ttm=f" | YTD9M {cur['end']} {cur['val']/1e6:,.0f} TTM({dur(cur)}d) {(fy+cur['val']-prior[-1]['val'])/1e6:,.0f}"
        print(f"  {k:7s} {tag}: "+' '.join(f"{y}:{v/1e6:,.0f}" for y,v in sorted(ann.items())[-7:])+ttm)
    for k,tags in STOCK.items():
        tag,us=series(f,tags)
        if not tag: continue
        l=max([x for x in us if 'start' not in x] or [{'end':'-','val':0,'form':'-'}],key=lambda x:(x['end'],x.get('filed','')))
        print(f"  {k:7s} {tag}: {l['val']/1e6:,.0f} @ {l['end']} {l['form']}")
