# Quinn -- arithmetic verification of Bear's hand-calculated ADBE DCF (2026-11-10)
# Source of assumptions: agent_notes/bear/2026-05-09_ADBE.md § "Re-Analysis Update -- 2026-11-08 (VS2, Full)" §1.1-1.4, §6, §7
# NO assumption changed. Locked (Atlas 2026-11-08): WACC 10.10%, FV/sh = EV/391.5 - 1.85 (net debt $724M), tax 22.6%, 10y explicit.
# Run: python -I bear_verify.py
WACC, TAX, SH, ND0, PRICE = 0.1010, 0.226, 391.5, 724.0, 239.30
REV26 = 26601.0
S = {  # g FY27..FY36, GAAP EBIT margin FY27..FY36, RONIC explicit, terminal RONIC, TGR, prob, Bear FV, Bear FV5
 'S1': dict(g=[9.5,9.0,8.5,8.0,7.5,6.5,5.5,4.5,3.75,3.0], m=[35.0,35.5]+[36.0]*8, r=0.50, rt=0.25, tgr=0.030, p=0.25, bear=318.70, bear5=508.74),
 'S2': dict(g=[7.0,6.0,5.5,5.0,4.5,4.0,3.75,3.5,3.25,3.0], m=[34.0]*10, r=0.35, rt=0.15, tgr=0.025, p=0.40, bear=240.45, bear5=380.27),
 'S3': dict(g=[5.0,3.5,3.0,2.5,2.5]+[2.0]*5, m=[33.5,32.5,31.5,30.5]+[30.0]*6, r=0.15, rt=WACC, tgr=0.020, p=0.25, bear=173.53, bear5=271.75),
 'S4': dict(g=[2.0,0,-1,-1,0]+[1.0]*5, m=[33,31,29,28]+[27.0]*6, r=WACC, rt=WACC, tgr=0.010, p=0.10, bear=145.15, bear5=222.15),
}
# Emma reinvestment style (emma_dcf.py): capex 0.85%->1.2% rev, D&A 2.95%->2.0% rev (ramp 5y), M&A 2.0% rev
def ramp(a, b, i, n=5): return b if i >= n-1 else a + (b-a)*i/(n-1)

def run(s, emma_reinv=False, emma_years=10):
    g = [x/100 for x in s['g']]; m = [x/100 for x in s['m']]
    rev, rows, pv = REV26, [], 0.0
    for i in range(10):
        rev *= 1 + g[i]; nopat = rev*m[i]*(1-TAX)
        if i < 9:
            gn = g[i+1]; rate = 0.0 if gn <= 0 else gn/s['r']   # reinvest 0 when g<=0 (S4 rule)
        else:
            rate = s['tgr']/s['rt']                            # year 10 = TGR / terminal RONIC
        reinv = nopat*rate
        if emma_reinv and i < emma_years:
            reinv = rev*(ramp(0.0085,0.012,i) - ramp(0.0295,0.020,i) + 0.020)
        fcff = nopat - reinv; df = (1+WACC)**(i+1); pv += fcff/df
        rows.append(dict(yr=2027+i, rev=rev, nopat=nopat, reinv=reinv, fcff=fcff, pv=fcff/df))
    n11 = rows[-1]['nopat']*(1+s['tgr'])
    tv = n11*(1 - s['tgr']/s['rt'])/(WACC - s['tgr'])
    pvtv = tv/(1+WACC)**10; ev = pv + pvtv
    return dict(rows=rows, pv=pv, tv=tv, pvtv=pvtv, ev=ev, fv=ev/SH - ND0/SH)

def fv5(s, d):
    ev, nd, sh, bbs = d['ev'], ND0, SH, []
    for t in range(5):
        f = d['rows'][t]['fcff']; ev = ev*(1+WACC) - f
        intr = max(nd, 0)*0.0387                     # after-tax interest on positive net debt only
        pre = nd - f + intr                          # FCFF retained as cash, no interest income
        bb = 0.032*(ev - pre)                        # 3.2% of shares bought at intrinsic value
        nd = pre + bb; sh *= 0.968; bbs.append(bb)
    eq5 = ev - nd
    eq0 = d['ev'] - ND0
    cons = (eq5 + sum(b*(1+WACC)**(4-t) for t, b in enumerate(bbs))) / (eq0*(1+WACC)**5) - 1
    return dict(ev5=ev, nd5=nd, sh5=sh, fv5=eq5/sh, bb=bbs, cons=cons)

if __name__ == '__main__':
    pw = pw5 = 0
    print("Scen  SumPVexp   TV      PV(TV)   EV       FV      Bear     diff%  | EV5     ND5     FV5     Bear5   diff%  cons")
    for k, s in S.items():
        d = run(s); f = fv5(s, d); pw += s['p']*d['fv']; pw5 += s['p']*f['fv5']
        print(f"{k}  {d['pv']:8.0f} {d['tv']:8.0f} {d['pvtv']:8.0f} {d['ev']:8.0f} {d['fv']:7.2f} {s['bear']:7.2f} {(d['fv']/s['bear']-1)*100:+6.2f} | "
              f"{f['ev5']:7.0f} {f['nd5']:7.0f} {f['fv5']:7.2f} {s['bear5']:7.2f} {(f['fv5']/s['bear5']-1)*100:+6.2f} {f['cons']*100:+5.1f}%")
        if k == 'S2':
            print("   S2 rows:", [(r['yr'], round(r['nopat']), round(r['fcff']), round(r['pv'])) for r in d['rows']])
            print("   S2 buybacks:", [round(b) for b in f['bb']], "shares5", round(f['sh5'],2))
        if k == 'S3':
            print("   S3 reinv FY27-31:", [round(r['reinv']) for r in d['rows'][:5]], "NOPAT31", round(d['rows'][4]['nopat']))
        print(f"   FY27 rev {d['rows'][0]['rev']:.0f}  FY31 NOPAT {d['rows'][4]['nopat']:.0f}  PV(TV)/EV {d['pvtv']/d['ev']*100:.1f}%")
    print(f"\nP-W FV ${pw:.2f} (Bear 233.75, {(pw/233.75-1)*100:+.2f}%) | MOS FV/P-1 {(pw/PRICE-1)*100:+.2f}%")
    print(f"P-W FV5 ${pw5:.2f} (Bear 369.45, {(pw5/369.45-1)*100:+.2f}%) | exp return {((pw5/PRICE)**0.2-1)*100:.2f}%/yr")
    print(f"Blended 0.4*308.39+0.3*297.22+0.3*PW = ${0.4*308.39+0.3*297.22+0.3*pw:.2f}")
    # Sensitivity M1: Emma-style reinvestment in S2
    b = run(S['S2'])['fv']
    for yrs, lab in ((10, 'FY27-36 all'), (9, 'FY27-35 (FY36 keep TGR/RONIC)')):
        e = run(S['S2'], emma_reinv=True, emma_years=yrs)['fv']
        print(f"M1 Emma reinv in S2 [{lab}]: S2 ${e:.2f} (+${e-b:.2f}/sh) -> P-W +${0.4*(e-b):.2f}")
    # Sensitivity: probability S1 +/-10pp swapped with S3
    fv = {k: run(s)['fv'] for k, s in S.items()}
    for d1 in (-0.10, 0.10):
        p = {'S1':0.25+d1,'S2':0.40,'S3':0.25-d1,'S4':0.10}
        print(f"Prob S1 {p['S1']:.2f}/S3 {p['S3']:.2f}: ${sum(p[k]*fv[k] for k in fv):.2f}")
    for lab, p in (('Binary bear 10/35/45/10', [.10,.35,.45,.10]), ('Binary bull 45/40/10/5', [.45,.40,.10,.05])):
        print(f"{lab}: ${sum(pp*fv[k] for pp, k in zip(p, fv)):.2f}")
    # margin +/-1pp every scenario
    for dm in (-1, 1):
        t = sum(s['p']*run(dict(s, m=[x+dm for x in s['m']]))['fv'] for s in S.values())
        print(f"Margin {dm:+d}pp all scenarios: P-W ${t:.2f}")
