import json, sys
from hist import *
from sec import *
exec(open(os.path.join(os.path.dirname(os.path.abspath(sys.modules['hist'].__file__)),'roicq.py')).read()) if False else None
o = json.load(open('screen_out.json'))
for t in sys.argv[1:]:
    x = o[t]; print('==', t, 'end', x['end'], 'mcap', round(x['mcap']/1e6), 'sh', round(x['sh']/1e6,2), 'ND', round(x['nd']/1e6), 'EQ', round((x['eq'] or 0)/1e6),'EBITDA',round(x['ebitda']/1e6),'OI',round(x['oi']/1e6),'CFO',round(x['cfo']/1e6),'capex',round(x['capex']/1e6),'SBC',round(x['sbc']/1e6))
    print('  FY', x['fys'], 'FCF', [round(v/1e6) for v in x['fcfh']], 'SBC', [round(v/1e6) for v in x['sbch']])
    print('  ROIC', round(100*x['roic'],1) if x['roic']==x['roic'] else None, 'hist', [round(100*v,1) if v==v and v is not None else None for v in x['roic_hist']], 'beta', round(x['beta'],2), round(x['bb'],2), 'ke', round(100*x['ke'],2), 'WACC', round(100*x['wacc'],2))
    print('  EV/EBITDA', x['evx'], 'pct', x['evx_pct'], x['evx_min'], x['evx_med'], x['evx_max'], 'naive5Y', round(x['naive'],2), 'exSBC', round(x['naive_sbc'],2), 'TTM', round(x['naive_ttm'],2), 'PT', x['pt'])
    f = facts(t)
    OI2=['OperatingIncomeLoss']
    ends = sorted({a['end'] for a in series(f, REV) if a.get('start') and a['end']>='2025-03-01'})
    for e in ends:
        oi = ttm_at(f, OI2, e); eq = inst1(f, EQ, e); d = debt(f,e); m = mkt(f,e)
        print('   ',e,'TTM OI',round(oi/1e6) if oi is not None else None,'Rev',round((ttm_at(f,REV,e) or 0)/1e6),'IC',round(((eq or 0)+d-m)/1e6),'ROIC@21%', round(100*oi*.79/((eq or 0)+d-m),1) if oi is not None and (eq or 0)+d-m>0 else None)
    fl=sorted({(a['form'],a['end'],a['filed']) for a in series(f,REV) if a.get('start')},key=lambda z:z[2])[-1]; print('  latest filing',fl)
