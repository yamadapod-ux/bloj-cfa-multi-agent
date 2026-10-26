# Emma -- WGO VS2 FCFF DCF (2026-10-26). All inputs from agent_notes/atlas/2026-10-26_WGO_data.md
# (locked P1-P16) unless marked EMMA (Emma's own judgment, fixed before running this script).
import copy

PRICE = 28.65            # Data Pkg A (Yahoo + SA, close 2026-10-23)
REV26 = 2703.9           # Data Pkg B1 (XBRL)
BASE = dict(
    wacc=0.0791,         # P1
    tax=0.223,           # P6
    tgr=0.025,           # P13
    ronic=0.0991,        # P13
    rev27=2725.0,        # P9 (FY27 guide midpoint, 8-K Q4)
    # EMMA: revenue growth FY28..FY36 (FY27 fixed by guide)
    growth=[0.06, 0.07, 0.06, 0.04, 0.035, 0.03, 0.03, 0.025, 0.025],
    m27=0.023,           # EMMA: FY27 GAAP EBIT margin implied by GAAP EPS guide midpoint $1.20 (see notes)
    mid=0.0692,          # P10 mid-cycle EBIT margin
    reach=2030,          # EMMA: FY in which mid-cycle is reached (P10: no earlier than FY29)
    capex=0.0155,        # P11 capex % revenue
    capex_early=None,    # alt: (pct, n_years) for early-year capex
    da27=60.0,           # FY26 actual D&A (38.3 dep + 21.7 amort), 8-K Q4
    da_norm=0.0149,      # 10y avg D&A % revenue (Data Pkg B1)
    da_conv=2031,        # EMMA: D&A converges linearly to normal by FY31
    nwc=0.142,           # EMMA calc: (AR 153.5 + Inv 404.7 - AP 174.1)/Rev 2703.9 (Data Pkg C)
    net_debt=274.9,      # P16
    nonop=22.8,          # VS2 1.2 bridge
    shares=28.6,         # P14
    years=10,            # P9
)

def margin_path(p, fy):
    if fy == 2027:
        return p['m27']
    if fy >= p['reach']:
        return p['mid']
    # linear from FY27 to reach year
    t = (fy - 2027) / (p['reach'] - 2027)
    return p['m27'] + t * (p['mid'] - p['m27'])

def run(p, detail=False):
    p = dict(p)
    fys = list(range(2027, 2027 + p['years']))
    rev_prev = REV26
    rows = []
    pv_sum = 0.0
    for i, fy in enumerate(fys):
        if fy == 2027:
            rev = p['rev27']
        else:
            g = p['growth'][i - 1] if i - 1 < len(p['growth']) else p['tgr']
            rev = rev_prev * (1 + g)
        m = margin_path(p, fy)
        ebit = rev * m
        nopat = ebit * (1 - p['tax'])
        # D&A convergence
        if fy >= p['da_conv']:
            da = rev * p['da_norm']
        else:
            t = (fy - 2027) / (p['da_conv'] - 2027)
            da = p['da27'] + t * (rev * p['da_norm'] - p['da27'])
        cx = p['capex']
        if p['capex_early'] and i < p['capex_early'][1]:
            cx = p['capex_early'][0]
        capex = rev * cx
        dnwc = p['nwc'] * (rev - rev_prev)
        fcff = nopat - (capex - da) - dnwc
        df = (1 + p['wacc']) ** (i + 1)
        pv = fcff / df
        pv_sum += pv
        rows.append(dict(fy=fy, rev=rev, g=rev / rev_prev - 1, m=m, ebit=ebit, nopat=nopat,
                         da=da, capex=capex, dnwc=dnwc, fcff=fcff, df=df, pv=pv))
        rev_prev = rev
    last = rows[-1]
    nopat_t1 = last['nopat'] * (1 + p['tgr'])
    rr = p['tgr'] / p['ronic']
    fcff_t1 = nopat_t1 * (1 - rr)
    tv = fcff_t1 / (p['wacc'] - p['tgr'])
    pv_tv = tv / last['df']
    ev = pv_sum + pv_tv
    eq = ev - p['net_debt'] + p['nonop']
    fv = eq / p['shares']
    out = dict(rows=rows, pv_sum=pv_sum, tv=tv, pv_tv=pv_tv, ev=ev, eq=eq, fv=fv,
               tv_pct=pv_tv / ev, rr=rr, fcff_t1=fcff_t1, nopat_t1=nopat_t1)
    return out

def fv(**kw):
    p = copy.deepcopy(BASE); p.update(kw); return run(p)['fv']

def solve(key, lo, hi, target=PRICE, **extra):
    """bisection on a scalar param so FV = target"""
    f = lambda x: fv(**{key: x}, **extra) - target
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        return None
    for _ in range(100):
        mid = (lo + hi) / 2
        fm = f(mid)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2

def fv5(p):
    """VS2 1.4: Equity at end of FY31 (year 5)."""
    r = run(p)
    rows = r['rows']
    w = p['wacc']
    # PV at end of year 5 of FCFF years 6..10 + TV
    ev5 = sum(rows[j]['fcff'] / (1 + w) ** (j - 4) for j in range(5, len(rows)))
    ev5 += r['tv'] / (1 + w) ** (len(rows) - 5)
    nd = p['net_debt']
    dps = 1.44; shares = p['shares']; divs = []
    kd_at = 0.0625 * (1 - p['tax'])
    for j in range(5):
        div = dps * shares * (1.03 ** j)        # EMMA: dividend +3%/yr (FY26 raise +3%, 8-K Q4)
        interest_at = nd * kd_at
        nd = nd - (rows[j]['fcff'] - interest_at - div)
        divs.append(div)
    eq5 = ev5 + p['nonop'] - nd
    fv5_ps = eq5 / shares                        # shares held flat: SBC expensed = buyback offset
    # consistency: Equity0*(1+CoE)^5 - FV(dividends) at CoE
    coe = 0.0963
    eq0 = r['eq']
    fv_divs = sum(d * (1 + coe) ** (4 - j) for j, d in enumerate(divs))
    implied = eq0 * (1 + coe) ** 5 - fv_divs
    return dict(ev5=ev5, nd5=nd, eq5=eq5, fv5=fv5_ps, implied=implied,
                gap=eq5 / implied - 1, divs=sum(divs))

if __name__ == '__main__':
    b = run(BASE)
    print('=== BASE ===')
    print(f"{'FY':>5}{'Rev':>9}{'g':>7}{'EBIT%':>7}{'EBIT':>8}{'NOPAT':>8}{'D&A':>7}{'Capex':>7}{'dNWC':>7}{'FCFF':>8}{'PV':>8}")
    for x in b['rows']:
        print(f"{x['fy']:>5}{x['rev']:>9.1f}{x['g']*100:>6.1f}%{x['m']*100:>6.2f}%{x['ebit']:>8.1f}{x['nopat']:>8.1f}{x['da']:>7.1f}{x['capex']:>7.1f}{x['dnwc']:>7.1f}{x['fcff']:>8.1f}{x['pv']:>8.1f}")
    print(f"PV explicit {b['pv_sum']:.1f} | NOPAT_T+1 {b['nopat_t1']:.1f} RR {b['rr']*100:.1f}% FCFF_T+1 {b['fcff_t1']:.1f} | TV {b['tv']:.1f} PV(TV) {b['pv_tv']:.1f} | EV {b['ev']:.1f} | TV% {b['tv_pct']*100:.1f}%")
    print(f"Equity {b['eq']:.1f} | FV/share {b['fv']:.2f} | MOS {(b['fv']-PRICE)/b['fv']*100:.1f}%")
    # no-growth floors
    print('No-growth floor (FY26 NOPAT 51.4 / WACC):', round((51.4/0.0791 - 274.9 + 22.8)/28.6, 2))
    ng_mid = 2725*0.0692*(1-0.223)/0.0791
    print('No-growth mid-cycle (FY27 rev x 6.92%):', round((ng_mid-274.9+22.8)/28.6, 2))
    # market-implied perpetual NOPAT
    ev_mkt = 814.9 + 274.9 - 22.8
    print('Market EV(op) ', round(ev_mkt,1), 'implied no-growth NOPAT', round(ev_mkt*0.0791,1),
          'EBIT margin on FY27 rev', round(ev_mkt*0.0791/(1-0.223)/2725*100,2), '%')

    print('\n=== SCENARIOS ===')
    bear = dict(growth=[0.0, 0.04, 0.04, 0.035, 0.03, 0.03, 0.025, 0.025, 0.025],
                rev27=2650.0, m27=0.021, mid=0.050, reach=2031, ronic=0.0791)
    bull = dict(growth=[0.09, 0.09, 0.06, 0.04, 0.035, 0.03, 0.03, 0.025, 0.025],
                rev27=2800.0, m27=0.026, mid=0.0795, reach=2029)
    for name, kw in [('Bear', bear), ('Base', {}), ('Bull', bull)]:
        p = copy.deepcopy(BASE); p.update(kw); r = run(p)
        print(f"{name}: FV {r['fv']:.2f} EV {r['ev']:.1f} TV% {r['tv_pct']*100:.1f}% MOS {(r['fv']-PRICE)/r['fv']*100:.1f}%  FY31 rev {r['rows'][4]['rev']:.0f}")
    # Bear variant: margin stays 2.5% until FY30 then 4%
    bear2 = dict(bear); bear2.update(mid=0.04, reach=2032, m27=0.021)
    p = copy.deepcopy(BASE); p.update(bear2); print('Deep bear (4% mid, FY32):', round(run(p)['fv'],2))
    pw = 0.25*fv(**bear)+0.5*b['fv']+0.25*fv(**bull)
    print('P-W 25/50/25:', round(pw,2))

    print('\n=== FV5 ===')
    f5 = fv5(BASE)
    print({k: round(v, 2) for k, v in f5.items()})
    print('Implied annual return (price only):', round(((f5['fv5']/PRICE)**0.2-1)*100,2), '%',
          '| + dividend yield 5.03%')

    print('\n=== 1.6 SENSITIVITY ===')
    base_fv = b['fv']
    tests = [
        ('P1 WACC 10.0%', dict(wacc=0.10)),
        ('P1 WACC 13.0%', dict(wacc=0.13)),
        ('P1 WACC 7.85% (bottom-up incl op leases)', dict(wacc=0.0785)),
        ('P2/P3 stale median 6.76%', dict(wacc=0.0676)),
        ('P4 Blume only 8.02%', dict(wacc=0.0802)),
        ('P4 Bottom-up only 7.81%', dict(wacc=0.0781)),
        ('P5 Kd 5.89% -> WACC 7.81%', dict(wacc=0.0781)),
        ('P6 tax 21%', dict(tax=0.21, wacc=0.0791+0.359*0.0625*(0.223-0.21))),
        ('P6 tax 25%', dict(tax=0.25, wacc=0.0791-0.359*0.0625*(0.25-0.223))),
        ('P9 5-yr explicit', dict(years=5)),
        ('P10 mid 5.77% (ex-boom)', dict(mid=0.0577)),
        ('P10 mid 7.95% (pre-COVID)', dict(mid=0.0795)),
        ('P10 reach FY29', dict(reach=2029)),
        ('P10 reach FY31', dict(reach=2031)),
        ('P11 capex 0.89% FY27-28', dict(capex_early=(0.0089, 2))),
        ('P11 capex 2.0% all years', dict(capex=0.02)),
        ('P11 D&A = 1.49% from FY27', dict(da27=2725*0.0149)),
        ('P13 TGR 2.0%', dict(tgr=0.02)),
        ('P13 TGR 3.0%', dict(tgr=0.03)),
        ('P13 RONIC = WACC', dict(ronic=0.0791)),
        ('P13 RONIC 12%', dict(ronic=0.12)),
        ('P14 shares 28.44M', dict(shares=28.444)),
        ('P14 shares +461K options', dict(shares=28.6+0.461)),
        ('P15 op leases in net debt (double count)', dict(net_debt=274.9+44.4)),
        ('P16 converts at FV 324', dict(net_debt=274.9-26.0)),
        ('EMMA NWC 18%', dict(nwc=0.18)),
        ('EMMA growth -1pp all yrs', dict(growth=[g-0.01 for g in BASE['growth']])),
    ]
    for name, kw in tests:
        v = fv(**kw)
        print(f"{name:45s} FV {v:7.2f}  dEmma {((v/base_fv)-1)*100:+6.1f}%")

    print('\n=== GAP-CLOSING (FV = $28.65) ===')
    print('mid-cycle margin:', solve('mid', 0.01, 0.0692))
    print('WACC:', solve('wacc', 0.0791, 0.40))
    print('TGR:', solve('tgr', -0.30, 0.025))
    print('RONIC:', solve('ronic', 0.01, 0.0991))
    # revenue: scale all growth by k (k*growth), FY27 fixed
    def fvk(k): return fv(growth=[g*k for g in BASE['growth']])
    lo, hi = -5.0, 1.0
    for _ in range(80):
        m = (lo+hi)/2
        if fvk(m) > PRICE: hi = m
        else: lo = m
    k = (lo+hi)/2
    rr = [BASE['rev27']]
    for g in BASE['growth']: rr.append(rr[-1]*(1+g*k))
    print('growth scale k', round(k,3), 'FY27-36 CAGR', round(((rr[-1]/2725)**(1/9)-1)*100,2), '%')
    # margin + reach combined: mid margin if reach FY32
    print('mid margin if reach FY32:', solve('mid', 0.01, 0.0692, reach=2032))

    print('\n=== EXTRA TESTS ===')
    # (1) steady-state reinvestment = g/RONIC from FY31 (replaces driver-based capex/NWC)
    p = copy.deepcopy(BASE); r = run(p)
    pv = 0
    for i, x in enumerate(r['rows']):
        f = x['fcff']
        if x['fy'] >= 2031:
            f = x['nopat'] * (1 - x['g'] / p['ronic'])
        pv += f / x['df']
    ev = pv + r['pv_tv']; print('g/RONIC reinvest from FY31: FV', round((ev - 274.9 + 22.8) / 28.6, 2))
    print('TGR 0%:', round(fv(tgr=0.0), 2), '| TGR -2%:', round(fv(tgr=-0.02), 2))
    # (2) revenue held: FY28+ grows only 2.5% (no cyclical volume recovery), margin still to 6.92%
    print('No volume recovery (g=2.5% all yrs), margin 6.92%:', round(fv(growth=[0.025]*9), 2))
    print('No volume recovery + mid 5.77%:', round(fv(growth=[0.025]*9, mid=0.0577), 2))
    print('WACC 10% + mid 5.77%:', round(fv(wacc=0.10, mid=0.0577), 2))
    print('WACC 13% + mid 5.77%:', round(fv(wacc=0.13, mid=0.0577), 2))
    # solve WACC under bear
    print('WACC to hit price, mid 5.77%:', solve('wacc', 0.0791, 0.40, mid=0.0577))

    print('\n=== CROSS-CHECKS ===')
    rev27 = 2725.0; nd = 274.9; no = 22.8; sh = 28.6
    ebitda_mid = rev27 * (0.0692 + 0.0149)
    for name, mult in [('WGO 5Y avg EV/EBITDA 7.74x (SA, Mar-26)', 7.74),
                       ('WGO 5Y avg fwd 7.38x', 7.38),
                       ('Core peer median 8.76x', 8.76),
                       ('WGO FY22-26 median 10.13x', 10.13)]:
        print(f"{name}: EBITDA_mid {ebitda_mid:.1f} -> FV {(mult*ebitda_mid - nd + no)/sh:.2f}")
    print('Market EV / mid-cycle EBITDA:', round(1089.8 / ebitda_mid, 2), 'x')
    int_fy27 = 18.5
    eps_mid = (rev27 * 0.0692 - int_fy27) * (1 - 0.223) / sh
    print('mid-cycle EPS', round(eps_mid, 2))
    for name, pe in [('Peer fwd P/E median 13.97x', 13.97), ('WGO FY23 P/E 8.91x', 8.91), ('THO fwd 19.29x', 19.29)]:
        print(f"  {name}: FV {pe*eps_mid:.2f}")
    print('Trough: FY27 cons EPS 2.00 x 13.97 =', round(2.00 * 13.97, 2), '| FY28 2.52 x 13.97 =', round(2.52 * 13.97, 2),
          '| THO-only fwd 19.29 x 2.00 =', round(2.00*19.29, 2))
    bvps = 1236.6 / 28.444
    print('BVPS', round(bvps, 2), '| 5Y median P/B 1.36 ->', round(1.36 * bvps, 2))
    ni_mid = (rev27 * 0.0692 - int_fy27) * (1 - 0.223)
    roe = ni_mid / 1236.6
    jpb = (roe - 0.025) / (0.0963 - 0.025)
    print('mid ROE', round(roe * 100, 2), '% justified P/B', round(jpb, 3), '-> FV', round(jpb * bvps, 2))
    print('market-implied ROE at P/B 0.66:', round((0.66 * (0.0963 - 0.025) + 0.025) * 100, 2), '%')
    # operating leverage line FY24->FY23
    print('Op-leverage line margin at FY30 rev 3276:', round(4.39 + (3276-2973.5)/(3490.7-2973.5)*(8.61-4.39), 2))
