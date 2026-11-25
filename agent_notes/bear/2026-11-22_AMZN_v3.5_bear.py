# AMZN v3.5 -- BEAR re-anchor. COPY of agent_notes/emma/2026-11-22_AMZN_v3.5_model.py (calculation functions copied verbatim;
# Emma's file is NOT modified). Only Bear's own model dict + Bear-locked inputs are new (see agent_notes/bear/2026-11-22_AMZN_v3.5.md s.0).
# Shared facts (WACC set, net debt, non-op bridge, shares, tax 23%, D&A P&E basis, Ads growth path, FY26 anchors) = CFG35 unchanged.
# Bear-locked: FY2027 capex 332.5 (median of named post-Q3 estimates 304/310/355/395) -- B5.
# Run: python -I agent_notes/bear/2026-11-22_AMZN_v3.5_bear.py
# HAND-CALC reference (Bear session had no code-execution tool): Bear FV 134.66 | FV5 193.02 | no-growth 91.72 | implied RONIC 13.2%
#   WACC Blume 115.08 / BU 158.58 | capex27 309 -> 136.45, 395 -> 129.89 | RONIC 12.1% -> 156.16, 7% -> 97.45 | AWS capex calendar -> 151.67
import math, json, copy

YEARS = list(range(2026, 2036))
TGR = 0.03
RET_BASE = 588.199
AWS_BASE = 128.725
ADS_BASE = 68.63
V34_AWS_G = [.33, .28, .23, .19, .16, .14, .12, .10, .09, .08]
V34_AWS_M = [.355, .365, .375, .385, .395, .405, .41, .415, .42, .42]
V34_AWS_C = [.90, .75, .60, .45, .35, .28, .22, .18, .16, .15]
V34_AWS_DA = [.17, .18, .185, .19, .19, .185, .18, .175, .17, .165]

def lin(a, b, n=10):
    return [a + (b - a) * i / (n - 1) for i in range(n)]

def glide(vec, delta):
    return [v + delta * (1 - i / 9) for i, v in enumerate(vec)]

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

def anchors35(q4_ads_mode='q2q3', q4_aws_mode='q3', ebit_q4=31.0, rev_q4=243.5, da_q4_extra=0.0):
    aws9, aws9_25, aws_q3, aws_q3_25 = 125.803, 93.146, 45.984, 33.006
    q4_25 = AWS_BASE - aws9_25
    q4_g = aws_q3 / aws_q3_25 - 1 if q4_aws_mode == 'q3' else 42.232 / 30.873 - 1
    aws_q4 = q4_25 * (1 + q4_g)
    aws26 = aws9 + aws_q4
    ebit_aws = 48.555 + aws_q4 * (17.773 / 45.984)
    ads9, ads_q4_25 = 56.689, ADS_BASE - 47.318
    gq = (19.809 + 19.637) / (15.694 + 17.703) - 1 if q4_ads_mode == 'q2q3' else 19.637 / 17.703 - 1
    ads26 = ads9 + ads_q4_25 * (1 + gq)
    rev26 = 584.069 + rev_q4
    ebit26 = 79.389 + ebit_q4
    ret26 = rev26 - aws26
    ret_ebit = ebit26 - ebit_aws
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
C_BY_G = {.40: .90, .36: .90, .33: .90, .28: .75, .23: .60, .19: .45, .16: .35, .14: .28, .12: .22, .10: .18, .09: .16, .08: .15}

def cfg35_aws(a=A35, g_path=None, m_cap=.42, shift_m=True):
    g = g_path or [a['aws_g26']] + V34_AWS_G[:9]
    dm = a['aws_m26'] - V34_AWS_M[0]
    m = [min(v + dm, m_cap) if shift_m else v for v in V34_AWS_M]
    m[0] = a['aws_m26']
    c = [C_BY_G.get(round(x, 2), .90) for x in g]
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
    g['MODELS'] = {}
    g['ADS_G'] = lin(c['ads_g0'], c['ads_gT'])
    g['ADS_M'] = {'Emma': None, 'Quinn Base': None, 'Bear': 'low', 'Quinn Bear': 'low', 'Quinn Bull': 'high'}
    g['PEER_ADS'] = c['ads_peer'] or {'META': .3808, 'GOOGL': .3311}
    g['PEER_RET'] = c['core_t'] or {'WMT': .0394, 'COST': .0385, 'TGT': .0503}
    g['NOPAT_CUR'] = c['nopat_cur']

# ---------------- v3.4 functions (verbatim copy) ----------------
def build(seg):
    rev, out = seg['base'], []
    for i, y in enumerate(YEARS):
        rev = rev * (1 + seg['g'][i])
        nopat = rev * seg['m'][i] * (1 - TAX)
        cap, da = rev * seg['capex'][i], rev * seg['da'][i]
        out.append(dict(y=y, rev=rev, g=seg['g'][i], ebit=rev * seg['m'][i], nopat=nopat, capex=cap, da=da, fcff=nopat - cap + da))
    return out

def seg_value(rows, wacc, mode, ronic=None):
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
    v = seg_value(rows, wacc, mode, ronic)
    pv5 = sum(r['fcff'] / (1 + wacc) ** (i + 1 - 5) for i, r in enumerate(rows) if i >= 5)
    pv5 += sum(f / (1 + wacc) ** (t - 5) for t, f in v['flows'])
    pv5 += v['tv'] / (1 + wacc) ** (v['n_end'] - 5)
    return pv5

def pick(d, how):
    v = sorted(d.values())
    return {'low': v[0], 'high': v[-1]}.get(how, (v[len(v) // 2] if len(v) % 2 else (v[len(v)//2 - 1] + v[len(v)//2]) / 2))

def split_retail(ret_rows, name):
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
    nop = [sum(rs[i]['nopat'] for rs in rows_list) for i in range(10)]
    ni = [sum(rs[i]['capex'] - rs[i]['da'] for rs in rows_list) for i in range(10)]
    return sum(nop[i] - nop[i - 1] for i in range(1, 10)) / sum(ni[i - 1] for i in range(1, 10))

def value(name, step):
    m = MODELS[name]
    wacc = WACC
    mode = 'vs2'
    ronic = m['ronic']
    if ronic == 'WACC':
        ronic = wacc
    aw, rt = build(m['aws']), build(m['ret'])
    for i, tgt in [(0, CAPEX_Y1), (1, CAPEX_Y2)]:
        k = tgt / (aw[i]['capex'] + rt[i]['capex'])
        for rows in (aw, rt):
            rows[i]['capex'] *= k
            rows[i]['fcff'] = rows[i]['nopat'] - rows[i]['capex'] + rows[i]['da']
    segs = {'AWS': aw}
    ads, core, info = split_retail(rt, name); segs.update(Ads=ads, Retail=core)
    vals = {k: seg_value(v, wacc, mode, ronic) for k, v in segs.items()}
    ev = sum(v['ev'] for v in vals.values())
    nd, sh, nonop = NET_DEBT_NEW, SH_DIL, NONOP_AT
    eq = ev - nd + nonop
    return dict(fv=eq / sh, ev=ev, eq=eq, segs=segs, vals=vals, wacc=wacc, ronic=ronic, nd=nd, sh=sh, info=info, mode=mode)

def fv5(res):
    wacc, ronic = res['wacc'], res['ronic']
    ev5 = sum(ev_at_year5(rows, wacc, res['mode'], ronic) for rows in res['segs'].values())
    nd = res['nd']
    for i in range(5):
        f = sum(rows[i]['fcff'] for rows in res['segs'].values())
        nd = nd - f + nd * KD_AT
    sh5 = res['sh'] * (1 + DIL) ** 5
    eq5 = ev5 + NONOP_AT - nd
    return dict(ev5=ev5, nd5=nd, sh5=sh5, eq5=eq5, fv5=eq5 / sh5, gap=eq5 / (res['eq'] * (1 + COE) ** 5) - 1)

def nogrowth(wacc, nd, sh, nonop):
    return (NOPAT_CUR / wacc - nd + nonop) / sh

# ---------------- BEAR v3.5 (locked before run -- notes s.0) ----------------
def bear_model(aws_adv=True, aws_capex_adv=True, ret_adv=False, aws_m=None, ronic='WACC'):
    g_b, c_b = lin(.28, .08), lin(.88, .16)                               # Bear v3.4 own vectors
    aws_g = [A35['aws_g26']] + (g_b[:9] if aws_adv else g_b[1:])          # B1: FY26 actual, then Bear v3.4 path advanced 1y
    aws_c = [.88] + (c_b[:9] if aws_capex_adv else c_b[1:])               # B3: capex intensity advanced with growth state
    aws_mm = aws_m or [A35['aws_m26']] * 10                               # B2: FY26 actual 38.61% = Bear cap 38.6% -> flat
    rg_b = lin(.09, .03)
    ret_g = [A35['ret_g0']] + (rg_b[:9] if ret_adv else rg_b[1:])         # B4: retail calendar path, FY26 actual
    ret_m = [A35['ret_m0']] + lin(.058, .061)[1:]                         # only yr-1 margin matters (split_retail)
    ret_c = lin(95.9 / (RET_BASE * 1.09), .048)                           # Bear v3.4 retail capex (calendar)
    return dict(aws=dict(base=AWS_BASE, g=aws_g, m=aws_mm, capex=aws_c, da=DA_AWS),
                ret=dict(base=RET_BASE, g=ret_g, m=ret_m, capex=ret_c, da=RET_DA), ronic=ronic)

CFG_BEAR = copy.deepcopy(CFG35); CFG_BEAR['capex_y2'] = 332.5          # B5

def run_bear(cfg=CFG_BEAR, **kw):
    configure(cfg)
    MODELS['Bear'] = bear_model(**kw)
    return value('Bear', 7)

if __name__ == '__main__':
    r = run_bear(); f = fv5(r)
    print('BEAR v3.5 FV %.2f (hand 134.66) | EV %.1f | WACC %.4f | segs' % (r['fv'], r['ev'], r['wacc']), {k: round(v['ev'], 1) for k, v in r['vals'].items()})
    print('FV5 %.2f (hand 193.02) nd5 %.1f sh5 %.3f gap %+.3f | exp ret %.4f' % (f['fv5'], f['nd5'], f['sh5'], f['gap'], (f['fv5'] / 246.82) ** .2 - 1))
    print('implied RONIC %.4f (hand 0.1317) | no-growth %.2f ex-nonop %.2f' % (implied_ronic(list(r['segs'].values())), nogrowth(WACC, NET_DEBT_NEW, SH_DIL, NONOP_AT), nogrowth(WACC, NET_DEBT_NEW, SH_DIL, 0)))
    for i, y in enumerate(YEARS):
        s = r['segs']
        print(y, 'rev %.1f NOPAT %.1f capex %.1f DA %.1f FCFF %.1f' % tuple(sum(v[i][k] for v in s.values()) for k in ('rev', 'nopat', 'capex', 'da', 'fcff')))
    base = r['fv']
    def alt(lab, cfg=CFG_BEAR, **kw):
        x = run_bear(cfg, **kw)['fv']; print('%-52s %7.2f (%+6.2f, Blended %+5.2f)' % (lab, x, x - base, .3 * (x - base)))
    alt('WACC Blume only', dict(CFG_BEAR, wacc_mode='blume'))
    alt('WACC bottom-up only', dict(CFG_BEAR, wacc_mode='bu'))
    for v in (269.0, 77.259 * 4, 395.0):
        alt('FY27 capex %.1f' % v, dict(CFG_BEAR, capex_y2=v))
    alt('terminal RONIC 12.1%', ronic=.121)
    alt('terminal RONIC 7% (structural)', ronic=.07)
    alt('AWS capex intensity calendar (not advanced)', aws_capex_adv=False)
    alt('AWS growth calendar (not advanced)', aws_adv=False, aws_capex_adv=False)
    alt('retail growth advanced', ret_adv=True)
    alt('AWS margin -3pp', aws_m=[A35['aws_m26']] + [A35['aws_m26'] - .03] * 9)
    alt('AWS margin +3pp', aws_m=[A35['aws_m26']] + [A35['aws_m26'] + .03] * 9)
    nn = [list(x) for x in NONOP35]; nn[0][1] *= .75; nn[1][1] *= .75
    alt('Anthropic marks -25%', dict(CFG_BEAR, nonop=[tuple(x) for x in nn]))
    nn = [list(x) for x in NONOP35]; nn[0][1] = 10.0; nn[1][1] = 8.0
    alt('Anthropic marks to cost', dict(CFG_BEAR, nonop=[tuple(x) for x in nn]))
