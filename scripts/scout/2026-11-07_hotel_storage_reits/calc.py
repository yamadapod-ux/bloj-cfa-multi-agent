# Scout Round 88 -- Filter A/B-Zero/B/C/D/E2 arithmetic. Inputs: Yahoo+Nasdaq close 11-06, Q3 2026 releases cited in the report.
RF,ERP=4.859,4.41
#      px,    hi,    low,  beta, FFO,   capex$M, sh,  div,  debt,   cash,  ebitda, med5y
R={'HST':(24.62,26.19,16.62,1.04,2.21,562.5+12.5,687.3,0.80,5084,1492,1865,5.16),
'PK':(15.74,17.14,9.84,1.25,2.025,275,201,1.00,None,None,640,9.32),
'RHP':(132.05,137.46,89.60,1.11,9.29,None,70.7,4.80,4659.3,348.2,933.5,3.98),
'APLE':(18.88,18.98,11.22,0.95,1.36/.75,90,236.1,0.96,1490.3,42.7,487.5,6.77),
'SHO':(12.52,13.08,8.69,0.98,1.015,110,183.5,0.36,955,236.5,256.5,3.14),
'XHR':(21.39,22.06,12.74,1.09,2.11,72.5,95.7,0.56,1400,161,281,3.10),
'DRH':(14.04,14.72,8.14,1.01,1.25,77.5,207.5,0.44,1100,140,324.5,1.90),
'EXR':(159.19,163.18,125.71,1.01,8.45,None,220.0,6.48,13405.8,114.8,None,4.39),
'CUBE':(45.02,46.41,35.09,0.96,2.59,None,226.1,2.12,3540,14.3,None,4.74)}
ys=[]
for t,(p,h,l,b,f,cx,sh,dv,de,ca,eb,med) in R.items():
    k=RF+b*ERP; ff=f/(k/100)
    s=f"{t:5} off {100*(p/h-1):6.1f}% A-px {.8*h:7.2f} need {100*(.8*h/p-1):6.1f}% lowup {100*(p/l-1):5.0f}% CoE {k:5.2f} P/FFO {p/f:5.1f} FFOy {100*f/p:5.2f} spread {100*f/p-k:+5.2f} yld {100*dv/p:4.2f} med {med} pay {100*dv/f:3.0f}% FV {ff:7.2f} P/FV {p/ff:.2f}"
    if cx: 
        fa=f-cx/sh; fv2=fa/(k/100); s+=f" | capex/sh {cx/sh:.2f} FAD {fa:.2f} payFAD {100*dv/fa:.0f}% FV2 {fv2:.2f} P/FV2 {p/fv2:.2f}"
    if de and eb: s+=f" | ND/EBITDA {(de-ca)/eb:.2f}"
    print(s)
print('PK ND 3725/640',3725/640,'HST adj cash',(5084-991)/1865,'PSA off',100*(337.46/345.89-1),'SPX off',100*(7376.86/7844.52-1))
