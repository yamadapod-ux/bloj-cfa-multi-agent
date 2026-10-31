## Quality Compounder Watchlist -- Expensive Wide-Moat (2026-10-28)

**Trigger:** CIO-directed (brief dated 2026-10-28; run 2026-10-31 on **Oct 30, 2026 close**). The mandate is the **opposite of VALUE-FIRST scout**: find businesses with very high moats that are **expensive right now** (P/FV > 1.15×), and set a trigger price to wait for. **Screen-level only.** Emma/Quinn/Bear were not called, there is no team Blended FV, and Max did not trade. Filter A/D (VALUE-FIRST) were deliberately not used, per the brief.

**Universe and exclusions:**
- **Screened 26 tickers** across 11 sectors (non-software/AI).
- **Hard exclusions:** names already held or in `portfolio.js`, the brief's list (V/FICO/MCO/VEEV/AVGO/MSFT/META/NVDA/GOOGL/AMZN + PODD/ZTS/NKE/MMS/SLM/CRI/NBIX/BYD/WGO/OWL), and names already in `decisions.md` (MA, SPGI, MSCI, HEI, MTD, ICE, ACGL, TDG, COST).
- **Also skipped:** names with a dedicated scout entry already (VRSK R75, CPRT/ISRG).
- **IDXX:** appeared only in Round 11's rejection table ("great business, too expensive" — FCF yield < 3%). It was never fully analyzed, so it is included here, matching this mandate exactly.
- **Exchanges/data:** CME (ROIC ~11%, Round 11), FDS (ROIC 15–21%, avg ~18%) and VRSK (already scouted) → **no new candidate in this group passes.**

**Data sources (primary/exact cross-check — scripts in `scripts/scout/2026-10-31_quality_compounders/`, Morgan can re-run with `python screen.py <tickers>` + `python special.py`):**
- **Fundamentals:** SEC EDGAR XBRL companyfacts (`data.sec.gov/api/xbrl/companyfacts/CIK##########.json`), pulled 2026-10-31. TTM = FY + YTD − prior YTD.
  - ROIC = EBIT×(1−tax)/(equity + debt − cash & securities), FY year-end, 5 years.
  - **Debt-concept fix:** WM/RSG/ECL report under `LongTermDebtAndCapitalLeaseObligations*`, which the old script (`ai_selloff/hist.py`) missed, reading debt = 0. CPRT keeps cash in HTM securities. Patched in this round's `hist.py` before computing.
- **RACE** files a 20-F (IFRS, EUR): FY2025 data, diluted shares 178.3M (`AdjustedWeightedAverageShares`, because the dei cover count is stale from 2020). EUR/USD 1.117 (Yahoo `EURUSD=X`).
- **KNSL** = insurer → residual-income model on book value (P/B–ROE), not EBIT-DCF.
- **Prices (Oct 30 close), 2 sources:** Yahoo chart API (`query1.finance.yahoo.com/v8/finance/chart/TICKER`) and Nasdaq quote API (`api.nasdaq.com/api/quote/TICKER/info`) match **exactly (0.00% diff) for all 16 names**.
- **Consensus revenue growth (FY+1/FY+2) + Street PT:** stockanalysis.com `/stocks/TICKER/forecast/` (S&P Global consensus, updated 10-05 → 10-30). **Single source** (consensus is not in SEC).
- **Rf / ERP / beta:**
  - Rf = 10Y UST **4.93%** (Yahoo ^TNX, Oct 30). ERP = Damodaran implied **4.20%**, carried from the 10-27 round.
  - β = raw 5Y monthly vs ^GSPC (Yahoo adjclose) → Blume. Kd = (Rf + 80bps)×(1−21%). Market-value weights.
  - **Not a VS2 §1.1 two-method WACC.**

**FV method (screen-level, one model for every name so they're comparable):**
- **NOPAT/reinvestment DCF:** FCFF = NOPAT × (1 − g/RONIC).
  - EBIT margin held at TTM (SEC). Tax = TTM effective rate, bounded 15–27%.
  - Growth = consensus FY+1/FY+2, fading linearly to TGR 3% by year 10.
  - RONIC fades from TTM ROIC (cap 100%) to **20%** in year 10. Terminal value uses g/RONIC (no free growth).
- **Leases excluded** (ORLY/ROL/CTAS have sizable leases → FV leans a little high for those). No VS2 §1.2 non-op bridge.
- **KNSL:** ROE fades from TTM 27.8% to 15% by year 10. BV grows by min(consensus growth, ROE×95%). TV = (ROE−Ke)×BV/(Ke−g).
- **Bucket:** **Value for all 16.** Consensus revenue growth FY+1 is ≤17.4% for every name, so the Growth gate (>20%) can't be reached. MNST's TTM is +20.4%, but consensus is 17.4% → 9.6%.
  - → **Trigger = MOS 15% = 0.85 × Screen FV** (CLAUDE.md § MOS Threshold, Value bucket).
- **Implied k** = the consensus-growth multiplier the current price implies (k = 1.0 means the price matches consensus exactly). It's the same idea as Growth reverse-DCF, kept for context.
- **"Trigger @WACC−1pp"** = a looser bound. Use it if you believe the market should discount wide moats at a lower rate. **It is not an official gate.**

{TABLE}

*Sorted by % drop needed to reach the trigger (least first). All 16 have P/FV > 1.15× → "expensive" per the brief ✅. 5Y ROIC = FY2021→latest FY from SEC (KNSL = ROE, ORLY/GWW/IDXX/MNST latest SEC = Q2'26, CTAS/PAYX = FQ1'27 Aug, MSI = Q2'26 Jul).*

**Moat evidence (why the moat is wide — not just a popular name):**
> Morningstar moat rating **could not be verified per ticker this round.** WebSearch only returned Morningstar index docs; [one Morningstar index doc](https://indexes.morningstar.com/api/docs/694ab7c2f85146e3acf6ce8e) lists WST as wide moat. The evidence below = **5Y ROIC from SEC (quantitative proof of excess return) + structural mechanism (Morningstar 5-factor)**. Atlas/Emma must verify the moat source in any full analysis.

| Ticker | Moat source | Quantitative evidence (SEC) | Flag |
|---|---|---|---|
| **PAYX** | Switching cost (payroll + tax filing + HR for SMBs — switching mid-year is very costly) + client-fund float | EBIT margin 39%; ROIC 53–57% before the Paycor acquisition | ROIC fell to 23–27% after the acquisition (goodwill). EV/Rev at the 10th pctile → de-rated a lot already |
| **RMD** | Intangible (patents + brand for CPAP/masks) + switching cost (installed base + cloud-connected devices → resupply masks) | EBIT margin 33%; ROIC 17–26% | ⚠️ ROIC 17% in FY22 — 5Y avg ~22%, slightly below "consistently >20%". GLP-1 is the main bear thesis |
| **ORLY** | Cost advantage (dense distribution network + hub stores; parts availability that competitors can't match) | ROIC 54–72% (highest on the list); EBIT 19.6% | ROIC trending down 72→54%. Leases not included → ROIC/FV overstated. 2025 split normalized via Yahoo split events |
| **ROL** | Cost advantage (route density) + brand (Orkin) + recurring contracts | ROIC 29–41% | ⚠️ **Fell −47.6% from its 52W high** after the Q2 miss (7/22: EPS −5.9% vs consensus, op. margin 18.7% vs 19.8%) + Piper downgrade 9/23 ([Fool](https://www.fool.com/investing/2026/07/23/why-rollins-stock-is-plummeting-lower-today/), [Nasdaq](https://www.nasdaq.com/articles/why-rollins-stock-plummeting-lower-today)) + a law-firm investigation ([Glancy](https://www.glancylaw.com/cases/rollins-inc-1/)) → E3 overhang. Still 1.59× over FV despite the drop. EV/Rev at the 5th pctile |
| **TT** | Intangible (brand + engineering in commercial HVAC) + installed base → services | ROIC 18→28% (rising) | ⚠️ ROIC 18% in FY21. Partly linked to data-center cooling (AI capex) |
| **MNST** | Intangible (brand) + distribution moat via KO's bottling network | ROIC 28–39%; EBIT 29%; net cash $3.4B | EV/Rev at the 95th pctile → most expensive vs its own history |
| **KNSL** | Cost advantage (E&S combined ratio below industry, thanks to its own tech platform + small-ticket underwriting) | ROE 22–34%; P/B 4.3× | Consensus revenue FY+1 +3.7% / FY+2 ~0% (E&S cycle softening). Implied k n/m — the price can't be explained by any growth path in this RI model. Model simplified |
| **ITW** | Cost advantage + intangible (80/20 business model, niche leadership) | ROIC 28–31% (most stable); EBIT 26.6% | Slow growth (consensus 3.6–4.9%) |
| **GWW** | Efficient scale + cost advantage (MRO logistics, KeepStock vending) | ROIC 29–41% | EV/Rev at the 95th pctile |
| **FAST** | Switching cost (onsite + vending machines installed in customer plants) + cost advantage (local network) | ROIC 29–35% | EV/Rev at the 95th pctile; price ≈ Street PT median |
| **SHW** | Intangible (brand) + cost advantage (company-owned stores reaching pro painters directly) | ROIC 20–24% | Net debt $11.5B; ROIC sits right at the edge of the 20% bar |
| **MSI** | Switching cost + efficient scale (LMR radio networks for police/fire — government contracts, long lifecycle) | ROIC 22–39% | ROIC fell to 22% in the latest FY (acquisitions). EV/Rev at the 85th pctile. Not AI/software |
| **RACE** | Intangible (brand + scarcity — controls supply, pricing power) | ROIC 24–31% (rising); EBIT 29.5% | Borrowings include captive-finance debt → ROIC/ND slightly distorted. FY2025 data (20-F) — no TTM |
| **CTAS** | Cost advantage (route density, uniform-rental scale) + switching cost (multi-year contracts) | ROIC 22→29% (rising steadily) | EV/Rev at the 75th pctile; implied k 3.3× |
| **IDXX** | Switching cost (in-clinic analyzer installed base → consumables recurring revenue) + intangible | ROIC 47–58% | WACC 10.6% (β 1.54, high for a quality name) → FV falls harshly. Was scout-rejected in Round 11 as "too expensive" |
| **WST** | Switching cost + regulatory (components are written into the drug filings of pharma customers — changing supplier means re-filing) | ROIC 35→18% (falling) | ⚠️ ROIC trending down below 20% in the last 2 years. Highest P/FV on the list, 3.0×. Morningstar index lists it as wide moat |

**Screened but did not qualify (10):**
- **ROIC < 20% (not consistent high-return compounders):**
  - WM 10–12% · RSG 9–11% · ECL 8–15% · AME 12–13% · ROP 5–6% · CHD 8–14% · FDS 15–21% · CPRT 15–34% (falling).
  - WM/RSG/ECL looked like >20% on the first pass. The cause was missing debt (see the fix above). They fail after the fix.
- **AZO — not expensive:** P/FV **0.76×** (FV $4,189 vs $3,170, EV/Rev 20th pctile, implied k 0.36×).
  - This is a VALUE-FIRST candidate, not this mandate: −20.7% from 52W high, so Filter A passes.
  - ⚠️ ROIC is falling 117→48%.
  - → **Propose sending AZO to the regular scout pipeline** (Filter A–E + Tier 1) next round.
- **WAT:** after the BD Biosciences merger, TTM data is distorted (EBIT margin 7%, ROIC 1.4%, consensus +104%) → can't compute a screen FV. Wait for 4 clean quarters.
- **ADP:** companyfacts has no `OperatingIncomeLoss`, and client-fund assets/obligations distort net debt → couldn't compute in the same model. PAYX covers this group.

**Max's assessment — what the CIO must know before using these trigger prices:**
1. **Screen FV runs systematically below Street PT for every name** (Street PT median ≈ current price, while our FV = 0.33–0.83× price). Reasons:
   - A Blume-β WACC of 7.6–10.6% plus terminal RONIC 20% is strict for wide moats, which the market discounts at a lower rate and expects to hold excess returns longer.
   - This is the same issue as AMZN v3.2 (Market-Implied Sanity Check). Every name here has |MOS| ≥ 35% except ORLY/RMD/PAYX.
   - The sensitivity to WACC is large: −1pp WACC raises FV by 15–45%. Use **"Trigger @WACC−1pp"** as an early-warning level → that's the point to send it to a full VS2 pipeline.
2. **A 50–70% drop for wide-moat compounders is rare** (it usually needs a 2008/2020-style crash or a structural moat break). The names with realistic triggers: **PAYX / RMD / ORLY** (−30% to −32%; looser bound −10% to −14%).
3. **The names closest to trigger have mostly already been de-rated vs their own history:**
   - PAYX EV/Rev 10th pctile · RMD 15th · ORLY 53rd. ROL is at the 5th pctile but still 1.59× over FV.
   - In other words, the market has already re-priced them partly, and the bear thesis is concrete: PAYX = SMB employment / Paycor integration; RMD = GLP-1; ROL = Q2 miss + investigation.
4. **No Blended FV:** these triggers come from a single screen-level DCF, not 40/30/30. When a price hits trigger @WACC−1pp → Charlie dispatches the full VS2 pipeline (Atlas classification → Emma/Quinn/Bear → Morgan) before any deploy. **Don't buy at the screen trigger directly.**
5. **Proposal to Charlie:** add all 16 as a "Quality Watch" lane with alerts at both levels, and Max checks them in every Portfolio Review (Mode 3).
   - **Not added to `buy_list.md` yet**, because none of the 16 has been fully analyzed (buy_list = fully analyzed names only).

*Max — 2026-10-31 | Quality Compounder Watchlist (CIO-directed 2026-10-28) | 26 screened → 16 listed · 0 trade*
