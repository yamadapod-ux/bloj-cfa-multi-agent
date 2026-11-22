# Quinn MYRG model 2026-11-21 (independent; mid-cycle margin; VS2). Inputs from Atlas Data Package 2026-11-21.
PRICE = 247.71
SH = 15.721      # diluted wtd shares Q3'26 (SEC 10-Q via Atlas)
ND = 255.10      # net debt incl leases (Atlas)
JV = 3.258       # investment in JVs (Atlas)
WACC = 0.0981    # locked (Atlas)
TAX = 0.265      # 9M26 effective 26.6% (10-Q)
KD_AT = 0.0497   # after-tax Kd (Atlas)
CASH_R = 0.036   # after-tax Rf proxy for net cash
REV26 = 4540.0   # consensus FY2026E (Yahoo analysis via Atlas)
NWC = 0.07       # dNWC as % of d revenue (derived from TTM OCF bridge; assumption)


def scen(g, m, capex, da, ronic, tgr=0.03, wacc=WACC, margin_shift=0.0):
    rev = [REV26]
    fcff = []
    for i in range(10):
        r = rev[-1] * (1 + g[i])
        n = r * (m[i] + margin_shift) * (1 - TAX)
        if i < 5:
            f = n - (capex[i] - da[i]) * r - NWC * (r - rev[-1])
        else:
            f = n * (1 - g[i] / ronic)   # VS2 1.3: reinvestment = g / RONIC in fade
        rev.append(r)
        fcff.append(f)
    nT = rev[-1] * (1 + tgr) * (m[9] + margin_shift) * (1 - TAX)
    fT = nT * (1 - tgr / ronic)
    tv10 = fT / (wacc - tgr)
    t = [i + 0.5 for i in range(10)]
    pv = sum(f / (1 + wacc) ** tt for f, tt in zip(fcff, t))
    pvtv = tv10 / (1 + wacc) ** 9.5
    ev = pv + pvtv
    eq = ev + JV - ND
    ev5 = sum(f / (1 + wacc) ** (tt - 5) for f, tt in zip(fcff[5:], t[5:])) + tv10 / (1 + wacc) ** 4.5
    nd = ND
    for i in range(5):
        rate = KD_AT if nd > 0 else CASH_R
        nd = nd * (1 + rate) - fcff[i]
    eq5 = ev5 + JV - nd
    return dict(fv=eq / SH, ev=ev, tvshare=pvtv / ev, fv5=eq5 / SH, nd5=nd, eq0=eq, eq5=eq5,
                rev=rev, fcff=fcff, cagr5=(rev[5] / rev[0]) ** 0.2 - 1)


def fade(last, tgr=0.03, n=5):
    return [last + (tgr - last) * (i + 1) / n for i in range(n)]


CAP = [0.034, 0.033, 0.032, 0.030, 0.029]
DA = [0.0195, 0.0205, 0.0215, 0.0225, 0.0235]
gB = [0.152, 0.09, 0.07, 0.06, 0.05]; gB += fade(0.05)
mB = [0.060, 0.0550, 0.0510, 0.0470, 0.0450] + [0.0450] * 5
gU = [0.17, 0.14, 0.11, 0.09, 0.07]; gU += fade(0.07)
mU = [0.0650, 0.0640, 0.0610, 0.0580, 0.0560] + [0.0560] * 5
gD = [0.08, -0.08, -0.03, 0.03, 0.04]; gD += fade(0.04)
mD = [0.0520, 0.0200, 0.0300, 0.0330, 0.0350] + [0.0350] * 5
S = {'Bull': (0.25, gU, mU, 0.18), 'Base': (0.45, gB, mB, 0.14), 'Bear': (0.30, gD, mD, 0.098)}
res = {k: scen(g, m, CAP, DA, r) for k, (p, g, m, r) in S.items()}
pw = sum(S[k][0] * res[k]['fv'] for k in S)
pw5 = sum(S[k][0] * res[k]['fv5'] for k in S)


def pwfv(**kw):
    return sum(p * scen(g, m, CAP, DA, r, **kw)['fv'] for k, (p, g, m, r) in S.items())


def path(mt):
    return [0.060 + (mt - 0.060) * min(i, 4) / 4 for i in range(5)] + [mt] * 5


def fv_for(sc, mt, ron=0.14):
    g = [x * sc for x in gB[:5]]; g += fade(g[4])
    r = scen(g, path(mt), CAP, DA, ron)
    return r['fv'], r['cagr5']


if __name__ == '__main__':
    for k, v in res.items():
        print(k, 'p=%.2f FV=%.2f EV=%.0f TV/EV=%.1f%% FV5=%.2f rev5CAGR=%.1f%% ND5=%.0f' % (S[k][0], v['fv'], v['ev'], v['tvshare'] * 100, v['fv5'], v['cagr5'] * 100, v['nd5']))
        print('  FCFF', [round(x) for x in v['fcff']])
    print('PW FV %.2f MOS(FV/P-1) %.1f%% MOS((FV-P)/FV) %.1f%% | PW FV5 %.2f ER %.2f%%' % (pw, (pw / PRICE - 1) * 100, (pw - PRICE) / pw * 100, pw5, ((pw5 / PRICE) ** 0.2 - 1) * 100))
    for mm, lab in [(0.045, 'mid-cycle 4.5%'), (0.0605, 'TTM 6.05%')]:
        n = 4314.7 * mm * (1 - TAX); ev = n / WACC
        print('no-growth', lab, 'NOPAT %.0f EV %.0f per sh %.2f' % (n, ev, (ev + JV - ND) / SH))
    ke = 0.1016
    for k, v in res.items():
        print(k, 'Eq5/(Eq0*(1+Ke)^5) = %.3f' % (v['eq5'] / (v['eq0'] * (1 + ke) ** 5)))
    b = res['Base']
    ev_mkt = PRICE * SH - JV + ND
    print('mkt EV %.0f ; EV/EBITDA FY27E(base) %.2f ; Base FV implied EV/TTM EBITDA %.2f ; PW implied %.2f' % (ev_mkt, ev_mkt / (b['rev'][1] * (0.060 + DA[0])), b['ev'] / 338.7, (pw * SH - JV + ND) / 338.7))
    print('own yr-end EV/EBITDA FY21-25 avg %.2f' % ((11.25 + 9.45 + 13.48 + 20.60 + 14.99) / 5))
    margins = [0.030, 0.0375, 0.045, 0.0525, 0.060]
    scales = [0.4, 0.7, 1.0, 1.3, 1.6]
    cg = []
    for sc in scales:
        g = [x * sc for x in gB[:5]]; g += fade(g[4]); cg.append(scen(g, mB, CAP, DA, 0.14)['cagr5'])
    print('\nSENS1 margin(terminal) x growth scale; 5Y rev CAGR:', [round(x * 100, 1) for x in cg])
    for mt in margins:
        print('%.2f%%' % (mt * 100), [round(fv_for(sc, mt)[0], 1) for sc in scales])
    print('\nSENS2 margin x WACC (base growth, RONIC 14%)')
    for mt in margins:
        print('%.2f%%' % (mt * 100), [round(scen(gB, path(mt), CAP, DA, 0.14, wacc=w)['fv'], 1) for w in [0.0881, 0.0931, 0.0981, 0.1031, 0.1081]])
    for mt in [0.045, 0.0525, 0.060]:
        lo, hi = 0.0, 8.0
        for _ in range(80):
            mid = (lo + hi) / 2
            if fv_for(mid, mt)[0] < PRICE: lo = mid
            else: hi = mid
        print('Reverse DCF terminal margin %.2f%%: growth scale %.2f -> 5Y rev CAGR %.1f%% (FV %.1f)' % (mt * 100, mid, fv_for(mid, mt)[1] * 100, fv_for(mid, mt)[0]))
    lo, hi = 0.02, 0.15
    for _ in range(80):
        mid = (lo + hi) / 2
        if scen(gB, path(mid), CAP, DA, 0.14)['fv'] < PRICE: lo = mid
        else: hi = mid
    print('implied terminal margin at base growth: %.2f%%' % (mid * 100))
    print('consensus 2025->27 rev CAGR %.1f%% ; 1.2x = %.1f%%' % (((5230 / 3657.9) ** 0.5 - 1) * 100, 1.2 * ((5230 / 3657.9) ** 0.5 - 1) * 100))
    print('\nJC table (PW FV): base %.2f' % pw)
    print('WACC 10.3%%: %.2f | 9.5%%: %.2f | +1.15pp: %.2f' % (pwfv(wacc=0.103), pwfv(wacc=0.095), pwfv(wacc=WACC + 0.0115)))
    print('TGR 2.5%%: %.2f | 3.5%%: %.2f' % (pwfv(tgr=0.025), pwfv(tgr=0.035)))
    print('margin +1pp: %.2f | -1pp: %.2f' % (pwfv(margin_shift=0.01), pwfv(margin_shift=-0.01)))
    print('prob 20/45/35: %.2f | 30/45/25: %.2f' % (0.20 * res['Bull']['fv'] + 0.45 * b['fv'] + 0.35 * res['Bear']['fv'], 0.30 * res['Bull']['fv'] + 0.45 * b['fv'] + 0.25 * res['Bear']['fv']))
