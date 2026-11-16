# Emma MU VS2 DCF (2026-11-08). Run: cd scripts/scout/2026-11-06_memory && python -I emma_dcf.py
# All inputs: agent_notes/charlie/2026-11-06_MU_verified_inputs.md [S1-S4] + Atlas locked package (agent_notes/atlas/2026-08-27_MU.md, 2026-11-06 update).
import json, time, statistics as st

# ---------------- locked inputs (Atlas) ----------------
PX = 656.39; PX_ID = 696.0; SH = 1150.0; BRIDGE = 55601.0          # bridge $M -> +48.35/share
WACC = 0.125; TAX = 0.155; RF = 0.0484; ERP = 0.0441
# ---------------- history [S4] ($M) ----------------
REV = {16:12399,17:20322,18:30391,19:23406,20:21435,21:27705,22:30758,23:15540,24:25111,25:37378,26:133188}
OP  = {16:168,17:5868,18:14994,19:7376,20:3003,21:6283,22:9702,23:-5745,24:1304,25:9770,26:99340}
DA  = {16:2980,17:3861,18:4759,19:5424,20:5650,21:6214,22:7116,23:7756,24:7780,25:8352,26:9503}
CAPEX={16:5817,17:4734,18:8879,19:9780,20:8223,21:10030,22:12067,23:7676,24:8386,25:15857,26:30712}
PPE = {19:28240,20:31031,21:33213,22:38549,23:37928,24:39749,25:46590,26:63310}
AR  = {19:2778,20:3494,21:4920,22:4765,23:2048,24:5419,25:7163,26:31793}
INV = {19:5118,20:5373,21:4487,22:6663,23:8387,24:8875,25:8355,26:10372}
APA = {19:4626,20:5817,21:5325,22:6090,23:3958,24:7299,25:9649,26:22605}
TAXP= {19:693,20:280,21:394,22:888,23:177,24:451,25:1124,26:14761}
COGS26 = 25684

def out(*a): print(*a)

# ---------------- Q1: mid-cycle margin ----------------
yrs = range(16,26)
rw_ebit = sum(OP[y] for y in yrs)/sum(REV[y] for y in yrs)
rw_ebitda = sum(OP[y]+DA[y] for y in yrs)/sum(REV[y] for y in yrs)
simple = st.mean(OP[y]/REV[y] for y in yrs)
pk_ebit = OP[18]/REV[18]; pk_ebitda = (OP[18]+DA[18])/REV[18]
SCA = 0.35
M_EBIT = SCA*pk_ebit + (1-SCA)*rw_ebit
M_EBITDA = SCA*pk_ebitda + (1-SCA)*rw_ebitda
capint = sum(CAPEX[y] for y in yrs)/sum(REV[y] for y in yrs); daint = sum(DA[y] for y in yrs)/sum(REV[y] for y in yrs)
out(f"Q1 hist FY16-25: simple EBIT {simple:.2%} | rev-wtd EBIT {rw_ebit:.2%} EBITDA {rw_ebitda:.2%} | FY18 peak EBIT {pk_ebit:.2%} EBITDA {pk_ebitda:.2%}")
out(f"   capex/rev {capint:.1%} D&A/rev {daint:.1%} -> MID-CYCLE EBIT {M_EBIT:.2%} EBITDA {M_EBITDA:.2%} (SCA wt {SCA:.0%} at prior peak)")

# ---------------- Q2: mid-cycle revenue (bits x ASP) ----------------
opex26 = REV[26]-COGS26-OP[26]; cost26_52 = (COGS26+opex26)*52/53     # 53-week -> 52-week
T26_base = cost26_52/(1-M_EBIT)
rev26_52 = REV[26]-54229/14
asp_mult = T26_base/(REV[25]*1.25)                                     # FY26 bits = FY25 x1.25 [S1]
g_trend = 0.08
out(f"Q2 FY26 52wk rev {rev26_52:,.0f} (YoY {rev26_52/REV[25]-1:+.1%}); FY26 cost (52wk) {cost26_52:,.0f}; T26 mid-cycle rev {T26_base:,.0f} = {T26_base/REV[26]:.0%} of FY26; "
    f"implied mid-cycle ASP = {asp_mult:.2f}x FY25 ASP (FY26 ASP {REV[26]/(REV[25]*1.25):.2f}x); trend g FY17-25 {(REV[25]/REV[17])**(1/8)-1:.1%} FY19-25 {(REV[25]/REV[19])**(1/6)-1:.1%}")

# ---------------- model ----------------
BASE = dict(wacc=WACC, tgr=0.025, ronic=0.15, m_ebit=M_EBIT, m_ebitda=M_EBITDA, T26=T26_base, gT=g_trend,
            r27=262.5e3, g28=0.12, dec29=-0.34, dec30=-0.39, M=[0.9,1.0,1.25,1.3,0.95,1.0],   # M FY31..36
            em27=0.88, em28=0.86, capex=[55e3,55e3,40e3,28e3,22e3], gross=1.0, nwc=0.15, nwc_tr=0.20,
            fade=5, bridge=BRIDGE, union=0.0, nodown=False, exp_years=10, shares=SH, termmargin=None)

def model(o=None, detail=False):
    p = dict(BASE); p.update(o or {})
    T = {26:p['T26']}
    for y in range(27,37): T[y] = T[y-1]*(1+p['gT'])
    R = {27:p['r27'], 28:p['r27']*(1+p['g28'])}
    if p['nodown']:
        for y in range(29,37): R[y] = R[y-1]*1.03
    else:
        R[29] = R[28]*(1+p['dec29']); R[30] = R[29]*(1+p['dec30'])
        for i,y in enumerate(range(31,37)): R[y] = T[y]*p['M'][i]
    mE = p['m_ebitda']
    ppe = PPE[26]; nwc_prev = AR[26]+INV[26]-APA[26]; rows=[]; fcff={}; ebit={}
    for y in range(27,37):
        Mt = R[y]/T[y]
        em = p['em27'] if y==27 else p['em28'] if y==28 else (1-(1-mE)/Mt)
        if p['nodown'] and y>28: em = p['em28']
        ebitda = R[y]*em
        if y<=31: cap = p['capex'][y-27]
        else:
            da_est = 0.16*ppe; tgt = T[y]/0.80
            cap = max(0.9*da_est, da_est+(tgt-ppe)/2)
        cap *= p['gross']
        da = 0.16*(ppe+0.5*cap); ppe_new = ppe+cap-da
        e = ebitda-da
        if p['union'] and e>0: e *= (1-p['union'])
        nwc = R[y]*(p['nwc_tr'] if (Mt<1 and not p['nodown']) else p['nwc'])
        nopat = e*(1-TAX) if e>0 else e
        f = nopat+da-cap-(nwc-nwc_prev)
        ic0 = ppe+nwc_prev; ic1 = ppe_new+nwc
        rows.append((2000+y,R[y],R[y]/R.get(y-1,REV[26])-1,Mt,em,da,e/R[y],nopat,cap,nwc-nwc_prev,f,nopat/((ic0+ic1)/2),ppe_new))
        fcff[y]=f; ebit[y]=e; ppe=ppe_new; nwc_prev=nwc
    w = p['wacc']; tg = p['tgr']; ro = p['ronic']
    pv = {y:fcff[y]/(1+w)**(y-26-0.5) for y in fcff}                   # mid-year convention
    tm = p['termmargin'] if p['termmargin'] is not None else p['m_ebit']
    # fade FY37..: growth from FY36 trend growth linearly to TGR, reinvestment = g/RONIC
    g36 = R[36]/R[35]-1; gstart = p['gT'] if not p['nodown'] else 0.03
    fade_pv = 0.0; Rf_ = R[36]; nf = p['fade'] if gstart > tg+0.03 else 0; frows=[]
    for k in range(1,nf+1):
        g = gstart-(gstart-tg)*k/nf; Rf_ *= (1+g); n = Rf_*tm*(1-TAX)*(1-p['union'])
        f = n*(1-g/ro); fade_pv += f/(1+w)**(10+k-0.5); frows.append((2036+k,Rf_,g,n,f))
    R_T1 = Rf_*(1+tg); nT = R_T1*tm*(1-TAX)*(1-p['union']); fT = nT*(1-tg/ro)
    TV = fT/(w-tg); N = 10+nf; pvTV = TV/(1+w)**(N-0.5)  # TV at mid-year-consistent timing
    ev = sum(pv.values())+fade_pv+pvTV
    fv = ev/p['shares']+p['bridge']/p['shares']
    r = dict(ev=ev, fv=fv, pvexp=sum(pv.values()), fade_pv=fade_pv, pvTV=pvTV, tvshare=pvTV/ev, beyond=(fade_pv+pvTV)/ev,
             rows=rows, frows=frows, g36=g36, nf=nf, fcff=fcff, R=R, T=T, p=p, nT=nT, fT=fT, TV=TV)
    return r

b = model(); FV = b['fv']
out("\nYEAR  Rev  g  M(x trend)  EBITDAm  D&A  EBITm  NOPAT  capex  dNWC  FCFF  ROIC(avg IC)  PP&E")
for r in b['rows']:
    out(f"{r[0]} {r[1]:9,.0f} {r[2]:+6.1%} {r[3]:5.2f} {r[4]:6.1%} {r[5]:7,.0f} {r[6]:6.1%} {r[7]:8,.0f} {r[8]:7,.0f} {r[9]:7,.0f} {r[10]:8,.0f} {r[11]:6.1%} {r[12]:8,.0f}")
out("trend T:", {2000+y:round(v) for y,v in b['T'].items()})
out(f"FY36 growth {b['g36']:+.1%} vs TGR+3pp {BASE['tgr']+0.03:.1%} -> fade years {b['nf']}")
for f in b['frows']: out(f"  fade {f[0]} rev {f[1]:,.0f} g {f[2]:.2%} NOPAT {f[3]:,.0f} FCFF {f[4]:,.0f}")
out(f"terminal: NOPAT {b['nT']:,.0f} reinvest {BASE['tgr']/BASE['ronic']:.1%} FCFF {b['fT']:,.0f} TV {b['TV']:,.0f}")
out(f"EV {b['ev']:,.0f} = PV explicit {b['pvexp']:,.0f} + PV fade {b['fade_pv']:,.0f} + PV TV {b['pvTV']:,.0f} | PV(TV)/EV {b['tvshare']:.1%} | (fade+TV)/EV {b['beyond']:.1%}")
out(f"EMMA DCF FV ${FV:.2f} | MOS@{PX} {FV/PX-1:+.1%} | MOS@{PX_ID} {FV/PX_ID-1:+.1%}")
mkt_ev = PX*SH-BRIDGE
out(f"market EV {mkt_ev:,.0f}")

# cumulative boom cash
cum = sum(b['fcff'][y] for y in range(27,29)); out(f"FCFF FY27+28 {cum:,.0f} (= ${cum/SH:.0f}/sh undiscounted); PV FY27-31 share of EV {sum(b['fcff'][y]/(1.125)**(y-26.5) for y in range(27,32))/b['ev']:.1%}")

# ---------------- historical through-cycle ROIC (FY20-25) ----------------
ic = {y:PPE[y]+AR[y]+INV[y]-APA[y] for y in PPE}
nop = {y:OP[y]*(1-TAXP[y]/OP[y] if OP[y]>0 else 1) for y in range(20,27)}
roic_hist = sum(nop[y] for y in range(20,26))/sum((ic[y]+ic[y-1])/2 for y in range(20,26))
out(f"hist ROIC FY20-25 (sum NOPAT/sum avg IC) {roic_hist:.1%}; FY26 ROIC {nop[26]/((ic[26]+ic[25])/2):.1%}; IC FY26 {ic[26]:,.0f}")
out(f"mid-cycle FY26 NOPAT {T26_base*M_EBIT*(1-TAX):,.0f} / IC FY26 {ic[26]:,.0f} = {T26_base*M_EBIT*(1-TAX)/ic[26]:.1%}; no-growth value peak NOPAT ${(OP[26]*(1-0.148)/WACC+BRIDGE)/SH:.0f}/sh, mid-cycle ${(T26_base*M_EBIT*(1-TAX)/WACC+BRIDGE)/SH:.0f}/sh")

# ---------------- 1.6 judgment-call sensitivity ----------------
def fv(o): return model(o)['fv']
T26_hist = cost26_52/(1-rw_ebit)
sens = [
 ("WACC bottom-up 11.44%", dict(wacc=0.1144)),
 ("WACC Blume-only 13.56% (CIO input)", dict(wacc=0.1356)),
 ("WACC ERP-consistent 13.28%", dict(wacc=0.1328)),
 ("WACC external 10.4%", dict(wacc=0.104)),
 ("Bridge: no SCA deposit deduction", dict(bridge=BRIDGE+12700)),
 ("Capex gross (x30,712/27,367)", dict(gross=30712/27367)),
 ("TGR 1.0%", dict(tgr=0.01)), ("TGR 3.0%", dict(tgr=0.03)),
 ("No fade (TV right after FY36)", dict(fade=0)),
 ("Mid-cycle EBIT = history 21.6% (SCA wt 0)", dict(m_ebit=rw_ebit, m_ebitda=rw_ebitda, T26=T26_hist)),
 ("Mid-cycle SCA wt 70% (structural)", dict(m_ebit=0.7*pk_ebit+0.3*rw_ebit, m_ebitda=0.7*pk_ebitda+0.3*rw_ebitda, T26=cost26_52/(1-(0.7*pk_ebit+0.3*rw_ebit)))),
 ("Mid-cycle = SCA floor claim on 100% (49.3%)", dict(m_ebit=pk_ebit, m_ebitda=pk_ebitda, T26=cost26_52/(1-pk_ebit))),
 ("Trend growth 6%", dict(gT=0.06)), ("Trend growth 10%", dict(gT=0.10)),
 ("Terminal RONIC = WACC 12.5%", dict(ronic=0.125)), ("Terminal RONIC 20%", dict(ronic=0.20)),
 ("FY27-28 = consensus 275.5/320.1", dict(r27=275.5e3, g28=320.06/275.5-1)),
 ("Downturn milder (-20%/-20%, trough 1.0x)", dict(dec29=-0.20, dec30=-0.20, M=[1.0,1.0,1.25,1.3,0.95,1.0])),
 ("Downturn deeper (-45%/-45%, trough 0.7x)", dict(dec29=-0.45, dec30=-0.45, M=[0.7,0.9,1.25,1.3,0.95,1.0])),
 ("Downturn 1yr later (FY30 start)", dict(dec29=0.05, dec30=-0.34, M=[1.5,0.9,1.25,1.3,0.95,1.0])),
 ("Union profit-share 6.8% of EBIT (all yrs)", dict(union=0.068)),
 ("No down-cycle (consensus-style +3%/yr after FY28)", dict(nodown=True, r27=275.5e3, g28=320.06/275.5-1)),
]
out("\n1.6 SENSITIVITY  base FV %.2f" % FV)
for nm,o in sens:
    v = fv(o); out(f"  {nm:52s} FV ${v:8.2f}  d {v/FV-1:+6.1%}")

# ---------------- market-implied gap closing ----------------
def solve(f, lo, hi, target=PX, n=80):
    flo = f(lo)-target; fhi = f(hi)-target
    if flo*fhi > 0: return None
    for _ in range(n):
        mid=(lo+hi)/2; fm=f(mid)-target
        if flo*fm<=0: hi=mid
        else: lo=mid; flo=fm
    return (lo+hi)/2
out("\nGAP-CLOSING (FV = $%.2f)" % PX)
g_tgr = solve(lambda x: fv(dict(tgr=x)), 0.0, 0.12); out("  TGR:", g_tgr)
g_tm = solve(lambda x: fv(dict(termmargin=x)), 0.2, 3.0); out("  terminal+fade EBIT margin:", g_tm)
g_mid = solve(lambda x: fv(dict(m_ebit=x, m_ebitda=x+(M_EBITDA-M_EBIT), T26=cost26_52/(1-x))), 0.2, 0.95); out("  mid-cycle EBIT (FY29+ & terminal, T26 re-derived):", g_mid)
g_w = solve(lambda x: fv(dict(wacc=x)), 0.03, 0.125); out("  WACC:", g_w)
def scaled(s):
    o = dict(T26=T26_base*s, r27=262.5e3*s); return fv(o)
s = solve(scaled, 1.0, 5.0)
if s:
    r = model(dict(T26=T26_base*s, r27=262.5e3*s)); out(f"  revenue level scale x{s:.2f} -> FY26-36 CAGR {(r['R'][36]/REV[26])**0.1-1:.1%} (base {(b['R'][36]/REV[26])**0.1-1:.1%}); FY26-31 CAGR {(r['R'][31]/REV[26])**0.2-1:.1%}")

# ---------------- reverse DCF: implied FY26-28 CAGR (boom size) ----------------
def boom(g): return fv(dict(r27=REV[26]*(1+g), g28=g))
gi = solve(boom, 0.0, 3.0); out(f"\nREVERSE DCF implied FY26-28 CAGR {gi:.1%} vs consensus 55.0% (ratio {gi/0.55:.2f}x, gate 1.2x = 66.0%)")
out(f"  base model FY26-28 CAGR {((b['R'][28])/REV[26])**0.5-1:.1%}")
out(f"  implied mid-cycle EBIT margin {g_mid:.1%} vs FY16-25 rev-wtd {rw_ebit:.1%}, FY18 peak {pk_ebit:.1%}")

# ---------------- Layer-2 / cross-check: EV/EBITDA vs 5Y history ----------------
g = json.load(open('data/cf_MU.json','rb'))['facts']['us-gaap']
y5 = json.load(open('data/y_MU_5y.json','rb'))['chart']['result'][0]
px = dict(zip(y5['timestamp'], y5['indicators']['quote'][0]['close']))
fyend = {'2021-09-02':21,'2022-09-01':22,'2023-08-31':23,'2024-08-29':24,'2025-08-28':25,'2026-09-03':26}
WSH = {20:1131,21:1141,22:1122,23:1093,24:1118,25:1125,26:1143}
ps=[]; pe=[]
for ts,pr in sorted(px.items()):
    if not pr: continue
    ds = time.strftime('%Y-%m-%d', time.gmtime(ts)); fy=[v for k,v in fyend.items() if k<=ds]
    fy = fy[-1] if fy else 20
    mc = pr*WSH[fy]; ps.append(mc/REV[fy]); e=OP[fy]+DA[fy]
    if e>0: pe.append(mc/e)
def pct(v, arr): return sum(1 for a in arr if a<=v)/len(arr)
evs = mkt_ev/REV[26]; T27 = b['T'][27]; mid_ebitda27 = T27*M_EBITDA
out(f"\nMULTIPLES 5Y monthly n={len(ps)}: P/S med {st.median(ps):.2f} p70 {sorted(ps)[int(.7*len(ps))]:.2f}; EV/Rev now {evs:.2f} -> pct {pct(evs,ps):.0%}")
evm = mkt_ev/mid_ebitda27; evt = mkt_ev/(OP[26]+DA[26])
out(f"  mcap/EBITDA med {st.median(pe):.2f} p33 {sorted(pe)[len(pe)//3]:.2f} p70 {sorted(pe)[int(.7*len(pe))]:.2f}; EV/trailing EBITDA {evt:.2f} pct {pct(evt,pe):.0%}; EV/mid-cycle EBITDA FY27 ({mid_ebitda27:,.0f}) {evm:.1f}x pct {pct(evm,pe):.0%}")
# cross-check value: median multiple x mid-cycle EBITDA + PV of boom excess FCFF over normal FCFF (FY27-31)
def normal_fcff(y): return b['T'][y]*M_EBIT*(1-TAX)*(1-g_trend/0.15)
excess = sum((b['fcff'][y]-normal_fcff(y))/(1+WACC)**(y-26-0.5) for y in range(27,32))
for nm,mult in [('median',st.median(pe)),('p33',sorted(pe)[len(pe)//3])]:
    evx = mult*mid_ebitda27+excess; out(f"  cross-check ({nm} {mult:.2f}x): EV {evx:,.0f} -> FV ${evx/SH+BRIDGE/SH:.2f} (vs DCF {FV:.2f}, gap {(evx/SH+BRIDGE/SH)/FV-1:+.1%}); PV boom excess {excess:,.0f}")
# implied: multiple on mid-cycle EBITDA embedded in DCF ex-boom
out(f"  DCF EV ex-boom-excess / mid-cycle EBITDA FY27 = {(b['ev']-excess)/mid_ebitda27:.1f}x")

# ---------------- VS2 1.4 forward value year 5 (end FY31) ----------------
def fv5(o=None):
    r = model(o); p=r['p']; w=p['wacc']
    ev5 = sum(r['fcff'][y]/(1+w)**(y-31-0.5) for y in range(32,37)) + (r['fade_pv']+r['pvTV'])*(1+w)**5
    nc = p['bridge']; ra = RF*(1-TAX)
    for y in range(27,32): nc = nc*(1+ra)+r['fcff'][y]
    sh5 = p['shares']*(1.015)**5
    return (ev5+nc)/sh5, ev5, nc, sh5, r
f5, ev5, nc5, sh5, _ = fv5()
ke = RF+((1.99+1.51)/2)*ERP; eq0 = FV*SH
out(f"\nFV5 (end FY31) ${f5:.2f}: EV5 {ev5:,.0f} + net cash5 {nc5:,.0f} / shares5 {sh5:,.0f} (dilution 1.5%/yr FY23-26 diluted 1093->1143)")
out(f"  consistency: Eq0 x (1+ke {ke:.2%})^5 = {eq0*(1+ke)**5:,.0f} vs Eq5 {f5*sh5:,.0f} ({f5*sh5/(eq0*(1+ke)**5)-1:+.1%})")
for nm,pp in [('656.39',PX),('696',PX_ID)]:
    out(f"  exp. return/yr @{nm}: {(f5/pp)**0.2-1:+.1%} vs S&P Rf+ERP {RF+ERP:.2%}")
out(f"  FV5 at WACC 13.56%: ${fv5(dict(wacc=0.1356))[0]:.2f}; at 11.44%: ${fv5(dict(wacc=0.1144))[0]:.2f}")

# ================= ADDENDUM 2026-11-08 (review fixes) =================
out("\n=== ADDENDUM (review fixes 2026-11-08) ===")
# Fix 1: apples-to-apples percentile -- history is mcap-based, so compare mcap-based 'now'
mc_now = PX*SH; ps_now = mc_now/REV[26]; pe_tr_now = mc_now/(OP[26]+DA[26]); pe_mid_now = mc_now/mid_ebitda27
out(f"P/S now (mcap/FY26 rev) {ps_now:.2f} pct {pct(ps_now,ps):.0%} | @696 {PX_ID*SH/REV[26]:.2f} pct {pct(PX_ID*SH/REV[26],ps):.0%}")
out(f"mcap/trailing EBITDA {pe_tr_now:.2f} pct {pct(pe_tr_now,pe):.0%} | mcap/mid-cycle EBITDA FY27 {pe_mid_now:.1f}x pct {pct(pe_mid_now,pe):.0%}")
out(f"P/S percentiles: min {min(ps):.2f} p33 {sorted(ps)[len(ps)//3]:.2f} med {st.median(ps):.2f} p70 {sorted(ps)[int(.7*len(ps))]:.2f} max {max(ps):.2f}")
# Fix 2: test trough bias in median mcap/EBITDA -- exclude months mapped to trough FY23/FY24 EBITDA
pe_x=[]; 
for ts,pr in sorted(px.items()):
    if not pr: continue
    ds = time.strftime('%Y-%m-%d', time.gmtime(ts)); fy=[v for k,v in fyend.items() if k<=ds]; fy = fy[-1] if fy else 20
    if fy in (23,24): continue
    e=OP[fy]+DA[fy]
    if e>0: pe_x.append(pr*WSH[fy]/e)
mx = st.median(pe_x); evx = mx*mid_ebitda27+excess
out(f"median mcap/EBITDA excl. trough-EBITDA months (FY23-24 base) n={len(pe_x)}: {mx:.2f}x -> FV ${evx/SH+BRIDGE/SH:.2f} gap {(evx/SH+BRIDGE/SH)/FV-1:+.1%}")
# mid-cycle-normalised: mcap / (rev-wtd hist EBITDA margin x that year's revenue)
pe_n=[]
for ts,pr in sorted(px.items()):
    if not pr: continue
    ds = time.strftime('%Y-%m-%d', time.gmtime(ts)); fy=[v for k,v in fyend.items() if k<=ds]; fy = fy[-1] if fy else 20
    if fy==26: continue
    pe_n.append(pr*WSH[fy]/(REV[fy]*rw_ebitda))
mn = st.median(pe_n); evn = mn*mid_ebitda27+excess
out(f"median mcap / normalised EBITDA (rev x {rw_ebitda:.1%}), FY20-25 bases n={len(pe_n)}: {mn:.2f}x -> FV ${evn/SH+BRIDGE/SH:.2f} gap {(evn/SH+BRIDGE/SH)/FV-1:+.1%}")
# Fix 3: gap-closing on downturn timing
for nm,o in [("downturn starts FY30 (1y later)", dict(dec29=0.05, dec30=-0.34, M=[1.5,0.9,1.25,1.3,0.95,1.0])),
             ("downturn starts FY31 (2y later)", dict(dec29=0.05, dec30=0.03, M=[2.4,1.3,0.9,1.3,0.95,1.0])),
             ("downturn FY31 2y later, trough FY33", dict(dec29=0.05, dec30=0.03, M=[2.4,1.6,0.9,1.2,0.95,1.0]))]:
    out(f"  {nm:40s} FV ${fv(o):.2f}")
# Fix 4: trigger prices
f_gate = fv(dict(r27=REV[26]*1.66, g28=0.66))
out(f"PRICE where reverse-DCF implied FY26-28 CAGR = 1.2x consensus (66.0%): ${f_gate:.2f}; MOS15 on Emma FV: ${FV/1.15:.2f}; MOS25: ${FV/1.25:.2f}")
# Fix 5: FV5 consistency -- cash drag (retained cash earns after-tax Rf, not ke)
r0=model(); nc_ke = BRIDGE
for y in range(27,32): nc_ke = nc_ke*(1+ke)+r0['fcff'][y]
out(f"FV5 if retained cash compounds at ke instead of after-tax Rf: net cash5 {nc_ke:,.0f} (vs {nc5:,.0f}) -> Eq5 {ev5+nc_ke:,.0f} vs Eq0x(1+ke)^5 {eq0*(1+ke)**5:,.0f} ({(ev5+nc_ke)/(eq0*(1+ke)**5)-1:+.1%}); FV5/sh {(ev5+nc_ke)/sh5:.2f}")
# union derivation check: 15% demand x Taiwan share of op profit (DRAM 75.6% of rev x ~60% Taiwan DRAM output, media)
out(f"union 15% x DRAM share {100680/133188:.1%} x Taiwan 60% = {0.15*100680/133188*0.60:.2%} of EBIT")
