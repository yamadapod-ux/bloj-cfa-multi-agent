# Filter D Street-PT Override Threshold — Quantified Simulation (Option B Deep-Dive)

*2026-10-01 | Vera (Performance Tracker) | Follow-up to `agent_notes/charlie/2026-10-01_near_miss_diagnostic.md` Part 3, Option B, at CIO request to go one level deeper on a single specific lever: narrowing Filter D's Street-PT **tie-break/override** threshold from 25% to 23% (a 2 percentage-point change).*

**Status: pure analysis. No filter thresholds, no CLAUDE.md content, and no live gating logic were modified in producing this report. This is a supplementary what-if simulation only — the CIO has not decided to act on Option B.**

---

## 0. Important scope correction before the simulation (read first)

CLAUDE.md's Filter D actually contains **two distinct Street-PT thresholds**, and the original diagnostic's Option B narrative (which this report was commissioned to pressure-test) blurred them together:

| Threshold | Where it applies | Current value | Mechanism |
|---|---|---|---|
| **Fallback PASS bar** | Used only when naive FV is **not computable** (e.g. LUV — structurally negative/near-zero through-cycle FCF, so FCF÷WACC produces no meaningful positive FV) | **20%** | If Street PT upside clears 20%, Filter D passes on the Street-PT leg alone, in place of naive FV |
| **Tie-break OVERRIDE bar** | Used when naive FV **is computable** and says REJECT (price > naive FV), but Street PT is very bullish | **25%** | If Street PT upside **also** clears 25%, Street PT is allowed to override naive FV and the candidate passes; below 25%, naive FV governs and the candidate is rejected (per the exact CLAUDE.md text: *"ถ้า Street PT สูงกว่ามาก (>25%) แต่ naive FV ต่ำกว่าราคา = ใช้ naive FV เป็นเกณฑ์ตัดสิน"*) |

**The CIO's question specifically names "the Street-PT override threshold... from 25% to 23%" — this is the tie-break bar (25%), which governs LMT, AXP, and PEP's Filter D deaths. It does NOT govern LUV's**, whose Filter D death runs through the *fallback* bar (20%), a different number entirely. The original diagnostic's Option B paragraph proposed changing *both* numbers at once (20%→18% and 25%→22%, not even a consistent "2pp" on both legs) and then summarized the combined effect loosely as "LUV and LMT flip." That was directionally useful for a first-pass diagnostic but is **not precise enough for a real decision** — Part 1 below recomputes each candidate individually against the literal 25%→23% change only, and Part 2 extends the sensitivity to lower thresholds to show what it would actually take to reproduce the original "both flip" narrative.

---

## 1. Candidate-by-candidate recompute: 25% (current) vs 23% (hypothetical)

Every Filter D hairline-miss candidate from the near-miss diagnostic, with the exact governing number identified per CLAUDE.md's own tie-break logic.

### LMT (Round 50) — governed by the 25% tie-break bar ✅ in scope

- Naive FV (FCF-yield-implied): price ~9.6% **above** naive FV → naive FV says REJECT
- Street PT: **+22.83% to +23.0%** upside (MarketBeat, 19 analysts, $637.56 avg PT vs $518-519 price)
- **At 25% (current):** 22.83-23.0% < 25% → tie-break does NOT trigger → naive FV governs → **REJECT** (as actually happened, confirmed in `watchlist.md` Round 50)
- **At 23% (hypothetical):** the range **straddles 23% exactly at its high end.** Low estimate (22.83%) is still 0.17pp short; high estimate (23.0%) sits exactly at the line. This is **not a clean flip** — it is a genuine boundary case where the outcome depends on which end of the disclosed 22.83-23% range you treat as authoritative, and on whether the rule reads as "> threshold" (strict) or "≥ threshold." **Verdict: marginal/ambiguous flip, not a confirmed pass**, unlike the original diagnostic's clean "flips to fast-track" framing.

### AXP (Round 42) — governed by the 25% tie-break bar ✅ in scope

- Naive FV: price 23.6% **above** naive FV ($308.89 vs $249.90) → REJECT
- Street PT: **+20.9% to +21.7%** upside ($373.50-$375.96 consensus vs $308.89 price)
- **At 25% (current):** 20.9-21.7% < 25% → REJECT (as actually happened)
- **At 23% (hypothetical):** 20.9-21.7% is still **below 23%** at every point in its disclosed range (closest approach 21.7%, still 1.3pp short) → **does NOT flip.**

### PEP (Round 48) — governed by the 25% tie-break bar ✅ in scope

- D-Legacy naive FV: 0.914× (reject-boundary) vs EV/EBITDA cross-check 0.746× (fast-track-quality) — methods disagree, which is itself the primary routing reason (→ learning-queue), independent of the Street-PT leg
- Street PT: **+20.6% to +20.8%** upside ($155.00-$155.20 consensus vs $128.6 price)
- **At 25% (current):** 20.6-20.8% < 25% → tie-break does not trigger
- **At 23% (hypothetical):** 20.6-20.8% is still **below 23%** at every point (closest approach 20.8%, 2.2pp short) → **does NOT flip.** PEP's Filter D outcome is additionally driven by the method-disagreement rule, which this threshold change does not touch at all — so even setting the Street-PT question aside, PEP's routing is not Street-PT-bound the way LMT's is.

### LUV (Round 51) — governed by the SEPARATE 20% fallback bar ❌ out of scope for this specific lever

- Naive FV: not computable (structurally negative/near-zero through-cycle FCF — explicit methodology breakdown, not a numeric miss)
- Street PT: **+19.34%** upside ($50.22 consensus vs $42.08 price)
- The applicable threshold is the **20% fallback PASS bar**, not the 25% tie-break bar. **A 25%→23% change leaves LUV's governing number (20%) completely untouched — LUV does not flip under the literal question asked.** To flip LUV, the *fallback* bar specifically would need to drop to ≤19.34% (i.e., 20%→19% or lower, a ~1pp cut) — a different parameter change from the one under review here, and not part of this simulation's scope per the CIO's framing. Noted for completeness since LUV was named in the original diagnostic's Option B paragraph.

### Summary of Part 1

| Ticker | Governing threshold | Current value | Street PT gap | At 25% | At 23% |
|---|---|---|---|---|---|
| LMT | Tie-break (25%) | 25% | 22.83-23.0% | REJECT | **Boundary/ambiguous — not a clean flip** |
| AXP | Tie-break (25%) | 25% | 20.9-21.7% | REJECT | REJECT (no flip) |
| PEP | Tie-break (25%) | 25%, plus disagreement rule | 20.6-20.8% | LEARNING-QUEUE | LEARNING-QUEUE (no flip; disagreement rule also unaffected) |
| LUV | Fallback (20%, different parameter) | 20% | 19.34% | REJECT | **N/A — this lever does not touch LUV's threshold** |

**Headline finding: a literal 25%→23% change flips zero candidates cleanly, with LMT sitting exactly on the new boundary.** This materially revises the original diagnostic's Option B claim that a 2pp change would flip "LUV and LMT" and move the fast-track rate from 0% to ~20% — that claim implicitly bundled two different threshold changes (20%→18% AND 25%→22%, a 3pp cut on the second leg, not 2pp) into one "2pp" narrative. Isolated to the single number the CIO is actually asking about, the effect is far smaller.

---

## 2. Sensitivity table — effect of the tie-break threshold at 25/24/23/22/20%

Only candidates genuinely gated by the **25% tie-break mechanism** can be affected by this lever (LMT, AXP, PEP). LUV is excluded (different parameter, see Part 1) and shown in its own row for reference. The other 20 of the diagnostic's 24 named candidates died at Filter A/B/C/E or a different Filter D sub-test (0.80-0.90× D-ratio band: BKNG, KMB, PYPL; naive-FV-decisive: NVR, BSX, AXP's P/B cross-check) and are **structurally unaffected by any change to this one number** — they would not flip regardless of where this threshold is set.

| Threshold | LMT (22.83-23.0%) | AXP (20.9-21.7%) | PEP (20.6-20.8%) | LUV (19.34%, different lever) | Tie-break flips (of 3 eligible) | Resulting Scout→Fast-track rate* |
|---|---|---|---|---|---|---|
| **25% (current)** | REJECT | REJECT | REJECT/LQ | REJECT (separate 20% bar) | **0 / 3** | **0%** (matches actual 0/~10) |
| **24%** | REJECT (still short by ≤1.17pp) | REJECT | REJECT | — | **0 / 3** | 0% |
| **23% (the question asked)** | **Boundary — marginal/ambiguous** | REJECT | REJECT | — | **0-1 / 3** | **0-10%** |
| **22%** | **FLIPS** (22.83-23.0% > 22%) | REJECT (21.7% still short) | REJECT (20.8% still short) | — | **1 / 3** | **~10%** |
| **20%** | FLIPS | **FLIPS** (21.7% > 20%, 20.9% also clears) | **FLIPS** (20.6-20.8% > 20%, narrowly — PEP's low end 20.6% clears, but this is now itself a boundary case) | not applicable (separate lever) | **3 / 3** | **~30%** (upper end of 15-30% baseline) |

*Scout→Fast-track rate recomputed using the diagnostic's own denominator (~9-11 candidates that reached Filter D/E judgment this period, per Part 1(c) of the original report). 1 flip ≈ 1/10 ≈ 10%; 3 flips ≈ 3/10 ≈ 30%.

**What this table actually shows the CIO:**
1. **The funnel is not meaningfully sensitive at a 2pp change (25%→23%).** It takes a **5-percentage-point cut (25%→20%)** — not 2pp — to reproduce the original diagnostic's "~20% fast-track rate" narrative, and even then only by flipping LMT + AXP + PEP together, not LUV (which needs its own separate 1pp cut on a different parameter).
2. **LMT is the single pressure point.** It is the only name in the current dataset close enough to flip on a small tie-break adjustment, and even for LMT the honest read at exactly 23% is a boundary case, not a clean pass.
3. A threshold move large enough to reliably move the funnel (≥5pp, to ~20%) is also large enough to raise a legitimate "how much are we just backsolving to a target hit-rate" concern — see Part 4.

---

## 3. Directional sanity-check — did the stocks that would flip move the way the thesis predicts?

**Explicit limitation, stated up front per the task instructions: this is NOT a 6-month (or even 6-week) backtest. These candidates were scouted 1-3 calendar days before this check (2026-09-28 to 2026-09-30 vs this report's 2026-10-01 date). Any price move over 1-3 days is noise, not signal, and should not be treated as evidence the Filter D thesis is right or wrong. This section exists only because the task asked for an honest, short-notice directional gut-check — it is explicitly not a formal outcome test and carries near-zero statistical weight.**

Only LMT is a genuine (if boundary) flip candidate at 23%; AXP, PEP, and LUV do not flip at 23% per Part 1, but are checked below anyway since they were named in the original diagnostic and the CIO's deep-dive interest covers the whole cluster.

| Ticker | Scout price / date | Current price (2-source, 2026-09-30/10-01) | Move | Thesis direction (bullish — expects appreciation toward Street PT) | Confirmed so far? |
|---|---|---|---|---|---|
| **LMT** | ~$518-519 (2026-09-29) | **$508.36-$509.25** (TechGraph, exa.ai/market data — both 2026-09-30/10-01) | **-1.7% to -2.0%** | Bullish | **No** — moved against the thesis, but magnitude is well within normal 1-2 day noise for a $500+ industrial name; a fresh $871M Pentagon F-35 contract was also disclosed 2026-09-29 and did not move the stock up, which is mildly discouraging but not conclusive at this horizon |
| **AXP** | $308.89 (2026-09-28) | **~$304-306** (Morningstar prev-close $305.66, DefenseWorld Oct-1-open $304.21 — tightest 2-source cluster; other quotes in the $311-338 range appear stale/inconsistent and are disregarded) | **-1.0% to -1.6%** | Bullish | **No** — also moved against the thesis; Citigroup cut its AXP PT from $355 to $340 on 2026-10-01, a modest negative revision in the same window |
| **PEP** | ~$128.6 (2026-09-29) | **$126.72** (2026-09-30, a fresh 52-week low per 247wallst.com) | **-1.5%**, and the stock set a *new* 52-week low the day after being scouted | Bullish | **No, and this is the most negative signal of the three** — not just noise-level drift but two analyst **downgrades with real PT cuts** landed in the same window: JPMorgan cut PEP to Neutral and slashed its PT from $170 to $138 (2026-09-29/30), Deutsche Bank downgraded a day earlier. This actively erodes the Street-PT number the whole tie-break calculation depends on — PEP's case for an eventual fast-track is getting *weaker*, not stronger, in real time, independent of where the threshold is set. |
| **LUV** | $42.08 (2026-09-30) | **$41.60-$41.78** (Yahoo close 09-30, MarketBeat) | **-0.7% to -1.1%** | Bullish (not a 23%-lever flip, shown for completeness) | **No**, but same-day/next-day noise, not informative either way |

**Honest read: all four names moved modestly against the fast-track thesis in the 1-3 days since being scouted, and PEP's move is accompanied by real negative analyst-PT revisions that directly undercut the Street-PT number the tie-break rule relies on.** Given the horizon, none of this should be read as disconfirming evidence of the underlying investment thesis — it is far too early, and daily noise this size is unremarkable for any of these names. But it also provides **zero supporting evidence** for loosening the gate right now, and PEP's case specifically looks *weaker*, not stronger, than it did 48 hours ago. If anything, this is a mild argument for Option C (wait for real checkpoints) over immediate action on Option B.

---

## 4. Why was 25% chosen, and is 2pp a meaningful erosion of that reasoning?

**Searched `agent_notes/charlie/` in full (`2026-09-01_strategic_note.md`, `2026-09-06_funnel_redesign_proposal.md`, `learning_queue_2026-09.md`, plus CLAUDE.md's own Filter D section) for a dedicated rationale note explaining the specific choice of 25% (as opposed to 20%, 22%, or 30%) for the tie-break bar. None exists.**

What the record does show (`2026-09-06_funnel_redesign_proposal.md`, § 3.A, the commit that introduced Filter D and both thresholds in the same text block):
- The **20% fallback bar** is explicitly anchored to the MOS logic elsewhere in CLAUDE.md: "มี MOS อย่างน้อย ~20% ก่อนเข้า pipeline" — i.e., 20% was chosen because it matches the margin-of-safety the Return-side rules already require downstream (Value-bucket MOS ≥15%, with a buffer). This is a documented, principled anchor.
- The **25% tie-break bar** has **no equivalent documented anchor**. The proposal's exact text simply states the rule ("ถ้า Street PT สูงกว่ามาก (>25%)... ใช้ naive FV เป็นเกณฑ์ตัดสิน") without separately justifying why the override bar sits 5pp above the base pass bar rather than, say, 3pp or 10pp. The most plausible **inferred** (not confirmed) rationale, based on the surrounding design intent in the same proposal (Charlie's own stated goal for Filter D: *"ไม่ใช้ Street PT เป็นเกณฑ์เดี่ยว (Street extrapolate peak)"* — i.e., explicitly distrust sell-side PTs because analysts anchor to prior peaks) is that the override bar was deliberately set **meaningfully above** the base pass threshold so that Street PT could only override a failed DCF when the bullish signal was unambiguously strong — a 5pp buffer functions as a built-in skepticism margin against exactly the "Street extrapolates the old peak" failure mode the rule's own author flagged as the reason not to trust Street PT in the first place.

**Weighing 2pp (25%→23%) against that inferred rationale:**
- If the 5pp buffer exists specifically to discount analyst peak-extrapolation bias, a 2pp cut removes **40% of that buffer** (5pp → 3pp) — not a trivial erosion in proportional terms, even though it looks small in absolute percentage-point terms.
- Separately, and more concretely: the recomputation in Part 1 shows that even stripping away the rationale question entirely, a 2pp cut has **almost no mechanical effect on this dataset** (0-1 of 3 eligible candidates, with the "1" being a genuine boundary case) — so whatever philosophical erosion a 2pp cut represents, it would not yet be "paid for" by meaningfully more fast-track flow. The threshold would need to move far enough (to ~20-21%, a 4-5pp cut — most of the inferred buffer) before it visibly moves the funnel.
- **Practical implication for the CIO:** a 2pp change is simultaneously (a) too small to materially change the Scout→Fast-track rate on the current dataset, and (b) large enough, proportionally, to meaningfully erode an already-undocumented safety buffer whose only textual support is an inference, not a derivation. Neither side of that trade looks obviously attractive.

---

## 5. Recommendation

**Framed, per the task instruction, entirely as: "if the CIO decides to act on Option B, here is the precise number and its quantified effect" — this is not a proposal to act, and nothing has been implemented.**

- **Do not adopt 23%.** The simulation shows it produces 0 clean flips (1 genuine boundary case, LMT) against this dataset — it does not meaningfully move the Scout→Fast-track rate, and the original diagnostic's implied "~20% rate at a 2pp change" claim does not hold up under a candidate-by-candidate recompute once LUV (governed by a different parameter) is correctly excluded from this specific lever.
- **Staying at 25% remains defensible** on the current evidence: it has correctly rejected every Filter D candidate checked here so far (consistent with the original diagnostic's "gate ไม่ต้องแก้... มันตัดสินถูก" track record), and the 1-3 day directional sanity-check in Part 3 — while far too short to be real evidence — if anything leans slightly *against* loosening right now (PEP's Street PT is actively being cut by two analysts in the same window the tie-break rule depends on).
- **If the CIO does want to act on something resembling Option B, the quantified number that actually produces the originally-claimed effect (~2-3 flips, ~20-30% fast-track rate) is a cut to roughly 20-21%, not 23%** — a 4-5pp change, not 2pp — and even that only reliably captures LMT + AXP + PEP; it still does **not** capture LUV, which sits behind a separate 20% fallback parameter that was not in scope of this specific question and would need its own, independently-justified 1pp adjustment.
- **Lowest-risk next step, consistent with the original diagnostic's own Option C:** do not change any number now. Re-run this exact candidate-by-candidate recompute at the next scheduled checkpoint (2026-11-15, already proposed in the original diagnostic) once LMT/TXT/LUV's Q3 earnings and a few more weeks of price action are in — at that point the Part 3 sanity-check will carry actual signal instead of 1-3-day noise, and any threshold decision will rest on real evidence rather than a backsolved number.

**No filter thresholds, CLAUDE.md content, or gating logic were changed in producing this report.**

---

*Vera (Performance Tracker) — 2026-10-01 | Filter D Street-PT threshold simulation, Option B deep-dive per CIO request. Key corrective finding: a literal 25%→23% change (the exact question asked) flips 0 candidates cleanly (1 boundary case, LMT) — not "LUV and LMT" as the original diagnostic's Option B paragraph implied, because that paragraph bundled two different threshold parameters (the 20% fallback bar governing LUV, and the 25% tie-break bar governing LMT/AXP/PEP) into one "2pp" narrative. Reproducing the originally-claimed ~20% fast-track effect requires a 4-5pp cut (to ~20-21%), not 2pp, and even then does not reach LUV. Recommendation: stay at 25% on current evidence; if CIO wants to act, the number that actually works is ~20-21%, not 23%, and should wait for the 2026-11-15 interim checkpoint for real (not 1-3-day) price evidence.*
