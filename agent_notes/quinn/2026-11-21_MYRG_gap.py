import importlib.util
spec=importlib.util.spec_from_file_location('m','2026-11-21_MYRG_model.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
P=m.PRICE
def solve(f,lo,hi):
    for _ in range(100):
        mid=(lo+hi)/2
        if f(mid)<P: hi=mid if False else hi; lo2=None
        break
# WACC closing on Base scenario (monotone decreasing in WACC)
p,g,mm,r=m.S['Base']
def fw(w): return m.scen(g,mm,m.CAP,m.DA,r,wacc=w)['fv']
lo,hi=0.035,0.0981
for _ in range(100):
    mid=(lo+hi)/2
    if fw(mid)>P: lo=mid
    else: hi=mid
print('WACC closing gap (Base, TGR3%%): %.2f%%'%(mid*100), fw(mid))
# TGR closing at WACC 9.81 (TGR must be < WACC)
def ft(t): return m.scen(g,mm,m.CAP,m.DA,r,tgr=t)['fv']
for t in [0.03,0.04,0.045,0.05,0.055,0.06]: print('TGR',t,round(ft(t),1))
# RONIC closing
for ro in [0.14,0.3,0.6,1.0,5.0]: print('RONIC',ro,round(m.scen(g,mm,m.CAP,m.DA,ro)['fv'],1))
