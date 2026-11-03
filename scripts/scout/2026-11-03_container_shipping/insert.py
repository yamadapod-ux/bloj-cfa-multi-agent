# Round 84: append scout report, prune note, Pending row, deployment_log entry.
import os
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(D, '..', '..', '..')
wl = os.path.join(R, 'portfolio', 'watchlist.md'); dl = os.path.join(R, 'portfolio', 'deployment_log.md')
s = open(wl, encoding='utf8').read()
assert 'Round 84' not in s
anchor = '**Prune Pass 2026-11-02 (Mode 1 Step 0 — Round 83):**'
note = """**Prune Pass 2026-11-03 (Mode 1 Step 0 — Round 84):** I checked all 15 live Pending rows against De-list Rules #1-3. **De-listed 0 · SLA fixed 0.**
- **Rule #1:** no target date has passed yet. **NBIX = 11-03 (today)** must be re-run or archived at the next prune. Remaining dates: CRI 11-06, IBKR/URI/EME/INDI/ANIP/BKSY/VMD/WYNN/VICI/ALLY/BYD 11-07, MMS 11-20, WGO 12-19. The 11-01 warning on IBKR/URI/EME (archive after 11-07 with no Tier 1 re-run) stands.
- **Rule #2/#3:** `dashboard/portfolio.js` OPEN is still ADBE/NOW/CRM/REGN/ADSK (`b9e8815`, 11-02 close re-mark). `decisions.md` has 0 hits for any live ticker. Round 84 adds **CMRE** (learning-queue) → live 16.

"""
assert s.count(anchor) == 1
s = s.replace(anchor, note + anchor, 1)
row = ("| CMRE | Costamare Inc. | Industrials / Marine Shipping — containership owner-lessor on long charters to top liners + Neptune Maritime Leasing platform (Value bucket) | 2026-11-03 (Round 84) | "
       "$13.45 (Nov 2 close; Yahoo + Nasdaq.com exact, mkt cap $1,626M) · 52W $11.92–18.06 (high 2026-04-09) = **−25.5%** | "
       "**17.9% owner FCF** (CFO $446M − D&A $134M − pref div $21M, TTM to Q3 6-K) · reported FCF negative (newbuild advances) · EV/EBITDA 5.7× | "
       "TTM rev −3% ($853M); $6.0B contracted backlog, 5.8y TEU-weighted duration | "
       "ROIC 9.8% TTM (@15% tax; 11.5% pre-tax) · 5Y avg 11.4% vs computed WACC 7.45% / band 10% | "
       "**🟡 LEARNING-QUEUE** — Tier 1 pass. A ✅ cyclical (Q1 miss + Suez-reopening capacity fear) · B-Zero ✅ ND/EBITDA 2.0×, equity +$2.29B · B ✅ · C ✅ · **D ⚠️ straddles** 0.65× (TTM) / **0.84× (15% mid-cycle haircut)** / 1.21× (30%) @7.45%, fails all cells @10% band · E 2/3 (E1 ❌ commodity asset; related-party manager flagged). P/B 0.71×, P/E ≈5×. **Entry $12.00–13.50 · Stop $10.70** — detail: § Scout Report Round 84 | "
       "**LEARNING-QUEUE — Tier 1.5 lightweight (Emma DCF on backlog + NAV/residual-value cross-check, Bear-lite on the 22-newbuild capex + post-2027 re-chartering); target 2026-11-17.** Upgrade: lightweight MOS ≥25%, or Q4 shows no re-charter rate erosion, or price −15% more |\n")
i = s.index('| WGO | Winnebago Industries'); j = s.index('\n', i) + 1
s = s[:j] + row + s[j:]
s = s.rstrip('\n') + '\n' + open(os.path.join(D, 'r84.md'), encoding='utf8').read()
open(wl, 'w', encoding='utf8').write(s)
log = """
## Scout Round 84 — Marine Shipping ex-Tankers (containership lessors/liners, gas carriers/FLNG, shuttle tankers, small-cap dry bulk) — 2026-11-03

| Ticker | Action | Gate / Rationale |
|--------|--------|------------------|
| NVGS | `QUICK-SCREEN SKIP` (Tier 1 check 2a) | Owner FCF (CFO − D&A) TTM $61.8M → naive FV $6.25 vs $20.00 = 3.20× at computed WACC 7.57%. The 5Y-avg actual FCF basis gives 1.38×. The reported TTM FCF basis (0.58×) excludes the vessels-under-construction tag and is not through-cycle. |
| CMRE | LEARNING-QUEUE (`LEARNING-QUEUE`) | Tier 1 pass. A −25.5% cyclical · B owner FCF 17.9% · C ROIC 9.8% ≥ WACC 7.45% · D straddles 0.65/0.84/1.21× (0/15/30% mid-cycle haircut) at computed WACC, fails at the 10% band · E 2/3. No pipeline dispatched; Tier 1.5 target 2026-11-17. |

- **Other rejects** (watchlist only, not Tier-1 skips): GLNG/SHIP at B · KNOP/CMDB/DSX at C · HSHP at D · DLNG/CTRM at E 0/3 · TOPS at A (permanent).
- **Regime:** RISK-ON 3/4 (Atlas 2026-10-27). Scout-only CIO task; no trade.
- **Data:** SEC EDGAR XBRL companyfacts plus 6-K exhibits (CMRE Q3, NVGS/DLNG Q2). Prices from 2 sources (Yahoo + Nasdaq.com, 2026-11-02 close). Full tables: `portfolio/watchlist.md` § Scout Report Round 84.

*Max — 2026-11-03 | Scout Round 84 — 0 fast-track, 1 learning-queue (CMRE), 1 QUICK-SCREEN SKIP; no trade.*
"""
t = open(dl, encoding='utf8').read()
assert 'Round 84' not in t
open(dl, 'w', encoding='utf8').write(t.rstrip('\n') + '\n' + log)
print('ok')
