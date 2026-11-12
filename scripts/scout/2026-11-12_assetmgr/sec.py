# Round 93 -- SEC EDGAR companyfacts: FY2021-25 annual flows, TTM = 9M26 + FY25 - 9M25, latest balance-sheet stocks.
import urllib.request as u, json, sys
H={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36'}
cik={'LAZ':1311370,'EVR':1360901,'PJT':1626115,'HLI':1302215}
FLOW={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenuesNetOfInterestExpense'],'op':['OperatingIncomeLoss'],
 'pretax':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],
 'ni':['NetIncomeLoss'],'ni_all':['ProfitLoss'],'ocf':['NetCashProvidedByUsedInOperatingActivities'],
 'capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],'int':['InterestExpense','InterestExpenseNonoperating','InterestExpenseDebt'],
 'buyback':['PaymentsForRepurchaseOfCommonStock'],'div':['PaymentsOfDividendsCommonStock','PaymentsOfDividends']}
STOCK={'eq':['StockholdersEquity'],'eq_nci':['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
 'cash':['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents'],
 'debt':['LongTermDebt','SeniorNotes','LongTermDebtNoncurrent','DebtInstrumentCarryingAmount'],'assets':['Assets'],'shares':['CommonStockSharesOutstanding']}
out={}
for t,c in cik.items():
    f=json.loads(u.urlopen(u.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json',headers=H),timeout=60).read())
    g=f['facts'].get('us-gaap',{}); r={'name':f['entityName']}
    def ser(tags,instant=False):
        for tg in tags:
            if tg in g:
                us=list(g[tg]['units'].values())[0]; return tg,us
        return None,[]
    for k,tags in FLOW.items():
        tg,us=ser(tags); d={}
        for x in us:
            if x.get('form') not in ('10-K','10-Q') or 'start' not in x: continue
            dur=(int(x['end'][:4])*12+int(x['end'][5:7]))-(int(x['start'][:4])*12+int(x['start'][5:7]))
            if dur in (11,12) and x['end'][5:7]=='12': d[f"FY{x['end'][:4]}"]=x['val']
            if dur in (8,9) and x['end'][5:7]=='09': d[f"9M{x['end'][:4]}"]=x['val']
        if all(z in d for z in ('9M2026','FY2025','9M2025')): d['TTM']=d['9M2026']+d['FY2025']-d['9M2025']
        r[k]={'tag':tg,**{z:round(v/1e6,1) for z,v in sorted(d.items()) if z>='FY2020'}}
    for k,tags in STOCK.items():
        tg,us=ser(tags); us=[x for x in us if x.get('form') in ('10-K','10-Q')]
        if us:
            x=max(us,key=lambda x:x['end']); r[k]={'tag':tg,'end':x['end'],'val':round(x['val']/1e6,2)}
    out[t]=r; print(t,json.dumps(r)[:3000]); print()
json.dump(out,open('data/sec.json','w'),indent=1)
