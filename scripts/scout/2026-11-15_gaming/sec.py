import json, urllib.request, sys, time
UA={'User-Agent':'CFA-scout research research@example.com'}
CIK={'WYNN':1174922,'BRSL':1619762,'INSE':1615063,'SRAD':1836470,'GENI':1834489,'ACEL':1698991,'BALY':1747079}
T={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','Revenue'],
 'oi':['OperatingIncomeLoss','ProfitLossFromOperatingActivities'],
 'ni':['NetIncomeLoss','ProfitLoss','ProfitLossAttributableToOwnersOfParent'],
 'ocf':['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations','CashFlowsFromUsedInOperatingActivities'],
 'capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities'],
 'capint':['PaymentsToAcquireIntangibleAssets','PaymentsToDevelopSoftware','PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities'],
 'sbc':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense','ExpenseFromSharebasedPaymentTransactionsWithEmployees','AdjustmentsForSharebasedPayments'],
 'eq':['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','Equity','EquityAttributableToOwnersOfParent'],
 'ltd':['LongTermDebt','LongTermDebtNoncurrent','LongTermDebtAndCapitalLeaseObligations','NoncurrentPortionOfNoncurrentBorrowings','Borrowings','NoncurrentBorrowings'],
 'std':['LongTermDebtCurrent','ShortTermBorrowings','DebtCurrent','CurrentBorrowings','CurrentPortionOfNoncurrentBorrowings'],
 'cash':['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents','CashAndCashEquivalents'],
 'gw':['Goodwill'],'da':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortisationAndImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLoss'],
 'int':['InterestExpense','InterestExpenseNonoperating','FinanceCosts'],'buyback':['PaymentsForRepurchaseOfCommonStock','PaymentsToAcquireOrRedeemEntitysShares']}
for t in sys.argv[1:]:
    d=json.loads(urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK[t]:010d}.json",headers=UA),timeout=60).read())
    F={}; [F.update(v) for k,v in d['facts'].items() if k!='dei']
    print('=====',t,d['entityName'])
    sh=d['facts'].get('dei',{}).get('EntityCommonStockSharesOutstanding',{}).get('units',{}).get('shares',[])
    byf={}
    for s in sh: byf[(s['end'])]=byf.get(s['end'],0)+s['val'] if False else s['val']
    print(' dei shares last3:',sorted(byf.items())[-3:])
    for k,tags in T.items():
        best=None
        for tg in tags:
            if tg not in F: continue
            for cur,units in F[tg]['units'].items():
                if cur not in('USD','EUR'): continue
                mx=max(x['end'] for x in units)
                if best is None or mx>best[1]: best=(tg,mx,units,cur)
        if not best: print(' ',k,'NA'); continue
        tg,_,units,cur=best; dd={}
        for x in units:
            key=(x.get('start'),x['end'])
            if key not in dd or x['filed']>dd[key]['filed']: dd[key]=x
        rows=sorted(dd.values(), key=lambda x:x['end']); rows=[r for r in rows if 'start' in r] or rows
        if 'start' in rows[-1]:
            def mo(x): return (int(x['end'][:4])*12+int(x['end'][5:7]))-(int(x['start'][:4])*12+int(x['start'][5:7]))
            fy=[(x['end'][:7],round(x['val']/1e6,1)) for x in rows if mo(x)>=11][-6:]
            rec=[(x['start'][:7],x['end'][:7],round(x['val']/1e6,1)) for x in rows if x['end']>='2025-01-01' and mo(x)<11][-8:]
            print(f'  {k} [{tg},{cur}] FY:',fy); print('     ytd/q:',rec)
        else: print(f'  {k} [{tg},{cur}]:',[(x['end'],round(x['val']/1e6,1)) for x in rows][-5:])
    time.sleep(0.4)
