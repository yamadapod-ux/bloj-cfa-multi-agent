import json, urllib.request, sys, time
UA={'User-Agent':'CFA-scout research contact-not-provided research@example.com'}
CIK={'TTD':1671933,'PINS':1506293,'SNAP':1564408,'CRTO':1576427}
TAGS={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'],
 'oi':['OperatingIncomeLoss'],'ni':['NetIncomeLoss'],
 'ocf':['NetCashProvidedByUsedInOperatingActivities'],
 'capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
 'capsw':['PaymentsToDevelopSoftware'],
 'sbc':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
 'eq':['StockholdersEquity'],'debt':['LongTermDebt','LongTermDebtNoncurrent','ConvertibleNotesPayable','ConvertibleDebtNoncurrent','SeniorNotes'],
 'cash':['CashAndCashEquivalentsAtCarryingValue'],'sti':['ShortTermInvestments','MarketableSecuritiesCurrent','AvailableForSaleSecuritiesDebtSecuritiesCurrent'],
 'lti':['LongTermInvestments','MarketableSecuritiesNoncurrent','AvailableForSaleSecuritiesDebtSecuritiesNoncurrent'],
 'buyback':['PaymentsForRepurchaseOfCommonStock'],'tax':['IncomeTaxExpenseBenefit'],'pretax':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],
 'da':['DepreciationDepletionAndAmortization','DepreciationAndAmortization']}
for t in sys.argv[1:]:
    u=f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK[t]:010d}.json"
    d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
    g=d['facts'].get('us-gaap',{})
    shares=d['facts'].get('dei',{}).get('EntityCommonStockSharesOutstanding',{}).get('units',{}).get('shares',[])
    print('=====',t,d['entityName'])
    sh={}
    for s in shares: sh.setdefault(s['end'],0); sh[s['end']]+=0
    # sum share classes per end date per filing
    byf={}
    for s in shares: byf.setdefault((s['accn'],s['end']),0); byf[(s['accn'],s['end'])]+=s['val']
    print(' shares (last 3):', sorted(byf.items(), key=lambda x:x[0][1])[-3:])
    for k,tags in TAGS.items():
        best=None
        for tg in tags:
            if tg not in g: continue
            units=g[tg]['units'].get('USD',[])
            if not units: continue
            mx=max(x['end'] for x in units)
            if best is None or mx>best[1]: best=(tg,mx,units)
        if not best: print(' ',k,'NA'); continue
        tg,_,units=best
        # dedupe by (start,end) keep latest filed
        dd={}
        for x in units:
            key=(x.get('start'),x['end']); 
            if key not in dd or x['filed']>dd[key]['filed']: dd[key]=x
        rows=sorted(dd.values(), key=lambda x:x['end'])
        if 'start' in rows[-1]:
            fy=[ (x['end'],x['val']) for x in rows if x.get('fp')=='FY' or (x.get('form','').startswith('10-K') and x.get('start') and (int(x['end'][:4])*12+int(x['end'][5:7]))-(int(x['start'][:4])*12+int(x['start'][5:7]))>=11)]
            fy=[f for f in fy][-6:]
            ytd=[(x['start'],x['end'],x['val']) for x in rows if x['end']>='2025-01-01']
            print(f'  {k} [{tg}] FY:',[(e[:7],round(v/1e6,1)) for e,v in fy if True][-6:])
            print(f'     recent:',[(s[:7],e[:7],round(v/1e6,1)) for s,e,v in ytd][-8:])
        else:
            print(f'  {k} [{tg}]:',[(x['end'],round(x['val']/1e6,1)) for x in rows][-6:])
    time.sleep(0.5)
