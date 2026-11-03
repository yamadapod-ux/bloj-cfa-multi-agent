# Scout Round 84 — Marine Shipping ex-tanker (container lessors, gas carriers, shuttle tankers, small dry bulk), 2026-11-03.
# Fundamentals: SEC EDGAR companyfacts (10-K/10-Q). Price: Yahoo chart + Nasdaq.com quote (2 sources). Street PT: stockanalysis.
from hist import *
import json, re, sys, statistics as st, bisect
Rf = float(os.environ.get('RF', '0.0493')); ERP = 0.042
UA2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120'}

def sa(t):
    fn = f'sa_{t}.html'
    if not os.path.exists(fn):
      try:
        open(fn, 'w', encoding='utf8').write(u.urlopen(u.Request(f'https://stockanalysis.com/stocks/{t.lower()}/forecast/', headers=UA2), timeout=30).read().decode('utf8', 'ignore'))
      except Exception: return None
    h = open(fn, encoding='utf8').read()
    tg = re.search(r'targets:\{low:([0-9.]+),high:([0-9.]+),count:(\d+),median:([0-9.]+),average:([0-9.]+),updated:"([0-9-]+)"', h)
    return tg.groups() if tg else None

def nasdaq(t):
    r = u.Request(f'https://api.nasdaq.com/api/quote/{t}/info?assetclass=stocks', headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'})
    d = json.loads(u.urlopen(r, timeout=20).read())['data']
    return float(d['primaryData']['lastSalePrice'].strip('$').replace(',', '')), d['primaryData']['lastTradeTimestamp'], d['keyStats']['fiftyTwoWeekHighLow']['value']

def beta(t):
    a = ych(t, '5y', '1mo'); b = ych('^GSPC', '5y', '1mo')
    A = dict(zip(a['timestamp'], a['indicators']['adjclose'][0]['adjclose'])); B = dict(zip(b['timestamp'], b['indicators']['adjclose'][0]['adjclose']))
    k = [x for x in sorted(A) if x in B and A[x] and B[x]]
    ra = [A[k[i]] / A[k[i-1]] - 1 for i in range(1, len(k))]; rb = [B[k[i]] / B[k[i-1]] - 1 for i in range(1, len(k))]
    ma, mb = st.mean(ra), st.mean(rb)
    return sum((x-ma)*(y-mb) for x, y in zip(ra, rb)) / (len(ra)-1) / st.variance(rb)

SBC = ['ShareBasedCompensation', 'AllocatedShareBasedCompensationExpense']
INTX = ['InterestExpense', 'InterestExpenseNonoperating', 'InterestExpenseDebt']
def ttm2(f, c, e):
    if c is OPI:
        v = _ttm2(f, OPI, e)
        if v is not None: return v
        p = _ttm2(f, PTI + ['IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic'], e); i = _ttm2(f, INTX, e) or 0
        return p + i if p is not None else None
    return _ttm2(f, c, e)
def _ttm2(f, c, e):
    v = ttm_at(f, c, e)
    if v is not None: return v
    s = [x for x in series(f, c) if x.get('start') and 350 <= dur(x) <= 380 and x['end'] <= e]
    return max(s, key=lambda x: x['end'])['val'] if s else None
def fy(f, c, end):
    s = [x for x in series(f, c) if x.get('start') and 350 <= dur(x) <= 380 and x['end'] == end]
    return s[0]['val'] if s else None
def roic_at(f, e, annual=False):
    g = (lambda c: fy(f, c, e)) if annual else (lambda c: ttm2(f, c, e))
    oi = g(OPI)
    if oi is None and annual:
        p = fy(f, PTI, e); oi = p + (fy(f, INTX, e) or 0) if p is not None else None
    tx = g(TAX); pti = g(PTI)
    if oi is None: return None, None
    tax = min(max(tx/pti, 0.15), 0.27) if (pti and tx is not None and pti > 0) else 0.21
    eq = inst1(f, EQ, e) or 0; ic = eq + debt(f, e) - mkt(f, e)
    return (oi*(1-tax)/ic if ic > 0 else float('nan')), tax

out = {}
for t in sys.argv[1:]:
    try:
        f = facts(t); rows, sp = run(t); e = rows[-1][0]
        y = ych(t, '1y', '1d'); q = y['indicators']['quote'][0]
        price = y['meta']['regularMarketPrice']; hi = max(x for x in q['high'] if x)
        try: np_, nts, rng = nasdaq(t)
        except Exception as ex: np_, nts, rng = None, None, repr(ex)
        nhi = float(rng.split('-')[1].strip().strip('$').replace(',', '')) if np_ else None
        sh = shares(f, e, sp); nd = debt(f, e) - mkt(f, e); r = ttm_at(f, REV, e)
        rpy = ttm_at(f, REV, rows[-5][0]) if len(rows) >= 5 else None
        oi = ttm2(f, OPI, e); da = ttm2(f, DA, e) or 0; ebitda = oi + da
        cfo = ttm2(f, CFO, e); cx = ttm2(f, CAPEX, e) or 0; sbc = ttm2(f, SBC, e) or 0
        eq = inst1(f, EQ, e)
        ro, tax = roic_at(f, e)
        fys = sorted({x['end'] for x in series(f, REV) if x.get('start') and 350 <= dur(x) <= 380})[-5:]
        rh = [roic_at(f, d, True)[0] for d in fys]
        fcfh = [(fy(f, CFO, d) or 0) - (fy(f, CAPEX, d) or 0) for d in fys]
        sbch = [fy(f, SBC, d) or 0 for d in fys]
        b = beta(t); bb = 0.67*b + 0.33; E_ = price*sh; D_ = debt(f, e)
        ke = Rf + bb*ERP; kd = (Rf + 0.008)*0.79; wacc = (E_*ke + D_*kd)/(E_ + D_)
        # EV/EBITDA history at each quarter-end (5Y)
        evh = []
        for (d, p, s_, rv, n, m) in rows:
            if d < '2021-10-01': continue
            o_ = ttm2(f, OPI, d); a_ = ttm2(f, DA, d)
            if o_ and a_ and o_ + a_ > 0: evh.append((p*s_ + n)/(o_ + a_))
        ev = E_ + nd; evx = ev/ebitda if ebitda > 0 else float('nan')
        pct = 100*sum(1 for v in evh if v <= evx)/len(evh) if evh else None
        evr_h = sorted(m for (d, p, s_, rv, n, m) in rows if d >= '2021-10-01'); evr = ev/r
        evr_pct = 100*sum(1 for v in evr_h if v <= evr)/len(evr_h)
        nfcf = st.mean(fcfh) if fcfh else float('nan'); nfcf_sbc = st.mean([a - s for a, s in zip(fcfh, sbch)] or [float('nan')])
        naive = (nfcf/wacc - nd)/sh; naive_sbc = (nfcf_sbc/wacc - nd)/sh; naive_ttm = ((cfo - cx)/wacc - nd)/sh
        o = dict(t=t, end=e, price=price, hi=hi, off=price/hi - 1, np=np_, nts=nts, nrng=rng, noff=(np_/nhi - 1) if np_ else None,
                 sh=sh, nd=nd, eq=eq, rev=r, yoy=(r/rpy - 1) if rpy else None, oi=oi, ebitda=ebitda, nd_ebitda=nd/ebitda if ebitda > 0 else None,
                 cfo=cfo, capex=cx, sbc=sbc, fcf=cfo - cx, fcfy=(cfo - cx)/E_, fcfy_sbc=(cfo - cx - sbc)/E_, fys=fys, fcfh=fcfh, sbch=sbch,
                 roic=ro, tax=tax, roic_hist=rh, roic5=st.mean([x for x in rh if x == x and x is not None] or [float('nan')]) if rh else None,
                 beta=b, bb=bb, ke=ke, wacc=wacc, evx=evx, evx_pct=pct, evx_min=min(evh) if evh else None, evx_med=st.median(evh) if evh else None, evx_max=max(evh) if evh else None,
                 evr=evr, evr_pct=evr_pct, nfcf=nfcf, nfcf_sbc=nfcf_sbc, naive=naive, naive_sbc=naive_sbc, naive_ttm=naive_ttm,
                 pfv=price/naive if naive > 0 else None, pfv_sbc=price/naive_sbc if naive_sbc > 0 else None, pt=sa(t), mcap=E_)
        out[t] = o
        print(f"{t:5} {e} px {price:8.2f} hi {hi:8.2f} off {100*o['off']:6.1f}% | nasdaq {np_} rng {rng} off {100*(o['noff'] or 0):6.1f}%")
        try:
            print(f"      rev {r/1e9:6.2f}B yoy {100*(o['yoy'] or 0):5.1f}% EBITDA {ebitda/1e9:5.2f}B ND/EBITDA {o['nd_ebitda'] or 0:4.2f}x EQ {(eq or 0)/1e9:6.1f}B | FCF {o['fcf']/1e9:5.2f}B yld {100*o['fcfy']:4.1f}% (ex-SBC {100*o['fcfy_sbc']:4.1f}%) EV/EBITDA {evx:5.1f}x pct {pct:.0f} [{o['evx_min']:.1f}/{o['evx_med']:.1f}/{o['evx_max']:.1f}]")
            print(f"      ROIC {100*ro:5.1f}% FY {[round(100*x,1) if x==x and x is not None else None for x in rh]} 5Yavg {100*o['roic5']:.1f}% | beta {b:.2f}->{bb:.2f} WACC {100*wacc:.2f}% | normFCF {nfcf/1e9:.2f}B naive {naive:.2f} P/FV {o['pfv']} | exSBC naive {naive_sbc:.2f} | TTM naive {naive_ttm:.2f} | PT {o['pt']}")
        except Exception: print('      (fmt skipped)', {k: o[k] for k in ['rev','yoy','ebitda','nd_ebitda','eq','fcf','fcfy','evx','evx_pct','roic','roic_hist','wacc','naive','naive_ttm','pfv','pt']})
    except Exception as ex:
        import traceback; print(t, 'ERR', repr(ex)); traceback.print_exc(limit=2)
json.dump(out, open('screen_out.json', 'w'), default=str)
