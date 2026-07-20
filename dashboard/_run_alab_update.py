#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update dashboard/data.js — replace ALAB object with v2 corrected data
Uses re.sub with DOTALL — safe for multiline replacement
Run from: C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\
"""

import re
import os
import subprocess

DATA_JS = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

with open(DATA_JS, "r", encoding="utf-8") as f:
    content = f.read()

# New ALAB object — v2 corrected
new_alab = r"""  {
    ticker: "ALAB",
    company: "Astera Labs Inc",
    date: "2026-05-20",
    version: "v2-price-fix",
    recommendation: "HOLD/WAIT",
    bucket: "Growth",
    price: 251.71,
    blendedFV: 112,
    mos: -55.5,
    esgAdjFV: 105,
    conviction: 6.2,
    emmaFV: 122,
    quinnFV: 109,
    bearFV: 80,
    weights: "Emma 40% + Quinn 30% + Bear 30%",
    entryZone: "$130-160 (T1) / $110-130 (T2)",
    stopLoss: "$100 (-20% from T1 mid $125)",
    maxPosition: "3% (TC x0.75)",
    horizon: "3-5Y",
    regime: "TRANSITIONAL-CAUTIOUS",
    sector: "Semiconductors",
    marketCap: 41.87,
    q1Revenue: 308.4,
    q1RevenueGrowth: 93,
    gaapNI: 80.3,
    fy2024Revenue: 396.3,
    evNTMRev: 31,
    evNTMRevPercentile: "85-90th",
    growthMOSMethod1: "PASS (0.875x < 1.2x)",
    growthMOSMethod2: "FAIL (31x > 70th pct gate)",
    priceAuditFail: true,
    priceAuditV1: 60,
    priceAuditDiscrepancy: "+319%",
    profitabilityMilestone: true,
    esgE: 5,
    esgS: 6,
    esgG: 4.5,
    esgOverall: 5.2,
    deployStatus: "SKIPPED",
    deployReason: "Conv 6.2 < 7.0 gate + MOS -55.5% + Growth MOS M2 FAIL + TC Regime",
    watchlistAlert: "$130-160 (T1)",
    spAtAnalysis: 7403,
    notes: "PRICE AUDIT FAIL v1: $60 (est.) vs $251.71 actual = +319% worst in portfolio. Q1 2026: Rev $308.4M +93% YoY, GAAP NI $80.3M = PROFITABLE. Blended FV $48.5->$112 (+131%). Weight corrected 40/35/25->40/30/30. EV/Rev 31x = 85-90th pct = highest in portfolio analysis.",
    fullContent: `# ALAB — Astera Labs Inc (v2 Price Fix 2026-05-20)

**PRICE AUDIT FAIL:** v1 used ~$60 (est.) — actual price $251.71 (+319% discrepancy). All values recalculated.

## Key Numbers (v2)
- Price: $251.71 (verified — Zacks + Investing.com)
- Market Cap: $41.87B (171.3M shares x $251.71)
- Q1 2026 Revenue: $308.4M (+93% YoY) — GAAP NI $80.3M (PROFITABLE)
- Blended FV: $112 (Emma $122x40% + Quinn $109x30% + Bear $80x30%)
- MOS: -55.5% (price 55.5% above FV)
- Conviction: 6.2/10
- EV/NTM Rev: ~31x = 85-90th percentile (EXPENSIVE)

## Growth MOS
- Method 1 PASS: Implied CAGR 43.75% vs consensus 50% = 0.875x (< 1.2x gate)
- Method 2 FAIL: 31x EV/Rev > 70th percentile gate

## Recommendation: HOLD/WAIT FOR PULLBACK
- Entry T1: $130-160 | T2: $110-130
- Stop Loss: $100 (-20% from T1 midpoint $125)
- Max Position: 3% (TC x0.75 multiplier)
- Deploy Gate: Conviction <7.0 FAIL + Growth MOS M2 FAIL + TC Regime suspended

## Bear Challenges (v2)
- P/E ~130x annualized NTM — priced for perfection
- SBC dilution ~5% annually reduces per-share value
- 31x EV/Rev = only justified if 50%+ CAGR sustains 5+ years
- Customer concentration: Microsoft/Google/AWS = >80% revenue

## What Would Change Our Mind
- Bull: Price pullback to $130-160 (T1) + Regime RISK-ON + Q2 2026 Revenue >$380M
- Bear: Revenue miss <$280M OR hyperscaler capex cut announcement
- Thesis Invalidation: CXL standard not adopted by next-gen GPU (H200+ successor)

*Report: reports/ALAB_2026-05-20.md | Updated: 2026-05-20*`
  }"""

# Pattern to find existing ALAB object — search for ticker: "ALAB" block
pattern = r'\{\s*\n\s*ticker:\s*"ALAB".*?\}'
match = re.search(pattern, content, re.DOTALL)

if match:
    content = content[:match.start()] + new_alab.strip() + content[match.end():]
    print(f"[OK] Replaced existing ALAB object at position {match.start()}")
else:
    # Insert before closing bracket of REPORTS array
    insert_pattern = r'(\]\s*;\s*\n\s*(?:const|var|let)\s+LAST_UPDATED|\]\s*;\s*$)'
    insert_match = re.search(insert_pattern, content, re.MULTILINE)
    if insert_match:
        insert_pos = insert_match.start()
        content = content[:insert_pos] + new_alab.strip() + ",\n" + content[insert_pos:]
        print(f"[OK] Inserted new ALAB object at position {insert_pos}")
    else:
        print("[ERROR] Could not find insertion point in data.js")
        exit(1)

# Update LAST_UPDATED
content = re.sub(
    r'(LAST_UPDATED\s*=\s*["\'])[\d-]+(["\'])',
    r'\g<1>2026-05-20\g<2>',
    content
)
print("[OK] LAST_UPDATED set to 2026-05-20")

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(content)

print("[OK] data.js written")

# Validate with node
result = subprocess.run(
    ["node", "-e", "try{require('./data.js');console.log('VALID')}catch(e){console.log('ERROR:'+e.message);process.exit(1)}"],
    capture_output=True,
    text=True,
    cwd=r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard"
)

if "VALID" in result.stdout:
    print("[OK] data.js validated by node — VALID")
else:
    print(f"[ERROR] node validation failed: {result.stdout} {result.stderr}")

print("\n=== DONE: data.js updated ===")
