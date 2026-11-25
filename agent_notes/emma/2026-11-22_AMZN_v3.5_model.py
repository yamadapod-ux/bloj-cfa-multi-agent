# AMZN v3.5 (VS2, post-Q3 2026) — reproducible model. COPY of agent_notes/emma/2026-10-08_AMZN_v3.4_model.py:
# calculation code (build / seg_value / ev_at_year5 / split_retail / value / layer2 / fv5) is UNCHANGED; only the INPUTS were moved
# into config dicts (CFG34 = v3.4 locked inputs, CFG35 = v3.5 inputs) so each changed input can be switched one at a time.
# Sources: agent_notes/atlas/2026-10-07_AMZN_v3.md § Addendum v3.5 + agent_notes/emma/2026-11-22_AMZN_v3.5.md § 0 (pre-registration).
# Run: python -I this_file.py
import math, json, sys, copy

YEARS = list(range(2026, 2036))           # explicit 10y, end-year discounting (v3.2 convention, 2026 = t1)
TGR = 0.03
RET_BASE = 588.199                        # FY2025 NA+Intl net sales ($B)
AWS_BASE = 128.725                        # FY2025 AWS net sales ($B)
ADS_BASE = 68.63                          # FY2025 advertising services ($B)
V34_AWS_G = [.33, .28, .23, .19, .16, .14, .12, .10, .09, .08]
V34_AWS_M = [.355, .365, .375, .385, .395, .405, .41, .415, .42, .42]
V34_AWS_C = [.90, .75, .60, .45, .35, .28, .22, .18, .16, .15]
V34_AWS_DA = [.17, .18, .185, .19, .19, .185, .18, .175, .17, .165]
C_BY_G = {.40: .90, .36: .90, .33: .90, .28: .75, .23: .60, .19: .45, .16: .35, .14: .28, .12: .22, .10: .18, .09: .16, .08: .15}  # v3.4 (growth, capex/rev) pairs

def lin(a, b, n=10):
    return [a + (b - a) * i / (n - 1) for i in range(n)]

def glide(vec, delta):
    """vec + delta fading linearly to 0 by the last explicit year."""
    return [v + delta * (1 - i / 9) for i, v in enumerate(vec)]

# ---------------- CFG34 = v3.4 locked inputs ----------------
NONOP34 = [('Anthropic nonvoting preferred', 92.5, 10.0), ('Anthropic convertible notes (AFS, FV)', 97.9, 8.0),
           ('OpenAI Series C preferred (cost)', 28.7, 28.7), ('Other private equity', 1.1, 1.1),
           ('Marketable equity securities', 4.7, 0.0), ('Equity warrants', 4.3, 0.0), ('Equity-method investments', 0.395, 0.395)]
PEER_EV34 = {'WMT': (31.80, .0486), 'COST': (34.65, .0759), 'MSFT': (25.57, .1973), 'GOOGL': (28.21, .2215), 'META': (21.49, .2173)}
PEER_PE34 = {'WMT': 36.05, 'COST': 41.35, 'MSFT': 26.77, 'GOOGL': 26.10, 'META': 22.97}
CFG34 = dict(
    tax=.196, tax_kd=.196, rf=.0530, erp=.0420, raw_beta=(1.46 + 1.45) / 2,
    price=259.92, sh_basic=10.786313572, sh_dil=10.903,
    debt=132.224, fin_lease=13.5, fin_oblig=8.3, cash=78.213 + 44.775,
    nonop=NONOP34, capex_y1=220.0, capex_y2=269.0,
    rev_ttm={'AWS': 148.4, 'Ads': 76.07, 'Retail': 551.2}, wacc_mode='avg',
    aws_g=V34_AWS_G, aws_m=V34_AWS_M, aws_capex=V34_AWS_C, aws_da=V34_AWS_DA, ret_da=lin(.030, .035),
    ret_g0=.11, ret_m0=.062, ads_g0=37.052 / 29.615 - 1, ads_gT=.092,
    ebitda_ttm=168.91, da_ttm=168.91 - 93.71, ntm_g=.1449, fwd_pe=27.26, peer_ev=PEER_EV34, peer_pe=PEER_PE34,
    nopat_cur=64.3, ronic_emma=.1849, tgr=.03, core_t=None, ads_peer=None, dil=(10.889 / 10.492) ** (1 / 2.5) - 1,
)

# ---------------- CFG35 = v3.5 inputs (anchors derived from sourced actuals; see notes § 0) ----------------
def anchors35(q4_ads_mode='q2q3', q4_aws_mode='q3', ebit_q4=31.0, rev_q4=243.5, da_q4_extra=0.0):
    # AWS FY2026 (10-Q R54 / R53; Q4 = Q3 YoY growth and Q3 margin)
    aws9, aws9_25, aws_q3, aws_q3_25 = 125.803, 93.146, 45.984, 33.006
    q4_25 = AWS_BASE - aws9_25
    q4_g = aws_q3 / aws_q3_25 - 1 if q4_aws_mode == 'q3' else 42.232 / 30.873 - 1
    aws_q4 = q4_25 * (1 + q4_g)
    aws26 = aws9 + aws_q4
    ebit_aws = 48.555 + aws_q4 * (17.773 / 45.984)
    # Ads FY2026
    ads9, ads_q4_25 = 56.689, ADS_BASE - 47.318
    gq = (19.809 + 19.637) / (15.694 + 17.703) - 1 if q4_ads_mode == 'q2q3' else 19.637 / 17.703 - 1
    ads26 = ads9 + ads_q4_25 * (1 + gq)
    # consolidated anchors (guide midpoint)
    rev26 = 584.069 + rev_q4
    ebit26 = 79.389 + ebit_q4
    ret26 = rev26 - aws26
    ret_ebit = ebit26 - ebit_aws
    # P&E D&A (10-Q R58): Q4 = Q3 (+extra)
    da_aws = 24.583 + 9.230 + da_q4_extra * .6
    da_ret = 13.346 + 3.916 + 4.566 + 1.346 + da_q4_extra * .4
    return dict(aws26=aws26, aws_g26=aws26 / AWS_BASE - 1, aws_m26=ebit_aws / aws26, ads26=ads26, ads_g26=ads26 / ADS_BASE - 1,
                rev26=rev26, ebit26=ebit26, ret26=ret26, ret_g0=ret26 / RET_BASE - 1, ret_m0=ret_ebit / ret26,
                da_aws=da_aws, da_ret=da_ret, da_aws_ratio=da_aws / aws26, da_ret_ratio=da_ret / ret26, ebit_aws=ebit_aws)

A35 = anchors35()
NONOP35 = [('Anthropic nonvoting preferred', 92.5, 10.0), ('Anthropic convertible notes (AFS, FV)', 146.2, 8.0),
           ('OpenAI Series C preferred (cost)', 50.0, 50.0), ('Other private equity', 1.2, 1.2),
           ('Marketable equity securities', 4.7, 0.0), ('Equity warrants', 4.3, 0.0), ('Equity-method investments', 0.395, 0.395)]
PEER_EV35 = {'WMT': (32.64, .0486), 'COST': (41.46, .0784), 'MSFT': (22.47, .2080), 'GOOGL': (20.05, .2476), 'META': (16.06, .2291)}
PEER_PE35 = {'WMT': 41.17, 'COST': 48.36, 'MSFT': 23.34, 'GOOGL': 19.29, 'META': 17.02}

def cfg35_aws(a=A35, g_path=None, m_cap=.42, shift_m=True):
    g = g_path or [a['aws_g26']] + V34_AWS_G[:9]                       # J3b: v3.4 path advanced one year
    dm = a['aws_m26'] - V34_AWS_M[0]
    m = [min(v + dm, m_cap) if shift_m else v for v in V34_AWS_M]       # J3c
    m[0] = a['aws_m26']
    c = [C_BY_G.get(round(x, 2), .90) for x in g]                       # J3d: capex intensity follows growth state (v3.4 pairs)
    return g, m, c

_g, _m, _c = cfg35_aws()
CFG35 = copy.deepcopy(CFG34)
CFG35.update(
    tax=.23, rf=.04916, erp=.0441, raw_beta=1.50, price=246.82, sh_basic=10.813138306, sh_dil=10.929,
    debt=179.952, fin_lease=14.495, fin_oblig=9.726, cash=55.783 + 58.443, nonop=NONOP35, capex_y2=77.259 * 4,
    aws_g=_g, aws_m=_m, aws_capex=_c,
    aws_da=glide(V34_AWS_DA, A35['da_aws_ratio'] - V34_AWS_DA[0]), ret_da=glide(lin(.030, .035), A35['da_ret_ratio'] - .030),
    ret_g0=A35['ret_g0'], ret_m0=A35['ret_m0'], ads_g0=A35['ads_g26'],
    ebitda_ttm=183.72, da_ttm=183.72 - 104.37, ntm_g=.1574, fwd_pe=24.96, peer_ev=PEER_EV35, peer_pe=PEER_PE35,
    nopat_cur=104.37 * (1 - .23),
)
# NOTE: tax_kd stays .196 = Atlas-locked Kd tax shield (Atlas §5) — 1 bp effect on WACC vs 23%; disclosed in notes.

GROUPS = [  # (label, keys switched from CFG34 -> CFG35), fixed attribution order
    ('a1 price + layer-2 market data', ['price', 'ebitda_ttm', 'da_ttm', 'ntm_g', 'fwd_pe', 'peer_ev', 'peer_pe', 'nopat_cur']),
    ('a2 Rf / ERP / raw beta', ['rf', 'erp', 'raw_beta']),
    ('a3 debt / leases / cash (net debt + weights)', ['debt', 'fin_lease', 'fin_oblig', 'cash']),
    ('a4 non-op bridge', ['nonop']),
    ('a5 shares (basic + diluted)', ['sh_basic', 'sh_dil']),
    ('b  capex FY2027 269 -> 309', ['capex_y2']),
    ('c1 AWS growth path (FY26 anchor + 1y advance)', ['aws_g']),
    ('c2 AWS margin path', ['aws_m']),
    ('c3 AWS capex intensity (advance)', ['aws_capex']),
    ('d1 Ads FY26 anchor (+18.1% Q4)', ['ads_g0']),
    ('d2 tax 19.6% -> 23.0%', ['tax']),
    ('d3 D&A (P&E basis, actual anchor)', ['aws_da', 'ret_da']),
    ('d4 retail FY26 growth + EBIT anchor (guide)', ['ret_g0', 'ret_m0']),
]

# ---------------- configure: sets module globals used by the (unchanged) v3.4 functions ----------------
def configure(c):
    g = globals()
    g['TAX'] = c['tax']; g['TGR'] = c['tgr']
    g['RF'], g['ERP'] = c['rf'], c['erp']
    g['RAW_BETA'] = c['raw_beta']
    g['BLUME'] = 0.67 * c['raw_beta'] + 0.33
    g['BU_UNLEV'] = {'AWS': 1.25, 'Ads': 1.01, 'Retail': 0.78}
    g['REV_TTM'] = c['rev_ttm']
    g['PRICE'] = c['price']; g['SH_BASIC'] = c['sh_basic']; g['SH_DIL'] = c['sh_dil']
    g['DEBT'] = c['debt']; g['FIN_LEASE'] = c['fin_lease']; g['FIN_OBLIG'] = c['fin_oblig']; g['CASH'] = c['cash']
    g['KD_PRE'] = c['rf'] + 0.0055
    g['KD_AT'] = g['KD_PRE'] * (1 - c['tax_kd'])
    g['D_MKT'] = c['debt'] + c['fin_lease'] + c['fin_oblig']
    g['E_MKT'] = c['price'] * c['sh_basic']
    g['WD'] = g['D_MKT'] / (g['D_MKT'] + g['E_MKT']); g['WE'] = g['E_MKT'] / (g['D_MKT'] + g['E_MKT'])
    w = {k: v / sum(c['rev_ttm'].values()) for k, v in c['rev_ttm'].items()}
    g['w'] = w
    g['BU_UNLEV_AVG'] = sum(g['BU_UNLEV'][k] * w[k] for k in w)
    g['BU_LEV'] = g['BU_UNLEV_AVG'] * (1 + (1 - 0.21) * g['D_MKT'] / g['E_MKT'])
    g['COE_BLUME'], g['COE_BU'] = c['rf'] + g['BLUME'] * c['erp'], c['rf'] + g['BU_LEV'] * c['erp']
    g['WACC_BLUME'] = g['WE'] * g['COE_BLUME'] + g['WD'] * g['KD_AT']
    g['WACC_BU'] = g['WE'] * g['COE_BU'] + g['WD'] * g['KD_AT']
    mode = c['wacc_mode']
    g['WACC'] = {'avg': (g['WACC_BLUME'] + g['WACC_BU']) / 2, 'blume': g['WACC_BLUME'], 'bu': g['WACC_BU']}[mode] if not isinstance(mode, float) else mode
    g['COE'] = (g['COE_BLUME'] + g['COE_BU']) / 2
    g['NET_DEBT_NEW'] = c['debt'] + c['fin_lease'] + c['fin_oblig'] - c['cash']
    g['NONOP'] = c['nonop']
    g['NONOP_PRE'] = sum(v for _, v, _ in c['nonop'])
    g['NONOP_TAX'] = sum(0.21 * max(v - k, 0) for _, v, k in c['nonop'])
    g['NONOP_AT'] = g['NONOP_PRE'] - g['NONOP_TAX']
    g['DIL'] = c['dil']
    g['CAPEX_Y1'], g['CAPEX_Y2'] = c['capex_y1'], c['capex_y2']
    g['SP500_EXP'] = c['rf'] + c['erp']
    g['NET_DEBT_OLD'], g['SH_OLD'], g['WACC_OLD'] = 9.24, 10.90, 0.1095
    g['DA_AWS'] = c['aws_da']; g['RET_DA'] = c['ret_da']
    g['RET_CAPEX_E'] = lin(65.9 / (RET_BASE * 1.11), .048)
    g['EMMA_AWS'] = dict(base=AWS_BASE, g=c['aws_g'], m=c['aws_m'], capex=c['aws_capex'], da=c['aws_da'])
    g['MODELS'] = {
        'Emma':       dict(aws=g['EMMA_AWS'],                            ret=retail(c['ret_g0'], .04, c['ret_m0'], .080), ronic=c['ronic_emma']),
        'Bear':       dict(aws=aws(.28, .08, .355, .386, .88, .16), ret=retail(.09, .03, .058, .061, lin(95.9 / (RET_BASE * 1.09), .048)), ronic='WACC'),
        'Quinn Bull': dict(aws=aws(.35, .15, .36, .44, .88, .12),   ret=retail(.12, .05, .062, .090), ronic=.314),
        'Quinn Base': dict(aws=aws(.30, .09, .35, .40, .88, .16),   ret=retail(.105, .042, .059, .075), ronic=.1849),
        'Quinn Bear': dict(aws=aws(.24, .04, .34, .355, .90, .30),  ret=retail(.08, .028, .058, .060), ronic='WACC'),
    }
    g['ADS_G'] = lin(c['ads_g0'], c['ads_gT'])
    g['ADS_M'] = {'Emma': None, 'Quinn Base': None, 'Bear': 'low', 'Quinn Bear': 'low', 'Quinn Bull': 'high'}
    g['PEER_ADS'] = c['ads_peer'] or {'META': .3808, 'GOOGL': .3311}
    g['PEER_RET'] = c['core_t'] or {'WMT': .0394, 'COST': .0385, 'TGT': .0503}
    g['PEER_FWD_EVEBIT'] = {k: ev / (1 + gg) for k, (ev, gg) in c['peer_ev'].items()}
    g['PEER_FWD_PE'] = c['peer_pe']
    g['AMZN_EBITDA_TTM'], g['AMZN_DA_TTM'] = c['ebitda_ttm'], c['da_ttm']
    g['NTM_REV_G'] = c['ntm_g']; g['AMZN_FWD_PE'] = c['fwd_pe']; g['CORE_EPS_NTM'] = c['price'] / c['fwd_pe']
    g['NOPAT_CUR'] = c['nopat_cur']

# ---------------- v3.4 functions (UNCHANGED) ----------------
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
    flows = []
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

def retail(g0, g1, m0, m1, capex=None):
    return dict(base=RET_BASE, g=lin(g0, g1), m=lin(m0, m1), capex=capex or RET_CAPEX_E, da=RET_DA)

def aws(g0, g1, m0, m1, c0, c1):
    return dict(base=AWS_BASE, g=lin(g0, g1), m=lin(m0, m1), capex=lin(c0, c1), da=DA_AWS)

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
    return dict(fv=fv, ev=ev, eq=eq, pv_tv_share=sum(v['pv_tv'] for v in vals.values()) / ev,
                pv_tv_fade_share=pv_tv / ev, segs=segs, vals=vals, wacc=wacc, ronic=ronic, nd=nd, sh=sh, info=info, mode=mode)

def med(d):
    v = sorted(d.values()); n = len(v); return v[n // 2] if n % 2 else (v[n//2-1] + v[n//2]) / 2

def layer2(res):
    segs = res['segs']
    da_y2 = sum(s[1]['da'] for s in segs.values())
    capex_y1 = sum(s[0]['capex'] for s in segs.values())
    ebitda_ntm = AMZN_EBITDA_TTM * (1 + NTM_REV_G)
    ebit_unadj = ebitda_ntm - AMZN_DA_TTM * (1 + NTM_REV_G)
    adjust = capex_y1 / AMZN_DA_TTM > 2
    # v3.4 reading kept: D&A-year-2 rule only if model y2 D&A exceeds TTM D&A grown (else use unadjusted EBIT + flag). v3.5 flag: model D&A is P&E basis,
    # TTM D&A (stockanalysis) is cash-flow basis -> comparison is conservative; unadjusted EBIT is the like-for-like EBIT either way.
    da_rule_usable = adjust and da_y2 > AMZN_DA_TTM * (1 + NTM_REV_G)
    ebit = ebitda_ntm - da_y2 if da_rule_usable else ebit_unadj
    ev_mult = med(PEER_FWD_EVEBIT) * ebit
    fv_evebit = (ev_mult - res['nd'] + NONOP_AT) / res['sh']
    fv_pe = med(PEER_FWD_PE) * CORE_EPS_NTM + NONOP_AT / res['sh']
    fv_mult = (fv_evebit + fv_pe) / 2
    tvs, tvs_alt = res['pv_tv_share'], res['pv_tv_fade_share']
    wt = lambda s: 1.0 if s <= .70 else (.75 if s <= .85 else .60)
    wd, wd_alt = wt(tvs), wt(tvs_alt)
    return dict(da_y2=da_y2, capex_y1=capex_y1, capex_da=capex_y1 / AMZN_DA_TTM, ebitda_ntm=ebitda_ntm, ebit_unadj=ebit_unadj, ebit_adj=ebit,
                mult_evebit=med(PEER_FWD_EVEBIT), mult_pe=med(PEER_FWD_PE), fv_evebit=fv_evebit, fv_pe=fv_pe, fv_mult=fv_mult,
                fv_evebit_unadj=(med(PEER_FWD_EVEBIT) * ebit_unadj - res['nd'] + NONOP_AT) / res['sh'],
                tv_share=tvs, tv_fade_share=tvs_alt, w_dcf=wd, w_dcf_alt=wd_alt, fv=wd * res['fv'] + (1 - wd) * fv_mult,
                fv_alt=wd_alt * res['fv'] + (1 - wd_alt) * fv_mult, gap=fv_mult / res['fv'] - 1)

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
    fv5_ = dcf5
    if l2:
        segs = res['segs']
        ebit31 = sum(s[5]['ebit'] for s in segs.values())
        nopat31 = sum(s[5]['nopat'] for s in segs.values())
        fv_e = (l2['mult_evebit'] * ebit31 - nd + NONOP_AT) / sh5
        core_ni = nopat31 - nd * KD_AT
        fv_p = l2['mult_pe'] * core_ni / sh5 + NONOP_AT / sh5
        out.update(ebit31=ebit31, fv5_evebit=fv_e, fv5_pe=fv_p, fv5_mult=(fv_e + fv_p) / 2)
        fv5_ = l2['w_dcf'] * dcf5 + (1 - l2['w_dcf']) * out['fv5_mult']
    out['fv5'] = fv5_
    return out

def nogrowth(wacc, nd, sh, nonop):
    return (NOPAT_CUR / wacc - nd + nonop) / sh

# ---------------- driver ----------------
NAMES = ['Emma', 'Bear', 'Quinn Bull', 'Quinn Base', 'Quinn Bear']

def run(c, full=False):
    configure(c)
    R = {n: value(n, 7) for n in NAMES}
    l2 = layer2(R['Emma'])
    q = .25 * R['Quinn Bull']['fv'] + .5 * R['Quinn Base']['fv'] + .25 * R['Quinn Bear']['fv']
    emma, bear = l2['fv'], R['Bear']['fv']
    bl = .4 * emma + .3 * q + .3 * bear
    out = dict(emma=emma, emma_dcf=R['Emma']['fv'], quinn=q, bear=bear, blended=bl, mos=bl / c['price'] - 1, wacc=WACC, tv_share=l2['tv_share'], l2=l2)
    if full:
        f = {n: fv5(R[n], l2 if n == 'Emma' else None) for n in NAMES}
        q5 = .25 * f['Quinn Bull']['fv5'] + .5 * f['Quinn Base']['fv5'] + .25 * f['Quinn Bear']['fv5']
        b5 = .4 * f['Emma']['fv5'] + .3 * q5 + .3 * f['Bear']['fv5']
        out.update(R=R, f=f, emma5=f['Emma']['fv5'], quinn5=q5, bear5=f['Bear']['fv5'], blended5=b5, exp_ret=(b5 / c['price']) ** .2 - 1, sp=SP500_EXP)
    return out

def apply_keys(base, new, keys):
    c = copy.deepcopy(base)
    for k in keys:
        c[k] = copy.deepcopy(new[k])
    return c

def show_cfg(c):
    return {k: (round(v, 5) if isinstance(v, float) else v) for k, v in c.items() if k in
            ('tax', 'tax_kd', 'rf', 'erp', 'raw_beta', 'price', 'sh_basic', 'sh_dil', 'debt', 'fin_lease', 'fin_oblig', 'cash', 'capex_y1', 'capex_y2',
             'ret_g0', 'ret_m0', 'ads_g0', 'ads_gT', 'tgr', 'ronic_emma', 'dil', 'nopat_cur', 'fwd_pe', 'ntm_g', 'ebitda_ttm', 'da_ttm')}

if __name__ == '__main__':
    r34 = run(CFG34, True)
    print('CHECK v3.4 reproduction: Emma %.2f Quinn %.2f Bear %.2f Blended %.2f (v3.4 report 218.29 / 241.12 / 139.38 / 201.47)' % (r34['emma'], r34['quinn'], r34['bear'], r34['blended']))
    r35 = run(CFG35, True)
    print('\n=== ANCHORS v3.5 ==='); print(json.dumps({k: round(v, 4) for k, v in A35.items()}))
    print('AWS g path', [round(x, 4) for x in CFG35['aws_g']]); print('AWS m path', [round(x, 4) for x in CFG35['aws_m']]); print('AWS capex ratio', CFG35['aws_capex'])
    print('AWS D&A ratio', [round(x, 4) for x in CFG35['aws_da']]); print('Retail D&A ratio', [round(x, 4) for x in CFG35['ret_da']])
    print('shared-input dict (SHARED):'); print(json.dumps(show_cfg(CFG35), indent=0))
    # WACC check vs Atlas (Blume 10.35 / BU 8.76 / base 9.55)
    print('\nWACC v3.5: raw beta %.3f Blume %.4f | BU unlev %.4f lev %.4f | COE %.4f/%.4f | WACC Blume %.4f BU %.4f base %.4f COE %.4f | We %.4f Wd %.4f Kd_at %.4f gap %.0fbps' % (
        RAW_BETA, BLUME, BU_UNLEV_AVG, BU_LEV, COE_BLUME, COE_BU, WACC_BLUME, WACC_BU, WACC, COE, WE, WD, KD_AT, (WACC_BLUME - WACC_BU) * 1e4))
    print('NonOp pre %.2f tax %.2f AT %.2f /sh %.2f | net debt %.2f | D %.2f E %.1f' % (NONOP_PRE, NONOP_TAX, NONOP_AT, NONOP_AT / SH_DIL, NET_DEBT_NEW, D_MKT, E_MKT))
    R = r35['R']; l2 = r35['l2']
    print('\n%-11s %9s %9s' % ('model', 'v3.4', 'v3.5(ref)'))
    for n in NAMES:
        print('%-11s %9.2f %9.2f' % (n, r34['R'][n]['fv'], R[n]['fv']))
    print('FINAL v3.5  Emma %.2f (DCF %.2f) | Quinn P-W %.2f | Bear %.2f | Blended %.2f | MOS %.2f%%' % (r35['emma'], r35['emma_dcf'], r35['quinn'], r35['bear'], r35['blended'], r35['mos'] * 100))
    print('LAYER2', json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in l2.items()}))
    for n in NAMES:
        x = R[n]; print(n, 'EV %.1f TV%% %.3f TV+fade%% %.3f ronic %.4f' % (x['ev'], x['pv_tv_share'], x['pv_tv_fade_share'], x['ronic']), {k: round(v['ev'], 1) for k, v in x['vals'].items()})
    print('No-growth value (NOPAT cur / WACC, nd, +nonop): %.2f ; ex-nonop %.2f' % (nogrowth(WACC, NET_DEBT_NEW, SH_DIL, NONOP_AT), nogrowth(WACC, NET_DEBT_NEW, SH_DIL, 0)))
    f = r35['f']
    for n in NAMES:
        print('FV5', n, {k: round(v, 3) for k, v in f[n].items()})
    print('FV5 Emma %.2f Quinn %.2f Bear %.2f Blended5 %.2f | exp ret/yr %.4f vs S&P %.4f | v3.4 Blended5 %.2f ret %.4f' % (
        r35['emma5'], r35['quinn5'], r35['bear5'], r35['blended5'], r35['exp_ret'], r35['sp'], r34['blended5'], r34['exp_ret']))
    # year table (Emma)
    configure(CFG35)
    segs = R['Emma']['segs']
    print('\nEmma year | ' + ' | '.join(segs) + ' | cons rev | EBIT (m%) | NOPAT | capex | D&A | FCFF')
    for i, y in enumerate(YEARS):
        rv = sum(v[i]['rev'] for v in segs.values()); eb = sum(v[i]['ebit'] for v in segs.values())
        print(y, ' '.join('%.1f' % v[i]['rev'] for v in segs.values()), '| %.1f %.1f(%.1f%%) %.1f %.1f %.1f %.1f' % (
            rv, eb, eb / rv * 100, sum(v[i]['nopat'] for v in segs.values()), sum(v[i]['capex'] for v in segs.values()),
            sum(v[i]['da'] for v in segs.values()), sum(v[i]['fcff'] for v in segs.values())))
    for k, v in R['Emma']['vals'].items():
        print('  %s EV %.1f = PVexp %.1f + PVfade %.1f + PVTV %.1f (fade yrs %d)' % (k, v['ev'], v['pv_exp'], v['pv_fade'], v['pv_tv'], v['n_end'] - 10))
    print('AWS FY26 EBIT %.2f margin %.4f; consolidated FY26 EBIT %.2f' % (A35['ebit_aws'], A35['aws_m26'], sum(v[0]['ebit'] for v in segs.values())))
    for n in ['Bear', 'Quinn Base']:
        sg = R[n]['segs']
        print(n, 'FY26 rev %.1f EBIT %.1f capex %.1f D&A %.1f' % (sum(v[0]['rev'] for v in sg.values()), sum(v[0]['ebit'] for v in sg.values()), sum(v[0]['capex'] for v in sg.values()), sum(v[0]['da'] for v in sg.values())))

    # ---------- cumulative attribution v3.4 -> v3.5, plus isolated and leave-one-out ----------
    print('\nATTRIBUTION (cumulative in fixed order; isolated = v3.4 + only this change; LOO = v3.5 minus only this change). FV $/share')
    print('%-48s %8s %8s %8s %9s %8s %8s | iso dBl | LOO dBl' % ('step', 'Emma', 'Quinn', 'Bear', 'Blended', 'dBl', 'MOS%'))
    cur = copy.deepcopy(CFG34); prev = r34
    print('%-48s %8.2f %8.2f %8.2f %9.2f %8s %8.1f' % ('v3.4 (price 259.92)', prev['emma'], prev['quinn'], prev['bear'], prev['blended'], '', prev['mos'] * 100))
    for lab, keys in GROUPS:
        cur = apply_keys(cur, CFG35, keys)
        res = run(cur)
        iso = run(apply_keys(CFG34, CFG35, keys)); loo_cfg = copy.deepcopy(CFG35)
        for k in keys: loo_cfg[k] = CFG34[k]
        loo = run(loo_cfg)
        print('%-48s %8.2f %8.2f %8.2f %9.2f %+8.2f %8.1f | %+7.2f | %+7.2f   (Emma d %+.2f, TV%% %.3f)' % (
            lab, res['emma'], res['quinn'], res['bear'], res['blended'], res['blended'] - prev['blended'], res['mos'] * 100,
            iso['blended'] - r34['blended'], r35['blended'] - loo['blended'], res['emma'] - prev['emma'], res['tv_share']))
        prev = res
    print('check cumulative end == v3.5: %.4f vs %.4f' % (prev['blended'], r35['blended']))
    print('MOS v3.5 vs price %.2f: %.2f%% ; |MOS|>=35%%? %s' % (CFG35['price'], r35['mos'] * 100, abs(r35['mos']) >= .35))

    # ---------- VS2 1.6 judgment-call sensitivity (one change at a time from the v3.5 base) + J1 WACC reconciliation diagnostics ----------
    base = r35
    def alt(label, fn, src=''):
        c = copy.deepcopy(CFG35); fn(c); r = run(c)
        print('%-62s Emma %7.2f (%+6.1f%%) Quinn %7.2f Bear %7.2f Blended %7.2f (%+6.1f%%) WACC %.2f%% TV%% %.3f %s' % (
            label, r['emma'], (r['emma'] / base['emma'] - 1) * 100, r['quinn'], r['bear'], r['blended'], (r['blended'] / base['blended'] - 1) * 100, r['wacc'] * 100, r['tv_share'], src))
        return r
    def set_(**kw):
        return lambda c: c.update(kw)
    def from_anchor(a, g_path=None, m_cap=.42, shift_m=True, m_flat=False, **kw):
        def fn(c):
            g_, m_, c_ = cfg35_aws(a, g_path=g_path, m_cap=m_cap, shift_m=shift_m)
            if m_flat: m_ = [a['aws_m26']] * 10
            c.update(aws_g=g_, aws_m=m_, aws_capex=c_, ret_g0=a['ret_g0'], ret_m0=a['ret_m0'], ads_g0=a['ads_g26'],
                     aws_da=glide(V34_AWS_DA, a['da_aws_ratio'] - V34_AWS_DA[0]), ret_da=glide(lin(.030, .035), a['da_ret_ratio'] - .030)); c.update(kw)
        return fn
    print('\nSENSITIVITY base: Emma %.2f Quinn %.2f Bear %.2f Blended %.2f' % (base['emma'], base['quinn'], base['bear'], base['blended']))
    # J1 WACC
    r_b = alt('J1 WACC = Blume only', set_(wacc_mode='blume'))
    r_u = alt('J1 WACC = bottom-up only', set_(wacc_mode='bu'))
    ev = {k: max(v['ev'], 0) for k, v in base['R']['Emma']['vals'].items()}
    print('   J1 diag: Emma segment EV shares', {k: round(v / sum(ev.values()), 3) for k, v in ev.items()})
    alt('J1 diag: BU weights = Emma segment EV (circular, diagnostic only)', set_(rev_ttm=ev))
    configure(dict(CFG35, rev_ttm=ev)); print('   EV-weighted BU: unlev %.3f lev %.3f COE_BU %.4f WACC_BU %.4f WACC(avg w/ Blume) %.4f | Blume COE %.4f' % (BU_UNLEV_AVG, BU_LEV, COE_BU, WACC_BU, (WACC_BLUME + WACC_BU) / 2, COE_BLUME))
    configure(CFG35)
    # J2 capex 2027
    for v in [269.0, 332.5, 395.0]:
        alt('J2 FY2027 capex = %.1f' % v, set_(capex_y2=v))
    # J3 AWS
    alt('J3a Q4 AWS YoY = Q2 YoY (36.8%) instead of Q3 (39.3%)', from_anchor(anchors35(q4_aws_mode='q2')))
    gm = [A35['aws_g26'], .40, .40, .33, .28, .23, .19, .16, .14, .12]
    alt('J3b AWS mgmt ">40%" 2027+2028 then v3.4 shape (capex follows growth)', lambda c: c.update(zip(('aws_g', 'aws_m', 'aws_capex'), cfg35_aws(g_path=gm))))
    g0 = [A35['aws_g26']] + V34_AWS_G[1:]
    alt('J3b AWS v3.4 calendar path (2027=28% ...) no advance', lambda c: c.update(zip(('aws_g', 'aws_m', 'aws_capex'), cfg35_aws(g_path=g0))))
    alt('J3c AWS margin uncapped (v3.4 path + shift -> 45.1%)', lambda c: c.update(aws_m=cfg35_aws(m_cap=.99)[1]))
    alt('J3c AWS margin = v3.4 path unchanged (35.5% -> 42%) w/ FY26 actual', lambda c: c.update(aws_m=[A35['aws_m26']] + V34_AWS_M[1:]))
    alt('J3c AWS margin flat 38.6%', lambda c: c.update(aws_m=[A35['aws_m26']] * 10))
    alt('J3d AWS capex intensity = v3.4 ratios unshifted', lambda c: c.update(aws_capex=V34_AWS_C))
    # J4 Ads
    alt('J4 Ads Q4 YoY = Q3 alone (+10.9%)', set_(ads_g0=anchors35(q4_ads_mode='q3')['ads_g26']))
    # J5 tax
    alt('J5 tax 21%', set_(tax=.21)); alt('J5 tax 19.6% (v3.4)', set_(tax=.196))
    # J6 D&A
    d_aws, d_ret = A35['da_aws_ratio'] - V34_AWS_DA[0], A35['da_ret_ratio'] - .030
    alt('J6 D&A offset persists (no glide to 0)', lambda c: c.update(aws_da=[v + d_aws for v in V34_AWS_DA], ret_da=[v + d_ret for v in lin(.030, .035)]))
    k = 80.832 / 56.987
    alt('J6 D&A = cash-flow basis $80.8B (Atlas figure; WRONG-basis bound)', lambda c: c.update(aws_da=glide(V34_AWS_DA, A35['da_aws_ratio'] * k - V34_AWS_DA[0]), ret_da=glide(lin(.030, .035), A35['da_ret_ratio'] * k - .030)))
    alt('J6 D&A = v3.4 ratios', lambda c: c.update(aws_da=V34_AWS_DA, ret_da=lin(.030, .035)))
    alt('J6 D&A Q4 = Q3 + $2B', from_anchor(anchors35(da_q4_extra=2.0)))
    # J7 EBIT anchor
    alt('J7 Q4 guide LOW end (EBIT 28.5, rev 240.0)', from_anchor(anchors35(ebit_q4=28.5, rev_q4=240.0)))
    alt('J7 Q4 guide HIGH end (EBIT 33.5, rev 247.0)', from_anchor(anchors35(ebit_q4=33.5, rev_q4=247.0)))
    # J9 bridge
    nn = [list(x) for x in NONOP35]; nn[1][2] = 5.9
    alt('J9 Anthropic notes cost basis 5.9 (Atlas AOCI-implied)', set_(nonop=[tuple(x) for x in nn]))
    nn = [list(x) for x in NONOP35]; nn[4][1] = 4.096
    alt('J9 marketable equity 4.096 (10-Q L1+L2 as read)', set_(nonop=[tuple(x) for x in nn]))
    alt('J9 term loan $17.5B excluded from debt', set_(debt=179.952 - 17.5))
    alt('J9 HYPOTHETICAL: $164.9B unstarted leases counted as debt', set_(fin_oblig=9.726 + 164.9))
    nn = [list(x) for x in NONOP35]; nn[0][1] = 92.5 * .75; nn[1][1] = 146.2 * .75
    alt('J9 Anthropic marks -25% (Bear flip trigger)', set_(nonop=[tuple(x) for x in nn]))
    # J10 locked / unrefreshed
    alt('J10 Emma terminal RONIC 12.0%', set_(ronic_emma=.12))
    alt('J10 Emma terminal RONIC = WACC', set_(ronic_emma=0.0955))
    alt('J10 Emma terminal RONIC 31.4% (3Y incr. ROIC)', set_(ronic_emma=.314))
    alt('J10 TGR 2.5%', set_(tgr=.025)); alt('J10 TGR 3.5%', set_(tgr=.035))
    alt('J10 core-retail terminal margin peers refreshed (WMT 4.45/COST 3.80/TGT 5.03 stale)', set_(core_t={'WMT': .0445, 'COST': .0380, 'TGT': .0503}))
    alt('J10 Ads peer margins refreshed (META 37.78 / GOOGL 33.32)', set_(ads_peer={'META': .3778, 'GOOGL': .3332}))
    # J11 layer 2
    r_old = alt('J11 layer-2 inputs = v3.4 stale multiples (weight stays 100% DCF)', set_(peer_ev=PEER_EV34, peer_pe=PEER_PE34))
    print('   layer-2 cross-check v3.5: fv_mult %.2f (EV/EBIT %.2f, P/E %.2f) vs DCF %.2f -> gap %+.1f%% | stale v3.4 multiples: fv_mult %.2f' % (
        base['l2']['fv_mult'], base['l2']['fv_evebit'], base['l2']['fv_pe'], base['emma_dcf'], base['l2']['gap'] * 100, r_old['l2']['fv_mult']))
    print('   J8 literal TV share %.3f -> weight DCF %.2f; alt reading (fade as TV) %.3f -> weight %.2f -> Emma alt %.2f (%+.1f%%), Blended alt %.2f' % (
        base['l2']['tv_share'], base['l2']['w_dcf'], base['l2']['tv_fade_share'], base['l2']['w_dcf_alt'], base['l2']['fv_alt'],
        (base['l2']['fv_alt'] / base['emma'] - 1) * 100, .4 * base['l2']['fv_alt'] + .3 * base['quinn'] + .3 * base['bear']))
    # Atlas / external WACC cross-check helper (Alcapital 11/18: COE 13.33% -> WACC-equivalent with v3.5 weights)
    configure(CFG35)
    print('Alcapital COE 13.33%% -> WACC-equiv %.2f%% ; base %.2f%% -> gap %.0f bps' % ((WE * .1333 + WD * KD_AT) * 100, WACC * 100, ((WE * .1333 + WD * KD_AT) - WACC) * 1e4))
