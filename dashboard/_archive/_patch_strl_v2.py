#!/usr/bin/env python3
"""
_patch_strl_v2.py — Update STRL entry in data.js to v2 (correct price $880)
Run: python "C:\\Users\\user\\Desktop\\บลจ\\บลจ CFA\\dashboard\\_patch_strl_v2.py"
"""

import re

data_file = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

with open(data_file, "r", encoding="utf-8") as f:
    content = f.read()

# --- 1. Update LAST_UPDATED ---
content = content.replace(
    'const LAST_UPDATED = "2026-05-07";',
    'const LAST_UPDATED = "2026-05-07 (v2 STRL re-analysis)";'
)

# --- 2. Find the STRL object start and end ---
# STRL object starts at the { before ticker: "STRL"
# and ends at the } after the fullContent backtick close

strl_pattern = re.compile(
    r'(\s*\{[^{]*?ticker:\s*"STRL".*?fullContent:\s*`.*?`\s*\})',
    re.DOTALL
)

new_full_content = '''# STRL — Sterling Infrastructure, Inc.
### Equity Research Report | RE-ANALYSIS v2 | 2026-05-07 | Price: ~$880

## Info

| Field | Detail |
|-------|--------|
| Ticker | STRL (NASDAQ) |
| Date | 2026-05-07 (Re-Analysis v2) |
| Price | ~$880.00 (corrected from $130 error in v1) |
| Market Cap | ~$25.8B (29.3M shares x $880) |
| Sector | Industrials / Infrastructure & Construction Services |
| S&P 500 at Analysis Date | ~5,650 |

## Recommendation

| Field | Detail |
|-------|--------|
| Recommendation | AVOID (upgraded from HOLD/WAIT in v1) |
| Entry Zone | $200-270 (genuine re-rating) OR $665-735 (if reverse split 7:1 confirmed) |
| Blended Fair Value | $156 (ESG-adjusted) |
| Margin of Safety | -82.3% |
| Stop Loss | N/A (AVOID — do not enter) |
| Max Position | 0% (Kelly Criterion = NEGATIVE) |

## Score Dashboard

| Blended FV | MOS | ESG Score | Conviction Avg | Horizon |
|-----------|-----|-----------|---------------|---------|
| $156 | -82.3% | 5.0/10 | 7.3/10 | N/A (AVOID) |

## TL;DR

- VERDICT: AVOID — at $880, STRL trades like a SaaS company (P/S ~10.7x) while being a construction contractor (peer median P/S 0.7x = 15x premium with no moat justification)
- WHY: Blended FV $156 = MOS -82.3%; No scenario in 5x5 Sensitivity Matrix reaches $880 (extreme bull CAGR 25%, Margin 17% = $750 = still below $880); Kelly = NEGATIVE all scenarios
- CRITICAL FLAG: Possible Reverse Stock Split — $130 x 7 = $910 approx $880 (7:1 split). If confirmed: shares = 4.19M, FV = $672, MOS = -23.6% => revert to HOLD/WAIT. Verify shares outstanding before any action.

## Re-Analysis Change Log (v1 to v2)

| Item | v1 (Wrong) | v2 (Correct) | Impact |
|------|----------|----------|--------|
| Price | $130 | $880 | MOS changes from -26% to -82.3% |
| Market Cap | ~$3.8B | ~$25.8B | Mid-Cap to Large-Cap territory |
| Rating | HOLD/WAIT | AVOID | Downgraded |
| Blended FV | $96 | $156 | DCF rebuilt with macro-updated WACC |
| Kelly | 3% (at entry zone) | NEGATIVE | Zero position |
| P/E Forward | ~20x | ~123-147x | Extreme overvaluation confirmed |
| P/S | ~0.8x | ~10.7x | 15x premium over peer median |
| ESG Score | 5.4/10 | 5.0/10 | Governance concern: buyback at $880 |
| New Bear Challenge | None | Reverse Split hypothesis | Critical unknown added |

## Peer Comparison (Updated)

| Ticker | P/E Fwd | EV/EBITDA | ROE | ROIC | P/S | Moat |
|--------|---------|-----------|-----|------|-----|------|
| STRL (v2 $880) | ~123-147x | ~75-80x | ~22% | ~14% | ~10.7x | Narrow |
| PWR (Quanta) | 25x | 16x | 21% | 13% | 1.2x | Narrow-Wide |
| EME (EMCOR) | 22x | 14x | 30% | 18% | 0.9x | Narrow-Wide |
| PRIM (Primoris) | 13x | 8x | 15% | 9% | 0.3x | Narrow |
| MYRG (MYR) | 15x | 9x | 17% | 11% | 0.4x | Narrow |

STRL at $880 = EXTREME OUTLIER. P/E 5-10x above every peer.

## Sensitivity Matrix 5x5 (Fair Value per Share)

Variables: Revenue CAGR x Operating Margin Exit | WACC 10% | Terminal Growth 2.5%

|  | Op Margin 9% | Op Margin 11% | Op Margin 13% | Op Margin 15% | Op Margin 17% |
|--|--|--|--|--|--|
| Rev CAGR 8% | $108 | $152 | $196 | $240 | $285 |
| Rev CAGR 12% | $145 | $196 | $248 | $300 | $355 |
| Rev CAGR 16% | $190 | $255 | $320 | $390 | $460 |
| Rev CAGR 20% | $245 | $325 | $410 | $495 | $580 |
| Rev CAGR 25% | $315 | $420 | $525 | $635 | $750 |

KEY: No cell reaches $880. Extreme bull (CAGR 25%, Margin 17%) = $750 = still below $880.
To justify $880: need CAGR >30% + Margin >20% = never achieved in construction sector history.

## Conviction Scores

Emma: 7/10 — High conviction IN AVOID; DCF Bull $384 < $880
Quinn: 8/10 — Numbers clearest ever: Kelly negative, no scenario justify
Bear: 7/10 — AVOID clear; 3pts held back for reverse split uncertainty
Average: 7.3/10 — Strong consensus AVOID

## What Would Change Our Mind

Bull Flip Triggers:
1. Price pullback to $200-270 (genuine re-rating case)
2. Reverse split confirmed -> recalibrate with new share count
3. Operating margin sustained >=12% for 3Q consecutive
4. EPS growth >=40% YoY for 3Q consecutive
5. Major structural contract shift to cost-plus basis

Bear Flip Triggers (confirm AVOID):
1. Management continues buyback at $880+ = capital misallocation confirmed
2. E-Infrastructure revenue miss >=15% 2Q consecutive
3. Operating margin <9% 2Q consecutive
4. Multiple expansion further (P/S > 12x)
5. Hyperscaler announces in-house construction capabilities

Thesis Invalidation:
1. Reverse split confirmed -> complete re-analysis with adjusted shares
2. E-Infrastructure % falls below 35% -> AI proxy thesis gone
3. Major hyperscaler client cancels contract >=500M

## Team

Charlie (Orchestrator) | Emma (Equity) | Quinn (Quant) | Bear (Risk) | Leo (Recorder)
Date: 2026-05-07 v2 | บลจ. CFA Multi-Strategy Aggressive Growth
Benchmark: S&P 500 ~5,650 at analysis date
'''

new_strl_object = '''  {
    ticker: "STRL",
    company: "Sterling Infrastructure, Inc.",
    date: "2026-05-07",
    reAnalysisVersion: "v2",
    sector: "Industrials / Infrastructure & Construction",
    price: 880.00,
    recommendation: "AVOID",
    blendedFV: 156.00,
    targetBull: 320.00,
    targetBase: 156.00,
    stopLoss: 0,
    convictionEmma: 7,
    convictionQuinn: 8,
    convictionBear: 7,
    convictionAvg: 7.3,
    pwEV: 164.60,
    beta: 1.10,
    sharpe1Y: 0.55,
    maxDrawdown: -0.38,
    moat: "Narrow",
    esgRating: "Medium-Low",
    esgScore: 5.0,
    keyThesis: "RE-ANALYSIS v2: AVOID at $880. Blended FV $156 = MOS -82.3%. P/S 10.7x vs peer median 0.7x = extreme overvaluation. Kelly NEGATIVE. CRITICAL: Possible Reverse Split (7:1) - verify shares before investing.",
    topRisk: "Valuation mean-reversion (P/S 10.7x to 1.5x = -86%) + Momentum reversal (AI narrative break = -50 to -80%) + Reverse split uncertainty",
    entryZone: "$200-270 (genuine) / $665-735 (reverse split)",
    positionSize: "0% (AVOID / Kelly Negative)",
    reportFile: "../reports/STRL_2026-05-07.md",
    fullContent: ''' + '`' + new_full_content + '`' + '''
  }'''

# Replace STRL object using regex
match = strl_pattern.search(content)
if match:
    content = content[:match.start()] + "\n" + new_strl_object + "\n" + content[match.end():]
    print(f"Found STRL object at chars {match.start()}-{match.end()}, replaced successfully")
else:
    print("ERROR: Could not find STRL object pattern in data.js")
    print("Manual update required")
    exit(1)

with open(data_file, "w", encoding="utf-8") as f:
    f.write(content)

print("data.js updated successfully with STRL v2:")
print("  price: 130 -> 880")
print("  recommendation: HOLD -> AVOID")
print("  blendedFV: 96 -> 156")
print("  convictionAvg: 6.0 -> 7.3")
print("  esgScore: 5.4 -> 5.0")
print("  pwEV: 85.20 -> 164.60")
