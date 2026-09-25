# Lessons Briefing — Latest (maintained by Leo, updated 2026-09-25)

**Purpose:** condensed briefing fed to Emma/Quinn/Bear before each new analysis, standing in for the full learning-log.md (1,078 lines) that the real Claude Code agents re-read every session. This is a deliberate compromise: cheaper than full re-read, richer than no history at all.

## Top recurring patterns (from learning-log.md + decisions.md history)
1. **Dual-gate-failure is the single most common outcome** — MOS passing alone or Conviction passing alone is NOT enough. Both must clear simultaneously (Value: MOS≥15% AND Conviction≥7.0; Growth: RevGrowth>20% AND Conviction≥6.5-7.0). Recurred 8+ times in one quarter (WPM, PGR, DXCM, ABBV, ACGL, CRDO, TOST, MRVL...). **Do not round conviction up or treat a near-miss as a pass.**
2. **"Beaten-down" price alone does not mean "cheap"** — several names down 20-35% from highs (NVR, EMN, VMC) turned out to be fairly-valued-or-worse because fundamentals deteriorated in step with price (not a market overreaction). Always check whether the decline reflects real business deterioration vs pure sentiment before assuming MOS will be positive.
3. **"Record high" / extreme framing needs independent verification** — WPM QA incident: team called gold price "record high" when it was actually -26% off the real ATH. Don't let framing language go unverified by Morgan.
4. **Terminal Value >50% of DCF EV is a real red flag, not just a caveat** — DXCM incident: Terminal Growth Rate error (3.5% vs 1-3% ceiling) forced a full recompute cascade (Emma FV, Bear P-W EV, Blended FV all changed) and a second QA round. Always sanity-check TGR before finalizing, and treat a high TV% as raising, not lowering, the bar for conviction.
5. **Buyback-driven EPS growth can mask real operating deterioration** — DECK 2026-09 case: EPS beat while operating income fell 6% YoY, purely from a 7.4% share-count reduction. Always check operating income trend, not just EPS, when a company narrative claims "beat and raise."
6. **Analyst downgrades and short-interest trend matter as corroborating (not sole) evidence** — a single downgrade is noise; multiple downgrades + rising short interest + a competitor visibly taking market share (e.g., On Running vs HOKA in run-specialty channel) together constitute a real signal worth weighting heavily in Bear's case.
7. **Scout price data must be independently verified (≥2 sources)** — CNC and ZETA incidents: scout prices were wrong by 30%+ due to single-source or stale data, wasting a full pipeline run on invalid inputs. Verify scout-stage prices before committing pipeline resources.
8. **CIO Full Autonomy Mode is active since 2026-05-11** — team can execute trades post-QA-PASS without asking CIO to confirm each time, but Max Consultation Rule (Max must consult Charlie before BUY/SELL/TRIM) still applies.
9. **Regime is not always the binding constraint** — don't assume Force Deploy Suspension is why a trade isn't happening; check conviction/MOS gates independently, since those can fail even under RISK-ON (see DECK 2026-09-25 correction).

## Format/process rules to not forget
- Every report needs `[CFA Lx: ...]` tag on every section heading (house format rule)
- Blended FV weight is 40/35/25 or 40/30/30 depending on latest CLAUDE.md revision — **always re-verify live, don't trust any cached number including this briefing**
- Dashboard/tracker files: never overwrite wholesale — targeted edit/append only (2026-08-24 incident wiped 561 lines of tracker.md this way)
