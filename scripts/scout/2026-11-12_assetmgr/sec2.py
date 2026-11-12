# Round 93 -- supplement: SBC for all 4; HLI fiscal year ends March -> FY (Apr-Mar) + TTM = 6M to 2026-09 + FY Mar-2026 - 6M to 2025-09.
import urllib.request as u, json
H={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36'}
cik={'LAZ':1311370,'EVR':1360901,'PJT':1626115,'HLI':1302215}
TAGS={'sbc':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],'rev':['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues'],'op':['OperatingIncomeLoss'],'ni':['NetIncomeLoss'],
 'ocf':['NetCashProvidedByUsedInOperatingActivities'],'capex':['PaymentsToAcquirePropertyPlantAndEquipment'],'buyback':['PaymentsForRepurchaseOfCommonStock'],'pretax':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest']}
out={}
for t,c in cik.items():
    f=json.loads(u.urlopen(u.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json',headers=H),timeout=60).read()); g=f['facts']['us-gaap']
    fye='03' if t=='HLI' else '12'; ytdm='09'; ytdlen=6 if t=='HLI' else 9
    r={}
    for k,tags in TAGS.items():
        if t!='HLI' and k!='sbc': continue
        d={}
        for tg in tags:
            if tg not in g: continue
            for x in list(g[tg]['units'].values())[0]:
                if x.get('form') not in ('10-K','10-Q') or 'start' not in x: continue
                dur=(int(x['end'][:4])*12+int(x['end'][5:7]))-(int(x['start'][:4])*12+int(x['start'][5:7]))
                if dur in (11,12) and x['end'][5:7]==fye: d.setdefault(f"FY{x['end'][:4]}",x['val'])
                if dur in (ytdlen-1,ytdlen) and x['end'][5:7]==ytdm: d.setdefault(f"YTD{x['end'][:4]}",x['val'])
            if d: r[k+'_tag']=tg; break
        fy='FY2026' if t=='HLI' else 'FY2025'
        if all(z in d for z in ('YTD2026',fy,'YTD2025')): d['TTM']=d['YTD2026']+d[fy]-d['YTD2025']
        r[k]={z:round(v/1e6,1) for z,v in sorted(d.items()) if z>='FY2020'}
    out[t]=r; print(t,json.dumps(r))
json.dump(out,open('data/sec2.json','w'),indent=1)
