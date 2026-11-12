# Round 93 -- Filter A/B/C/D + Tier 1 arithmetic. Inputs: data/px*.json (Yahoo), data/sec*.json (SEC companyfacts), stockanalysis mcap/shares (sa.json).
# FCF = OCF - capex - SBC (SBC treated as cash cost: advisory firms pay a large share of comp in stock; reported FCF adds SBC back).
# Net debt uses senior notes only (lease cost already inside OCF). LAZ SBC TTM proxy = FY2025 (AllocatedShareBasedCompensationExpense; 9M tag not filed).
px={'LAZ':41.90,'EVR':298.08,'PJT':152.94,'HLI':146.17}
sh={'LAZ':97.66,'EVR':39.38,'PJT':40.46,'HLI':69.42}           # stockanalysis shares (M)
wacc={'LAZ':.11,'EVR':.10,'PJT':.10,'HLI':.10}
nd={'LAZ':1690.25-1263.96,'EVR':-1226.34+0,'PJT':-257.37,'HLI':-837.0}  # EVR/PJT/HLI: no funded debt taken -> cash only (conservative = generous to FV)
ttm={'LAZ':(700.3,15.3,359.7),'EVR':(1766.8,41.6,779.2),'PJT':(732.6,44.7,241.1),'HLI':(426.7,24.9,199.3)}
avg5={'LAZ':((866.1+834.0+164.7+742.8+519.3)/5,(39.7+49.5+28.3+45.5+31.9)/5,(234.0+240.6+250.6+277.7+359.7)/5),
      'EVR':((1384.9+531.4+458.0+988.2+1256.5)/5,(28.0+23.2+20.0+30.1+74.0)/5,(422.2+467.3+515.4+569.7+675.1)/5),
      'PJT':((124.2+242.7+441.5+531.0+526.3)/5,(6.5+3.4+3.9+3.3+45.9)/5,(108.9+165.5+178.5+209.2+234.3)/5),
      'HLI':((736.6+136.3+328.5+848.6+704.1)/5,(8.7+50.7+66.7+39.7+22.3)/5,(91.88+156.94+166.6+168.44+201.3)/5)}
ni5={'LAZ':(542.5+392.5-57.3+286.7+251.0)/5,'EVR':(868.6+531.4+285.2+417.7+640.7)/5,'PJT':(190.0+164.8+145.7+238.5+309.7)/5,'HLI':(437.8+254.2+280.3+399.7+425.7)/5}
for t in px:
    mc=px[t]*sh[t]; o,c,s=ttm[t]; f_t=o-c-s; o5,c5,s5=avg5[t]; f5=o5-c5-s5
    fv=lambda f,w=wacc[t]:(f/w-nd[t])/sh[t]
    print(f"{t}: mcap {mc:,.0f} | FCF raw TTM {o-c:,.0f} ({(o-c)/mc:.1%}) | FCF-SBC TTM {f_t:,.0f} ({f_t/mc:.1%}) | 5Y FCF-SBC {f5:,.0f} ({f5/mc:.1%})")
    print(f"   naive FV 5Y ${fv(f5):.2f} -> P/FV {px[t]/fv(f5):.2f}x | TTM ${fv(f_t):.2f} -> {px[t]/fv(f_t):.2f}x | NI-5Y ${fv(ni5[t]):.2f} -> {px[t]/fv(ni5[t]):.2f}x | WACC-2pp 5Y ${fv(f5,wacc[t]-.02):.2f} -> {px[t]/fv(f5,wacc[t]-.02):.2f}x")
# ROIC (EBIT proxy x 0.75 / (equity incl NCI + funded debt - cash))
roic={'LAZ':(266.9*.75)/(940.49+1690.25-1263.96),'LAZ_5Y':(((723.8+516.8-80.0+386.5+327.6)/5)*.75)/(940.49+1690.25-1263.96),
      'EVR':(1036.5*.75)/(2281.16),'PJT':(374.2*.75)/1052.94,'HLI':(517.9*.75)/2307.0}
for k,v in roic.items(): print('ROIC',k,f"{v:.1%}")
