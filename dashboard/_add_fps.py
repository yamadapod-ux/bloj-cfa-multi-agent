#!/usr/bin/env python3
"""
Leo's dashboard update script — adds FPS to REPORTS array
Usage: python _add_fps.py
"""

import re

DATA_JS = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

FPS_OBJECT = '''  {
    ticker: "FPS",
    company: "Forgent Power Solutions, Inc.",
    date: "2026-05-22",
    version: "v1",
    sector: "Industrials — Electrical Distribution Equipment",
    price: 49.00,
    recommendation: "HOLD/WAIT",
    blendedFV: 28.65,
    esgAdjFV: 28.08,
    targetBull: 55.00,
    targetBase: 40.00,
    stopLoss: 22.92,
    convictionEmma: 5.5,
    convictionQuinn: 5.0,
    convictionBear: 7.5,
    convictionAvg: 6.0,
    mosPct: -41.7,
    pwEV: 38.00,
    beta: 1.60,
    sharpe1Y: -0.32,
    moat: "Narrow",
    esgRating: "Medium",
    esgScore: 6.3,
    macroRegime: "RISK-ON",
    sp500Reference: 5650,
    entryZone: "$25–30 (near Blended FV $28.65)",
    positionSize: "5% (Growth bucket, RISK-ON 1.0x — เมื่อ entry zone ถึง)",
    keyThesis: "AI Data Center Power Infrastructure pure-play. Revenue TTM $1.196B (+387%). Backlog $1.5B, BTB 2.3x. BUT MOS -41.7%. Growth MOS FAIL: Reverse DCF 2.09x + EV/Rev >90th pct. FCF -$97.66M, leverage 3.73x. Conviction 6.0 < gate 6.5 → ไม่ deploy ณ $49. Entry zone $25-30.",
    topRisk: "FCF ติดลบ, leverage 3.73x, cash runway <1 ปี, AI CapEx cycle pause risk, moat อ่อน (project-based re-bid), Multiple compression จาก EV/Rev 11.34x สู่ sector median 3.2x",
    bucket: "Growth",
    morganQA: "CONDITIONAL PASS",
    priceSource1: "Investing.com $48.52",
    priceSource2: "Stockanalysis $49.00",
    revenueGrowthYoY: 103,
    revenueTTM: 1196,
    revenueGuidance: "FY2026 $1,350–1,390M",
    grossMarginTTM: 34.33,
    ebitdaTTM: 164.38,
    netIncomeTTM: 25.99,
    fcfTTM: -97.66,
    netDebt: 613.73,
    netDebtToEbitda: 3.73,
    backlog: 1500,
    bookToBill: 2.3,
    forwardPE: 46.47,
    emmaFV: 24.00,
    quinnPWEV: 38.00,
    bearPWEV: 25.50,
    reverseDCFImpliedCAGR: 47,
    growthMOSStatus: "FAIL — Both methods (Reverse DCF 2.09x > 1.2x threshold, EV/Rev >90th pct > 70th pct threshold)",
    kellyPosition: 0,
    sensitivityVariables: "Revenue CAGR x EBITDA Margin Terminal",
    forwardReturnEstimate3Y: "+13.3% CAGR (45% total) from entry zone $27.50",
    fullContent: \`# FPS — Forgent Power Solutions, Inc.
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

**Date:** 2026-05-22 | **Price:** $49.00 (Verified: Investing.com $48.52 + Stockanalysis $49.00)
**Recommendation:** HOLD/WAIT FOR PULLBACK | **Blended FV:** $28.65 | **MOS:** -41.7%
**Entry Zone:** $25–30 | **Stop Loss:** $22.92 (-20% จาก entry mid $28.65)
**Conviction:** 6.0/10 | **Morgan QA:** CONDITIONAL PASS

## TL;DR
- Verdict: HOLD/WAIT — ธุรกิจดีมาก demand แข็ง แต่ราคา $49 แพงกว่า Blended FV $28.65 ถึง 42%
- ทำไม: Growth MOS FAIL ทั้ง 2 วิธี (ต้องการ 47% CAGR vs consensus 20–25%) + FCF negative + Leverage 3.73x
- Downside Risk: Bear case ดาวน์ไปถึง $5-15 (-70-90%) ถ้า AI CapEx pause + equity dilution

## Business Overview
FPS ออกแบบและผลิตระบบจ่ายไฟฟ้าแรงสูงสำหรับ AI Data Centers, Power Grids, Industrial Facilities
Revenue TTM: $1,196M (+387% YoY) | Backlog: $1.5B | Book-to-Bill: 2.3x
FCF TTM: -$97.66M (negative — scaling) | Net Debt: $613.73M | Net Debt/EBITDA: 3.73x

## Valuation Summary
Emma DCF (Base): $18.70 | Emma FV (Weighted): $24.00
Quinn P-W EV: $38.00 | WACC: 12.0% | Kelly: 0%
Bear P-W EV: $25.50 | Bear Base Case: $5.55
**Blended FV = Emma×0.40 + Quinn×0.30 + Bear×0.30 = $28.65**

## Growth MOS Check (Growth Bucket)
Reverse DCF: Implied CAGR 47% vs consensus 22.5% = 2.09x → FAILS 1.2x threshold
EV/Revenue Percentile: 11.34x = >90th percentile → FAILS 70th pct threshold
Result: GROWTH MOS FAIL — ไม่ผ่าน IPS gate

## Conviction
Emma: 5.5/10 | Quinn: 5.0/10 | Bear: 7.5/10 | Average: 6.0/10
Average 6.0/10 < Growth gate 6.5 → ไม่ deploy ณ ราคา $49

## Key Risks
1. FCF ติดลบ, leverage 3.73x, cash runway <1Y → dilution risk
2. AI CapEx Pullback (30% prob) → revenue growth crash
3. Moat อ่อน (NARROW/fragile) → margin compression ถ้า supply normalize
4. Multiple compression (P/E 46.47x → sector median 19x = -59%)

## Recommendation
HOLD/WAIT FOR PULLBACK — Entry zone $25-30 | Stop $22.92 | Rอ FCF positive + leverage < 2x

## Catalyst Calendar
Jun 2026: Q4 FY2026 Earnings [HIGH — watch guidance vs 82%]
Aug 2026: FCF Update [HIGH — positive FCF = BUY trigger]
Dec 2026: FY2027 Outlook [CRITICAL — hyperscaler CapEx 2027]
2027: Growth Normalization check [CRITICAL — BTB < 1.0x = AVOID]
\`
  }'''

with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

# Update LAST_UPDATED
content = content.replace('const LAST_UPDATED = "2026-05-21";', 'const LAST_UPDATED = "2026-05-22";')

# Find the closing ]; of REPORTS array and insert FPS before it
# The pattern is: last object ends with }, then ];
# We need to insert FPS before ];

# Find position of "];" that closes REPORTS array
# Looking for the specific pattern of the last entry
target = '\n\n];\n\n// Computed summaries'
replacement = f',\n{FPS_OBJECT}\n\n];\n\n// Computed summaries'

if target in content:
    content = content.replace(target, replacement, 1)
    print("SUCCESS: FPS object inserted into REPORTS array")
else:
    # Try alternative pattern
    target2 = '\n];\n\n// Computed summaries'
    replacement2 = f',\n{FPS_OBJECT}\n];\n\n// Computed summaries'
    if target2 in content:
        content = content.replace(target2, replacement2, 1)
        print("SUCCESS (alt pattern): FPS object inserted")
    else:
        print("ERROR: Could not find REPORTS array closing bracket")
        print("Looking for pattern near line 5086...")
        # Print lines around 5086
        lines = content.split('\n')
        for i in range(max(0, 5080-1), min(len(lines), 5095)):
            print(f"Line {i+1}: {repr(lines[i][:80])}")
        exit(1)

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(content)

print("DONE: dashboard/data.js updated with FPS entry")
print("Run: node -e \"const d = require('./data.js'); console.log('OK: REPORTS count =', d.REPORTS ? 'loaded' : 'error')\" to verify")
