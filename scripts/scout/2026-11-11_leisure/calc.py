# Round 92 Leisure & Recreation -- scout arithmetic. Inputs: SEC companyfacts (data/cf_*.json via sec.py), price close 2026-11-10 (Yahoo meta = stockanalysis.com).
P={'FUN':10.16,'PLNT':61.34,'XPOF':4.59,'PTON':5.81,'GOLF':85.03,'LUCK':3.40}
SH={'FUN':102.31,'PLNT':74.52,'XPOF':40.5,'PTON':525.4,'GOLF':57.20,'LUCK':134.7}  # M; PLNT from stockanalysis (no dei tag); XPOF/PTON/LUCK = diluted wtd avg 10-Q
mc={t:P[t]*SH[t] for t in P}
# net debt ex-operating-lease ($M, latest 10-Q)
ND={'FUN':4906-268,'PLNT':2469-310-90,'XPOF':504-27,'PTON':1338-1342,'GOLF':855-108,'LUCK':1791+455-38}
fcf_ttm={'FUN':461-313,'PLNT':413-199,'XPOF':-10-2,'PTON':388-9.9,'GOLF':319-80,'LUCK':127-109}
fcf5={'FUN':[408-183,326-220,373-321,327-480],'PLNT':[189-54,240-100,330-136,344-155,418-164],
      'XPOF':[14-4,52-9,33-7,12-5,28-4],'PTON':[-2020-337,-388-82,-66-20,333-9,388-10],
      'GOLF':[314-38,-68-61,372-75,245-75,194-74],'LUCK':[178-162,218-149,155-194,177-141,104-114]}
W={'FUN':0.10,'PLNT':0.095,'XPOF':0.13,'PTON':0.11,'GOLF':0.09,'LUCK':0.11}
for t in P:
    a=sum(fcf5[t])/len(fcf5[t])
    fv5=(a/W[t]-ND[t])/SH[t]; fvt=(fcf_ttm[t]/W[t]-ND[t])/SH[t]
    print(f"{t}: mcap {mc[t]:,.0f} | ND {ND[t]:,.0f} | FCF TTM {fcf_ttm[t]:,.0f} ({fcf_ttm[t]/mc[t]*100:.1f}%) | 5Y avg {a:,.0f} ({a/mc[t]*100:.1f}%) | naiveFV 5Y ${fv5:.2f} TTM ${fvt:.2f} | P/FV "
          +(f"{P[t]/fv5:.2f}x" if fv5>0 else "neg")+" / "+(f"{P[t]/fvt:.2f}x" if fvt>0 else "neg"))
# GOLF extras: adj EBIT ex IEEPA refund 44.7
eb=359-44.7; print('GOLF adj EBIT',eb,'EBITDA',eb+55,'EV',mc['GOLF']+ND['GOLF'],'EV/EBITDA %.1f'%((mc['GOLF']+ND['GOLF'])/(eb+55)),'ROIC %.1f%%'%(eb*0.77/(867+ND['GOLF'])*100),
      'NOPAT FV $%.2f'%((eb*0.77/0.09-ND['GOLF'])/SH['GOLF']), 'WACC8 TTM $%.2f'%((fcf_ttm['GOLF']/0.08-ND['GOLF'])/SH['GOLF']))
print('PLNT EBITDA',430+162,'EV/EBITDA %.1f'%((mc['PLNT']+ND['PLNT'])/592),'ROIC(EBITx.75/(eq+ND)) %.1f%%'%(430*.75/(-609+ND['PLNT'])*100),'NOPAT FV $%.2f'%((430*.75/0.095-ND['PLNT'])/SH['PLNT']),'WACC8 TTM $%.2f'%((fcf_ttm['PLNT']/0.08-ND['PLNT'])/SH['PLNT']))
print('LUCK EV/EBITDA %.1f'%((mc['LUCK']+ND['LUCK'])/(137+129)),'ROIC %.1f%%'%(137*.77/(-434+ND['LUCK'])*100))
print('FUN EV',mc['FUN']+ND['FUN'],'ND/AdjEBITDA guide-ish')
print('PTON 2Y post-restructuring avg FCF',(fcf5['PTON'][3]+fcf5['PTON'][4])/2,'-> FV $%.2f'%(((fcf5['PTON'][3]+fcf5['PTON'][4])/2/0.11-ND['PTON'])/SH['PTON']))
