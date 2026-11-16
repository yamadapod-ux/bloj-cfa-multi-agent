# Quinn MU 2026-11-08 reverse-DCF companion: consensus FY27/FY28 revenue held, solve persistence of peak margin
import copy,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from quinn_dcf_1108 import *
b=copy.deepcopy(SC['Base']); a27=275500/(REV0*1.18)-1; a28=320060/(REV0*1.18*1.20)/(1+a27)-1
b['asp']={2027:a27*100,2028:a28*100}
r=path(b); print('consensus FY27/28 rev $%.0fB/$%.0fB margins %.1f%%/%.1f%% NOPAT/share FY27 $%.0f FY28 $%.0f'%(r[0]['rev']/1e3,r[1]['rev']/1e3,r[0]['m']*100,r[1]['m']*100,r[0]['nopat']/SH,r[1]['nopat']/SH))
print('Base FV with consensus FY27-28: $%.2f'%value(b,r)['fv'])
for price in [PX,PXI]:
  for yrs in range(1,9):
    s2=copy.deepcopy(b)
    for y in range(2029,2029+yrs): s2['m'][y]=80
    v=value(s2,path(s2))['fv']
    if v>=price: print('@$%.2f: 80%% margin must hold FY29..FY%d (%d yrs beyond consensus window), FV $%.2f'%(price,2028+yrs,yrs,v)); break
    print('  thru FY%d -> $%.2f'%(2028+yrs,v))
