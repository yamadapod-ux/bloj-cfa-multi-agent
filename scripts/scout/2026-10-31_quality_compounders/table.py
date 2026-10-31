import json
S=json.load(open('screen_CTAS.json')); X=json.load(open('special.json'))
SEC={'CTAS':'Industrials — uniform/facility services','ROL':'Consumer services — pest control','ORLY':'Consumer disc. — auto parts retail','MNST':'Consumer staples — energy drinks',
'RMD':'Healthcare equipment — sleep/respiratory','WST':'Healthcare — pharma packaging/injectables','IDXX':'Healthcare diagnostics — veterinary','SHW':'Materials — paint/coatings',
'PAYX':'Payments/HR infra — payroll/HCM','GWW':'Industrials — MRO distribution','FAST':'Industrials — fastener/MRO distribution','ITW':'Industrials — diversified machinery',
'TT':'Industrials — HVAC/climate','MSI':'Tech hardware (non-AI) — public-safety comms','KNSL':'Specialty insurance — E&S','RACE':'Luxury — sports cars'}
rows=[]
for t,o in list(S.items())+list(X.items()):
    if t not in SEC: continue
    p=o['price']; fv=o['fv']; trg=0.85*fv; trgg=0.85*o['fv_wm']
    rh=o.get('roic_hist') or o.get('roeh')
    rs='/'.join(f"{100*v:.0f}" for _,v in rh)
    pt=o['pt']; 
    rows.append((trg/p-1,f"| **{t}** | {SEC[t]} | ${p:,.2f} | {'ROE' if t=='KNSL' else 'ROIC'} {rs} | {100*o['wacc' if t!='KNSL' else 'ke']:.2f}% | **${fv:,.2f}** | {p/fv:.2f}× | **${trg:,.2f}** | **{100*(trg/p-1):+.1f}%** | ${trgg:,.2f} ({100*(trgg/p-1):+.1f}%) | {'n/m' if o['k']>5.9 else f'{o['k']:.2f}×'} | {('%.0fth'%o['evrev_pct']) if 'evrev_pct' in o else ('P/B %.1f×'%o['pb'] if t=='KNSL' else 'n/a (20-F)')} | ${float(pt[3]):,.0f} ({pt[0]}–{pt[1]}) |"))
rows.sort()
print("| Ticker | Sector | Price Oct 30 | 5Y ROIC % (FY, SEC) | WACC/Ke | Screen FV | P/FV | **Trigger (MOS 15%)** | **% ต้องลง** | Trigger @WACC−1pp | Implied k | EV/Rev 5Y pctile | Street PT median (range) |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for _,r in rows: print(r)
