# Independent Audit — Scout Commit `bc34425` (Logistics / Trucking / Rail Equipment, 2026-10-28)

**Auditor:** Morgan (independent; did not author the scout) · **Date:** 2026-10-28
**Scope:** `portfolio/watchlist.md` diff in `bc34425` (Prune Pass 2026-10-28 + Scout History entry, +98 lines)
**Method:** ดึงข้อมูลเองจาก primary source ทั้งหมด ไม่อ่านตัวเลขจาก scout
- SEC EDGAR XBRL companyfacts `data.sec.gov/api/xbrl/companyfacts/CIK##########.json` — JBHT (0000728535), KNX (0001492691), WERN (0000793074), TRN (0000099780), ODFL (0000878927), pulled 2026-10-28
- SEC EDGAR filings (ดึงเองและแปลงเป็น text):
  - KNX 8-K `0001492691-26-000065` Ex-99.1 (`exhibit99109302026.htm`)
  - WERN 8-K `0000793074-26-000165` Ex-99.1 (`wern-2026x930xex991.htm`)
  - TRN 10-Q Q2'26 `0000099780-26-000119` (`trn-20260630.htm`)
  - TRN 8-K `0000099780-26-000117` Ex-99.1 (`exh991pressrelease6302026.htm`)
  - submissions JSON ของทั้ง 3 ตัว
- **Prices:**
  - Source 1: Yahoo chart API `query1.finance.yahoo.com/v8/finance/chart/{T}`
  - Source 2: stockanalysis.com `/stocks/{t}/` + `/statistics/`
  - finviz บล็อก curl จึงไม่ได้ใช้

**Spot-check sample (4 ตัว + การแก้ TRN):**
- **JBHT** — ผ่าน C
- **KNX** — ตก C (verdict แนว improving)
- **WERN** — Tier-1 SKIP
- **TRN** — ตก C พร้อม correction เรื่อง gain

---

## 1. ผลตรวจรายจุด

| # | จุดที่ตรวจ | Scout อ้าง | Auditor verify (source) | ผล | Severity |
|---|---|---|---|---|---|
| 1 | JBHT TTM EBIT | 960 | FY25 865.069 − 9M'25 618.612 + 9M'26 713.593 = **960.05** (XBRL OperatingIncomeLoss, 10-Q filed 2026-10-23) | ✅ | — |
| 2 | JBHT ROIC | 15.2% | Tax TTM 220.4/896.5 = 24.6% · NOPAT 723.9 ÷ IC (equity 3,633.7 + LTD 1,123.8 − cash 3.75 = 4,753.8) = **15.2%** | ✅ | — |
| 3 | JBHT FCF TTM / yield | 1,494 − 528 + 153 = 1,119 · 5.2% (4.5% ex-proceeds) | CFO 1,494.0 · capex 527.5 (XBRL) · ex-proceeds 966.5 (matches SA FCF $966.50M) · shares 93.22M × $231.95 = $21.62B → 5.2% / 4.5% | ✅ | — |
| 4 | JBHT FY21–25 FCF and naive FV | 347/345/145/809/1,103 · avg 550 · $50/sh | CFO − PaymentsToAcquirePPE + ProceedsFromSaleOfMachineryAndEquipment = 346.8 / 345.0 / 144.4 / 808.8 / 1,103.5 · 550/0.095 = $5.79B − 1.12B ÷ 93.2M = **$50** | ✅ | — |
| 5 | JBHT price / 52W high | $231.95 / $299.76 (−22.6%) | Yahoo $231.95, 52W H $299.76 · stockanalysis $231.95 close Oct 27, range $157.82–299.76 | ✅ | — |
| 6 | KNX TTM EBIT, Q3, balance sheet, and API lag | 338.5 · Q3 178.7 (+255%) · equity $7.1B · net debt $2.1B · companyfacts has Q1 only | 8-K Ex-99.1: Q3 178,705 vs 50,326 (+255.1%); 9M'26 **312,140**; 9M'25 189,605 · FY25 216.062 (XBRL) → **338.6** · "$7.1 billion of stockholders' equity… Net Debt $2.1 billion" ✓ · XBRL facts stop at Q1'26 even though the 10-Q was filed 2026-07-29 (submissions JSON) | ✅ | — |
| 7 | KNX ROIC | 2.8% (run-rate 5.8%) | 338.6 × 0.76 ÷ 9.18B = 2.8% · 178.7 × 4 × 0.76 ÷ 9.18B = 5.9% | ✅ | — |
| 8 | KNX price / 52W | $63.02 / $82.86 (−23.9%) | Yahoo and stockanalysis both $63.02, range $41.24–82.86 | ✅ | — |
| 9 | WERN TTM EBIT | ~2.4 (FY25 12 − 9M'25 47.5 + 9M'26 37.9) | 11.657 − 47.468 + 37.904 = **2.09** | ⚠️ Small arithmetic gap (rounding FY25 to 12). ROIC is ~0% either way | LOW |
| 10 | WERN litigation $21.4M and "upcycle" quote | As claimed | Ex-99.1: "non-recurrence of litigation costs of $21.4 million" ✓ · CEO: "early stages of this freight upcycle" ✓ | ✅ | — |
| 11 | WERN classification as **Tier-1 SKIP #1** (requires "worsening 2 yr+") | "9M'26 is still below 9M'25" → worsening | The 9M'25 GAAP base of $47.5M includes a **one-time insurance and claims benefit of $44.2M** (Q2'25) and a contingent-consideration gain of $7.9M (Ex-99.1 non-GAAP reconciliation). Adjusted operating income is 9M'26 **$60.5M vs 9M'25 $25.7M (+136%)** and Q3 $21.0M vs $10.9M (+92%). On a recurring basis the TTM is **improving**, which matches KNX, the case the scout did not SKIP. The scout also stripped gains for TRN but not for WERN, so the method was applied inconsistently | ❌ Wrong label. Verdict unchanged: ROIC is still far below 80% of WACC, so WERN still fails C | **MEDIUM** |
| 12 | WERN price / 52W | $29.38 / $47.49 (−38.1%) | Yahoo and stockanalysis both $29.38, range $23.06–47.49 | ✅ | — |
| 13 | TRN: does the $163.9M gain exist? | "H1'26 EBIT 300.9 includes $163.9M" | 10-Q Q2'26: "Gains on dispositions of property and other divestitures" 6M'26 = **163.9**; total operating profit 300.9 ✓ | ✅ Amount is correct | — |
| 14 | TRN: what the gain is | "$163.9M of **lease-portfolio sale** gains" | The 10-Q splits it into: **$131.6M gain on divestiture of partially-owned leasing subsidiary (TRIP Holdings, non-cash, ASC 610-20)** + $30.2M lease portfolio sales + $2.1M other. Only 18% is lease-portfolio sales | ❌ Mislabelled | **MEDIUM** |
| 15 | TRN recurring ROIC | ~274 EBIT ex-gains → **~3.2%** | TTM gains = FY25 290.8 − H1'25 19.0 + H1'26 163.9 = 435.7 → EBIT ex-all-gains **319.0** (not 274; the scout's extra ~$45M deduction could not be reconciled). Tax TTM 24.8% · IC = 1,145.7 + 5,226.5 − 155.7 = 6,216.5 → **3.9%**. Lease-portfolio sales are a routine, recurring part of the model (10-Q: "the primary driver of fluctuations"; every quarter has them, ~$50–70M/yr). Keeping them in gives **~4.5%** | ⚠️ The correction is right in direction but too large (3.2% vs 3.9–4.5%). C fail is unchanged (80% × WACC ≈ 8%+) | **MEDIUM** |
| 16 | TRN reported ROIC and debt | 8.8% · debt $5.47B | $5.47B is debt as of **2025-12-31** (XBRL DebtInstrumentCarryingAmount 5,466.5). The 10-Q at 6/30/26 shows total debt **$5,226.5M**. Mixing balance-sheet dates gives 8.8%; the same date gives **9.1%** | ⚠️ Stale balance-sheet date. No effect on the verdict | LOW |
| 17 | TRN B-Zero flag | Equity $1.14B · SA Debt/EBITDA 8.4× | Equity incl. NCI 1,145.7 / Trinity 1,143.1 ✓ · SA Debt/EBITDA 8.37 ✓ | ✅ | — |
| 18 | TRN price / 52W | $25.50 / $38.31 (−33.4%) | Yahoo and stockanalysis both $25.50, range $24.28–38.31 | ✅ | — |
| 19 | WACC inputs | Rf 5.00% · ERP 4.20% · "β~1.05" → ~9.5% | Rf 5.00% matches `agent_notes/atlas/2026-10-27_regime.md` line 26 ✓ · **β~1.05 has no source.** stockanalysis 5Y betas: JBHT 1.31, KNX 1.21, WERN 1.29, TRN 1.36 (single source only). Blume-adjusted: JBHT 1.21 → Ke ≈ 10.1%, WACC ≈ 9.8% · KNX 1.14 → Ke ≈ 9.8%, WACC ≈ 8.9% (D/V ~17%). The 9.5% band is still within ±0.5pp, and a higher WACC only makes C and D stricter, so **no verdict flips** (JBHT 15.2% > 9.8% · SAIA 10.3% still ≥ 80%) | ⚠️ Beta claim unsourced and below the raw betas. ERP was carried from the 10-27 round, which the scout disclosed | **MEDIUM** |
| 20 | Hard exclusions | Compliant | None of the 14 tickers appears in `dashboard/portfolio.js` (OPEN: ADBE/NOW/CRM/REGN/ADSK), `portfolio/decisions.md`, or the excluded list PODD/ZTS/NKE/MMS/SLM/CRI/NBIX/BYD/WGO/OWL, and none is a live watchlist row before the commit. JBHT and ODFL appear in buy_list.md (l.261) and deployment_log.md (l.614–616), but only as **scout-level** Filter B rejects from R59, not full analyses. The scout disclosed the R59/R81 overlap and the CIO named JBHT and ODFL directly (Round 76 precedent) | ✅ | — |
| 21 | Rule "do not scout names within 10% of the 52W high unless the CIO directs it" | WAB −9.0% → "A ❌" | The CIO did not name WAB (Max added it under "anything else hit hard"). At −9.0% it falls inside the 10% band and should not have been in the screen at all. Verdict unchanged (rejected) | ⚠️ | LOW |
| 22 | Filter logic (sample: SNDR A, KNX/HTLD Tier-1, LSTR D, JBHT B) | — | SNDR −20.8% ≥ 20% → A pass ✓ · KNX ROIC 2.8% < 0.5 × WACC, but TTM is improving, so not SKIP — correct reading of "ROIC < 0.5 × WACC **and** worsening 2 yr+" ✓ · LSTR 1.44× naive FV > 0.90× → D fail ✓ · JBHT FCF yield 5.2% < 6% with EV/EBITDA in the top half → B-Legacy fail ✓ · Value bucket correct (no C survivor has growth >15%) ✓ | ✅ (the exception is #11) | — |
| 23 | Process claim: prices verified with 2 sources, no gap >2% | All ≤1.6% | 4/4 spot-checks match **to the cent** between Yahoo and stockanalysis (JBHT/KNX/WERN/TRN), and all four 52W highs match. Yahoo also matches for ODFL ($187.03) and LSTR ($168.78) | ✅ | — |

### Summary

| | Count |
|---|---|
| Checkpoints | **23** |
| ✅ Correct | **16** |
| ❌ / ⚠️ Problems | **7** — HIGH 0 · MEDIUM 4 (#11, #14, #15, #19) · LOW 3 (#9, #16, #21) |

---

## 2. Findings by severity

**HIGH (changes a verdict):** none. Every problem found pushes toward rejection or does not affect the funnel's final result (0 fast-track / 0 learning-queue).

**MEDIUM — should be fixed (affects classification, re-scout triggers, or the audit trail):**
1. **WERN Tier-1 SKIP #1 → should be "C ❌ (trend improving)" like KNX.** The scout's 9M'26 vs 9M'25 comparison used a GAAP base inflated by a one-time $44.2M insurance benefit. This is the same kind of gain distortion the scout corrected for TRN, but it was not applied here. Impact: WERN should be on the re-scout trigger list (item 3 of "What this round tells the team") alongside KNX and SNDR, but currently it is not.
2. **TRN gain mislabelled.** $131.6M of the $163.9M is the non-cash TRIP Holdings divestiture gain. Only $30.2M is lease-portfolio sales. The amount is correct; the description is wrong.
3. **TRN recurring ROIC overcorrected.** The scout's 3.2% does not reconcile. It should be ~3.9% with all gains removed, or ~4.5% if routine lease-sale gains are kept as part of the business model. The C fail is unchanged.
4. **Beta "~1.05" has no source** and is below the raw 5Y betas (1.21–1.36). Here the error biases toward rejection, so it causes no damage this round, but it must not be carried into any analysis where WACC is a deciding input.

**LOW:** WERN TTM arithmetic (2.4 vs 2.09) · TRN debt taken from 12/31/25 instead of 6/30/26 · WAB scouted inside 10% of its 52W high without the CIO naming it.

**What the scout did well (worth keeping as a standard):** it verified everything from primary SEC sources. It noticed on its own that the XBRL companyfacts API lags (KNX/LSTR) and switched to the 8-K tables, and that claim checks out. Spot-checked numbers are mostly exact to the decimal. No ticker was promoted on the strength of an unverified Filter C call, so the OWL `29c72c0` failure mode did not recur.

---

## 3. Overall verdict

```
CONDITIONAL PASS
```

- **Can the verdicts be used for decisions?** Yes. The conclusion of 0 fast-track / 0 learning-queue across 14 names is reliable. No error found would flip any ticker to fast-track or learning-queue: the C-fail names have ROIC far below 80% of WACC, and the B-fail names miss the FCF yield bar on SEC numbers that verified exactly.
- **Caveats (for CIO/Max to decide whether to edit — Morgan did not edit `watchlist.md`):**
  1. Change WERN's label from Tier-1 SKIP #1 to C ❌ (improving) and add WERN to the re-scout trigger list.
  2. Correct the TRN gain description ($131.6M TRIP divestiture + $30.2M lease sales + $2.1M other) and the recurring ROIC (~3.9–4.5%).
  3. Source beta (Blume-adjusted, ≥2 sources) whenever WACC is a deciding input in later rounds.
- **Reject type log (for Vera):** `DATA_ERROR` ×0 · `RULE_VIOLATION` ×2 (#11 Tier-1 rule misapplied by using a GAAP base distorted by a one-time item; #21 10%-of-high rule) · `SOURCE_MISSING` ×1 (#19 beta) · `SANITY_FAIL` ×2 (#14 label, #15 unreconciled number) · `FORMAT` ×0 · LOW arithmetic/date ×2 (#9, #16)

*Morgan — 2026-10-28 | Independent Audit of Scout `bc34425` (Logistics/Trucking/Rail Equipment)*
