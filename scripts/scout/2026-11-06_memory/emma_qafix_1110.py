# Emma MU QA-fix 2026-11-10 (after Morgan FAIL). Run: cd scripts/scout/2026-11-06_memory && python -I emma_qafix_1110.py
# Model = copy of emma_dcf.py model() with extra hooks (exp_years, nwc_mode, union by year, SCA end year, lease adj).
# Base (no hooks) must reproduce Emma FV $504.32. Does NOT modify emma_dcf.py.
import json, statistics as st
from datetime import date
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import quinn_dcf_1108 as Q

PX = 656.39; SH = 1150.0; BRIDGE = 55601.0; WACC = 0.125; TAX = 0.155; BLEND = 405.89
REV = {16:12399,17:20322,18:30391,19:23406,20:21435,21:27705,22:30758,23:15540,24:25111,25:37378,26:133188}
OP  = {16:168,17:5868,18:14994,19:7376,20:3003,21:6283,22:9702,23:-5745,24:1304,25:9770,26:99340}
DA  = {16:2980,17:3861,18:4759,19:5424,20:5650,21:6214,22:7116,23:7756,24:7780,25:8352,26:9503}
PPE26 = 63310; AR26 = 31793; INV26 = 10372; APA26 = 22605; COGS26 = 25684
yrs = range(16,26)
rw_ebit = sum(OP[y] for y in yrs)/sum(REV[y] for y in yrs)
rw_ebitda = sum(OP[y]+DA[y] for y in yrs)/sum(REV[y] for y in yrs)
pk_ebit = OP[18]/REV[18]; pk_ebitda = (OP[18]+DA[18])/REV[18]
M_EBIT = .35*pk_ebit+.65*rw_ebit; M_EBITDA = .35*pk_ebitda+.65*rw_ebitda
opex26 = REV[26]-COGS26-OP[26]; cost26_52 = (COGS26+opex26)*52/53
T26_base = cost26_52/(1-M_EBIT); T26_hist = cost26_52/(1-rw_ebit)

BASE = dict(wacc=WACC, tgr=0.025, ronic=0.15, m_ebit=M_EBIT, m_ebitda=M_EBITDA, T26=T26_base, gT=0.08,
            r27=262.5e3, g28=0.12, dec29=-0.34, dec30=-0.39, M=[0.9,1.0,1.25,1.3,0.95,1.0],
            em27=0.88, em28=0.86, capex=[55e3,55e3,40e3,28e3,22e3], gross=1.0, nwc=0.15, nwc_tr=0.20,
            fade=5, bridge=BRIDGE, union=0.0, shares=SH, termmargin=None,
            # --- new hooks ---
            exp_years=10, fade_from='trend',      # fade_from: 'trend' (normalised T) or 'actual' (R of last explicit yr) -- only matters if exp<10
            nwc_mode='level',                      # 'level' = Emma original (NWC = % of revenue, releases on decline)
                                                   # 'flow' = build up_rate x dRev on increase, release dn_rate x |dRev| on decline
            up_rate=0.15, dn_rate=0.0,
            union_from=27, union_to=99, union_term=True,
            sca_end=None,                          # if set (e.g. 31): FY>=sca_end and terminal use history margins (SCA wt 0) + T from history
            lease_fcff=0.0, lease_bridge=0.0)      # constant $M added to FCFF each yr (explicit+fade+terminal) / $M deducted from bridge

def model(o=None):
    p = dict(BASE); p.update(o or {})
    T = {26:p['T26']}
    for y in range(27,37): T[y] = T[y-1]*(1+p['gT'])
    Th = {26:T26_hist}
    for y in range(27,37): Th[y] = Th[y-1]*(1+p['gT'])
    def Ty(y): return Th[y] if (p['sca_end'] and y>=p['sca_end']) else T[y]
    def mEy(y): return rw_ebitda if (p['sca_end'] and y>=p['sca_end']) else p['m_ebitda']
    R = {27:p['r27'], 28:p['r27']*(1+p['g28'])}
    R[29] = R[28]*(1+p['dec29']); R[30] = R[29]*(1+p['dec30'])
    for i,y in enumerate(range(31,37)): R[y] = Ty(y)*p['M'][i]
    ppe = PPE26; nwc_prev = AR26+INV26-APA26; fcff={}; rows=[]
    for y in range(27,37):
        Mt = R[y]/Ty(y); mE = mEy(y)
        em = p['em27'] if y==27 else p['em28'] if y==28 else (1-(1-mE)/Mt)
        ebitda = R[y]*em
        if y<=31: cap = p['capex'][y-27]
        else:
            da_est = 0.16*ppe; tgt = Ty(y)/0.80
            cap = max(0.9*da_est, da_est+(tgt-ppe)/2)
        cap *= p['gross']
        da = 0.16*(ppe+0.5*cap); ppe_new = ppe+cap-da
        e = ebitda-da
        u = p['union'](y) if callable(p['union']) else (p['union'] if p['union_from']<=y<=p['union_to'] else 0)
        if u and e>0: e *= (1-u)
        if p['nwc_mode']=='level':
            nwc = R[y]*(p['nwc_tr'] if Mt<1 else p['nwc'])
        else:
            dR = R[y]-(R[y-1] if y>27 else REV[26])
            nwc = nwc_prev + (p['up_rate']*dR if dR>0 else p['dn_rate']*dR)
        nopat = e*(1-TAX) if e>0 else e
        f = nopat+da-cap-(nwc-nwc_prev)+p['lease_fcff']
        rows.append(dict(y=y,R=R[y],nopat=nopat,netcap=cap-da,dnwc=nwc-nwc_prev,fcff=f))
        fcff[y]=f; ppe=ppe_new; nwc_prev=nwc
    E = p['exp_years']; last = 26+E
    w = p['wacc']; tg = p['tgr']; ro = p['ronic']
    pv = {y:fcff[y]/(1+w)**(y-26-0.5) for y in range(27,last+1)}
    tm = p['termmargin'] if p['termmargin'] is not None else (rw_ebit if p['sca_end'] else p['m_ebit'])
    ut = (p['union'] if not callable(p['union']) else p['union'](99)) if p['union_term'] else 0
    gstart = p['gT']
    Rf_ = Ty(last) if (E<10 and p['fade_from']=='trend') else R[last]
    nf = p['fade'] if gstart > tg+0.03 else 0; fade_pv=0.0; fpvs=[]
    for k in range(1,nf+1):
        g = gstart-(gstart-tg)*k/nf; Rf_ *= (1+g); n = Rf_*tm*(1-TAX)*(1-ut)
        f = n*(1-g/ro)+p['lease_fcff']; d = f/(1+w)**(E+k-0.5); fade_pv += d; fpvs.append(d)
    R_T1 = Rf_*(1+tg); nT = R_T1*tm*(1-TAX)*(1-ut); fT = nT*(1-tg/ro)+p['lease_fcff']
    TV = fT/(w-tg); pvTV = TV/(1+w)**(E+nf-0.5)
    ev = sum(pv.values())+fade_pv+pvTV
    fv = ev/p['shares']+(p['bridge']-p['lease_bridge'])/p['shares']
    return dict(fv=fv, ev=ev, pv=pv, fade_pv=fade_pv, pvTV=pvTV, rows=rows, fcff=fcff, p=p)

def fv(o=None): return model(o)['fv']
FV0 = fv()
def line(nm, v): print(f"  {nm:62s} FV ${v:8.2f} | dEmma {v/FV0-1:+6.1%} | d$Blended {0.4*(v-FV0):+7.2f} ({0.4*(v-FV0)/BLEND:+5.1%})")
print(f"BASE reproduce: Emma FV ${FV0:.2f} (must be 504.32)")
b = model()
print("  base dNWC by yr:", {r['y']+2000: round(r['dnwc']) for r in b['rows']})

print("\n[1a] EXPLICIT HORIZON")
line("Locked: 10y explicit FY27-36 + 5y fade (base)", FV0)
line("7y explicit FY27-33 + 5y fade from trend rev (normalised)", fv(dict(exp_years=7)))
line("7y explicit FY27-33 + 5y fade from actual FY33 rev (1.25x trend)", fv(dict(exp_years=7, fade_from='actual')))
line("7y explicit + 8y fade (normalised)", fv(dict(exp_years=7, fade=8)))

print("\n[1b] LEASE")
# FY26 debt 5,179 = current 491 + LT 4,688; FinanceLeaseLiability FY26 = 2,387 (cur 491 + noncur 1,896) -> finance leases inside debt -> in bridge.
# Operating lease liability: latest XBRL FY25 = 775 (FY26 not tagged in companyfacts); op lease cost FY25 153, payments 149.
OPL = 775; OPC = 153; r_l = 0.05   # r_l = assumed implicit lease rate (Emma assumption)
line("Current: op-lease cost in EBIT/FCFF; op-lease liab NOT in bridge", FV0)
line("Alt A (consistent): op-lease liab $775M to net debt + add back interest (5%) a/t to FCFF", fv(dict(lease_bridge=OPL, lease_fcff=OPL*r_l*(1-TAX))))
line("Alt B (double-count, wrong): deduct $775M w/o EBIT adj", fv(dict(lease_bridge=OPL)))
line("Alt C (missing, wrong): add back full lease cost a/t, no debt", fv(dict(lease_fcff=OPC*(1-TAX))))

print("\n[2] dNWC BASIS")
nr = fv(dict(nwc_mode='flow', up_rate=0.15, dn_rate=0.0))
b5 = fv(dict(nwc_mode='flow', up_rate=0.15, dn_rate=0.05))
bx = fv(dict(nwc_mode='flow', up_rate=0.12, dn_rate=0.05))
lv0 = fv(dict(nwc=0.15, nwc_tr=0.15))
line("Emma original: NWC level 15% rev (20% in trough yrs) -> releases", FV0)
line("Emma level 15% flat (no trough build)", lv0)
line("Quinn basis: build 15% of dRev up, NO release", nr)
line("Bear release rate: build 15% up, release 5% of |dRev| down", b5)
line("Bear exact: build 12% up, release 5% down", bx)
rnr = model(dict(nwc_mode='flow', dn_rate=0.0))
print("  no-release dNWC by yr:", {r['y']+2000: round(r['dnwc']) for r in rnr['rows']})

# FY19/FY23 evidence from SEC XBRL cash-flow statement (cf_MU.json; sign: + = increase in asset / increase in liability)
g = json.load(open('data/cf_MU.json','rb'))['facts']['us-gaap']
def ann(t):
    d={}
    for x in list(g[t]['units'].values())[0]:
        if x.get('form')!='10-K' or x.get('fp')!='FY': continue
        if 'start' in x and (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<340: continue
        d[int(x['end'][:4])]=x['val']/1e6
    return d
rec=ann('IncreaseDecreaseInReceivables'); inv=ann('IncreaseDecreaseInInventories'); ap=ann('IncreaseDecreaseInAccountsPayableAndAccruedLiabilities')
ocl=ann('IncreaseDecreaseInOtherCurrentLiabilities')
print("\n  MU downturn working-capital cash flow (SEC 10-K via XBRL, $M; + = cash inflow):")
for fy in (2019,2020,2023):
    dR = REV[fy-2000]-REV[fy-2001]
    cf = -rec[fy]-inv[fy]+ap[fy]+(ocl.get(fy,0))
    print(f"   FY{fy}: dRev {dR:+,.0f} | receivables {-rec[fy]:+,.0f} inventories {-inv[fy]:+,.0f} AP&accrued {ap[fy]:+,.0f} other CL {ocl.get(fy,0):+,.0f} => net {cf:+,.0f} = {cf/(-dR):+.1%} of revenue decline")

print("\n[3] TAIWAN PROFIT-SHARE")
line("Taiwan 5% of EBIT from FY27 (all yrs + fade/terminal) -- Bear line item", fv(dict(union=0.05)))
line("Taiwan 2% / 10% (Bear range)", fv(dict(union=0.02)))
line("   10%", fv(dict(union=0.10)))
line("Quinn-P-W-equivalent: 3.0% FY27, 1.2% FY28, 0 after (Quinn mechanics)", fv(dict(union=lambda y: {27:0.03,28:0.012}.get(y,0.0))))

print("\n[4] SCA AFTER 2030")
line("Base: SCA wt 35% in mid-cycle all yrs + terminal", FV0)
line("SCA wt 0 all yrs (history 21.6%, T re-derived) [= emma_dcf #9]", fv(dict(m_ebit=rw_ebit, m_ebitda=rw_ebitda, T26=T26_hist)))
line("SCA 35% through FY30, wt 0 from FY31 + terminal", fv(dict(sca_end=31)))

print("\n[COMBOS]")
c1 = dict(nwc_mode='flow', dn_rate=0.0, union=0.05)
c2 = dict(nwc_mode='flow', dn_rate=0.05, union=0.05)
line("No release + Taiwan 5%", fv(c1))
line("Bear 5% release + Taiwan 5%", fv(c2))
line("No release + Taiwan 5% + SCA ends FY31", fv(dict(c1, sca_end=31)))
line("No release + Taiwan 5% + 7y explicit", fv(dict(c1, exp_years=7)))

# ---------------- Reconciliation Emma vs Quinn P-W (period x component, $/share) ----------------
print("\n[RECON] Emma vs Quinn P-W")
def quinn_pw(timing='quinn', ps_zero=False, nwc_release=None):
    agg = dict(ev=0.0)
    per = {}
    for k,s in Q.SC.items():
        s2 = dict(s)
        if ps_zero: s2['ps']=0.0
        r = Q.path(s2)
        if nwc_release is not None:   # re-compute FCFF with release on decline (level-free flow approach)
            for x in r:
                if x['rev']<x['rev']/(1+x['g']):
                    dn = nwc_release*(x['rev']-x['rev']/(1+x['g'])); x['fcff'] += x['dn']-dn; x['dn']=dn
        v = Q.value(s2, r)
        if timing=='emma':
            pvx = sum(x['fcff']/(1+WACC)**(i+0.5) for i,x in enumerate(r))
            fpv = v['fadepv']*(1+WACC)**(Q.T0-0.5)   # fade flows shift by (0.5 - T0) earlier/later
            tvp = v['tv']/(1+WACC)**14.5
            ev = pvx+fpv+tvp
        else:
            ev = v['ev']; tvp = v['pvtv']; fpv = v['fadepv']
        agg['ev'] += s['p']*ev
        for i,x in enumerate(r):
            t = (i+0.5) if timing=='emma' else (Q.T0+i)
            d = 1/(1+WACC)**t
            for c,val in (('nopat',x['nopat']),('netcap',-(x['cx']-x['da'])),('dnwc',-x['dn'])):
                per[(x['y'],c)] = per.get((x['y'],c),0)+s['p']*val*d
        per['fadeTV'] = per.get('fadeTV',0)+s['p']*(fpv+tvp)
    agg['fv'] = agg['ev']/SH+BRIDGE/SH; agg['per']=per
    return agg
q = quinn_pw(); qe = quinn_pw('emma'); q0 = quinn_pw(ps_zero=True)
print(f"  Quinn P-W FV (own timing) ${q['fv']:.2f} (must be 373.35) | re-timed to Emma mid-year convention ${qe['fv']:.2f} | Quinn with ps=0 ${q0['fv']:.2f}")
def emma_per(o=None):
    r = model(o); per={}
    for x in r['rows']:
        d = 1/(1+WACC)**(x['y']-26-0.5)
        per[(x['y']+2000,'nopat')] = x['nopat']*d; per[(x['y']+2000,'netcap')] = -x['netcap']*d; per[(x['y']+2000,'dnwc')] = -x['dnwc']*d
    per['fadeTV'] = r['fade_pv']+r['pvTV']; return per, r
ep, er = emma_per()
periods = [('Boom FY27-28',range(2027,2029)),('Downturn FY29-31',range(2029,2032)),('Recovery FY32-36',range(2032,2037))]
rows=[]
for nm,rg in periods:
    for c,cn in (('nopat','NOPAT (rev x margin, after Taiwan)'),('netcap','Net capex (capex - D&A)'),('dnwc','dNWC')):
        e_ = sum(ep[(y,c)] for y in rg)/SH; q_ = sum(qe['per'][(y,c)] for y in rg)/SH
        rows.append((nm,cn,e_,q_,e_-q_))
rows.append(('Fade+TV','Fade FY37-41 + terminal',ep['fadeTV']/SH,qe['per']['fadeTV']/SH,(ep['fadeTV']-qe['per']['fadeTV'])/SH))
tot=0
for r_ in rows: print(f"   {r_[0]:18s} {r_[1]:36s} Emma {r_[2]:8.2f} Quinn {r_[3]:8.2f} gap {r_[4]:+8.2f}"); tot+=r_[4]
print(f"   sum of gaps (same timing) {tot:+.2f} = Emma {FV0:.2f} - Quinn(re-timed) {qe['fv']:.2f} = {FV0-qe['fv']:+.2f}")
print(f"   discount-timing effect (Quinn t0=1/3, TV +0.5y) : Quinn own {q['fv']:.2f} - re-timed {qe['fv']:.2f} = {q['fv']-qe['fv']:+.2f}")
# Taiwan inside Quinn's NOPAT
print(f"   Taiwan in Quinn (ps -> 0): +{q0['fv']-q['fv']:.2f}/sh ; NWC release inside Emma: no-release FV {nr:.2f} -> {FV0-nr:+.2f}/sh")
qr15 = quinn_pw(nwc_release=0.15); qr5 = quinn_pw(nwc_release=0.05)
print(f"   Reverse test: Quinn P-W with 15% release on decline ${qr15['fv']:.2f} ({qr15['fv']-q['fv']:+.2f}) ; 5% release ${qr5['fv']:.2f} ({qr5['fv']-q['fv']:+.2f})")
# Emma downturn NWC release PV
rel = sum(ep[(y,'dnwc')] for y in range(2029,2032))/SH
print(f"   Emma PV of NWC release FY29-31: {rel:+.2f}/sh")

print("\n[5] LABELS")
print(f"  MOS25 trigger on Emma FV = {FV0:.2f}/1.25 = ${FV0/1.25:.2f}; on Blended {BLEND}/1.25 = ${BLEND/1.25:.2f}; MOS15 Blended ${BLEND/1.15:.2f}; MOS15 Emma ${FV0/1.15:.2f}")
print(f"  Fwd P/E @ $656.39 / FY27 EPS consensus $176.50 = {PX/176.50:.2f}x ; @ $692.51 = {692.51/176.50:.2f}x")

# ---------------- proposed new base: no NWC release + Taiwan 5% (FY27+) ----------------
print("\n[NEW BASE CANDIDATE] no release + Taiwan 5%")
NB = dict(nwc_mode='flow', dn_rate=0.0, union=0.05)
nb = model(NB); FVn = nb['fv']
RF = 0.0484; ERP = 0.0441
def solve(f, lo, hi, target=PX, n=80):
    flo = f(lo)-target; fhi = f(hi)-target
    if flo*fhi > 0: return None
    for _ in range(n):
        mid=(lo+hi)/2; fm=f(mid)-target
        if flo*fm<=0: hi=mid
        else: lo=mid; flo=fm
    return (lo+hi)/2
gi = solve(lambda g: fv(dict(NB, r27=REV[26]*(1+g), g28=g)), 0.0, 3.0)
gate = fv(dict(NB, r27=REV[26]*1.66, g28=0.66))
print(f"  FV ${FVn:.2f} | MOS@656.39 {FVn/PX-1:+.1%} | PV(TV)/EV {nb['pvTV']/nb['ev']:.1%} | reverse-DCF implied FY26-28 CAGR {gi:.1%} = {gi/0.55:.2f}x consensus | price at 1.2x gate ${gate:.2f}")
w=WACC; ev5 = sum(nb['fcff'][y]/(1+w)**(y-31-0.5) for y in range(32,37)) + (nb['fade_pv']+nb['pvTV'])*(1+w)**5
nc = BRIDGE
for y in range(27,32): nc = nc*(1+RF*(1-TAX))+nb['fcff'][y]
sh5 = SH*1.015**5; f5 = (ev5+nc)/sh5
print(f"  FV5 ${f5:.2f} (after-tax Rf cash) | exp return/yr @656.39 {(f5/PX)**0.2-1:+.1%}")
bl = 0.4*FVn+0.3*373.35+0.3*307.19
print(f"  Blended (Emma new) = 0.4x{FVn:.2f}+0.3x373.35+0.3x307.19 = ${bl:.2f} | MOS {bl/PX-1:+.1%} | MOS25 trigger ${bl/1.25:.2f} | Emma/1.25 ${FVn/1.25:.2f} | Emma/1.15 ${FVn/1.15:.2f}")
print(f"  Emma new vs Quinn gap {FVn/373.35-1:+.1%}")
for nm,o in [("  + SCA ends FY31", dict(sca_end=31)), ("  + 7y explicit", dict(exp_years=7)), ("  Bear 5% release instead of 0", dict(dn_rate=0.05)),
             ("  Taiwan 2%", dict(union=0.02)), ("  Taiwan 10%", dict(union=0.10)), ("  downturn 1y later", dict(dec29=0.05, dec30=-0.34, M=[1.5,0.9,1.25,1.3,0.95,1.0]))]:
    v = fv(dict(NB, **o)); print(f"  {nm:34s} ${v:.2f} ({v/FVn-1:+.1%})")

# ---------------- coordinator add 2026-11-10: WACC 10.3% row + MOS at 11-09 close $733.58 ----------------
P2 = 733.58
print("\n[ADD] WACC 10.3% (valueinvesting.io via Atlas addendum 11-10)")
line("WACC 10.3% on old base", fv(dict(wacc=0.103)))
vn = fv(dict(NB, wacc=0.103)); print(f"  WACC 10.3% on new base: ${vn:.2f} ({vn/FVn-1:+.1%})")
print(f"[ADD] MOS @ ${P2}: Emma old {FV0/P2-1:+.1%} | Emma new {FVn/P2-1:+.1%} | Blended old {BLEND/P2-1:+.1%} | Blended new {bl/P2-1:+.1%} | Quinn {373.35/P2-1:+.1%} | Bear {307.19/P2-1:+.1%}")
print(f"  FV5 exp return/yr @{P2}: new base {(f5/P2)**0.2-1:+.1%}")
