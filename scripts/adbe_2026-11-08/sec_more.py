import json,sys
from datetime import date
d=json.load(open(sys.argv[1]))['facts']['us-gaap']
tags=['PaymentsToAcquireBusinessesNetOfCashAcquired','InterestExpense','InterestExpenseNonoperating','InterestExpenseDebt','AmortizationOfIntangibleAssets','ContractWithCustomerLiabilityCurrent','IncreaseDecreaseInContractWithCustomerLiability','PaymentsForRepurchaseOfCommonStock','IncomeTaxExpenseBenefit','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','WeightedAverageNumberOfDilutedSharesOutstanding','ResearchAndDevelopmentExpense','SellingAndMarketingExpense','GeneralAndAdministrativeExpense','BusinessCombinationAcquisitionRelatedCosts','RevenueRemainingPerformanceObligation','InvestmentIncomeInterest','OtherNonoperatingIncomeExpense','NonoperatingIncomeExpense']
for t in tags:
  if t not in d: print(t,'MISSING');continue
  u=list(d[t]['units'].values())[0]
  ann={};q={};pt={};ytd={}
  for f in u:
    if f.get('form') not in ('10-K','10-Q'): continue
    if 'start' not in f: pt[f['end']]=f['val'];continue
    dd=(date.fromisoformat(f['end'])-date.fromisoformat(f['start'])).days
    if 350<dd<380: ann[f['end']]=f['val']
    elif 80<dd<100: q[f['end']]=f['val']
    elif 260<dd<290: ytd[f['end']]=f['val']
  print(t)
  if ann: print('  ANN',{k:ann[k] for k in sorted(ann)[-6:]})
  if q: print('  Q',{k:q[k] for k in sorted(q)[-7:]})
  if ytd: print('  9M',{k:ytd[k] for k in sorted(ytd)[-3:]})
  if pt: print('  PT',{k:pt[k] for k in sorted(pt)[-6:]})
