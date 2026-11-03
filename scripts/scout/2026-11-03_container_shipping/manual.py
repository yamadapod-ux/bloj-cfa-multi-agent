# Round 84 manual bridges from SEC filings (20-F FY2025 + 6-K Q2/Q3 2026). $M.
def grid(name,px,sh,fcf,claims,waccs,cuts):
    print(name)
    for w in waccs:
        row=[]
        for c in cuts:
            fv=(fcf*(1-c)/w-claims)/sh; row.append(f"cut{int(c*100)}%: ${fv:6.2f} ({px/fv if fv>0 else float('inf'):.2f}x)")
        print(f"  WACC {w*100:.2f}% | "+" | ".join(row))
# CMRE: TTM = FY25 cont + 9M26 - 9M25 (Q3 6-K 0001171843-26-006884)
cfo=536.867-418.8+328.0; da=129.538-(96.112+14.530)+(97.245+17.421); pref_div=20.92
oi=456.19-355.453+294.026; rev=877.9-665.928+640.63
debt=203.165+1604.433; cash=653.138+6.193+53.998+19.753; pref=49+99+100.5; nci=72.643; eq=2286.196; sh=120.897
own=cfo-da-pref_div; claims=debt-cash+pref+nci; mc=sh*13.45
ebitda=oi+da; ev=mc+claims
print(f"CMRE TTM rev {rev:.1f} OI {oi:.1f} D&A {da:.1f} EBITDA {ebitda:.1f} CFO {cfo:.1f} ownerFCF {own:.1f} netdebt {debt-cash:.1f} claims {claims:.1f} mcap {mc:.0f} EV/EBITDA {ev/ebitda:.2f} ownerFCFyld {own/mc*100:.1f}% P/B {mc/eq:.2f} ND/EBITDA {(debt-cash)/ebitda:.2f}")
ic=eq+nci+debt-cash; print(f"  ROIC pre-tax {oi/ic*100:.1f}% @15%tax {oi*.85/ic*100:.1f}%  IC {ic:.0f}")
ke=0.0489+1.04*0.042; E=mc; D=debt; P=pref; w=(E*ke+P*0.083+D*0.057)/(E+P+D); print(f"  WACC recompute Ke {ke*100:.2f}% WACC {w*100:.2f}%")
grid('CMRE',13.45,sh,own,claims,[w,0.10],[0,0.15,0.30])
# NVGS: TTM = FY25 + H1'26 - H1'25 (6-K 0001628280-26-052620)
cfo=201.662-103.744+95.766; da=134.497-66.0+63.398; oi=165.425-72.546+106.56
debt=139.987+641.941+138.422; cash=225.892+47.942; jv=247.737; nci=33.242; eq=1238.712; sh=61.493; mc=sh*20.0
own=cfo-da; claims=debt-cash+nci-jv; ebitda=oi+da
print(f"NVGS TTM OI {oi:.1f} D&A~{da:.1f} EBITDA {ebitda:.1f} CFO {cfo:.1f} ownerFCF {own:.1f} ({own/mc*100:.1f}%) reportedFCF {cfo-1.3:.1f} ({(cfo-1.3)/mc*100:.1f}%) ND {debt-cash:.1f} EV/EBITDA {(mc+claims)/ebitda:.2f} P/B {mc/eq:.2f}")
ic=eq+nci+debt-cash; print(f"  ROIC pre-tax {oi/ic*100:.1f}% @15% {oi*.85/ic*100:.1f}%")
grid('NVGS owner',20.0,sh,own,claims,[0.0757,0.10],[0])
grid('NVGS 5Yavg FCF 100',20.0,sh,100,claims,[0.0757,0.10],[0])
grid('NVGS reported TTM',20.0,sh,cfo-1.3,claims,[0.0757,0.10],[0])
# DLNG: TTM = FY25 + H1'26 - H1'25 (6-K 0001104659-26-106698)
cfo=90.265-42.384+47.549; da=32.064; oi=75.328-37.721+36.329; debt=256.64; cash=59.486; prefA=75.0; eqtot=499.596; sh=36.382; mc=sh*3.17
own=cfo-da-6.75; claims=debt-cash+prefA
print(f"DLNG TTM OI {oi:.1f} CFO {cfo:.1f} owner(after pref) {own:.1f} ({own/mc*100:.0f}% of mcap {mc:.0f}) ROIC {oi/(eqtot+debt-cash)*100:.1f}% P/commonBook {mc/(eqtot-73.216):.2f}")
grid('DLNG perpetuity',3.17,sh,own,claims,[0.0524,0.13,0.16],[0])
for n in (10,12): 
    a=(1-1.13**-n)/0.13; fv=(own*a-claims)/sh; print(f"  DLNG {n}-yr annuity @13%: ${fv:.2f} ({3.17/fv:.2f}x)")
