# Quinn -- WGO 2026-10-26 quantitative model (VS2). Pure Python (no numpy in env).
# Run: python -I 2026-10-26_WGO_model.py <yahoo_dir> <ff_dir> <xbrl_dir>
# Data fetched this session (2026-10-26):
#  Yahoo chart API monthly: https://query1.finance.yahoo.com/v8/finance/chart/{WGO,^GSPC,^TNX,THO}?period1=1072915200&period2=1793000000&interval=1mo&events=div
#  Yahoo chart API daily 10y: https://query1.finance.yahoo.com/v8/finance/chart/{WGO,^GSPC}?period1=1476662400&period2=1793000000&interval=1d&events=div
#  Ken French: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip (+ F-F_Momentum_Factor_CSV.zip), CRSP 202608
#  SEC XBRL companyconcept: https://data.sec.gov/api/xbrl/companyconcept/CIK0000107687/us-gaap/{Concept}.json, dei/EntityCommonStockSharesOutstanding
# Locked inputs: agent_notes/atlas/2026-10-26_WGO_data.md (WACC 7.91%, TGR 2.5%, RONIC 9.91%, tax 22.3%, ND 274.9, non-op +22.8, 28.6M sh)
import json, math, sys, datetime as dt
YD = sys.argv[1] if len(sys.argv) > 1 else 'C:/Users/user/AppData/Local/Temp/wgo_data/'
FD = sys.argv[2] if len(sys.argv) > 2 else 'C:/Users/user/AppData/Local/Temp/wgo_ff/'
XD = sys.argv[3] if len(sys.argv) > 3 else 'C:/Users/user/AppData/Local/Temp/wgo_xbrl/'
P0 = 28.65; RF = 0.05; SH = 28.6; ND0 = 274.9; NONOP = 22.8; TAX = 0.223
WACC = 0.0791; TGR = 0.025; RONIC = 0.0991; COE = 0.0963; KD_AT = 0.04856
def hdr(s): print('\n' + '=' * 8 + ' ' + s + ' ' + '=' * 8)

# ---------------- stats helpers ----------------
def mean(x): return sum(x) / len(x)
def sd(x):
    m = mean(x); return math.sqrt(sum((v - m) ** 2 for v in x) / (len(x) - 1))
def betacf(a, b, x):
    qab, qap, qam = a + b, a + 1, a - 1; c = 1.0; d = 1 - qab * x / qap
    d = 1 / (d if abs(d) > 1e-30 else 1e-30); h = d
    for m in range(1, 300):
        m2 = 2 * m; aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d; d = 1 / (d if abs(d) > 1e-30 else 1e-30); c = 1 + aa / c; h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d; d = 1 / (d if abs(d) > 1e-30 else 1e-30); c = 1 + aa / c; de = d * c; h *= de
        if abs(de - 1) < 1e-12: break
    return h
def betai(a, b, x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x))
    return bt * betacf(a, b, x) / a if x < (a + 1) / (a + b + 2) else 1 - bt * betacf(b, a, 1 - x) / b
def p_two(t, df): return betai(df / 2, 0.5, df / (df + t * t))
def p_F(F, d1, d2): return betai(d2 / 2, d1 / 2, d2 / (d2 + d1 * F))
def inv(A):
    n = len(A); M = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c])); M[c], M[p] = M[p], M[c]
        pv = M[c][c]; M[c] = [v / pv for v in M[c]]
        for r in range(n):
            if r != c:
                f = M[r][c]; M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]
def ols(y, Xcols, names):
    n = len(y); X = [[1.0] + [c[i] for c in Xcols] for i in range(n)]; k = len(X[0])
    XtX = [[sum(X[i][a] * X[i][b] for i in range(n)) for b in range(k)] for a in range(k)]
    Xty = [sum(X[i][a] * y[i] for i in range(n)) for a in range(k)]
    XtXi = inv(XtX); b = [sum(XtXi[a][j] * Xty[j] for j in range(k)) for a in range(k)]
    e = [y[i] - sum(b[a] * X[i][a] for a in range(k)) for i in range(n)]
    sse = sum(v * v for v in e); my = mean(y); sst = sum((v - my) ** 2 for v in y); s2 = sse / (n - k)
    se = [math.sqrt(s2 * XtXi[a][a]) for a in range(k)]
    # White HC0 robust SE
    meat = [[sum(X[i][a] * X[i][c] * e[i] ** 2 for i in range(n)) for c in range(k)] for a in range(k)]
    V = [[sum(XtXi[a][p] * sum(meat[p][q] * XtXi[q][c] for q in range(k)) for p in range(k)) for c in range(k)] for a in range(k)]
    seW = [math.sqrt(V[a][a]) for a in range(k)]
    r2 = 1 - sse / sst; ar2 = 1 - (1 - r2) * (n - 1) / (n - k); F = (r2 / (k - 1)) / ((1 - r2) / (n - k))
    dw = sum((e[i] - e[i - 1]) ** 2 for i in range(1, n)) / sse
    # Breusch-Pagan (n*R2 of e^2 on X), chi2 df=k-1 approximated by F-form p
    e2 = [v * v for v in e]; me2 = mean(e2)
    Xty2 = [sum(X[i][a] * e2[i] for i in range(n)) for a in range(k)]; g = [sum(XtXi[a][j] * Xty2[j] for j in range(k)) for a in range(k)]
    sse2 = sum((e2[i] - sum(g[a] * X[i][a] for a in range(k))) ** 2 for i in range(n)); sst2 = sum((v - me2) ** 2 for v in e2)
    r2bp = 1 - sse2 / sst2; Fbp = (r2bp / (k - 1)) / ((1 - r2bp) / (n - k))
    res = dict(n=n, r2=r2, adj_r2=ar2, F=F, pF=p_F(F, k - 1, n - k), DW=dw, BP_F=Fbp, BP_p=p_F(Fbp, k - 1, n - k), coef={})
    for a, nm in enumerate(['alpha'] + names):
        res['coef'][nm] = dict(b=b[a], se=se[a], t=b[a] / se[a], p=p_two(b[a] / se[a], n - k), seW=seW[a], tW=b[a] / seW[a], pW=p_two(b[a] / seW[a], n - k))
    return res
def pr_ols(title, r, ann_alpha=True):
    print(f"{title}: n={r['n']} R2={r['r2']:.3f} adjR2={r['adj_r2']:.3f} F={r['F']:.2f} (p={r['pF']:.4f}) DW={r['DW']:.2f} BP-F={r['BP_F']:.2f} (p={r['BP_p']:.3f})")
    for nm, c in r['coef'].items():
        extra = f"  [annualized {c['b']*12*100:.2f}%/yr]" if nm == 'alpha' and ann_alpha else ''
        print(f"   {nm:8s} b={c['b']:+.4f} se={c['se']:.4f} t={c['t']:+.2f} p={c['p']:.4f} | White se={c['seW']:.4f} t={c['tW']:+.2f} p={c['pW']:.4f}{extra}")

# ---------------- load data ----------------
def yahoo(fn, monthly=True):
    j = json.load(open(YD + fn))['chart']['result'][0]
    ts = j['timestamp']; q = j['indicators']['quote'][0]['close']; adj = j['indicators'].get('adjclose', [{}])[0].get('adjclose', q)
    out = {}
    for t, c, a in zip(ts, q, adj):
        if c is None: continue
        d = dt.datetime.fromtimestamp(t, dt.UTC).date()
        key = (d.year, d.month) if monthly else d
        out[key] = (c, a if a is not None else c)  # later duplicates (partial month) overwrite
    return dict(sorted(out.items()))
W = yahoo('m_WGO.json'); S = yahoo('m_%5EGSPC.json'); T = yahoo('m_%5ETNX.json'); TH = yahoo('m_THO.json')
Wd = yahoo('d10_WGO.json', False); Sd = yahoo('d10_%5EGSPC.json', False)
def rets(D, adj=True):
    ks = list(D.keys()); return {ks[i]: D[ks[i]][1 if adj else 0] / D[ks[i - 1]][1 if adj else 0] - 1 for i in range(1, len(ks))}
rW = rets(W); rS = rets(S); rTH = rets(TH)
ff = {}; mom = {}
for fn, dst in (('F-F_Research_Data_Factors.csv', ff), ('F-F_Momentum_Factor.csv', mom)):
    for line in open(FD + fn):
        p = [x.strip() for x in line.split(',')]
        if len(p[0]) == 6 and p[0].isdigit():
            if fn.startswith('F-F_Research') and len(p) >= 5: dst[(int(p[0][:4]), int(p[0][4:]))] = [float(v) / 100 for v in p[1:5]]
            elif fn.startswith('F-F_Mom') and len(p) >= 2 and p[1] and (int(p[0][:4]), int(p[0][4:])) not in dst: dst[(int(p[0][:4]), int(p[0][4:]))] = float(p[1]) / 100
print('Last month Yahoo:', list(W.keys())[-1], W[list(W.keys())[-1]], '| last FF month:', max(ff), '| last MOM:', max(mom))

# ---------------- 1. risk stats ----------------
hdr('1. RISK STATS')
def window(r, start, end): return {k: v for k, v in r.items() if start <= k <= end}
END = (2026, 10)
def risk(start, label):
    a = window(rW, start, END); b = window(rS, start, END); ks = [k for k in a if k in b]
    x = [a[k] for k in ks]; m = [b[k] for k in ks]; n = len(x); rfm = RF / 12
    ann_mean = mean(x) * 12; vol = sd(x) * math.sqrt(12)
    cagr = math.prod(1 + v for v in x) ** (12 / n) - 1; cagrS = math.prod(1 + v for v in m) ** (12 / n) - 1
    sharpe = (ann_mean - RF) / vol
    dd = math.sqrt(sum(min(0, v - rfm) ** 2 for v in x) / n) * math.sqrt(12); sortino = (ann_mean - RF) / dd
    cov = sum((x[i] - mean(x)) * (m[i] - mean(m)) for i in range(n)) / (n - 1); beta = cov / sd(m) ** 2
    corr = cov / (sd(x) * sd(m))
    dn = [i for i in range(n) if m[i] < 0]; up = [i for i in range(n) if m[i] >= 0]
    g = lambda v: math.prod(1 + t for t in v) ** (1 / len(v)) - 1
    dcap = g([x[i] for i in dn]) / g([m[i] for i in dn]); ucap = g([x[i] for i in up]) / g([m[i] for i in up])
    smS = (mean(m) * 12 - RF) / (sd(m) * math.sqrt(12))
    # historical VaR/CVaR monthly
    xs = sorted(x); kv = max(1, int(0.05 * n)); var95 = xs[kv - 1]; cvar = mean(xs[:kv])
    pvar = mean(x) - 1.645 * sd(x)
    print(f"{label} [{ks[0]}..{ks[-1]}] n={n}: CAGR {cagr*100:.2f}% (S&P price {cagrS*100:.2f}%) | arith ann {ann_mean*100:.2f}% | vol {vol*100:.2f}% | Sharpe {sharpe:.3f} (S&P {smS:.3f}) | Sortino {sortino:.3f} | beta {beta:.3f} corr {corr:.3f} | down-cap {dcap*100:.1f}% up-cap {ucap*100:.1f}% (down months {len(dn)}) | VaR95 1M hist {var95*100:.2f}% param {pvar*100:.2f}% CVaR {cvar*100:.2f}%")
    return dict(cagr=cagr, vol=vol, sharpe=sharpe, sortino=sortino, beta=beta, dcap=dcap, ucap=ucap)
R5 = risk((2021, 11), '5Y monthly'); R10 = risk((2016, 11), '10Y monthly'); R1 = risk((2025, 11), '1Y monthly')
def mdd_daily(D, start):
    ks = [k for k in D if k >= start]; pk = -1; pkd = None; m = 0; out = None
    for k in ks:
        v = D[k][1]
        if v > pk: pk, pkd = v, k
        ddv = v / pk - 1
        if ddv < m: m, out = ddv, (pkd, k)
    return m, out
for lab, st in (('5Y', dt.date(2021, 10, 25)), ('10Y', dt.date(2016, 10, 24))):
    m, (a, b) = mdd_daily(Wd, st); ms, (sa, sb) = mdd_daily(Sd, st)
    ksd = [k for k in Wd if k >= st]; rr = [Wd[ksd[i]][1] / Wd[ksd[i - 1]][1] - 1 for i in range(1, len(ksd))]
    print(f"MDD daily total-return {lab}: WGO {m*100:.1f}% (peak {a} -> trough {b}) | S&P {ms*100:.1f}% ({sa} -> {sb}) | daily vol {sd(rr)*math.sqrt(252)*100:.1f}%")
# daily beta 5y
ks = [k for k in Wd if k >= dt.date(2021, 10, 25) and k in Sd]
rw = [Wd[ks[i]][1] / Wd[ks[i - 1]][1] - 1 for i in range(1, len(ks))]; rs = [Sd[ks[i]][1] / Sd[ks[i - 1]][1] - 1 for i in range(1, len(ks))]
cv = sum((rw[i] - mean(rw)) * (rs[i] - mean(rs)) for i in range(len(rw))) / (len(rw) - 1)
print(f"Daily beta 5Y: {cv/sd(rs)**2:.3f} (n={len(rw)}) | daily param VaR95 1-day {(mean(rw)-1.645*sd(rw))*100:.2f}%")
# monthly since 2004 MDD
ks = list(W.keys()); pk = 0; m = 0
for k in ks:
    pk = max(pk, W[k][1]); m = min(m, W[k][1] / pk - 1)
print(f"MDD monthly-close total-return 2004-2026: {m*100:.1f}%")

# ---------------- 2. factor regressions ----------------
hdr('2. FACTOR REGRESSIONS (Ken French, through 2026-08)')
def fwin(start, end):
    ks = [k for k in ff if start <= k <= end and k in rW and k in mom]; return ks
for lab, st in (('10Y', (2016, 9)), ('5Y', (2021, 9))):
    ks = fwin(st, (2026, 8)); y = [rW[k] - ff[k][3] for k in ks]
    mk = [ff[k][0] for k in ks]
    pr_ols(f'CAPM {lab}', ols(y, [mk], ['MKT']))
    if lab == '10Y':
        pr_ols('Carhart 4F 10Y', ols(y, [mk, [ff[k][1] for k in ks], [ff[k][2] for k in ks], [mom[k] for k in ks]], ['MKT', 'SMB', 'HML', 'MOM']))
        dT = [(T[k][0] - T[prev][0]) for k in ks for prev in [list(T.keys())[list(T.keys()).index(k) - 1]]]  # pp change in 10Y yield
        pr_ols('2F MKT + d10Y(pp) 10Y', ols(y, [mk, dT], ['MKT', 'd10Y']))
        # Jensen alpha hypothesis test summary
ks = fwin((2016, 9), (2026, 8)); y = [rW[k] - ff[k][3] for k in ks]
xTH = [rTH[k] - ff[k][3] for k in ks]
pr_ols('WGO on THO excess (industry co-movement) 10Y', ols(y, [xTH], ['THO']))

# ---------------- 3. cycle analysis ----------------
hdr('3. RV DOWNTURN EPISODES (monthly close)')
def episode(D, pk_win, tr_win, label):
    pks = [k for k in D if pk_win[0] <= k <= pk_win[1]]; pk = max(pks, key=lambda k: D[k][1])
    trs = [k for k in D if max(pk, tr_win[0]) <= k <= tr_win[1]]; tr = min(trs, key=lambda k: D[k][1])
    drop = D[tr][1] / D[pk][1] - 1; dropP = D[tr][0] / D[pk][0] - 1
    mon = lambda a, b: (b[0] - a[0]) * 12 + b[1] - a[1]
    rec = next((k for k in D if k > tr and D[k][1] >= D[pk][1]), None)
    rec50 = next((k for k in D if k > tr and D[k][1] >= D[tr][1] * 1.5), None)
    print(f"{label}: peak {pk} adj {D[pk][1]:.2f} (px {D[pk][0]:.2f}) -> trough {tr} adj {D[tr][1]:.2f} (px {D[tr][0]:.2f}) | TR drop {drop*100:.1f}% price drop {dropP*100:.1f}% | {mon(pk,tr)} mo peak->trough | recover to peak (TR): {rec} ({mon(tr,rec) if rec else 'not yet'} mo) | +50% off trough: {rec50}")
    return pk, tr
for D, nm in ((W, 'WGO'), (TH, 'THO'), (S, 'S&P')):
    print('--', nm)
    episode(D, ((2004, 1), (2007, 12)), ((2007, 1), (2009, 12)), 'GFC 2004-09')
    episode(D, ((2017, 1), (2018, 12)), ((2018, 1), (2019, 12)), '2018-19 (pre-COVID)')
    episode(D, ((2017, 1), (2018, 12)), ((2018, 1), (2020, 6)), '2018-20 incl COVID')
    episode(D, ((2021, 1), (2022, 6)), ((2021, 6), (2024, 12)), '2022-24')
    episode(D, ((2021, 1), (2026, 10)), ((2021, 6), (2026, 10)), 'Current (2021 peak -> to date)')
lastk = list(W.keys())[-1]; pk = max((k for k in W if k >= (2021, 1)), key=lambda k: W[k][1])
print(f"Current drawdown from {pk} TR peak: {(W[lastk][1]/W[pk][1]-1)*100:.1f}% | price vs 2021 price-peak {(W[lastk][0]/max(W[k][0] for k in W if k>=(2021,1))-1)*100:.1f}%")

# ---------------- 3b. trough-zone valuation tests ----------------
hdr('3b. TROUGH-ZONE TEST: P/B monthly 2012-2026, EV/EBITDA & EV/Sales at FYE')
def xb(c, kind):
    j = json.load(open(XD + c + '.json')); out = {}
    for u, arr in j['units'].items():
        for x in arr:
            if kind == 'inst': out[x['end']] = x['val'] / 1e6
            elif x.get('fp') == 'FY' and x['form'].startswith('10-K') and 'start' in x:
                s = dt.date.fromisoformat(x['start']); e = dt.date.fromisoformat(x['end'])
                if 350 < (e - s).days < 380: out[x['end']] = x['val'] / 1e6
    return dict(sorted((dt.date.fromisoformat(k), v) for k, v in out.items()))
EQ = xb('StockholdersEquity', 'inst'); SHS = xb('shares', 'inst'); CASH = xb('CashAndCashEquivalentsAtCarryingValue', 'inst'); LTD = xb('LongTermDebt', 'inst')
OI = xb('OperatingIncomeLoss', 'dur'); DDA = xb('DepreciationDepletionAndAmortization', 'dur'); REVa = xb('SalesRevenueNet', 'dur'); REVa.update(xb('Revenues', 'dur'))
# FY17-22 D&A and FY18-26 revenue from Atlas Data Package §B1 (XBRL-derived)
pkg_rev = {2018: 2016.8, 2019: 1985.7, 2020: 2355.5, 2021: 3629.8, 2022: 4957.7, 2023: 3490.7, 2024: 2973.5, 2025: 2798.2, 2026: 2703.9}
pkg_da = {2017: 32.0, 2018: 19.2, 2019: 23.3, 2020: 38.1, 2021: 32.6, 2022: 53.7, 2023: 46.9, 2024: 58.6, 2025: 60.6, 2026: 60.0}
def last_before(D, d):
    ks = [k for k in D if k <= d]; return D[ks[-1]] if ks else None
pb = {}
for k in W:
    if k < (2012, 1): continue
    me = dt.date(k[0], k[1], 28)
    eq = last_before(EQ, me - dt.timedelta(days=45)); sh = last_before(SHS, me)
    if eq and sh: pb[k] = W[k][0] * sh / eq
cur_pb = P0 * 28.444142 / 1236.6; pb[lastk] = cur_pb
vals = sorted(pb.values()); pct = sum(1 for v in vals if v <= cur_pb) / len(vals)
print(f"P/B monthly n={len(vals)}: min {vals[0]:.2f} p10 {vals[int(.1*len(vals))]:.2f} p25 {vals[int(.25*len(vals))]:.2f} median {vals[len(vals)//2]:.2f} p75 {vals[int(.75*len(vals))]:.2f} max {vals[-1]:.2f} | current {cur_pb:.3f} = percentile {pct*100:.1f}%")
for k in [(2012, 1), (2016, 1), (2018, 12), (2019, 1), (2020, 3), (2022, 6), (2022, 9), (2023, 10), (2024, 10), (2025, 4), (2025, 5), (2026, 4)]:
    if k in pb: print(f"   P/B {k}: {pb[k]:.2f}")
print('   Lowest 6 P/B months:', [(k, round(v, 2)) for k, v in sorted(pb.items(), key=lambda kv: kv[1])[:6]])
print('FYE  price  mcap   debt  cash   EV     Rev    EBIT   D&A  EBITDA EV/EBITDA EV/Sales EBITmargin')
evs = []; eves = []
for fyd, oi in OI.items():
    fy = fyd.year if fyd.month >= 8 else fyd.year
    if fy < 2013: continue
    k = (fyd.year, 8); px = W[k][0]; sh = last_before(SHS, dt.date(fy, 12, 1)); mc = px * sh
    debt = last_before(LTD, fyd) if fy >= 2016 else 0.0
    cash = CASH.get(fyd, last_before(CASH, fyd)); ev = mc + (debt or 0) - cash
    rev = pkg_rev.get(fy) or REVa.get(fyd); da = pkg_da.get(fy) or DDA.get(fyd)
    eb = oi + da; evs.append(ev / eb); eves.append(ev / rev)
    print(f"FY{fy} {px:6.2f} {mc:6.0f} {debt or 0:6.0f} {cash:5.0f} {ev:6.0f} {rev:7.0f} {oi:6.1f} {da:5.1f} {eb:6.1f} {ev/eb:8.2f}x {ev/rev:7.2f}x {oi/rev*100:6.2f}%")
EVc = 814.9 + ND0; mid_ebitda = (0.0692 + 0.0149) * 2725
print(f"Current EV {EVc:.1f}: EV/TTM adj EBITDA(125.0) {EVc/125:.2f}x | EV/TTM GAAP EBITDA({66.2+60.0}) {EVc/126.2:.2f}x | EV/mid-cycle EBITDA (6.92%+1.49% x FY27 rev 2725 = {mid_ebitda:.1f}) {EVc/mid_ebitda:.2f}x | EV/Sales {EVc/2703.9:.3f}x")
print(f"FYE EV/EBITDA FY13-26 median {sorted(evs)[len(evs)//2]:.2f}x range {min(evs):.2f}-{max(evs):.2f} | EV/Sales median {sorted(eves)[len(eves)//2]:.3f} min {min(eves):.3f} | current EV/Sales percentile {sum(1 for v in eves if v<=EVc/2703.9)/len(eves)*100:.0f}% of FYE points")
# EV/mid-cycle EBITDA through history on same definition (rev x 8.41%) = EV/Sales / 0.0841
print(f"EV/normalized EBITDA (rev x 8.41%) history: median {sorted(eves)[len(eves)//2]/0.0841:.2f}x min {min(eves)/0.0841:.2f}x | current {EVc/2703.9/0.0841:.2f}x")

# ---------------- 4. DCF / P-W EV ----------------
hdr('4. INDEPENDENT FCFF DCF, P-W EV (Quinn own assumptions)')
REV26 = 2703.9; NWC_PCT = (153.5 + 404.7 - 174.1) / 2703.9   # 10-K R4 FY26 AR+Inv-AP / revenue
DA_PCT = 0.0149; CAPEX_N = 0.0155
def guide_margin(eps, rev): return (eps * SH / (1 - TAX) + 20.9) / rev   # GAAP EPS -> EBIT (add FY26 net interest 20.9)
def path(start, hold_to, reach, end_val, years=range(2027, 2037)):
    out = {}
    for y in years:
        if y <= hold_to: out[y] = start
        elif y >= reach: out[y] = end_val
        else: out[y] = start + (end_val - start) * (y - hold_to) / (reach - hold_to)
    return out
def scenario(cy26, cy27, hold_cy, reach, mid_units, m27, m_hold_to, m_target, p=0.025, wacc=WACC, g=TGR, ronic=RONIC, lit=0.0, lit_year=2028, capex27=0.012, verbose=False, name=''):
    cy = {2026: cy26}; cy.update(path(cy27, hold_cy, reach, mid_units))
    fyu = {y: cy[y - 1] / 3 + cy[y] * 2 / 3 for y in range(2027, 2037)}
    base_fyu27 = 290 / 3 + 285 * 2 / 3
    rev = {2026: REV26}; marg = path(m27, m_hold_to, reach, m_target)
    for y in range(2027, 2037): rev[y] = 2725 * fyu[y] / base_fyu27 * (1 + p) ** (y - 2027)
    rows = []; pv = 0; fcffs = {}
    for i, y in enumerate(range(2027, 2037), start=1):
        ebit = rev[y] * marg[y]; nopat = ebit * (1 - TAX)
        capex = rev[y] * (capex27 if y == 2027 else CAPEX_N); da = rev[y] * DA_PCT; dnwc = NWC_PCT * (rev[y] - rev[y - 1])
        reinv = capex - da + dnwc; gy = rev[y] / rev[y - 1] - 1
        plateau = cy[y] == cy[y - 1] and y > 2027
        if plateau: reinv = max(reinv, gy / ronic * nopat)
        f = nopat - reinv; fcffs[y] = f; pv += f / (1 + wacc) ** i
        rows.append((y, cy[y], rev[y], marg[y], ebit, nopat, reinv, f, gy))
    nT1 = rows[-1][5] * (1 + g); tv = nT1 * (1 - g / ronic) / (wacc - g); pvtv = tv / (1 + wacc) ** 10
    ev = pv + pvtv; lit_pv = lit / (1 + wacc) ** (lit_year - 2026)
    eq = ev - ND0 + NONOP - lit_pv; fv = eq / SH
    # FV5 (end FY31): EV5 = PV@5 of FCFF FY32-36 + TV; net debt roll-forward
    ev5 = sum(fcffs[y] / (1 + wacc) ** (y - 2031) for y in range(2032, 2037)) + tv / (1 + wacc) ** 5
    nd = ND0; divs = []; dps = 1.44
    for y in range(2027, 2032):
        div = dps * SH * 1.03 ** (y - 2027); divs.append(div)
        nd = nd * (1 + KD_AT) - fcffs[y] + div + (lit if y == lit_year else 0)
    eq5 = ev5 - nd + NONOP; fv5 = eq5 / SH  # shares flat: SBC expensed in EBIT (cost already charged) -> assume withholding/buyback offsets dilution
    cons = eq * (1 + COE) ** 5 - sum(d * (1 + COE) ** (4 - i) for i, d in enumerate(divs))
    if verbose:
        print(f"-- {name}: FY  CYunits  Rev   EBIT%  EBIT  NOPAT  Reinv  FCFF  g")
        for r in rows: print(f"   FY{r[0]} {r[1]:6.1f} {r[2]:7.1f} {r[3]*100:5.2f}% {r[4]:6.1f} {r[5]:6.1f} {r[6]:6.1f} {r[7]:6.1f} {r[8]*100:5.2f}%")
        print(f"   PV FCFF {pv:.1f} | TV {tv:.1f} PV(TV) {pvtv:.1f} = {pvtv/ev*100:.1f}% of EV | EV {ev:.1f} | -ND {ND0} +nonop {NONOP} -PV(lit {lit:.1f}) {lit_pv:.1f} | Equity {eq:.1f} | FV0 ${fv:.2f}")
        print(f"   FV5: EV5 {ev5:.1f} ND5 {nd:.1f} Eq5 {eq5:.1f} FV5 ${fv5:.2f} | consistency Eq0*(1+CoE)^5 - divs = {cons:.1f} -> gap {(eq5/cons-1)*100:+.1f}% | 5y return from P0 {((fv5)/P0)**0.2*100-100:.2f}%/yr (+div yld ~5%)")
    return dict(fv=fv, fv5=fv5, ev=ev, tvpct=pvtv / ev, eq=eq, eq5=eq5, cons_gap=eq5 / cons - 1, rows=rows)
m_base27 = guide_margin(1.20, 2725); m_bull27 = guide_margin(1.50, 2725 * (290 / 3 + 295 * 2 / 3) / (290 / 3 + 285 * 2 / 3)); m_bear27 = guide_margin(0.90, 2725 * (285 / 3 + 275 * 2 / 3) / (290 / 3 + 285 * 2 / 3))
print(f"FY27 GAAP EBIT margin implied by guide EPS: low {m_bear27*100:.2f}% mid {m_base27*100:.2f}% high {m_bull27*100:.2f}% | NWC% {NWC_PCT*100:.2f}%")
UNITS = dict(c2018=483.672, c2019=406.070, c2020=430.412, c2021=600.240, c2023=313.174, c2024=333.733, c2025=342.220)
exboom = mean([UNITS[k] for k in UNITS if k not in ('c2021',)]); print(f"RVIA avg 2018-25 ex-2021-22 (2022 not verified): {exboom:.1f}K | incl 2021: {mean(list(UNITS.values())):.1f}K")
lit_base = 0.5 * (0.01 * 55887 * 46275 / 1e6 + 5.0); lit_bear = 0.03 * 55887 * 46275 / 1e6 + 15.0
print(f"Litigation: base (50% x [1% x 55,887 x $46,275 + $5M legal]) = ${lit_base:.1f}M | bear (3% x 55,887 x $46,275 + $15M) = ${lit_bear:.1f}M")
# ---- operating-leverage regression: WGO adj EBIT margin (Data Pkg §B1) vs RVIA FY-blended industry units ----
# RVIA CY units: 2018 483,672 / 2019 406,070 (rvia.org Dec-2019) · 2020 430,412 (rvnews) · 2021 600,240 (rv-pro) · 2023 313,174 (rvnews ?p=199641)
# 2022 = 313,174/(1-0.365) DERIVED from "-36.5% vs 2022" (not a reported figure) · 2024 333,733 (rv-pro) · 2025 342,220 / 2026F 290K (rvnews 10-16-26)
CYU = {2018: 483.672, 2019: 406.070, 2020: 430.412, 2021: 600.240, 2022: 313.174 / (1 - 0.365), 2023: 313.174, 2024: 333.733, 2025: 342.220, 2026: 290.0}
MADJ = {2019: .0782, 2020: .0483, 2021: .1122, 2022: .1177, 2023: .0861, 2024: .0439, 2025: .0219, 2026: .0240}
fyux = {fy: CYU[fy - 1] / 3 + CYU[fy] * 2 / 3 for fy in MADJ}
for lab, yrs in (('all FY19-26', list(MADJ)), ('ex-COVID FY20', [y for y in MADJ if y != 2020])):
    rr = ols([MADJ[y] for y in yrs], [[fyux[y] for y in yrs]], ['units'])
    a_, b_ = rr['coef']['alpha']['b'], rr['coef']['units']['b']
    print(f"Margin-volume OLS {lab}: margin = {a_*100:.2f}% + {b_*100:.4f}pp x units(K) | R2 {rr['r2']:.3f} t(units) {rr['coef']['units']['t']:.2f} p {rr['coef']['units']['p']:.4f} n={rr['n']} | fitted @285K {(a_+b_*285)*100:.2f}% @330K {(a_+b_*330)*100:.2f}% @385K {(a_+b_*385)*100:.2f}% @410K {(a_+b_*410)*100:.2f}% | units for 6.92%: {(0.0692-a_)/b_:.0f}K")
REG_A, REG_B = a_, b_   # ex-COVID fit used
bear_margin = REG_A + REG_B * 330 + 0.005   # trough-avg CY23-25 volume (330K) + 0.5pp net cost savings (of $70-80M gross guide)
print(f"Bear terminal margin = fit@330K {(REG_A+REG_B*330)*100:.2f}% + 0.5pp savings = {bear_margin*100:.2f}% | Base check: fit@385K {(REG_A+REG_B*385)*100:.2f}% + 1.0pp savings = {(REG_A+REG_B*385+0.01)*100:.2f}% vs locked 6.92%")
SC = {
 'bull': dict(prob=0.20, kw=dict(cy26=290, cy27=295, hold_cy=2027, reach=2029, mid_units=410, m27=m_bull27, m_hold_to=2027, m_target=0.0692, p=0.025, ronic=0.12, lit=0.0)),
 'base': dict(prob=0.50, kw=dict(cy26=290, cy27=285, hold_cy=2027, reach=2030, mid_units=385, m27=m_base27, m_hold_to=2027, m_target=0.0692, p=0.025, ronic=RONIC, lit=lit_base)),
 'bear': dict(prob=0.30, kw=dict(cy26=285, cy27=275, hold_cy=2028, reach=2032, mid_units=330, m27=m_bear27, m_hold_to=2028, m_target=bear_margin, p=0.020, ronic=WACC, lit=lit_bear)),
}
res = {}
for k, v in SC.items(): res[k] = scenario(**v['kw'], verbose=True, name=k)
bear_v1 = scenario(**{**SC['bear']['kw'], 'mid_units': 350, 'm_target': 0.0577})
print(f"REVISION LOG: bear v1 (first run, 350K / 5.77% P10-alt-a) FV0 ${bear_v1['fv']:.2f} FV5 ${bear_v1['fv5']:.2f} -> bear v2 (330K / regression {bear_margin*100:.2f}%) FV0 ${res['bear']['fv']:.2f}")
pw_v1 = 0.2 * res['bull']['fv'] + 0.5 * res['base']['fv'] + 0.3 * bear_v1['fv']; print(f"   P-W v1 ${pw_v1:.2f}")
pw = sum(res[k]['fv'] * SC[k]['prob'] for k in SC); pw5 = sum(res[k]['fv5'] * SC[k]['prob'] for k in SC)
print(f"P-W FV0 ${pw:.2f} (MOS vs ${P0} {(pw/P0-1)*100:+.1f}%) | P-W FV5 ${pw5:.2f} -> {((pw5/P0)**0.2-1)*100:.2f}%/yr price + ~5% div yield")
sdv = math.sqrt(sum(SC[k]['prob'] * (res[k]['fv'] - pw) ** 2 for k in SC)); print(f"Scenario dispersion sd ${sdv:.2f}; P(FV<P0) = {sum(SC[k]['prob'] for k in SC if res[k]['fv']<P0):.2f}")
# no-growth values
ng_now = 66.2 * (1 - TAX) / WACC; ng_mid = 0.0692 * 2725 * (1 - TAX) / WACC
print(f"No-growth value: current NOPAT 51.4/WACC -> EV {ng_now:.0f} -> ${(ng_now-ND0+NONOP)/SH:.2f}/sh | mid-cycle NOPAT {0.0692*2725*(1-TAX):.1f}/WACC -> EV {ng_mid:.0f} -> ${(ng_mid-ND0+NONOP)/SH:.2f}/sh")
# market-implied
def solve(f, lo, hi):
    flo = f(lo)
    for _ in range(80):
        m = (lo + hi) / 2; fm = f(m)
        if (fm > 0) == (flo > 0): lo, flo = m, fm
        else: hi = m
    return (lo + hi) / 2
bk = SC['base']['kw']
im = solve(lambda mm: scenario(**{**bk, 'm_target': mm})['fv'] - P0, 0.01, 0.12)
iw = solve(lambda w: scenario(**{**bk, 'wacc': w})['fv'] - P0, 0.06, 0.25)
print(f"Market-implied (base path): mid-cycle margin {im*100:.2f}% at WACC 7.91% | WACC {iw*100:.2f}% at margin 6.92%")
ib = solve(lambda q: (q * res['bear']['fv'] + (1 - q) * (0.2 / 0.7 * res['bull']['fv'] + 0.5 / 0.7 * res['base']['fv'])) - P0, 0.0, 1.0)
print(f"Bear probability that makes P-W = P0 (bull:base kept 2:5): {ib*100:.1f}%")

# ---------------- 5. sensitivity ----------------
hdr('5. SENSITIVITY MATRICES (base volume path)')
wl = [0.07, 0.0791, 0.09, 0.10, 0.11]; ml = [0.05, 0.06, 0.0692, 0.08, 0.09]
print('WACC \\ mid-cycle EBIT margin: ' + ' '.join(f'{m*100:.2f}%' for m in ml))
for w in wl: print(f"  {w*100:5.2f}%: " + ' '.join(f"${scenario(**{**bk, 'wacc': w, 'm_target': m})['fv']:7.2f}" for m in ml))
print('Year mid-cycle reached (trough duration) \\ margin: ' + ' '.join(f'{m*100:.2f}%' for m in ml))
for ry in [2029, 2030, 2031, 2032, 2033]:
    print(f"  FY{ry} (trough {ry-2027}y): " + ' '.join(f"${scenario(**{**bk, 'reach': ry, 'hold_cy': 2027 + max(0, ry - 2030), 'm_hold_to': 2027 + max(0, ry - 2030), 'm_target': m})['fv']:7.2f}" for m in ml))
print('TV% base:', round(res['base']['tvpct'] * 100, 1), '| RONIC alt (base): =WACC', round(scenario(**{**bk, 'ronic': WACC})['fv'], 2), '| 12%', round(scenario(**{**bk, 'ronic': 0.12})['fv'], 2))
print('Base with zero litigation:', round(scenario(**{**bk, 'lit': 0})['fv'], 2), '| base with bear litigation:', round(scenario(**{**bk, 'lit': lit_bear})['fv'], 2))
print('Base price/mix 2.0%:', round(scenario(**{**bk, 'p': 0.02})['fv'], 2), '| Base mid units 350K:', round(scenario(**{**bk, 'mid_units': 350})['fv'], 2), '| Base mid units 425K:', round(scenario(**{**bk, 'mid_units': 425})['fv'], 2))
print('Base WACC +25bp (Fed hike):', round(scenario(**{**bk, 'wacc': WACC + 0.0023})['fv'], 2))

# WACC alternative: 10Y regression beta (CAPM, Ken French market, section 2) instead of Blume 1.141 -- FLAG, not a change of locked P1
b10 = 1.5872; coe10 = 0.05 + b10 * 0.042; w10 = 0.641 * coe10 + 0.359 * KD_AT
print(f"WACC alt (10Y OLS beta {b10}): CoE {coe10*100:.2f}% WACC {w10*100:.2f}% -> base FV ${scenario(**{**bk, 'wacc': w10})['fv']:.2f} | P-W FV ${sum(scenario(**{**SC[k]['kw'], 'wacc': w10})['fv']*SC[k]['prob'] for k in SC):.2f}")
w5 = 0.641 * (0.05 + 1.1707 * 0.042) + 0.359 * KD_AT
print(f"WACC alt (5Y OLS beta 1.1707): {w5*100:.2f}%")
print(f"SWS discount 12.5% (stale-rate): base ${scenario(**{**bk, 'wacc': 0.125})['fv']:.2f} | P-W ${sum(scenario(**{**SC[k]['kw'], 'wacc': 0.125})['fv']*SC[k]['prob'] for k in SC):.2f}")
# Market-implied: units plateau that (via regression margin, no savings) gives P0 at locked WACC
def reg_case(u, sav=0.0, w=WACC):
    return scenario(**{**bk, 'mid_units': u, 'm_target': REG_A + REG_B * u + sav, 'wacc': w})['fv']
iu = solve(lambda u: reg_case(u) - P0, 250, 500)
print(f"Market-implied plateau industry units (regression margin, no savings, WACC 7.91%): {iu:.0f}K -> margin {(REG_A+REG_B*iu)*100:.2f}%")
print('Regression-consistent base (385K, fit+1.0pp):', round(reg_case(385, 0.01), 2), '| 385K fit no savings:', round(reg_case(385), 2), '| 330K fit +0.5pp:', round(reg_case(330, 0.005), 2), '| 300K fit:', round(reg_case(300), 2))
print('P-W FV5 components:', {k: round(res[k]['fv5'], 2) for k in res}, '| cons gaps', {k: round(res[k]['cons_gap'] * 100, 1) for k in res})
