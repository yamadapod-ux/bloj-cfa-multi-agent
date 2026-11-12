# Round 93: extra tags (SBC, debt, diluted shares, NCI) from cached companyfacts
import json,sys
from datetime import date
def dur(x): return (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
TAGS=['ShareBasedCompensation','AllocatedShareBasedCompensationExpense','WeightedAverageNumberOfDilutedSharesOutstanding','LongTermDebt','NotesPayable','SeniorNotes','LongTermDebtNoncurrent','DebtInstrumentCarryingAmount','MinorityInterest','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','EmployeeRelatedLiabilitiesCurrent','AccruedEmployeeBenefitsCurrent','EmployeeRelatedLiabilitiesCurrentAndNoncurrent','PaymentsForRepurchaseOfCommonStock','PaymentsForRepurchaseOfEquity','OperatingIncomeLoss','CompensationAndBenefitsExpense','LaborAndRelatedExpense']
for t in sys.argv[1:]:
    f=json.load(open(f'data/cf_{t}.json')); g=f['facts']['us-gaap']; print('=====',t)
    for tag in TAGS:
        if tag not in g: continue
        us=[x for x in list(g[tag]['units'].values())[0] if x.get('form') in('10-K','10-Q')]
        ann={x['end'][:7]:x['val'] for x in us if 'start' in x and 350<dur(x)<380 and x['form']=='10-K'}
        q=[x for x in us if 'start' in x and x['form']=='10-Q' and x['end']>='2025-09-01']
        st=[x for x in us if 'start' not in x]
        s=f'  {tag}: '+' '.join(f'{k}:{v/1e6:,.0f}' for k,v in sorted(ann.items())[-6:])
        if q: s+=' | 10-Q '+' '.join(f"{x['start'][:7]}->{x['end']}:{x['val']/1e6:,.1f}" for x in sorted(q,key=lambda x:x['end'])[-4:])
        if st: l=max(st,key=lambda x:(x['end'],x.get('filed',''))); s+=f" | latest {l['val']/1e6:,.0f}@{l['end']}"
        print(s)
