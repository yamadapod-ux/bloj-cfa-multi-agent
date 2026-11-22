import importlib.util,sys
spec=importlib.util.spec_from_file_location('m','2026-11-21_MYRG_model.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
# multiples cross-check
SH,ND,JV=m.SH,m.ND,m.JV
def px(ev): return (ev+JV-ND)/SH
E_ttm=338.7
mid_ebitda=4314.7*(0.045+0.0200)
print('mid-cycle EBITDA (4.5pct EBIT + 2.0pct D&A on TTM rev): %.0f'%mid_ebitda)
for lab,mult in [('own FY21-25 median 13.48',13.48),('own avg ex-FY24 12.27',(11.25+9.45+13.48+14.99)/4),('peer median 11.46',11.46),('current 12.14',12.14)]:
    print(lab,'TTM-EBITDA price %.1f | mid-cycle EBITDA price %.1f'%(px(mult*E_ttm),px(mult*mid_ebitda)))
# implied terminal EV/EBITDA of base DCF at end yr10
for k in ['Bull','Base','Bear']:
    p,g,mm,r=m.S[k]
    nT=None
    res=m.res[k]; rev10=res['rev'][10]
    nopat11=rev10*1.03*mm[9]*(1-m.TAX); f11=nopat11*(1-0.03/r); tv=f11/(m.WACC-0.03)
    ebitda10=rev10*(mm[9]+0.0235)
    print(k,'TV(yr10)=%.0f implied EV/EBITDA(yr10) %.2f  EV/NOPAT %.1f'%(tv,tv/ebitda10,tv/(rev10*mm[9]*(1-m.TAX))))
# exit multiple that makes PW-base DCF = price (Base scenario)
p,g,mm,r=m.S['Base']; res=m.res['Base']
pv=sum(f/(1+m.WACC)**(i+0.5) for i,f in enumerate(res['fcff']))
need_ev=m.PRICE*SH-JV+ND; need_tv_pv=need_ev-pv; tv=need_tv_pv*(1+m.WACC)**9.5
e10=res['rev'][10]*(mm[9]+0.0235); print('Base: exit EV/EBITDA needed for price: %.1fx (TV %.0f / EBITDA10 %.0f)'%(tv/e10,tv,e10))
# Base with exit multiple 10x / 12x on yr10 EBITDA instead of Gordon
for mult in [8,10,12]:
    tvm=mult*e10; ev=pv+tvm/(1+m.WACC)**9.5; print('Base DCF w/ exit %dx: FV %.1f'%(mult,px(ev)))
print('--- P-W with exit-multiple terminal (variant, NOT primary) ---')
for mult in [8,10,12]:
    tot=0;tot5=0;lst=[]
    for k,(p,g,mm,r) in m.S.items():
        res=m.res[k]
        pv=sum(f/(1+m.WACC)**(i+0.5) for i,f in enumerate(res['fcff']))
        e10=res['rev'][10]*(mm[9]+0.0235)
        # bear: use lower multiple? keep same multiple for all (transparent)
        ev=pv+mult*e10/(1+m.WACC)**9.5; v=px(ev); tot+=p*v; lst.append(round(v,1))
        ev5=sum(f/(1+m.WACC)**(i+0.5-5) for i,f in enumerate(res['fcff']) if i>=5)+mult*e10/(1+m.WACC)**4.5
        nd=m.ND
        for i in range(5):
            nd=nd*(1+(m.KD_AT if nd>0 else m.CASH_R))-res['fcff'][i]
        tot5+=p*(ev5+JV-nd)/SH
    print('exit %dx: scen FVs %s  PW %.1f  PW FV5 %.1f ER %.1f%%'%(mult,lst,tot,tot5,((tot5/m.PRICE)**0.2-1)*100))
