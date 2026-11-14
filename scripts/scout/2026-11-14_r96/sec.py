import json, urllib.request, sys, time, datetime
UA={'User-Agent':'CFA-scout research research@example.com'}
def get(u): return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
tick=get('https://www.sec.gov/files/company_tickers.json')
CIK={v['ticker']:v['cik_str'] for v in tick.values()}
TAGS={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','RevenueFromContractWithCustomerIncludingAssessedTax'],
 'oi':['OperatingIncomeLoss'],'ni':['NetIncomeLoss'],
 'ocf':['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
 'capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
 'sbc':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
 'eq':['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
 'ltd':['LongTermDebt','LongTermDebtNoncurrent','LongTermDebtAndCapitalLeaseObligations'],
 'std':['LongTermDebtCurrent','ShortTermBorrowings','DebtCurrent','LongTermDebtAndCapitalLeaseObligationsCurrent'],
 'cash':['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents'],
 'sti':['ShortTermInvestments','MarketableSecuritiesCurrent'],
 'da':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet','Depreciation'],
 'gw':['Goodwill'],'dil':['WeightedAverageNumberOfDilutedSharesOutstanding'],'shs':['CommonStockSharesOutstanding']}
def months(s,e):
    a=datetime.date.fromisoformat(s); b=datetime.date.fromisoformat(e); return round((b-a).days/30.4)
out={}
for t in sys.argv[1:]:
    d=get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK[t]:010d}.json")
    g=d['facts'].get('us-gaap',{}); r={'name':d['entityName']}
    for k,tags in TAGS.items():
        units=[]
        seen=set()
        for tg in tags:
            if tg not in g: continue
            u=g[tg]['units']; uu=u.get('USD') or u.get('shares') or []
            for x in uu:
                key=(x.get('start'),x['end'])
                if key in seen: continue
                units.append(x)
            seen|={(x.get('start'),x['end']) for x in uu}
        if not units: r[k]=None; continue
        tg='+'.join(t2 for t2 in tags if t2 in g)
        dd={}
        for x in units:
            key=(x.get('start'),x['end'])
            if key not in dd or x['filed']>dd[key]['filed']: dd[key]=x
        rows=sorted(dd.values(), key=lambda x:x['end'])
        if 'start' in rows[-1] or any('start' in x for x in rows):
            dur=[x for x in rows if 'start' in x]
            fy=[x for x in dur if 11<=months(x['start'],x['end'])<=13]
            fyl=[(x['end'],x['val']) for x in fy][-7:]
            # latest YTD and prior-year same-length YTD
            last=max(dur,key=lambda x:(x['end'],months(x['start'],x['end'])))
            m=months(last['start'],last['end'])
            ttm=None
            if m>=11: ttm=last['val']; m=12
            else:
                # find FY ending before last.end and matching prior ytd
                lfy=[x for x in fy if x['end']<last['end']]
                if lfy:
                    lfy=lfy[-1]
                    py=[x for x in dur if months(x['start'],x['end'])==m and abs((datetime.date.fromisoformat(x['end'])-datetime.date.fromisoformat(last['end'])).days+365)<20]
                    if py: ttm=lfy['val']+last['val']-py[-1]['val']
            r[k]={'tag':tg,'fy':fyl,'ttm':ttm,'ttm_end':last['end'],'ytd_m':m}
        else:
            r[k]={'tag':tg,'last':rows[-1]['val'],'end':rows[-1]['end']}
    out[t]=r; print(t,'ok',r['name']); time.sleep(0.3)
json.dump(out,open('sec.json','w'),indent=0)
