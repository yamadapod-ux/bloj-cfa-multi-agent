# Quinn AMZN v3.5 — own 3 scenarios re-anchored to Q3-2026 actuals. Imports Emma's v3.5 model READ-ONLY and overrides only MODELS['Quinn *'].
# Judgment calls Q1-Q10 were locked in agent_notes/quinn/2026-11-22_AMZN_v3.5.md § 0 before this file was written/run.
# Run: python -I agent_notes/quinn/2026-11-22_AMZN_v3.5_scenarios.py
import importlib.util, copy, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, '..', 'emma', '2026-11-22_AMZN_v3.5_model.py')
spec = importlib.util.spec_from_file_location('emma35', P)
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
A = M.A35

# ---- locked assumptions (Q3, Q4, Q5, Q6, Q7) ----
LOCK = {
    'Quinn Bull': dict(g=(.38, .15), m=(.395, .44), c=(.88, .12), rg=(.115, .05), rm=(.066, .09), ronic=.314),
    'Quinn Base': dict(g=(.31, .09), m=(.388, .40), c=(.88, .16), rg=(.10, .042), rm=(.065, .075), ronic=.1849),
    'Quinn Bear': dict(g=(.26, .04), m=(.378, .355), c=(.90, .30), rg=(.075, .028), rm=(.062, .060), ronic='WACC'),
}

def scen(a, shift=0.0):
    g = [A['aws_g26']] + M.lin(a['g'][0] + shift, a['g'][1] + shift, 9)
    m = [A['aws_m26']] + M.lin(a['m'][0], a['m'][1], 9)
    aws = dict(base=M.AWS_BASE, g=g, m=m, capex=M.lin(*a['c']), da=M.DA_AWS)
    ret = dict(base=M.RET_BASE, g=[A['ret_g0']] + M.lin(a['rg'][0], a['rg'][1], 9),
               m=[A['ret_m0']] + M.lin(a['rm'][0], a['rm'][1], 9), capex=M.RET_CAPEX_E, da=M.RET_DA)
    return dict(aws=aws, ret=ret, ronic=a['ronic'])

def runq(cfg=None, over=None, base_shift=0.0, wts=(.25, .5, .25), full=False):
    cfg = cfg or M.CFG35
    M.configure(cfg)
    L = copy.deepcopy(LOCK)
    for k, v in (over or {}).items():
        L[k].update(v)
    M.MODELS['Quinn Bull'] = scen(L['Quinn Bull'])
    M.MODELS['Quinn Base'] = scen(L['Quinn Base'], base_shift)
    M.MODELS['Quinn Bear'] = scen(L['Quinn Bear'])
    R = {n: M.value(n, 7) for n in ('Quinn Bull', 'Quinn Base', 'Quinn Bear')}
    pw = wts[0] * R['Quinn Bull']['fv'] + wts[1] * R['Quinn Base']['fv'] + wts[2] * R['Quinn Bear']['fv']
    out = dict(R=R, pw=pw, bull=R['Quinn Bull']['fv'], base=R['Quinn Base']['fv'], bear=R['Quinn Bear']['fv'], wacc=M.WACC)
    if full:
        f = {n: M.fv5(R[n]) for n in R}
        out['f'] = f
        out['pw5'] = wts[0] * f['Quinn Bull']['fv5'] + wts[1] * f['Quinn Base']['fv5'] + wts[2] * f['Quinn Bear']['fv5']
    return out

def cfgx(**kw):
    c = copy.deepcopy(M.CFG35); c.update(kw); return c

if __name__ == '__main__':
    M.configure(M.CFG35)
    print('WACC %.4f (Blume %.4f BU %.4f) price %.2f netdebt %.2f nonopAT %.2f shdil %.3f' % (M.WACC, M.WACC_BLUME, M.WACC_BU, M.PRICE, M.NET_DEBT_NEW, M.NONOP_AT, M.SH_DIL))
    r = runq(full=True)
    print('\n=== SCENARIOS (v3.5, locked) ===')
    for n in ('Quinn Bull', 'Quinn Base', 'Quinn Bear'):
        x = r['R'][n]; sg = x['segs']
        rev = [sum(v[i]['rev'] for v in sg.values()) for i in range(10)]
        ebit = [sum(v[i]['ebit'] for v in sg.values()) for i in range(10)]
        print('%-11s FV %.2f EV %.1f RONIC %.4f TV%% %.3f | FY26 rev %.1f EBIT %.1f | FY27 EBIT %.1f | FY30 rev %.0f EBIT %.0f | FY35 rev %.0f EBIT %.0f (%.1f%%)' % (
            n, x['fv'], x['ev'], x['ronic'], x['pv_tv_share'], rev[0], ebit[0], ebit[1], rev[4], ebit[4], rev[9], ebit[9], ebit[9] / rev[9] * 100),
            {k: round(v['ev'], 1) for k, v in x['vals'].items()}, x['info'])
        print('   FY26 capex %.1f FY27 capex %.1f | AWS g %s' % (sum(v[0]['capex'] for v in sg.values()), sum(v[1]['capex'] for v in sg.values()),
              [round(v, 3) for v in sg['AWS'] and [row['g'] for row in sg['AWS']]]))
    print('P-W EV (25/50/25) = %.2f' % r['pw'])
    print('v3.4 Quinn P-W 241.12 (Bull 434.41 / Base 212.90 / Bear 104.27) ; Emma ref col (v3.4 assumptions + shared facts) 222.13')
    ng = M.nogrowth(M.WACC, M.NET_DEBT_NEW, M.SH_DIL, M.NONOP_AT); ng0 = M.nogrowth(M.WACC, M.NET_DEBT_NEW, M.SH_DIL, 0)
    print('No-growth floor %.2f (incl non-op) / %.2f ex non-op. Bear %.2f -> %s ; Bear RONIC %.4f vs WACC %.4f' % (
        ng, ng0, r['bear'], 'ABOVE floor' if r['bear'] > ng else 'BELOW floor', r['R']['Quinn Bear']['ronic'], M.WACC))
    print('\n=== FV5 ===')
    for n, f in r['f'].items():
        print(n, 'EV5 %.1f nd5 %.1f eq5 %.1f sh5 %.3f FV5 %.2f consistency %+.1f%%' % (f['ev5'], f['nd5'], f['eq5'], f['sh5'], f['fv5'], f['consistency_gap'] * 100))
    print('Quinn P-W FV5 %.2f ; exp return/yr %.2f%% vs S&P %.2f%%' % (r['pw5'], ((r['pw5'] / M.PRICE) ** .2 - 1) * 100, M.SP500_EXP * 100))
    print('P-W EV vs price %.2f: MOS %+.1f%%' % (M.PRICE, (r['pw'] / M.PRICE - 1) * 100))

    print('\n=== 5x5 SENSITIVITY: Quinn Base FV, WACC x AWS growth shift (all years) ===')
    base_w = M.WACC
    waccs = [.085, .09, base_w, .105, .115]
    print('shift\\WACC ' + ' '.join('%9.2f%%' % (w * 100) for w in waccs))
    cells = 0
    for sh in (-.06, -.03, 0.0, .03, .06):
        row = []
        for w in waccs:
            v = runq(cfgx(wacc_mode=float(w)), base_shift=sh)['base']
            row.append(v); cells += v >= M.PRICE
        print('%+5.0fpp   ' % (sh * 100) + ' '.join('%10.2f' % v for v in row))
    print('cells >= price %.2f: %d/25' % (M.PRICE, cells))

    print('\n=== SENSITIVITY / JUDGMENT CALLS (one at a time; base P-W %.2f Base %.2f Bull %.2f Bear %.2f) ===' % (r['pw'], r['base'], r['bull'], r['bear']))
    def show(lab, **kw):
        x = runq(**kw)
        print('%-58s Bull %7.2f Base %7.2f Bear %7.2f P-W %7.2f (%+6.1f%%) WACC %.2f%%' % (lab, x['bull'], x['base'], x['bear'], x['pw'], (x['pw'] / r['pw'] - 1) * 100, x['wacc'] * 100))
    show('Q1 WACC Blume 10.35%', cfg=cfgx(wacc_mode='blume'))
    show('Q1 WACC BU 8.76%', cfg=cfgx(wacc_mode='bu'))
    show('Q2 v3.4 literal scenarios (Emma ref column logic)', over=None) if False else None
    # Q2 literal v3.4 scenarios
    M.configure(M.CFG35)
    R0 = {n: M.value(n, 7) for n in ('Quinn Bull', 'Quinn Base', 'Quinn Bear')}
    pw0 = .25 * R0['Quinn Bull']['fv'] + .5 * R0['Quinn Base']['fv'] + .25 * R0['Quinn Bear']['fv']
    print('%-58s Bull %7.2f Base %7.2f Bear %7.2f P-W %7.2f (%+6.1f%%)' % ('Q2 v3.4 literal scenario starts (stale, reference)', R0['Quinn Bull']['fv'], R0['Quinn Base']['fv'], R0['Quinn Bear']['fv'], pw0, (pw0 / r['pw'] - 1) * 100))
    show('Q3 Base AWS start 28%', over={'Quinn Base': dict(g=(.28, .09))})
    show('Q3 Base AWS start 34%', over={'Quinn Base': dict(g=(.34, .09))})
    show('Q3 Bull AWS start 36%', over={'Quinn Bull': dict(g=(.36, .15))})
    show('Q3 Bull AWS start 40% (mgmt claim)', over={'Quinn Bull': dict(g=(.40, .15))})
    show('Q3 Bear AWS start 22%', over={'Quinn Bear': dict(g=(.22, .04))})
    show('Q3 Bear AWS start 30%', over={'Quinn Bear': dict(g=(.30, .04))})
    show('Q4 Base AWS terminal margin 38%', over={'Quinn Base': dict(m=(.388, .38))})
    show('Q4 Base AWS terminal margin 42%', over={'Quinn Base': dict(m=(.388, .42))})
    show('Q4 Bear AWS terminal margin 33%', over={'Quinn Bear': dict(m=(.378, .33))})
    for cx in (269.0, 332.5, 395.0):
        show('Q5 FY27 capex %.1f' % cx, cfg=cfgx(capex_y2=cx))
    show('Q6 Base retail margin terminal 6.5%', over={'Quinn Base': dict(rm=(.065, .065))})
    show('Q6 Base retail margin terminal 8.5%', over={'Quinn Base': dict(rm=(.065, .085))})
    show('Q7 Base RONIC 12%', over={'Quinn Base': dict(ronic=.12)})
    show('Q7 Base RONIC = WACC', over={'Quinn Base': dict(ronic='WACC')})
    show('Q7 TGR 2.5%', cfg=cfgx(tgr=.025))
    show('Q7 TGR 3.5%', cfg=cfgx(tgr=.035))
    for lab, w in (('Q8 weights 20/50/30', (.2, .5, .3)), ('Q8 weights 30/50/20', (.3, .5, .2))):
        x = runq(wts=w); print('%-58s P-W %7.2f (%+6.1f%%)' % (lab, x['pw'], (x['pw'] / r['pw'] - 1) * 100))
    # Bear RONIC rule detail: Bear with RONIC=WACC for comparison
    x = runq(over={'Quinn Bear': dict(ronic='WACC')})
    print('Bear scenario with terminal RONIC = WACC (not implied): %.2f' % x['bear'])
    # Bear with Ads weakened? (v3.4 open item 4) — extra downside diagnostic, NOT in base
    M.configure(M.CFG35)
    # Reverse check: market-implied
    print('\nMarket price %.2f vs Bull %.2f (%+.1f%%)' % (M.PRICE, r['bull'], (r['bull'] / M.PRICE - 1) * 100))
