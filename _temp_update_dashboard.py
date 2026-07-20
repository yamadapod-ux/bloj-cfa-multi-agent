#!/usr/bin/env python3
"""Leo: Add RDDT entry to dashboard/data.js via Python binary script (NOT Write tool)"""

import re

data_js_path = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

# Read as binary to preserve all content
with open(data_js_path, 'rb') as f:
    raw = f.read()

content = raw.decode('utf-8')

# Update LAST_UPDATED
content = content.replace('const LAST_UPDATED = "2026-05-29";', 'const LAST_UPDATED = "2026-05-30";')

# Build the new RDDT entry
report_content = r"""# RDDT — Reddit, Inc.
## BUY Growth Bucket T1 (8%) | Blended FV $169.25 | MOS -3.8% | Conviction 6.67/10

### TL;DR
- Revenue +69% YoY, Q2 guided +72% — highest growth rate in portfolio
- AI data licensing ($400M/yr potential) = emerging WIDE moat not priced in EV/Rev 12.6x
- Meta Forum (May 2026) + Google double-dependency = twin tail risks; stop $140.75

### Blended FV: Emma $140 x40% + Quinn $248.50 x30% + Bear $129 x30% = $169.25
### Growth MOS: Reverse DCF 1.03x (pass) + 55-60th pct multiple (pass)
### Entry Zone: $155-178 | Target: $226 base / $317 bull | Stop: $140.75 (-20%)"""

new_entry = """,
  {
    ticker: "RDDT",
    company: "Reddit, Inc.",
    date: "2026-05-30",
    version: "v1",
    sector: "Communication Services / Social Media",
    price: 175.94,
    recommendation: "BUY",
    blendedFV: 169.25,
    targetBull: 317.00,
    targetBase: 226.00,
    stopLoss: 140.75,
    convictionEmma: 7,
    convictionQuinn: 7,
    convictionBear: 6,
    convictionAvg: 6.67,
    mosPct: -3.8,
    pwEV: 248.50,
    beta: 1.80,
    sharpe1Y: 0.335,
    maxDrawdown: -0.65,
    moat: "Narrow+",
    esgRating: "Medium",
    esgScore: 6.0,
    esgAdjFV: 163.00,
    entryZoneLow: 155.00,
    entryZoneHigh: 178.00,
    maxPositionPct: 8,
    bucket: "Growth",
    macroRegime: "RISK-ON",
    sp500Ref: 7591.42,
    wacc: 13.5,
    revenueGrowthTTM: 70.6,
    grossMarginPct: 91.4,
    fcfYieldPct: 2.57,
    roic: 56.7,
    reportFile: "reports/RDDT_2026-05-30.md",
    businessSummary: "Reddit เป็น social media platform ที่มี 126.8M DAUq ใน 100,000+ niche communities มีรายได้หลักจาก digital advertising (94%) และ AI data licensing (6% high-growth). Revenue +69% YoY Q1 2026. Debt-free, $2.77B net cash. ROIC 56.7% (asset-light).",
    thesisBullets: [
      "Revenue +69% YoY accelerating — Q2 2026 guided +72% ($715-725M)",
      "AI data licensing = irreplicable 18-year UGC corpus; Google $60M/yr → $400M/yr by 2027 potential",
      "ARPU $5.23 growing +45% YoY with massive gap to META $40+ = long monetization runway",
      "Debt-free $2.77B net cash = 8.2% of market cap; no dilution risk",
      "Growth MOS both tests pass at $175.94 (Reverse DCF 1.03x + 55-60th pct multiple)"
    ],
    esgBreakdown: {
      environmental: 7,
      social: 5,
      governance: 6,
      overall: 6.0,
      keyRisk: "Content moderation at scale; AI data ethics (user consent); dual-class governance"
    },
    revenueSegments: [
      { name: "Advertising", pct: 94, yoyGrowth: 74 },
      { name: "AI Data Licensing & Other", pct: 6, yoyGrowth: 15 }
    ],
    competitorData: [
      { name: "Reddit (RDDT)", evRev: 12.6, revGrowth: 69, grossMargin: 91.4, arpu: 5.23, moat: "Narrow+" },
      { name: "Snap (SNAP)", evRev: 4.0, revGrowth: 11, grossMargin: 52, arpu: 2.50, moat: "Narrow" },
      { name: "Pinterest (PINS)", evRev: 5.0, revGrowth: 17, grossMargin: 80, arpu: 1.73, moat: "Narrow" },
      { name: "Meta (META)", evRev: 7.5, revGrowth: 33, grossMargin: 82, arpu: 40.0, moat: "Wide" }
    ],
    geographyRevenue: [
      { region: "United States", pct: 77, note: "High ARPU market" },
      { region: "International", pct: 23, note: "Growing faster, lower ARPU" }
    ],
    bullFlipTriggers: [
      "AI licensing revenue crosses $200M/year",
      "ARPU reaches $8+ in 2 consecutive quarters",
      "Meta Forum DAU < 10M after 12 months",
      "Google data deal renewal at $100M+ (2027)",
      "International ARPU reaches $3+ by FY2027"
    ],
    bearFlipTriggers: [
      "DAU growth falls below +10% YoY for 2 consecutive quarters",
      "ARPU growth slows below +20% YoY",
      "Google AI Overview reduces Reddit traffic by >15%",
      "Meta Forum DAU exceeds 50M within 18 months",
      "Q3 2026 revenue miss vs guidance by >5%"
    ],
    thesisInvalidation: [
      "Google terminates data deal AND DAU growth < 10% simultaneously",
      "Revenue growth < 20% YoY + EBITDA margin < 25% convergence",
      "EU GDPR enforcement banning AI data licensing"
    ],
    maxDrawdown: -0.65
  }
"""

# Find insertion point: before the closing ];
insertion_target = "\n];"
if insertion_target in content:
    # Find the LAST occurrence (closing of REPORTS array)
    last_pos = content.rfind(insertion_target)
    content = content[:last_pos] + new_entry + content[last_pos:]
    print("Inserted RDDT entry before closing ];")
else:
    print("ERROR: Could not find ]; in data.js")
    exit(1)

# Write back as binary
with open(data_js_path, 'wb') as f:
    f.write(content.encode('utf-8'))

print("dashboard/data.js updated successfully")

# Verify with node check
import subprocess
result = subprocess.run(['node', '--check', data_js_path], capture_output=True, text=True)
if result.returncode == 0:
    print("Node syntax check: PASS")
else:
    print(f"Node syntax check: FAIL")
    print(result.stderr)
