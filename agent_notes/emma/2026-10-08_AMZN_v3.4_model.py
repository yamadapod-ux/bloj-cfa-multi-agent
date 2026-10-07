# AMZN v3.4 (VS2) — reproducible model: rebuild v3.2 (Emma / Quinn x3 / Bear) then apply VS2 steps 1-8 cumulatively.
# All inputs: agent_notes/atlas/2026-10-07_AMZN_v3.md § Addendum v3.4 (VS2 Data Package). Run: python -I this_file.py
import math, json, sys

YEARS = list(range(2026, 2036))           # explicit 10y, end-year discounting (v3.2 convention, 2026 = t1)
TAX = 0.196                               # FY2025 effective (10-K: 19,087 / 97,311) — v3.2 assumption, unchanged
TGR = 0.03

# ---------------- Atlas VS2 Data Package (locked) ----------------
RF, ERP = 0.0530, 0.0420                  # 10Y UST avg(Treasury 5.28%, TradingEconomics 5.32%) 2026-10-07 ; Damodaran implied ERP 2026-10-01
RAW_BETA = (1.46 + 1.45) / 2              # stockanalysis 1.46 ; MarketBeat 1.45
BLUME = 0.67 * RAW_BETA + 0.33
BU_UNLEV = {'AWS': 1.25, 'Ads': 1.01, 'Retail': 0.78}       # Damodaran Jan-2026 cash-corrected: Software(Sys&App) / Advertising / Retail(General)
REV_TTM = {'AWS': 148.4, 'Ads': 76.07, 'Retail': 551.2}     # TTM to Q2'26 ($B), revenue weights (decided before valuation)
PRICE = 259.92
SH_BASIC = 10.786313572                   # cover page 10-Q (2026-07-22)
SH_DIL = 10.903                           # Q2'26 diluted weighted avg (10-Q)
DEBT = 132.224                            # LT debt 128.894 + current portion 3.330 (10-Q Note 5, carrying)
FIN_LEASE, FIN_OBLIG = 13.5, 8.3          # 10-Q Note 3 (finance leases not in cash capex)
CASH = 78.213 + 44.775                    # cash + marketable securities
KD_PRE = RF + 0.0055                      # Damodaran AA spread (S&P AA) Jan-2026
KD_AT = KD_PRE * (1 - TAX)
D_MKT = DEBT + FIN_LEASE + FIN_OBLIG      # operating leases excluded: rent sits in operating income -> FCF
E_MKT = PRICE * SH_BASIC
WD, WE = D_MKT / (D_MKT + E_MKT), E_MKT / (D_MKT + E_MKT)
w = {k: v / sum(REV_TTM.values()) for k, v in REV_TTM.items()}
BU_UNLEV_AVG = sum(BU_UNLEV[k] * w[k] for k in w)
BU_LEV = BU_UNLEV_AVG * (1 + (1 - 0.21) * D_MKT / E_MKT)
COE_BLUME, COE_BU = RF + BLUME * ERP, RF + BU_LEV * ERP
WACC_BLUME = WE * COE_BLUME + WD * KD_AT
WACC_BU = WE * COE_BU + WD * KD_AT
WACC = (WACC_BLUME + WACC_BU) / 2
COE = (COE_BLUME + COE_BU) / 2
NET_DEBT_OLD, SH_OLD, WACC_OLD = 9.24, 10.90, 0.1095
NET_DEBT_NEW = DEBT + FIN_LEASE + FIN_OBLIG - CASH
# Non-operating assets 2026-06-30 (10-Q): fair/carrying, cost basis, tax 21% x gain (DTL not disclosed -> flag)
NONOP = [  # name, value, cost
    ('Anthropic nonvoting preferred', 92.5, 10.0),
    ('Anthropic convertible notes (AFS, FV)', 97.9, 8.0),
    ('OpenAI Series C preferred (cost)', 28.7, 28.7),
    ('Other private equity (122.3-92.5-28.7)', 1.1, 1.1),
    ('Marketable equity securities', 4.7, 0.0),
    ('Equity warrants', 4.3, 0.0),
    ('Equity-method investments', 0.395, 0.395),
]
NONOP_PRE = sum(v for _, v, _ in NONOP)
NONOP_TAX = sum(0.21 * max(v - c, 0) for _, v, c in NONOP)
NONOP_AT = NONOP_PRE - NONOP_TAX
DIL = (10.889 / 10.492) ** (1 / 2.5) - 1   # diluted wtd shares FY2023 -> H1'26 (2.5y), no buybacks
CAPEX_Y1, CAPEX_Y2 = 220.0, 269.0
SP500_EXP = RF + ERP                       # Damodaran implied expected market return

# ---------------- helpers ----------------
def lin(a, b, n=10):
    return [a + (b - a) * i / (n - 1) for i in range(n)]

def build(seg):
    """seg: dict(base, g[list], m[list], capex[list], da[list]) -> per-year rows"""
    rev, out = seg['base'], []
    for i, y in enumerate(YEARS):
        rev = rev * (1 + seg['g'][i])
        nopat = rev * seg['m'][i] * (1 - TAX)
        cap, da = rev * seg['capex'][i], rev * seg['da'][i]
        out.append(dict(y=y, rev=rev, g=seg['g'][i], ebit=rev * seg['m'][i], nopat=nopat, capex=cap, da=da, fcff=nopat - cap + da))
    return out

def seg_value(rows, wacc, mode, ronic=None):
    """mode 'v32' = Gordon on FCFF2035 (v3.2). mode 'vs2' = fade (if g_last > TGR+3pp) + terminal reinvestment TGR/RONIC."""
    pv = sum(r['fcff'] / (1 + wacc) ** (i + 1) for i, r in enumerate(rows))
    flows = []  # post-explicit flows (year index, fcff)
    last = rows[-1]
    if mode == 'v32':
        tv = last['fcff'] * (1 + TGR) / (wacc - TGR); n_end = 10
    else:
        g_last = last['g']; n = 0
        nopat = last['nopat']
        if g_last > TGR + 0.03:
            n = min(10, math.ceil(round((g_last - TGR) / 0.01, 6)))
            for k in range(1, n + 1):
                g = g_last - k * (g_last - TGR) / n
                nopat *= (1 + g)
                flows.append((10 + k, nopat * (1 - g / ronic)))
        nopat_next = nopat * (1 + TGR)
        tv = nopat_next * (1 - TGR / ronic) / (wacc - TGR); n_end = 10 + n
    pv_fade = sum(f / (1 + wacc) ** t for t, f in flows)
    pv_tv = tv / (1 + wacc) ** n_end
    return dict(pv_exp=pv, pv_fade=pv_fade, pv_tv=pv_tv, ev=pv + pv_fade + pv_tv, flows=flows, tv=tv, n_end=n_end)

def ev_at_year5(rows, wacc, mode, ronic):
    """PV at end-2030 of FCFF 2031+ (explicit 2031-35 + fade + terminal)."""
    v = seg_value(rows, wacc, mode, ronic)
    pv5 = sum(r['fcff'] / (1 + wacc) ** (i + 1 - 5) for i, r in enumerate(rows) if i >= 5)
    pv5 += sum(f / (1 + wacc) ** (t - 5) for t, f in v['flows'])
    pv5 += v['tv'] / (1 + wacc) ** (v['n_end'] - 5)
    return pv5

# ---------------- v3.2 segment assumptions (from agent_notes v3.2 addenda) ----------------
AWS_BASE, RET_BASE = 128.725, 588.199      # FY2025 10-K segment net sales ($B); retail = NA+Intl
ADS_BASE = 68.63                            # FY2025 advertising services (10-K disaggregation; marketplacepulse / marketingdive)
# Emma AWS path = exact table in agent_notes/emma/2026-10-07_AMZN_v3.md (v3.1 E5, reused unchanged in v3.2)
EMMA_AWS = dict(base=AWS_BASE, g=[.33, .28, .23, .19, .16, .14, .12, .10, .09, .08],
                m=[.355, .365, .375, .385, .395, .405, .41, .415, .42, .42],
                capex=[.90, .75, .60, .45, .35, .28, .22, .18, .16, .15],
                da=[.17, .18, .185, .19, .19, .185, .18, .175, .17, .165])
DA_AWS = EMMA_AWS['da']
RET_DA = lin(.030, .035)
RET_CAPEX_E = lin(65.9 / (RET_BASE * 1.11), .048)

def retail(g0, g1, m0, m1, capex=None):
    return dict(base=RET_BASE, g=lin(g0, g1), m=lin(m0, m1), capex=capex or RET_CAPEX_E, da=RET_DA)

def aws(g0, g1, m0, m1, c0, c1):
    return dict(base=AWS_BASE, g=lin(g0, g1), m=lin(m0, m1), capex=lin(c0, c1), da=DA_AWS)

MODELS = {
    'Emma':       dict(aws=EMMA_AWS,                            ret=retail(.11, .04, .062, .080), ronic=.1849, reported=148.53),
    'Bear':       dict(aws=aws(.28, .08, .355, .386, .88, .16), ret=retail(.09, .03, .058, .061, lin(95.9 / (RET_BASE * 1.09), .048)), ronic='WACC', reported=89.13),
    'Quinn Bull': dict(aws=aws(.35, .15, .36, .44, .88, .12),   ret=retail(.12, .05, .062, .090), ronic=.314, reported=244.06),
    'Quinn Base': dict(aws=aws(.30, .09, .35, .40, .88, .16),   ret=retail(.105, .042, .059, .075), ronic=.1849, reported=134.27),
    'Quinn Bear': dict(aws=aws(.24, .04, .34, .355, .90, .30),  ret=retail(.08, .028, .058, .060), ronic='WACC', reported=14.17),
}
# Ads carve-out (step 5): Ads revenue path data-anchored and identical for all analysts; margin from digital-ads peers
ADS_G = lin(37.052 / 29.615 - 1, 0.092)     # H1'26 YoY (10-Q) -> eMarketer US digital ad growth 2028 (9.2%)
ADS_M = {'Emma': None, 'Quinn Base': None, 'Bear': 'low', 'Quinn Bear': 'low', 'Quinn Bull': 'high'}
PEER_ADS = {'META': .3808, 'GOOGL': .3311}  # stockanalysis operating margin 2026-10-07
PEER_RET = {'WMT': .0394, 'COST': .0385, 'TGT': .0503}
def pick(d, how):
    v = sorted(d.values())
    return {'low': v[0], 'high': v[-1]}.get(how, (v[len(v) // 2] if len(v) % 2 else (v[len(v)//2 - 1] + v[len(v)//2]) / 2))

def split_retail(ret_rows, name):
    """Ads + core retail; total NA+Intl revenue/capex/D&A unchanged; ads margin = digital-ads peer, core terminal margin = retail peer."""
    am, cm_t = pick(PEER_ADS, ADS_M[name]), pick(PEER_RET, ADS_M[name])
    ads, core, rev = [], [], ADS_BASE
    first_core_m = None
    for i, r in enumerate(ret_rows):
        rev *= (1 + ADS_G[i]); share = rev / r['rev']
        a_ebit = rev * am
        ads.append(dict(y=r['y'], rev=rev, g=ADS_G[i], ebit=a_ebit, nopat=a_ebit * (1 - TAX), capex=r['capex'] * share, da=r['da'] * share))
        crev = r['rev'] - rev
        if first_core_m is None:
            first_core_m = (r['ebit'] - a_ebit) / crev
        core.append(dict(y=r['y'], rev=crev, ebit=None))
    cms = lin(first_core_m, cm_t)
    prev = RET_BASE - ADS_BASE
    for i, c in enumerate(core):
        r = ret_rows[i]; share = c['rev'] / r['rev']
        c.update(g=c['rev'] / prev - 1, ebit=c['rev'] * cms[i], capex=r['capex'] * share, da=r['da'] * share); prev = c['rev']
        c['nopat'] = c['ebit'] * (1 - TAX)
    for x in ads + core:
        x['fcff'] = x['nopat'] - x['capex'] + x['da']
    return ads, core, dict(ads_margin=am, core_m0=first_core_m, core_mT=cm_t)

def implied_ronic(rows_list):
    """Sum dNOPAT(t) / Sum net investment(t-1) over explicit period, aggregated across segments."""
    nop = [sum(rs[i]['nopat'] for rs in rows_list) for i in range(10)]
    ni = [sum(rs[i]['capex'] - rs[i]['da'] for rs in rows_list) for i in range(10)]
    return sum(nop[i] - nop[i - 1] for i in range(1, 10)) / sum(ni[i - 1] for i in range(1, 10))

def value(name, step, emma_l2=None):
    m = MODELS[name]
    wacc = WACC_OLD if step < 1 else WACC
    mode = 'v32' if step < 4 else 'vs2'
    ronic = m['ronic']
    if ronic == 'WACC':
        ronic = wacc
    aw, rt = build(m['aws']), build(m['ret'])
    if step >= 4:
        # VS2 1.3: capex years 1-2 must be sourced -> FY2026 $220B (guidance, Atlas v3.1 E7) / FY2027 $269B (consensus,
        # Longbridge 2026-07-30; Wedbush $266B). Same fact for every analyst; scaled pro-rata to each model's own segment mix.
        for i, tgt in [(0, CAPEX_Y1), (1, CAPEX_Y2)]:
            k = tgt / (aw[i]['capex'] + rt[i]['capex'])
            for rows in (aw, rt):
                rows[i]['capex'] *= k
                rows[i]['fcff'] = rows[i]['nopat'] - rows[i]['capex'] + rows[i]['da']
    segs = {'AWS': aw}
    info = {}
    if step >= 5:
        ads, core, info = split_retail(rt, name); segs.update(Ads=ads, Retail=core)
    else:
        segs['Retail'] = rt
    if step >= 7 and name == 'Quinn Bear':
        ronic = implied_ronic(list(segs.values())); info['quinn_bear_ronic'] = ronic
    vals = {k: seg_value(v, wacc, mode, ronic) for k, v in segs.items()}
    ev = sum(v['ev'] for v in vals.values())
    nd = NET_DEBT_OLD if step < 3 else NET_DEBT_NEW
    sh = SH_OLD if step < 3 else SH_DIL
    nonop = NONOP_AT if step >= 2 else 0.0
    eq = ev - nd + nonop
    fv = eq / sh
    pv_tv = sum(v['pv_tv'] + v['pv_fade'] for v in vals.values()) if mode == 'vs2' else sum(v['pv_tv'] for v in vals.values())
    res = dict(fv=fv, ev=ev, eq=eq, pv_tv_share=sum(v['pv_tv'] for v in vals.values()) / ev,
               pv_tv_fade_share=pv_tv / ev, segs=segs, vals=vals, wacc=wacc, ronic=ronic, nd=nd, sh=sh, info=info, mode=mode)
    return res

# ---------------- Layer 2 (Emma only) ----------------
PEER_FWD_EVEBIT = {k: ev_ebit / (1 + g) for k, (ev_ebit, g) in
                   {'WMT': (31.80, .0486), 'COST': (34.65, .0759), 'MSFT': (25.57, .1973), 'GOOGL': (28.21, .2215), 'META': (21.49, .2173)}.items()}
PEER_FWD_PE = {'WMT': 36.05, 'COST': 41.35, 'MSFT': 26.77, 'GOOGL': 26.10, 'META': 22.97}
def med(d):
    v = sorted(d.values()); n = len(v); return v[n // 2] if n % 2 else (v[n//2-1] + v[n//2]) / 2
AMZN_EBITDA_TTM, AMZN_DA_TTM = 168.91, 168.91 - 93.71   # stockanalysis TTM (S&P Global) 2026-10-07
NTM_REV_G = 0.1449                          # consensus FY2027 revenue growth (stockanalysis forecast)
AMZN_FWD_PE = 27.26
CORE_EPS_NTM = PRICE / AMZN_FWD_PE          # consensus NTM EPS implied by forward P/E (excludes Anthropic marks: FY26 cons $8.31 < H1'26 GAAP EPS)

def layer2(res):
    segs = res['segs']
    da_y2 = sum(s[1]['da'] for s in segs.values())
    capex_y1 = sum(s[0]['capex'] for s in segs.values())
    ebitda_ntm = AMZN_EBITDA_TTM * (1 + NTM_REV_G)
    ebit_unadj = ebitda_ntm - AMZN_DA_TTM * (1 + NTM_REV_G)
    adjust = capex_y1 / AMZN_DA_TTM > 2
    # VS2 layer-2 item 3: capex/D&A > 2x -> use year-2 D&A. The v3.2 model's year-2 D&A ($61.4B) is BELOW actual TTM D&A
    # ($75.2B), contradicting the rule's premise (D&A rising) -> do not use it (would raise EBIT); use the alternative the
    # rule allows: unadjusted NTM EBIT (D&A scaled with revenue) + FLAG that multiples may be overstated.
    da_rule_usable = adjust and da_y2 > AMZN_DA_TTM * (1 + NTM_REV_G)
    ebit = ebitda_ntm - da_y2 if da_rule_usable else ebit_unadj
    ev_mult = med(PEER_FWD_EVEBIT) * ebit
    fv_evebit = (ev_mult - res['nd'] + NONOP_AT) / res['sh']
    fv_pe = med(PEER_FWD_PE) * CORE_EPS_NTM + NONOP_AT / res['sh']
    fv_mult = (fv_evebit + fv_pe) / 2
    # Trigger = PV(terminal value) / EV, literal VS2 wording. Fade years are an extension of the explicit forecast (VS2 1.3),
    # so they are NOT counted as TV. Alternative reading (fade counted as TV) reported as sensitivity: wd_alt / fv_alt.
    tvs, tvs_alt = res['pv_tv_share'], res['pv_tv_fade_share']
    wt = lambda s: 1.0 if s <= .70 else (.75 if s <= .85 else .60)
    wd, wd_alt = wt(tvs), wt(tvs_alt)
    return dict(da_y2=da_y2, capex_y1=capex_y1, capex_da=capex_y1 / AMZN_DA_TTM, ebitda_ntm=ebitda_ntm, ebit_unadj=ebit_unadj, ebit_adj=ebit,
                mult_evebit=med(PEER_FWD_EVEBIT), mult_pe=med(PEER_FWD_PE), fv_evebit=fv_evebit, fv_pe=fv_pe, fv_mult=fv_mult,
                fv_evebit_unadj=(med(PEER_FWD_EVEBIT) * ebit_unadj - res['nd'] + NONOP_AT) / res['sh'],
                tv_share=tvs, tv_fade_share=tvs_alt, w_dcf=wd, w_dcf_alt=wd_alt, fv=wd * res['fv'] + (1 - wd) * fv_mult,
                fv_alt=wd_alt * res['fv'] + (1 - wd_alt) * fv_mult, gap=fv_mult / res['fv'] - 1)

# ---------------- FV year 5 (step 8) ----------------
def fv5(res, l2=None):
    wacc, ronic = res['wacc'], res['ronic']
    ev5 = sum(ev_at_year5(rows, wacc, res['mode'], ronic) for rows in res['segs'].values())
    nd = res['nd']
    for i in range(5):
        f = sum(rows[i]['fcff'] for rows in res['segs'].values())
        nd = nd - f + nd * KD_AT
    sh5 = res['sh'] * (1 + DIL) ** 5
    eq5 = ev5 + NONOP_AT - nd
    dcf5 = eq5 / sh5
    out = dict(ev5=ev5, nd5=nd, sh5=sh5, eq5=eq5, fv5_dcf=dcf5, eq0=res['eq'], eq0_grown=res['eq'] * (1 + COE) ** 5)
    out['consistency_gap'] = eq5 / out['eq0_grown'] - 1
    fv5 = dcf5
    if l2:
        segs = res['segs']
        ebit31 = sum(s[5]['ebit'] for s in segs.values())
        nopat31 = sum(s[5]['nopat'] for s in segs.values())
        fv_e = (l2['mult_evebit'] * ebit31 - nd + NONOP_AT) / sh5
        core_ni = nopat31 - nd * KD_AT
        fv_p = l2['mult_pe'] * core_ni / sh5 + NONOP_AT / sh5
        out.update(ebit31=ebit31, fv5_evebit=fv_e, fv5_pe=fv_p, fv5_mult=(fv_e + fv_p) / 2)
        fv5 = l2['w_dcf'] * dcf5 + (1 - l2['w_dcf']) * out['fv5_mult']
    out['fv5'] = fv5
    return out

def nogrowth(wacc, nd, sh, nonop):
    return (64.3 / wacc - nd + nonop) / sh

if __name__ == '__main__':
    R = {}
    names = list(MODELS)
    for n in names:
        R[n] = {s: value(n, s) for s in [0, 1, 2, 3, 4, 5, 7]}
    l2 = layer2(R['Emma'][5])
    def qpw(step):
        return .25 * R['Quinn Bull'][step]['fv'] + .5 * R['Quinn Base'][step]['fv'] + .25 * R['Quinn Bear'][step]['fv']
    print('WACC: raw beta %.3f Blume %.3f | BU unlev %.3f lev %.3f | COE %.4f/%.4f | WACC Blume %.4f BU %.4f base %.4f COE %.4f | We %.4f Wd %.4f Kd_at %.4f'
          % (RAW_BETA, BLUME, BU_UNLEV_AVG, BU_LEV, COE_BLUME, COE_BU, WACC_BLUME, WACC_BU, WACC, COE, WE, WD, KD_AT))
    print('weights', {k: round(v, 4) for k, v in w.items()})
    print('NonOp pre %.2f tax %.2f AT %.2f /sh %.2f | net debt new %.2f | dil %.4f' % (NONOP_PRE, NONOP_TAX, NONOP_AT, NONOP_AT / SH_DIL, NET_DEBT_NEW, DIL))
    print('%-11s %8s %8s %8s %8s %8s %8s %8s %8s' % ('model', 'report', 's0rebld', 's1wacc', 's2nonop', 's3nd/sh', 's4fade', 's5ads', 's7'))
    for n in names:
        r = R[n]
        print('%-11s %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f' % (n, MODELS[n]['reported'], *[r[s]['fv'] for s in [0, 1, 2, 3, 4, 5, 7]]))
    print('Quinn P-W   %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f %8.2f' % (131.69, *[qpw(s) for s in [0, 1, 2, 3, 4, 5, 7]]))
    for n in names:
        for s in [0, 4, 5]:
            x = R[n][s]
            print(n, s, 'EV %.1f TV%% %.3f TV+fade%% %.3f ronic %.4f' % (x['ev'], x['pv_tv_share'], x['pv_tv_fade_share'], x['ronic']), {k: round(v['ev'], 1) for k, v in x['vals'].items()}, x['info'])
    print('LAYER2', json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in l2.items()}))
    print('peer fwd EV/EBIT', {k: round(v, 2) for k, v in PEER_FWD_EVEBIT.items()}, 'core EPS NTM %.3f' % CORE_EPS_NTM)
    emma_final = l2['fv']
    q_final = qpw(7)
    b_final = R['Bear'][7]['fv']
    blended = .4 * emma_final + .3 * q_final + .3 * b_final
    print('FINAL Emma %.2f Quinn %.2f Bear %.2f Blended %.2f MOS %.4f' % (emma_final, q_final, b_final, blended, blended / PRICE - 1))
    f = {n: fv5(R[n][7], l2 if n == 'Emma' else None) for n in names}
    for n in names:
        print('FV5', n, {k: round(v, 3) for k, v in f[n].items()})
    q5 = .25 * f['Quinn Bull']['fv5'] + .5 * f['Quinn Base']['fv5'] + .25 * f['Quinn Bear']['fv5']
    b5 = .4 * f['Emma']['fv5'] + .3 * q5 + .3 * f['Bear']['fv5']
    print('FV5 Emma %.2f Quinn %.2f Bear %.2f Blended5 %.2f  exp ret/yr %.4f  vs S&P %.4f' % (f['Emma']['fv5'], q5, f['Bear']['fv5'], b5, (b5 / PRICE) ** .2 - 1, SP500_EXP))
    print('no-growth value (VS2 WACC, new nd/sh, +nonop): %.2f ; ex-nonop %.2f' % (nogrowth(WACC, NET_DEBT_NEW, SH_DIL, NONOP_AT), nogrowth(WACC, NET_DEBT_NEW, SH_DIL, 0)))
    print('QuinnBear implied RONIC', R['Quinn Bear'][7]['info'])
    for n in names:
        print('implied explicit RONIC', n, round(implied_ronic(list(R[n][7]['segs'].values())), 4))
    l2['da_rule_usable'] = (l2['ebit_adj'] != l2['ebit_unadj'])
    print('layer2 D&A rule usable:', l2['da_rule_usable'], '| fv_evebit (model y2 D&A, NOT used) %.2f' % ((l2['mult_evebit'] * (l2['ebitda_ntm'] - l2['da_y2']) - NET_DEBT_NEW + NONOP_AT) / SH_DIL))
    # attribution table (Blended uses Emma step-6 only at the step-6 column)
    cols = [0, 1, 2, 3, 4, 5]
    print('\nATTRIBUTION  report | s0 | s1 | s2 | s3 | s4 | s5 | s6(Emma L2) | s7(QuinnBear)')
    em = [R['Emma'][s]['fv'] for s in cols] + [l2['fv'], l2['fv']]
    qq = [qpw(s) for s in cols] + [qpw(5), qpw(7)]
    bb = [R['Bear'][s]['fv'] for s in cols] + [R['Bear'][5]['fv'], R['Bear'][7]['fv']]
    bl = [.4 * a + .3 * b + .3 * c for a, b, c in zip(em, qq, bb)]
    for lab, rep, arr in [('Emma', 148.53, em), ('Quinn', 131.69, qq), ('Bear', 89.13, bb), ('Blended', 125.66, bl)]:
        print('%-8s %7.2f ' % (lab, rep) + ' '.join('%7.2f' % x for x in arr))
    print('MOS by step', ' '.join('%.1f%%' % ((x / PRICE - 1) * 100) for x in bl))
    def table(n, s=7):
        segs = R[n][s]['segs']
        print('\n', n, 'step', s, 'year | ' + ' | '.join(segs) + ' | cons rev | cons EBIT | cons NOPAT | capex | D&A | FCFF')
        for i, y in enumerate(YEARS):
            rv = sum(v[i]['rev'] for v in segs.values()); eb = sum(v[i]['ebit'] for v in segs.values())
            print(y, ' '.join('%.1f' % v[i]['rev'] for v in segs.values()), '| %.1f %.1f(%.1f%%) %.1f %.1f %.1f %.1f' % (
                rv, eb, eb / rv * 100, sum(v[i]['nopat'] for v in segs.values()), sum(v[i]['capex'] for v in segs.values()),
                sum(v[i]['da'] for v in segs.values()), sum(v[i]['fcff'] for v in segs.values())))
        for k, v in R[n][s]['vals'].items():
            print('  %s EV %.1f = PVexp %.1f + PVfade %.1f + PVTV %.1f (fade yrs %d)' % (k, v['ev'], v['pv_exp'], v['pv_fade'], v['pv_tv'], v['n_end'] - 10))
    for n in names:
        table(n)
    # Market-implied trigger
    emma_f = l2['fv']; final = .4 * emma_f + .3 * qpw(7) + .3 * R['Bear'][7]['fv']
    print('\nFINAL (after D&A rule) Emma %.2f Blended %.2f MOS %.2f%% | |MOS|>=35%%? %s' % (emma_f, final, (final / PRICE - 1) * 100, abs(final / PRICE - 1) >= .35))
    # Quinn 5x5 sensitivity on Quinn Base (VS2 final framework): WACC x AWS growth shift (pp, all years)
    import copy
    print('\nSENS Quinn Base: rows AWS growth shift pp, cols WACC')
    wl = [0.085, 0.09, WACC, 0.105, 0.115]
    base_m = copy.deepcopy(MODELS['Quinn Base'])
    for sh in [-0.06, -0.03, 0.0, 0.03, 0.06]:
        row = []
        for wv in wl:
            MODELS['Quinn Base'] = copy.deepcopy(base_m)
            MODELS['Quinn Base']['aws']['g'] = [g + sh for g in base_m['aws']['g']]
            WACC_SAVE = WACC; WACC = wv
            row.append(value('Quinn Base', 7)['fv']); WACC = WACC_SAVE
        print('%+.0fpp ' % (sh * 100) + ' '.join('%7.2f' % x for x in row))
    MODELS['Quinn Base'] = base_m
