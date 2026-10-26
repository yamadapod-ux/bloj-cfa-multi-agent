# Charlie -- WGO 2026-10-26: resolves Bear Open Item B-O8 (Bear's "≈" interpolations for combined
# WACC x mid-cycle alternatives). Re-runs Emma's and Quinn's OWN models unchanged, only overriding
# wacc / mid-cycle target. No new assumptions. Run from repo root:  python -I agent_notes/charlie/2026-10-26_WGO_combined_alt.py
# Quinn note: in Quinn's bear scenario terminal RONIC = WACC, so when WACC is overridden RONIC follows it
# (Quinn's own reported 9.22% P-W $48.88 kept bear RONIC at 7.91% -> slightly lower; difference $0.51).
# Bear FV has no script (Bear env had no Python) -> Bear values at alt WACC are Bear's own estimates
# ($28.9 @9.22%, $24 @10.35%; agent_notes/bear/2026-10-26_WGO.md §4) and are labelled as such.
import importlib.util, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
spec = importlib.util.spec_from_file_location('emma', os.path.join(ROOT, 'agent_notes/emma/2026-10-26_WGO_model.py'))
emma = importlib.util.module_from_spec(spec); spec.loader.exec_module(emma)

src = open(os.path.join(ROOT, 'agent_notes/quinn/2026-10-26_WGO_model.py'), encoding='utf-8').read().splitlines()
a = [i for i, l in enumerate(src) if l.startswith('REV26 = 2703.9')][0]
b = [i for i, l in enumerate(src) if l.startswith('m_base27 =')][0]
q = dict(SH=28.6, TAX=0.223, WACC=0.0791, TGR=0.025, RONIC=0.0991, ND0=274.9, NONOP=22.8,
         KD_AT=0.04856, COE=0.0963, P0=28.65, print=lambda *x, **k: None)
exec('\n'.join(src[a:b + 1]), q)
lit_b = 0.5 * (0.01 * 55887 * 46275 / 1e6 + 5.0); lit_r = 0.03 * 55887 * 46275 / 1e6 + 15.0
SC = {'bull': (0.2, dict(cy26=290, cy27=295, hold_cy=2027, reach=2029, mid_units=410, m27=q['m_bull27'], m_hold_to=2027, m_target=0.0692, p=0.025, ronic=0.12, lit=0.0)),
      'base': (0.5, dict(cy26=290, cy27=285, hold_cy=2027, reach=2030, mid_units=385, m27=q['m_base27'], m_hold_to=2027, m_target=0.0692, p=0.025, ronic=0.0991, lit=lit_b)),
      'bear': (0.3, dict(cy26=285, cy27=275, hold_cy=2028, reach=2032, mid_units=330, m27=q['m_bear27'], m_hold_to=2028, m_target=0.0450, p=0.020, ronic=0.0791, lit=lit_r))}

def quinn_pw(w=0.0791, mid=None):
    t = 0
    for k, (p, kw) in SC.items():
        kw = dict(kw, wacc=w)
        if k == 'bear': kw['ronic'] = w                       # bear RONIC = WACC by Quinn's own definition
        elif mid is not None: kw['m_target'] = min(kw['m_target'], mid)  # bear keeps its own 4.50%
        t += p * q['scenario'](**kw)['fv']
    return t

BEAR = {0.0791: 36.02, 0.0922: 28.9, 0.1035: 24.0}   # Bear own FV / Bear own estimates (see header)
P = 28.65
print('WACC   mid    Emma    Quinn   Bear   Blended  MOS')
for w in (0.0791, 0.0922, 0.1035):
    for m in (0.0692, 0.0577, 0.05, 0.0475):
        e = emma.fv(wacc=w, mid=m); qq = quinn_pw(w, m); bl = 0.4 * e + 0.3 * qq + 0.3 * BEAR[w]
        print(f'{w*100:5.2f}% {m*100:5.2f}% {e:7.2f} {qq:7.2f} {BEAR[w]:6.2f} {bl:7.2f} {(bl-P)/bl*100:+6.1f}%')
