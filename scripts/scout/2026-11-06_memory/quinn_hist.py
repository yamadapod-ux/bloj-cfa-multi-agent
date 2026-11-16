import json,sys,datetime as dt,os
base=os.path.dirname(os.path.abspath(__file__))
for n in ['MU','GSPC']:
    r=json.load(open(f'{base}/data/quinn_daily/d_{n}.json'))['chart']['result'][0]
    ts=r['timestamp']; c=r['indicators']['adjclose'][0]['adjclose']; cl=r['indicators']['quote'][0]['close']
    print(n,len(ts),dt.datetime.utcfromtimestamp(ts[0]).date(),dt.datetime.utcfromtimestamp(ts[-1]).date(),[round(x,2) if x else x for x in cl[-4:]],[round(x,2) if x else x for x in c[-4:]])
f=json.load(open(f'{base}/data/cf_MU.json','rb'))
g=f['facts']['us-gaap']
def ann(tags):
    out={}
    for t in tags:
        for un,rows in g.get(t,{}).get('units',{}).items():
            for x in rows:
                if not x.get('form','').startswith('10-K'): continue
                if 'start' in x:
                    d=(dt.date.fromisoformat(x['end'])-dt.date.fromisoformat(x['start'])).days
                    if d<340 or d>380: continue
                out[x['end'][:4]]=x['val']/1e6
    return dict(sorted(out.items()))
for k,t in {'rev':['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet'],'opinc':['OperatingIncomeLoss'],'ni':['NetIncomeLoss'],'ocf':['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],'capex':['PaymentsToAcquireProductiveAssets','PaymentsToAcquirePropertyPlantAndEquipment'],'da':['DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet'],'ppe':['PropertyPlantAndEquipmentNet'],'eq':['StockholdersEquity'],'cash':['CashAndCashEquivalentsAtCarryingValue'],'sti':['ShortTermInvestments'],'lti':['LongTermMarketableInvestments','LongTermInvestments'],'debt':['LongTermDebt','DebtAndCapitalLeaseObligations'],'inv':['InventoryNet'],'ar':['ReceivablesNetCurrent','AccountsReceivableNetCurrent'],'wadil':['WeightedAverageNumberOfDilutedSharesOutstanding'],'sbc':['ShareBasedCompensation'],'buy':['PaymentsForRepurchaseOfCommonStock'],'wc_inv':['IncreaseDecreaseInInventories'],'wc_ar':['IncreaseDecreaseInReceivables','IncreaseDecreaseInAccountsReceivable']}.items():
    a=ann(t); print(k,{y:round(v) for y,v in list(a.items())[-14:]})
