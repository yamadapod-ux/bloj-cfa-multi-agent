# Round 89 -- SEC EDGAR companyfacts: latest equity, debt, cash, revenue, shares, interest for office REITs.
import urllib.request as u, json, sys
H={'User-Agent':'bljcfa research yamadapod@gmail.com'}
tk=json.loads(u.urlopen(u.Request('https://www.sec.gov/files/company_tickers.json',headers=H)).read())
cik={v['ticker']:v['cik_str'] for v in tk.values()}
TAGS=['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','LongTermDebt','SecuredDebt','UnsecuredDebt','NotesPayable','DebtInstrumentCarryingAmount','CashAndCashEquivalentsAtCarryingValue','Revenues','InterestExpense','InterestExpenseNonoperating','NetIncomeLoss','ImpairmentOfRealEstate','RealEstateInvestmentPropertyAtCost','EntityCommonStockSharesOutstanding','PaymentsForCapitalImprovements','PaymentsToDevelopRealEstateAssets']
for t in sys.argv[1:]:
    c=cik[t]; f=json.loads(u.urlopen(u.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json',headers=H)).read())
    print(f'== {t} CIK {c}')
    for ns in ('us-gaap','dei'):
        for tag in TAGS:
            if tag in f['facts'].get(ns,{}):
                us=list(f['facts'][ns][tag]['units'].values())[0]
                us=[x for x in us if x.get('form') in ('10-Q','10-K')]
                if not us: continue
                last=max(us,key=lambda x:(x['end'],x.get('filed','')))
                # annual values for revenue/NI/impairment
                ann=sorted({x['end']:x['val'] for x in us if x.get('fp')=='FY' and x.get('form')=='10-K' and 'start' in x and (int(x['end'][:4])-int(x['start'][:4]))<=1 and x['end'][5:7]==x['start'][5:7] or False}.items())[-5:] if tag in ('Revenues','NetIncomeLoss','ImpairmentOfRealEstate','InterestExpense','InterestExpenseNonoperating','PaymentsForCapitalImprovements','PaymentsToDevelopRealEstateAssets') else ''
                print(f"  {tag}: {last['val']/1e6 if tag!='EntityCommonStockSharesOutstanding' else last['val']/1e6:,.1f}M end {last['end']} {last['form']} {last.get('accn')} {('FY:'+str([(a[:4],round(b/1e6)) for a,b in ann])) if ann else ''}")
