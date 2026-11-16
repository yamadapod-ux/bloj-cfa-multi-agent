# Emma -- ADBE VS2 Full Re-Analysis DCF (2026-11-08)
# Run: python -I emma_dcf.py
# All inputs from Atlas Data Package agent_notes/atlas/2026-11-08_ADBE.md (SEC XBRL / 10-Q / 8-K)
# and SEC XBRL companyfacts extract (scripts/adbe_2026-11-08/sec_more.py) unless flagged as Emma assumption.

PRICE = 239.30            # close 2026-11-06 (Yahoo + StockAnalysis)
SHARES = 391.5            # M diluted, 2026-08-28 (Atlas locked)
NET_DEBT = 724.0          # $M = 6,363 debt - 4,359 cash - 1,280 STI (Atlas locked; lease in FCF)
BRIDGE_PS = NET_DEBT / SHARES   # $1.85
WACC = 0.1010             # Atlas locked base
TGR = 0.030
TAX = 0.226               # 9M FY26 ETR (XBRL 1,589/7,017) -- consistent with WACC Kd tax
REV_FY26 = 26601.0        # FY26 guide midpoint $26.576-26.626B (8-K Q3 Ex 99.1)
TTM_REV = 25970.0
DEF_REV_PCT = 7094.0 / TTM_REV   # current deferred revenue / TTM revenue = 27.3%

BASE_G = [0.090, 0.080, 0.070, 0.065, 0.060, 0.055, 0.050, 0.045, 0.040, 0.035]  # FY27..FY36
BASE_M = [0.345, 0.345] + [0.350] * 8   # GAAP EBIT margin (SBC + amortization expensed)
CAPEX0, CAPEX_T = 0.0085, 0.012         # % rev, TTM 0.82% -> normalized 1.2% by FY31
DA0, DA_T = 0.0295, 0.020               # % rev, TTM 2.95% (766/25,970) -> 2.0% by FY31
MA = 0.020                              # tuck-in M&A % rev (6y avg cash acq ~$0.73B/yr ~3.3% avg rev; Semrush done)
RONIC_T = 0.25                          # terminal RONIC


def ramp(a, b, i, n=5):
    return b if i >= n - 1 else a + (b - a) * i / (n - 1)


def model(g=None, m=None, wacc=WACC, tgr=TGR, tax=TAX, ronic=RONIC_T, ma=MA,
          def_rev=False, shares=SHARES, bridge=NET_DEBT, fade_years=0, full=False):
    g = list(BASE_G if g is None else g)
    m = list(BASE_M if m is None else m)
    rows = []
    rev = REV_FY26
    n = len(g)
    # optional linear fade period after explicit years (VS2 1.3) -> growth from g[-1] to tgr
    if fade_years:
        last = g[-1]
        for k in range(1, fade_years + 1):
            g.append(last + (tgr - last) * k / (fade_years + 1))
            m.append(m[-1])
    pv = 0.0
    for i, gi in enumerate(g):
        prev = rev
        rev = rev * (1 + gi)
        ebit = rev * m[i]
        nopat = ebit * (1 - tax)
        if i < n:
            capex = rev * ramp(CAPEX0, CAPEX_T, i)
            da = rev * ramp(DA0, DA_T, i)
            acq = rev * ma
            reinv = capex - da + acq
        else:  # fade years: reinvestment = g / RONIC (no free growth)
            capex = da = acq = 0.0
            reinv = nopat * gi / ronic
        dnwc = -(rev - prev) * DEF_REV_PCT if def_rev else 0.0
        fcff = nopat - reinv - dnwc
        df = (1 + wacc) ** (i + 1)
        pv += fcff / df
        rows.append(dict(yr=2027 + i, g=gi, rev=rev, m=m[i], ebit=ebit, nopat=nopat, capex=capex, da=da,
                         acq=acq, reinv=reinv, dnwc=dnwc, fcff=fcff, df=df, pv=fcff / df))
    N = len(g)
    nopat_next = rows[-1]['nopat'] * (1 + tgr)
    reinv_rate = tgr / ronic
    fcff_next = nopat_next * (1 - reinv_rate)
    tv = fcff_next / (wacc - tgr)
    pv_tv = tv / (1 + wacc) ** N
    ev = pv + pv_tv
    fv = (ev - bridge) / shares
    out = dict(ev=ev, pv_exp=pv, pv_tv=pv_tv, tv=tv, tv_share=pv_tv / ev, fv=fv, rows=rows,
               reinv_rate=reinv_rate, fcff_next=fcff_next)
    return out if full else fv


def solve(fn, lo, hi, target=PRICE, it=80):
    flo = fn(lo) - target
    fhi = fn(hi) - target
    if flo * fhi > 0:
        return None
    for _ in range(it):
        mid = (lo + hi) / 2
        fm = fn(mid) - target
        if flo * fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def main():
    b = model(full=True)
    print("=== BASE FCFF TABLE ($M) ===")
    print("FY   g     Rev     EBITm  EBIT   NOPAT  Capex  D&A   M&A   Reinv  FCFF   PV")
    for r in b['rows']:
        print(f"{r['yr']} {r['g']*100:4.1f}% {r['rev']:7.0f} {r['m']*100:5.1f}% {r['ebit']:6.0f} {r['nopat']:6.0f} "
              f"{r['capex']:5.0f} {r['da']:5.0f} {r['acq']:5.0f} {r['reinv']:6.0f} {r['fcff']:6.0f} {r['pv']:6.0f}")
    r36 = b['rows'][-1]
    print(f"FY36 implied explicit RONIC proxy = g/(reinv/NOPAT) = {r36['g']/(r36['reinv']/r36['nopat']):.2f}")
    print(f"Terminal: NOPAT37 {r36['nopat']*(1+TGR):.0f}, reinv rate {b['reinv_rate']*100:.1f}%, FCFF37 {b['fcff_next']:.0f}, TV {b['tv']:.0f}")
    print(f"PV explicit {b['pv_exp']:.0f} | PV TV {b['pv_tv']:.0f} | EV {b['ev']:.0f} | PV(TV)/EV {b['tv_share']*100:.1f}%")
    fv = b['fv']
    print(f"FV/share = {b['ev']:.0f}/391.5 - 1.85 = ${fv:.2f}")
    print(f"MOS (FV/P-1) {(fv/PRICE-1)*100:.1f}% | (FV-P)/FV {(1-PRICE/fv)*100:.1f}%")
    # no-growth floor: NOPAT FY26E / WACC
    nopat26 = REV_FY26 * 0.35 * (1 - TAX)
    print(f"No-growth floor: NOPAT26E {nopat26:.0f}/WACC = EV {nopat26/WACC:.0f} -> ${(nopat26/WACC-NET_DEBT)/SHARES:.2f}")
    # fade check
    print(f"Fade check: FY36 g {BASE_G[-1]*100:.1f}% vs TGR+3pp {(TGR+0.03)*100:.1f}% -> fade {'REQUIRED' if BASE_G[-1] > TGR+0.03 else 'not required'}")
    # implied multiples of FV
    ev_fv = b['ev']
    print(f"Implied EV/EBITDA TTM (10,037): {ev_fv/10037:.1f}x | implied P/E FY27 non-GAAP 27.43: {fv/27.43:.1f}x | GAAP FY26 18.145: {fv/18.145:.1f}x")

    # ---- Cross-check multiples ----
    print("\n=== CROSS-CHECK MULTIPLES ===")
    peers = {'CRM': (14.57, 16.03, 21.87), 'INTU': (14.34, 13.50, 14.97), 'ADSK': (20.13, 23.64, 24.70),
             'WDAY': (15.99, 29.54, 38.38), 'NOW': (22.46, 33.17, 54.52)}
    import statistics as st
    pe = sorted(v[0] for v in peers.values()); eve = sorted(v[1] for v in peers.values()); evt = sorted(v[2] for v in peers.values())
    pe_med, eve_med, evt_med = st.median(pe), st.median(eve), st.median(evt)
    eps_fwd = 27.43 * 0 + PRICE / 8.91   # SA fwd EPS implied by 8.91x
    print(f"Fwd EPS implied by SA 8.91x = {eps_fwd:.2f}; consensus FY27 27.43")
    for lab, mult in [('peer median fwd P/E', pe_med), ('peer min fwd P/E (INTU)', pe[0]), ('ADBE 10Y low 7.5x', 7.5)]:
        print(f"  {lab} {mult:.2f}x x {eps_fwd:.2f} = ${mult*eps_fwd:.0f}")
    ebitda = 10037.0; ebit = 9271.0
    for lab, mult, base in [('EV/EBITDA peer median', eve_med, ebitda), ('EV/EBITDA peer min (INTU)', eve[0], ebitda),
                            ('EV/EBIT peer median', evt_med, ebit), ('EV/EBIT peer min', evt[0], ebit)]:
        print(f"  {lab} {mult:.2f}x x {base:.0f} -> ${(mult*base-NET_DEBT)/SHARES:.0f}")
    # core P/E on GAAP (SBC-burdened) FY27E: GAAP EPS FY26 guide 18.145 grown at 10%
    gaap27 = 18.145 * 1.10
    print(f"  GAAP FY27E EPS proxy {gaap27:.2f} x peer median 16.0 = ${gaap27*pe_med:.0f} (flag: peers' fwd P/E is non-GAAP)")

    # ---- Judgment-call sensitivity (VS2 1.6) ----
    print("\n=== JUDGMENT-CALL SENSITIVITY (vs Emma FV) ===")
    cases = [
        ("WACC external 8.6%", dict(wacc=0.086)),
        ("WACC Blume 9.98%", dict(wacc=0.0998)),
        ("WACC bottom-up 10.23%", dict(wacc=0.1023)),
        ("WACC ERP-consistent 10.62%", dict(wacc=0.1062)),
        ("Tax 18% (FY25)", dict(tax=0.18)),
        ("Tax 21.5% (TTM)", dict(tax=0.215)),
        ("TGR 2.5%", dict(tgr=0.025)),
        ("TGR 3.5%", dict(tgr=0.035)),
        ("Terminal RONIC = WACC 10.1%", dict(ronic=0.101)),
        ("Terminal RONIC 40%", dict(ronic=0.40)),
        ("Deferred rev benefit included", dict(def_rev=True)),
        ("M&A 0% rev", dict(ma=0.0)),
        ("M&A 3.3% rev (6y avg)", dict(ma=0.033)),
        ("Terminal/steady margin 33%", dict(m=[0.34, 0.335] + [0.33] * 8)),
        ("Margin 37% (FY25 36.6% + leverage)", dict(m=[0.35, 0.355] + [0.37] * 8)),
        ("Explicit 5y + 5y fade (g/RONIC)", dict(g=BASE_G[:5], m=BASE_M[:5], fade_years=5)),
        ("Shares 389.2M (cover 9-18)", dict(shares=389.2)),
        ("Cash reserve 2% rev ($519M)", dict(bridge=NET_DEBT + 519)),
        ("Debt at fair value $6.03B", dict(bridge=NET_DEBT - 333)),
    ]
    for lab, kw in cases:
        v = model(**kw)
        d = v / fv - 1
        print(f"  {lab:40s} FV ${v:7.2f}  d {d*100:+6.1f}%  {'FLAG >15%' if abs(d) > 0.15 else ''}")

    # ---- Scenarios ----
    print("\n=== SCENARIOS ===")
    citi_g = [0.060, 0.050, 0.045, 0.040, 0.040, 0.035, 0.035, 0.030, 0.030, 0.030]
    citi_m = [0.338, 0.335] + [0.335] * 8
    scen = {
        'Citi (ARR 5.3%/4.5%, GM -70bp)': dict(g=citi_g, m=citi_m),
        'Citi growth only (margin base)': dict(g=citi_g),
        'Bull (company pace ARR ~10%)': dict(g=[0.10, 0.095, 0.09, 0.08, 0.07, 0.065, 0.06, 0.05, 0.045, 0.04], m=[0.35, 0.355] + [0.36] * 8),
        'Structural decline (g->1%, margin 30%)': dict(g=[0.04, 0.03, 0.02, 0.02, 0.015, 0.01, 0.01, 0.01, 0.01, 0.01],
                                                    m=[0.33, 0.32, 0.31] + [0.30] * 7, tgr=0.01, ronic=0.101),
    }
    for lab, kw in scen.items():
        r = model(full=True, **kw)
        print(f"  {lab:42s} FV ${r['fv']:7.2f}  MOS {(r['fv']/PRICE-1)*100:+6.1f}%  PV(TV)/EV {r['tv_share']*100:.0f}%")

    # ---- Market-implied gap closing ----
    print("\n=== GAP-CLOSING (FV = $239.30) ===")
    t = solve(lambda x: model(tgr=x), -0.05, 0.06)
    print(f"  TGR closing gap: {t*100 if t is not None else float('nan'):.2f}%")
    mm = solve(lambda x: model(m=[x] * 10), 0.10, 0.40)
    print(f"  Flat EBIT margin all years closing gap: {mm*100:.1f}%")
    mt = solve(lambda x: model(m=BASE_M[:5] + [x] * 5), 0.05, 0.40)
    print(f"  Terminal-half margin (FY32-36+) closing gap: {mt*100 if mt else float('nan'):.1f}%")
    w = solve(lambda x: model(wacc=x), 0.08, 0.25)
    print(f"  WACC closing gap: {w*100:.2f}%")
    def cagr_fn(sc):
        return model(g=[x * sc for x in BASE_G])
    sc = solve(cagr_fn, -1.0, 1.0)
    gs = [x * sc for x in BASE_G]
    cg = 1.0
    for x in gs:
        cg *= 1 + x
    print(f"  Revenue path scale {sc:.3f} -> FY27 g {gs[0]*100:.1f}% , 10y CAGR {(cg**0.1-1)*100:.2f}%")
    # Citi path + margin needed
    cm = solve(lambda x: model(g=citi_g, m=[x] * 10), 0.10, 0.40)
    print(f"  With Citi growth path, flat margin closing gap: {cm*100:.1f}%")
    # Citi path + RONIC=WACC + TGR needed
    ct = solve(lambda x: model(g=citi_g, m=citi_m, ronic=0.101, tgr=x), -0.05, 0.06)
    print(f"  Citi path+margin+RONIC=WACC: TGR closing gap: {ct*100 if ct is not None else float('nan'):.2f}%")

    # ---- VS2 1.4 FV5 ----
    print("\n=== VS2 1.4 FORWARD VALUE YEAR 5 ===")
    rows = b['rows']
    N = len(rows)
    tv_N = b['tv']
    def ev_at(t):  # EV at end of year t (t=0 today) of FCFF t+1..N + TV
        v = tv_N / (1 + WACC) ** (N - t)
        for i in range(t, N):
            v += rows[i]['fcff'] / (1 + WACC) ** (i + 1 - t)
        return v
    kd_at = 0.05 * (1 - TAX)
    net_debt = NET_DEBT
    shares = SHARES
    cum_bb = 0.0
    print("  yr  EV_t     netdebt_t  FCFF  bb$   shares  V/sh")
    for t in range(1, 6):
        fcff = rows[t - 1]['fcff']
        interest = max(net_debt, 0) * kd_at  # after-tax interest on net debt (small)
        ev_t = ev_at(t)
        # buyback retires 3.2%/yr (3Y FY22-25 data) at intrinsic value per share -> value neutral
        v_pre = (ev_t - (net_debt - fcff + interest)) / shares
        bb = 0.032 * shares * v_pre
        net_debt = net_debt - fcff + interest + bb
        shares = shares * (1 - 0.032)
        cum_bb += bb
        print(f"  {t}  {ev_t:7.0f}  {net_debt:9.0f}  {fcff:5.0f} {bb:5.0f}  {shares:6.1f}  {(ev_t-net_debt)/shares:6.2f}")
    eq5 = ev_at(5) - net_debt
    fv5 = eq5 / shares
    eq0 = b['ev'] - NET_DEBT
    # consistency: Equity5 ~ Equity0*(1+r)^5 - FV of payouts (approx, using WACC as equity ~94% of V)
    approx = eq0 * (1 + WACC) ** 5
    # payouts grown at WACC: rough
    print(f"  Equity5 {eq5:.0f} | FV5/share ${fv5:.2f} | shares5 {shares:.1f}M | cum buyback {cum_bb:.0f}")
    print(f"  Consistency: Equity0*(1+WACC)^5 = {approx:.0f}; Equity5 + FV(buybacks+... ) check below")
    # total value check: per-share growth should ~ WACC-ish minus nothing since buyback value neutral
    print(f"  FV/share CAGR 0->5: {((fv5/fv)**0.2-1)*100:.2f}% (should be ~WACC {WACC*100:.2f}% since all FCFF retained/neutral)")
    print(f"  Emma exp return/yr from $239.30: {((fv5/PRICE)**0.2-1)*100:.2f}%")
    # alt: buyback at market price path (price grows 9.7%/yr from 239.30) -> accretive
    nd = NET_DEBT; sh = SHARES; p = PRICE
    for t in range(1, 6):
        fcff = rows[t - 1]['fcff']; interest = max(nd, 0) * kd_at
        p = p * 1.097
        bb = 0.88 * (fcff - interest)
        nd = nd - fcff + interest + bb
        sh = sh - bb / p
    fv5b = (ev_at(5) - nd) / sh
    print(f"  Alt (88% FCFF buyback at market path +9.7%/yr): shares5 {sh:.1f}M FV5 ${fv5b:.2f} exp ret {((fv5b/PRICE)**0.2-1)*100:.2f}%")


if __name__ == '__main__':
    main()
