#!/usr/bin/env python3
"""
Leo's dashboard update script — adds FPS to REPORTS array
"""

DATA_JS = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

FPS_OBJECT = """  {
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
    entryZone: "$25-30",
    positionSize: "5% Growth bucket RISK-ON",
    keyThesis: "AI Data Center Power Infrastructure pure-play. Revenue TTM $1.196B (+387%). Backlog $1.5B, BTB 2.3x. BUT MOS -41.7%. Growth MOS FAIL. FCF -$97.66M, leverage 3.73x. Entry zone $25-30.",
    topRisk: "FCF negative, leverage 3.73x, cash runway <1Y, AI CapEx pause risk, moat fragile",
    bucket: "Growth",
    morganQA: "CONDITIONAL PASS",
    revenueGrowthYoY: 103,
    revenueTTM: 1196,
    grossMarginTTM: 34.33,
    fcfTTM: -97.66,
    netDebt: 613.73,
    netDebtToEbitda: 3.73,
    backlog: 1500,
    bookToBill: 2.3,
    emmaFV: 24.00,
    quinnPWEV: 38.00,
    bearPWEV: 25.50,
    kellyPosition: 0,
    growthMOSStatus: "FAIL",
    fullContent: "FPS HOLD/WAIT | Price $49 | Blended FV $28.65 | MOS -41.7% | Conviction 6.0/10 | Growth MOS FAIL (Reverse DCF 2.09x, EV/Rev >90th pct) | Entry $25-30 | Stop $22.92 | FCF -$97.66M | Leverage 3.73x | Regime RISK-ON | Morgan CONDITIONAL PASS | 2026-05-22"
  }"""

with open(DATA_JS, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Update LAST_UPDATED on line 4
for i, line in enumerate(lines):
    if 'const LAST_UPDATED' in line:
        lines[i] = 'const LAST_UPDATED = "2026-05-22";\n'
        print(f"Updated LAST_UPDATED on line {i+1}")
        break

# Find the closing ]; line of REPORTS array
# Look for lines[5085] which is "];"
closing_idx = None
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped == '];' and i > 5000:
        closing_idx = i
        print(f"Found REPORTS closing ]; at line {i+1}")
        break

if closing_idx is None:
    print("ERROR: Could not find REPORTS closing ];")
    # Debug
    for i in range(5080, min(len(lines), 5095)):
        print(f"Line {i+1}: {repr(lines[i][:60])}")
else:
    # Insert FPS before the closing ];
    # Change line before ]; to add comma if needed (line 5084 ends with },)
    # Insert: FPS_OBJECT + newline before ];
    new_lines = lines[:closing_idx] + [FPS_OBJECT + '\n\n', lines[closing_idx]] + lines[closing_idx+1:]

    with open(DATA_JS, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print("SUCCESS: FPS object inserted into data.js")
    print(f"Total lines: {len(new_lines)}")

# Verify
with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

if '"FPS"' in content and 'LAST_UPDATED = "2026-05-22"' in content:
    print("VERIFICATION PASS: FPS found in data.js and LAST_UPDATED updated")
else:
    print("VERIFICATION FAIL: Check manually")
    if '"FPS"' not in content:
        print("  - FPS ticker not found")
    if 'LAST_UPDATED = "2026-05-22"' not in content:
        print("  - LAST_UPDATED not updated")
