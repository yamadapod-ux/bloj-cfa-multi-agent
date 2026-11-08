# Round 89 -- Filter D (REIT proxy): naive FV = FFO / CoE (ceiling) and adjusted floor; Filter E2 = FFO yield - CoE.
RF,ERP=4.859,4.41   # ^TNX close 11-06 (Yahoo) · Damodaran implied ERP 2026-11-01 (same as R88)
# ticker: price, blume beta, FFO/sh (FY26 guide mid or run-rate), adjusted FFO/sh for floor, label
D={'HPP':(8.49,1.71,1.18,-0.32,'AFFO Q3 -0.08 x4'),
   'DEI':(10.17,1.11,1.41,1.07,'AFFO ~$56M/q x4 / 209M sh'),
   'JBGS':(12.44,1.06,0.75,None,'9M core FFO 0.56 annualized'),
   'ARE':(44.80,1.06,6.40,5.02,'FFO - capitalized interest $240M/174.2M sh'),
   'ESRT':(5.31,1.26,0.785,0.415,'FFO - capex ~$100M/270M sh'),}
for t,(p,b,f,fl,lab) in D.items():
    coe=RF+b*ERP; fv=f/(coe/100)
    s=f"{t:5} CoE {coe:.2f}% P/FFO {p/f:.1f}x FFOyld {100*f/p:.1f}% E2 {100*f/p-coe:+.2f}pp | FV ceil ${fv:.2f} ({p/fv:.2f}x)"
    if fl is not None:
        fv2=fl/(coe/100); s+=f" | floor ${fv2:.2f} ({p/fv2:.2f}x if >0) [{lab}]"
    print(s)
