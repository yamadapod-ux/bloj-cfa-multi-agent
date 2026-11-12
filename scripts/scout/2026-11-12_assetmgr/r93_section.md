
## Scout Report § Round 93 (Asset Managers / Trust Banks / Capital Markets non-bank) — 2026-11-12

**Sector mandate:** Traditional asset managers (TROW, IVZ, BEN) · custody/trust banks (STT, NTRS) · wealth + asset management (AMP) · independent advisory/asset management (LAZ, which replaces BLK) · **supplementary** independent advisory boutiques (EVR, PJT, HLI) and brokers/investment banks (RJF, SF), all from the CIO's suggested substitute list. Previous rounds: R90 Memory/Storage · R91 Airlines · R92 Leisure.
**Coverage check:** I ran `grep -w` across `watchlist.md`, `decisions.md` and `dashboard/portfolio.js` before any price fetch.
- **BLK** was already scanned with 2-source verified prices in **R42** (2026-09-25/26, Financials sweep). It was cut at Filter A (−10.96%). Per the CIO's instruction it is **dropped from this round** and replaced by **LAZ** (same sub-sector: Lazard Asset Management is about half of revenue).
- **TROW / IVZ / BEN** appeared only in R77's "Single-source finviz pre-screen fails (70 — not counted as verified)" list. R81 then dropped them from its universe as a precaution against false positives, so they have **never been through Filter A–E with verified prices.** They are screened in full this round.
- **VRTS** was scanned in full in R81 (E 0/3 REJECT), so it was not used as a substitute.
- **STT / NTRS / AMP / LAZ / EVR / PJT / HLI / RJF / SF** have 0 hits in all 3 files.

**Trigger:** CIO ordered a new-sector Scout Round (2026-11-12). **Scout/screen only. No full pipeline was dispatched, and Atlas/Emma/Quinn/Bear were not called.**
**Hard exclusions:** none of PODD/ZTS/NKE/MMS/SLM/CRI/NBIX/BYD/WGO/OWL is in the universe. No overlap with holdings (ADBE/NOW/CRM/REGN/ADSK).
**Portfolio state:** 5 OPEN (ADBE / NOW / CRM / REGN / ADSK) per `dashboard/portfolio.js` (re-mark `0a14682`, close 11-11).
**Regime:** **TRANSITIONAL-CAUTIOUS** (`agent_notes/atlas/2026-11-06_regime.md`, 6 days old, not stale). Force Deploy is suspended and new positions are not allowed, so any survivor would only become a buy-list candidate.
**Data sources:**
- **Prices + 52W high:** close 2026-11-11 from the **Yahoo chart API** (`px.py` → `data/px.json`, `px2.json`), cross-checked with **stockanalysis.com** quote page + 52-Week Range for **all 12 tickers** ([LAZ](https://stockanalysis.com/stocks/laz/) · [TROW](https://stockanalysis.com/stocks/trow/) · [IVZ](https://stockanalysis.com/stocks/ivz/) · [BEN](https://stockanalysis.com/stocks/ben/) · [STT](https://stockanalysis.com/stocks/stt/) · [NTRS](https://stockanalysis.com/stocks/ntrs/) · [AMP](https://stockanalysis.com/stocks/amp/) · [EVR](https://stockanalysis.com/stocks/evr/) · [PJT](https://stockanalysis.com/stocks/pjt/) · [HLI](https://stockanalysis.com/stocks/hli/) · [RJF](https://stockanalysis.com/stocks/rjf/) · [SF](https://stockanalysis.com/stocks/sf/)). **Price and 52W high match exactly for every ticker (Δ 0%).**
- **Financial statements:** **SEC EDGAR companyfacts** (`sec.py`, `sec2.py` → `data/sec*.json`; 10-Q for the period ending 2026-09-30; HLI's fiscal year ends in March, so TTM = 6M FY27 + FY26 − 6M FY26). OCF was cross-checked against the [stockanalysis cash-flow page](https://stockanalysis.com/stocks/evr/financials/cash-flow-statement/) (swap the ticker in the URL) and **matches for all 4 Filter-A survivors**.
- All calculations are in `scripts/scout/2026-11-12_assetmgr/calc.py`.

**WACC:** scout-level proxy by size and beta (Filter D) is 10% for EVR/PJT/HLI and 11% for LAZ (higher beta + leverage). **This is not VS2 §1.1.** I also tested WACC −2pp and no result flips.
**FCF definition (important for this sector):** FCF = OCF − capex − **SBC**. Advisory firms pay 15–20% of revenue in stock (EVR SBC TTM $779M = 16% of revenue). Reported FCF adds SBC back, so it is overstated. This follows the DCF Cash Flow Consistency Rule (SBC > 10% of revenue). Reported FCF is shown alongside as an **upper bound that does not comply with the rule**.

### Step 0 — Prune
🗄️ Prune: de-listed **0** | SLA fixed **0** | live **9** (WYNN / VICI / ALLY / MMS / CRI / NBIX / BYD / WGO / CMRE)
- **Rule #1:** no target date has passed. ⚠️ **CRI target is 11-12 = today.** WYNN/VICI/ALLY/NBIX/BYD 11-14 · CMRE 11-17 · MMS 11-20 · WGO 12-19. ⚠️ **WYNN/VICI hit 60 days on 11-19** (repeated from R91/R92).
- **Rule #2 (close 11-11, Yahoo = stockanalysis):** WYNN $85.38 · VICI $24.94 · ALLY $38.27 · MMS $65.38 · CRI $34.60 · NBIX $174.41 · BYD $77.50 · WGO $31.53 · CMRE $12.98. None is more than 2× the top of its zone (highest is NBIX at 1.29× of $135), and none has a formal MOS below −30%.
  - ⚠️ **NBIX has recovered to −6.3% from its $186.12 high** (it was −9.1% in R92). It would not pass Filter A if screened today.
  - **BYD is −15.2%.** Both are flagged for Charlie's Tier 1 review on 11-14.
  - **ALLY is $38.27**, just above the top of its entry zone ($34–38).
- **Rule #3:** `decisions.md` has 0 hits for every live ticker. No change to OPEN positions.

### Filter A — down ≥20% from 52W high (close 2026-11-11)
| Ticker | Sub-industry | Price (Yahoo / SA) | 52W high (Yahoo / SA) | % from high | Result |
|---|---|---|---|---|---|
| TROW | Active asset manager | $110.69 / $110.69 | $122.00 (07-28) / $122.00 | −9.3% | ❌ |
| IVZ | Asset manager (ETF + active) | $28.63 / $28.63 | $33.66 (08-28) / $33.66 | −14.9% | ❌ |
| BEN | Asset manager (Franklin Templeton) | $36.30 / $36.30 | $36.79 (11-10) / $36.79 | −1.3% | ❌ (near ATH) |
| STT | Custody / trust bank | $174.17 / $174.17 | $195.93 (08-27) / $195.93 | −11.1% | ❌ |
| NTRS | Custody / trust bank + wealth | $178.71 / $178.71 | $195.78 (08-13) / $195.78 | −8.7% | ❌ |
| AMP | Wealth mgmt + asset mgmt (Columbia Threadneedle) | $520.06 / $520.06 | $572.56 (08-14) / $572.56 | −9.2% | ❌ |
| **LAZ** | Advisory + asset management | $41.90 / $41.90 | $58.75 (02-10) / $58.75 | **−28.7%** | ✅ |
| **EVR** *(supp.)* | Independent advisory boutique | $298.08 / $298.08 | $388.71 (01-16) / $388.71 | **−23.3%** | ✅ |
| **PJT** *(supp.)* | Independent advisory (restructuring + strategic) | $152.94 / $152.94 | $195.62 (01-22) / $195.62 | **−21.8%** | ✅ |
| **HLI** *(supp.)* | Independent advisory (mid-market + restructuring) | $146.17 / $146.17 | $195.06 (01-21) / $195.06 | **−25.1%** | ✅ |
| RJF *(supp.)* | Wealth mgmt / broker-dealer | $167.13 / $167.13 | $182.73 (08-06) / $182.73 | −8.5% | ❌ |
| SF *(supp.)* | Broker-dealer / investment bank | $73.02 / $73.02 | $89.83 (01-05) / $89.83 | −18.7% | ❌ (1.3pp short) |

**Filter A: 1/7 from the main list (LAZ) + 3/5 supplementary (EVR/PJT/HLI).** The 7 names the CIO named (asset managers, trust banks, AMP) are all within 15% of their highs except LAZ. **BEN is right at its ATH.** Same picture as R42: AUM-driven financials rise with the market.

### Beaten-down reason (Filter A survivors)
| Ticker | Reason | Classification |
|---|---|---|
| LAZ | Net-margin compression all year: Q3 2026 adj. EPS $0.36 with a 69.9% adj. comp ratio, plus higher tax (Earnings Whispers calls it a miss despite record Financial Advisory revenue). Q2 net income −91% and an 80-role cut. Trefis: −22.9% from 5/31 to 9/17 driven by net margin ([Lazard Q3 PR](https://lazard.com/news-announcements/lazard-reports-third-quarter-and-nine-month-2026-results/), [Earnings Whispers](https://www.earningswhispers.com/epsdetails/LAZ/202609), [Webull](https://www.webull.com/news/15284607506211840), [Trefis](https://www.trefis.com/data/companies/laz)) | ✅ **mostly cyclical/temporary.** The comp ratio is high because of the hiring cycle, and advisory revenue is at a record. ⚠️ Asset management flows are weak (secular active→passive), which is the structural part. |
| EVR | Fell from its January 2026 high in the February market sell-off with no single event. TTM revenue $4.87B vs FY25 $3.88B, a record year (SEC) | ✅ sentiment/cyclical ("peak-cycle" multiple derating) |
| PJT | Fell 9 days in a row in September (−19%, ~$928M of market cap); Q4 2025 revenue miss; UBS PT cut $180→$151 ([Trefis](https://www.trefis.com/articles/615814/9-red-days-in-a-row-pjt-partners-stock-is-down-19/2026-09-18), [RTTNews](https://www.rttnews.com/3616832/pjt-partners-stock-drops-9-after-record-2025-results-mixed-with-revenue-miss.aspx)) | ✅ sentiment (restructuring demand may fade as credit improves; that is cyclical) |
| HLI | Zacks: "down 21% YTD." 1H FY27 revenue $1,203M vs $1,265M a year earlier (−4.9%, SEC) ([Zacks](https://www.zacks.com/stock/news/2985933/houlihan-lokey-down-21-ytd:-buy-the-dip-or-stay-cautious)) | ✅ cyclical (mid-market M&A/restructuring timing) |

### Filter B-Zero — Balance sheet (SEC 10-Q 2026-09-30, $M)
| Ticker | Equity (parent / incl. NCI) | Funded debt | Cash | Net debt | Result |
|---|---|---|---|---|---|
| LAZ | +$949 / +$940 | $1,690 (LongTermDebt — senior notes) | $1,264 | $426 · ND/(EBIT+D&A TTM $301M) ≈ 1.4× | ✅ clean |
| EVR | +$1,943 / +$2,281 | n/m — no recent senior-notes XBRL tag; SA total debt $1.22B ≈ cash, most of it lease (EV ≈ mcap) | $1,226 | ≈ 0 (counted as net cash $1,226M in D, **generous to FV**) | ✅ |
| PJT | +$365 / +$1,053 (Up-C: NCI = partnership units) | none (SA debt $429M = lease) | $257 | net cash | ✅ (equity is small because of the Up-C structure, not because of losses) |
| HLI | +$2,307 | none (SA debt $494M = lease) | $837 | net cash | ✅ |

### Bucket
All survivors are in the **Value bucket** (B-Legacy / D-Legacy). Revenue growth (TTM vs latest fiscal year): EVR +25.6% is the only name above 15%, but that is a cyclical rebound, not a reinvestment phase (capex/revenue 0.9%), so B-V1 does not apply. LAZ +6% · PJT +6.5% · HLI −2.4%. None qualifies for the AI/Infra lane.

### Filter B + C (SEC, $M)
| Ticker | Reported FCF TTM (yield) | **FCF − SBC TTM** (yield) | FCF − SBC 5Y avg (yield) | ROIC TTM (EBIT×0.75 ÷ equity incl. NCI + funded debt − cash) · SA | WACC | B | C |
|---|---|---|---|---|---|---|---|
| LAZ | $685 (16.7%; SA 16.74% ✓) | $325 (**7.9%**) — SBC = FY25 $359.7M (proxy; 9M not filed) | $314 (7.7%) | **14.6%** (5Y avg EBIT 20.6%) · SA 7.1% (total debt incl. lease, no cash netting) | 11% | ✅ | ✅ (133% of WACC; SA basis 65% — see note) |
| EVR | $1,725 (14.7%; SA ✓) | $946 (**8.1%**) | $359 (3.1%) | **34.1%** (pretax as EBIT proxy) · SA 25.3% | 10% | ✅ (TTM) / ❌ (5Y) | ✅ |
| PJT | $688 (11.1%; SA ✓) | $447 (**7.2%**) | $181 (2.9%) | **26.7%** · SA 22.6% | 10% | ✅ (TTM) / ❌ (5Y) | ✅ |
| HLI | $402 (4.0%; SA 3.96% ✓) | $202 (2.0%) · FY26 $481 (4.7%) | $356 (3.5%) | **16.8%** · SA 14.8% | 10% | ❌ | ✅ |

**Note on LAZ ROIC:** SA's 7.1% puts total debt including leases ($2.30B) in IC without netting cash $1,264M. Since lease cost is already deducted in EBIT, I used funded debt net of cash. Both bases sit on either side of 80% of WACC, but the result does not flip because LAZ fails at D anyway.
**HLI fails B** on every basis (FCF yield 2.0–4.7%; P/B 4.4× is not an advisory-firm metric). It is still run through the D table below for calibration.

### Filter D + Tier 1 Quick-Screen
Naive FV = normalized (FCF − SBC) ÷ WACC − net debt (or + net cash), divided by stockanalysis shares (LAZ 97.66M · EVR 39.38M · PJT 40.46M incl. units · HLI 69.42M).

| Ticker | Naive FV 5Y (FCF−SBC) | **P / FV** | TTM (FCF−SBC) | NI 5Y avg | WACC −2pp | Reported FCF TTM (upper bound, not rule-compliant) | Result |
|---|---|---|---|---|---|---|---|
| **LAZ** | $24.85 | **1.69×** | $25.92 → 1.62× | $21.99 → 1.91× | $31.35 → 1.34× | ($685/11% − $426)/97.66 = $59.4 → 0.71× | Tier 1 **check 2a: >1.5× → `QUICK-SCREEN SKIP`** |
| **EVR** | $122.25 | **2.44×** | $271.36 → 1.10× | $170.48 → 1.75× | $145.03 → 2.06× | $469 → 0.64× | Tier 1 **check 2a → `QUICK-SCREEN SKIP`** — even on TTM at the cycle peak it is 1.10× (>0.90×) |
| **PJT** | $51.16 | **2.99×** | $116.79 → 1.31× | $58.20 → 2.63× | $62.36 → 2.45× | $176 → 0.87× | Tier 1 **check 2a → `QUICK-SCREEN SKIP`** |
| HLI | $63.36 | 2.31× | $41.23 → 3.55× | $63.85 → 2.29× | $76.19 → 1.92× | $70.0 → 2.09× | already failed B (rejected at B) |

- **Street PT cross-check (LAZ):** consensus is about $45–55 (MarketBeat range $45–52 from April, SA $55.38 in February, Options Analysis $48.50; no snapshot from November) = **+7% to +32%**, but the sources disagree and are stale ([MarketBeat](https://www.marketbeat.com/stocks/NYSE/LAZ/price-target), [stockanalysis forecast](https://stockanalysis.com/stocks/laz/forecast/), [Benzinga](https://www.benzinga.com/quote/LAZ/analyst-ratings)). The no-growth naive FV ($25) sits far below the Street, so the naive FV is the deciding basis per D-Legacy.
- **Why "reported FCF" makes LAZ/EVR look cheap:** it adds back SBC of $360–779M a year. That is real compensation paid in shares, offset by buybacks (LAZ buyback + dividends TTM $327M). Using it would break the DCF Cash Flow Consistency Rule §2.
- **Check 3 (red-flag search):** not run. It is enrichment, not a gate, and all 3 names already failed on arithmetic.
- **Filter E:** not assessed (no name passed D). A rough note: EVR/PJT would likely pass E1 (brand/relationship moat) + E2 (ROIC 25–34% >> 10%) + E3 → **they are high-quality businesses but have no MOS on a no-growth basis.**

### Final routing — Round 93
| Ticker | Failed at | Tag |
|---|---|---|
| TROW, IVZ, BEN, STT, NTRS, AMP | A (−1.3% to −14.9%) | reject |
| RJF, SF *(supp.)* | A (−8.5% / −18.7%) | reject |
| HLI *(supp.)* | B (FCF−SBC 2.0% TTM / 3.5% 5Y) | reject |
| LAZ | Tier 1 check 2a (1.69× naive FV; 1.34× even at WACC −2pp) | `QUICK-SCREEN SKIP` |
| EVR *(supp.)* | Tier 1 check 2a (2.44× naive FV; TTM 1.10×) | `QUICK-SCREEN SKIP` |
| PJT *(supp.)* | Tier 1 check 2a (2.99× naive FV; TTM 1.31×) | `QUICK-SCREEN SKIP` |

**0 fast-track · 0 learning-queue · 12 reject (8 A · 1 B · 3 `QUICK-SCREEN SKIP`: LAZ / EVR / PJT).** No row added to Pending Analysis, nothing added to `buy_list.md`. Tags recorded in `deployment_log.md`.

### Notes for CIO / Charlie
1. **Asset managers and trust banks are not beaten down.** All 7 names in the CIO's list except LAZ are within 15% of their highs, and BEN is at its ATH. AUM-driven revenue rides the market up, so this sub-sector is unlikely to pass Filter A while the S&P stays near its high. It should only be re-scanned after the market corrects ≥15%.
2. **Advisory boutiques (EVR/PJT/HLI/LAZ) are the part of financials that has pulled back** (−22% to −29% since January), but the decline is a multiple derate from peak-cycle earnings, not undervaluation. Normalized FCF after SBC is only about 1/3 to 1/2 of reported FCF.
3. **Lesson repeated from PLNT (R92) and the SaaS cases:** reported FCF yield of 11–17% looks very cheap, but in a high-SBC business it misleads. FCF − SBC has to be used from the scout stage (DCF Cash Flow Consistency Rule).
4. **The closest name is LAZ** (1.34× even at WACC 9%). On a no-growth basis it would need to fall to about $20 (≤0.80× of $24.85), which is −52% from here. That is far away.
5. **SF** missed Filter A by 1.3pp → it can be re-screened if it falls below $71.86 (−20%).

**Target analysis date:** none (0 candidates)

*Max — 2026-11-12 | Scout Round 93 (Asset Managers / Trust Banks / Capital Markets non-bank — 12 screened [TROW/IVZ/BEN/STT/NTRS/AMP/LAZ + supp. EVR/PJT/HLI/RJF/SF], 0 fast-track / 0 learning-queue / 12 reject [8 A · 1 B · 3 QUICK-SCREEN SKIP LAZ/EVR/PJT]; BLK excluded (R42 verified scan) → replaced by LAZ; TROW/IVZ/BEN first verified scan (R77 single-source only))*
