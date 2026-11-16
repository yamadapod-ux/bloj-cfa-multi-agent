import sys; sys.path.insert(0,'.')
from emma_dcf import *
citi_g=[0.060,0.050,0.045,0.040,0.040,0.035,0.035,0.030,0.030,0.030]; citi_m=[0.338,0.335]+[0.335]*8
print('TGR solve wide', solve(lambda x: model(tgr=x), -0.30, 0.06))
print('FV at TGR -5%', model(tgr=-0.05))
print('Citi+RONIC=WACC', model(g=citi_g,m=citi_m,ronic=0.101))
print('Citi+RONIC=WACC+TGR2%', model(g=citi_g,m=citi_m,ronic=0.101,tgr=0.02))
print('Citi + WACC 10.62', model(g=citi_g,m=citi_m,wacc=0.1062))
print('Citi + ronic=wacc + wacc10.62', model(g=citi_g,m=citi_m,ronic=0.101,wacc=0.1062))
r=model(g=citi_g,m=citi_m,full=True); print('Citi FY27 rev',r['rows'][0]['rev'],'NOPAT',r['rows'][0]['nopat'])
# Citi scenario margin needed
print('Citi growth, margin closing', solve(lambda x: model(g=citi_g,m=[x]*10), 0.1,0.4))
# CAGR of base
import math
c=1
for x in BASE_G: c*=1+x
print('base 10y CAGR',(c**0.1-1)*100)
# 5Y FV5 for Citi scenario and bull: reuse quickly via ratio approx not needed
