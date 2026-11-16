import json,sys
d=json.load(open(sys.argv[1]))['facts']['us-gaap']
tags=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','CostOfRevenue','OperatingIncomeLoss','NetIncomeLoss','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','ShareBasedCompensation','DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet','IncomeTaxExpenseBenefit','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','WeightedAverageNumberOfDilutedSharesOutstanding','EarningsPerShareDiluted','PaymentsForRepurchaseOfCommonStock','ResearchAndDevelopmentExpense']
bs=['CashAndCashEquivalentsAtCarryingValue','ShortTermInvestments','AvailableForSaleSecuritiesDebtSecuritiesCurrent','LongTermDebt','LongTermDebtNoncurrent','LongTermDebtCurrent','DebtCurrent','CommercialPaper','StockholdersEquity','ContractWithCustomerLiabilityCurrent','ContractWithCustomerLiabilityNoncurrent','OperatingLeaseLiability','OperatingLeaseLiabilityNoncurrent','Assets','Goodwill','RevenueRemainingPerformanceObligation']
def dur(f):
  from datetime import date
  a=date.fromisoformat(f['start']);b=date.fromisoformat(f['end']);return (b-a).days
for t in tags:
  if t not in d: print(t,'MISSING');continue
  u=list(d[t]['units'].values())[0]
  ann={};q={}
  for f in u:
    if 'start' not in f: continue
    dd=dur(f)
    if f.get('form') not in ('10-K','10-Q'): continue
    if 350<dd<380: ann[f['end']]=f['val']
    if 80<dd<100: q[f['end']]=f['val']
  print(t,'ANN',{k:ann[k] for k in sorted(ann)[-6:]})
  print('   Q',{k:q[k] for k in sorted(q)[-6:]})
for t in bs:
  if t not in d: print(t,'MISSING');continue
  u=list(d[t]['units'].values())[0]
  pts={f['end']:f['val'] for f in u if 'start' not in f}
  print(t,{k:pts[k] for k in sorted(pts)[-4:]})
dei=json.load(open(sys.argv[1]))['facts']['dei']
u=dei['EntityCommonStockSharesOutstanding']['units']['shares']
print('SharesOut',[(f['end'],f['val'],f['form']) for f in u[-3:]])
