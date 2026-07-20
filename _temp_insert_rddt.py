#!/usr/bin/env python3
"""
Leo: Insert RDDT entry into dashboard/data.js at line 5360 (before ];)
Uses binary read/write to preserve all content exactly.
"""
import os
import subprocess
import sys

data_js_path = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

# Read as binary
with open(data_js_path, 'rb') as f:
    raw = f.read()

content = raw.decode('utf-8')

# 1. Update LAST_UPDATED
old_date = 'const LAST_UPDATED = "2026-05-29";'
new_date = 'const LAST_UPDATED = "2026-05-30";'
if old_date in content:
    content = content.replace(old_date, new_date, 1)
    print("LAST_UPDATED updated to 2026-05-30")
else:
    print("WARNING: LAST_UPDATED pattern not found")

# 2. The RDDT entry to insert
rddt_entry = """,
  {
    ticker: "RDDT",
    company: "Reddit, Inc.",
    date: "2026-05-30",
    version: "v1",
    sector: "Communication Services / Social Media",
    price: 175.94,
    recommendation: "BUY",
    blendedFV: 169.25,
    esgAdjFV: 163.00,
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
    businessSummary: "Reddit เป็น social media platform 126.8M DAUq ใน 100,000+ niche communities. รายได้หลัก digital advertising 94% + AI data licensing 6% (high-growth). Revenue +69% YoY Q1 2026. Debt-free $2.77B net cash. ROIC 56.7% asset-light.",
    thesisBullets: [
      "Revenue +69% YoY accelerating — Q2 2026 guided +72% ($715-725M)",
      "AI data licensing = irreplicable 18-year UGC corpus; Google $60M/yr to $400M/yr potential by 2027",
      "ARPU $5.23 growing +45% YoY with massive gap to META $40+ = long monetization runway",
      "Debt-free $2.77B net cash (8.2% of market cap); no dilution risk",
      "Growth MOS both tests pass: Reverse DCF 1.03x + 55-60th pct multiple percentile"
    ],
    esgBreakdown: {
      environmental: 7,
      social: 5,
      governance: 6,
      overall: 6.0,
      keyRisk: "Content moderation at scale; AI data ethics (user consent for training); dual-class governance Huffman control"
    },
    revenueSegments: [
      { label: "Advertising", value: 94 },
      { label: "AI Data Licensing & Other", value: 6 }
    ],
    competitorData: [
      { ticker: "RDDT", company: "Reddit", evRev: 12.6, revGrowth: 69, grossMargin: 91.4, arpu: 5.23, moat: "Narrow+" },
      { ticker: "SNAP", company: "Snap", evRev: 4.0, revGrowth: 11, grossMargin: 52, arpu: 2.50, moat: "Narrow" },
      { ticker: "PINS", company: "Pinterest", evRev: 5.0, revGrowth: 17, grossMargin: 80, arpu: 1.73, moat: "Narrow" },
      { ticker: "META", company: "Meta Platforms", evRev: 7.5, revGrowth: 33, grossMargin: 82, arpu: 40.0, moat: "Wide" }
    ],
    geographyRevenue: [
      { region: "United States", pct: 77, note: "Primary ARPU market" },
      { region: "International", pct: 23, note: "Growing faster, lower ARPU — expansion opportunity" }
    ],
    bullFlipTriggers: [
      "AI licensing revenue crosses $200M/year — data moat commercial validation",
      "ARPU reaches $8+ in 2 consecutive quarters — monetization gap closing",
      "Meta Forum DAU less than 10M after 12 months — community moat validated",
      "Google data deal renewal at $100M+ (2027) — licensing moat strengthens",
      "International ARPU reaches $3+ by FY2027 — TAM expansion confirmed"
    ],
    bearFlipTriggers: [
      "DAU growth falls below 10% YoY for 2 consecutive quarters",
      "ARPU growth slows below 20% YoY",
      "Google AI Overview measurably reduces Reddit traffic by more than 15%",
      "Meta Forum DAU exceeds 50M within 18 months of launch",
      "Q3 2026 revenue misses guidance by more than 5%"
    ],
    thesisInvalidation: [
      "Google terminates data deal AND DAU growth below 10% simultaneously",
      "Revenue growth below 20% YoY AND EBITDA margin below 25% convergence",
      "EU GDPR enforcement action banning AI data licensing"
    ],
    keyThesis: "Reddit emerging as AI data infrastructure company with irreplicable 18-year UGC corpus. Revenue +69% YoY. ARPU $5.23 growing 45% YoY. AI licensing $60M/yr to $400M/yr potential. Growth MOS both tests pass at $175.94.",
    topRisk: "Meta Forum app launched May 2026 with 3B+ MAU distribution. Google double-dependency (traffic referral 25-30% + data deal). Bear FV $129. One year GAAP profit history.",
    entryZone: "$155-178 (T1 5% immediate) / $145-160 (T2 3% after Meta Forum assessment or AI licensing $200M+)",
    positionSize: "8% max (RISK-ON 1.0x; T1 5% = ~3 shares at $175.94; T2 3% conditional)",
    fullContent: "## RDDT - Reddit, Inc. | BUY Growth Bucket\\n### Blended FV $169.25 (Emma $140x40% + Quinn $248.50x30% + Bear $129x30%)\\n### MOS -3.8% (Growth MOS gates BOTH pass) | Conviction 6.67/10\\n\\n## Analysis: 2026-05-30 | Price: $175.94 | Stop: $140.75 (-20%)\\n## Entry Zone: $155-178 | Target: $226 (base) / $317 (bull)\\n\\n## Bull Thesis:\\n1. Revenue +69% YoY accelerating; Q2 guided +72%\\n2. AI data licensing = irreplicable 18-year corpus; $400M/yr potential\\n3. ARPU $5.23 massive gap to META $40+ = long runway\\n4. Debt-free $2.77B net cash; ROIC 56.7%\\n\\n## Bear Case:\\n1. Meta Forum launched May 2026 with 3B MAU distribution\\n2. Google double-dependency (traffic + data deal both at risk)\\n3. Only 1 year GAAP profit history\\n4. Bear FV $129\\n\\n## Sensitivity Matrix (Revenue Growth x EV/Rev Exit):\\n15% growth, 7x = $96 | 30% growth, 11x = $226 (base)\\n40% growth, 13x = $328 | 55% growth, 15x = $481\\n44% of 25 scenarios justify current price\\n\\nSource: reports/RDDT_2026-05-30.md"
  }
"""

# 3. Find insertion point: the line "  }\n];" (end of REPORTS array)
# Looking for the exact closing of the last entry before ];
close_pattern = "\n];"
# Find the last occurrence
last_idx = content.rfind(close_pattern)
if last_idx == -1:
    print("ERROR: Could not find closing ]; in file")
    sys.exit(1)

content = content[:last_idx] + rddt_entry + content[last_idx:]
print(f"RDDT entry inserted at position {last_idx}")

# 4. Write back as binary
with open(data_js_path, 'wb') as f:
    f.write(content.encode('utf-8'))

file_size = os.path.getsize(data_js_path)
print(f"File written: {file_size} bytes")

# 5. Syntax check
result = subprocess.run(
    ['node', '--check', data_js_path],
    capture_output=True, text=True
)
if result.returncode == 0:
    print("Node --check: PASS")
else:
    print(f"Node --check: FAIL")
    print("STDOUT:", result.stdout[:500])
    print("STDERR:", result.stderr[:500])
    sys.exit(1)

print("dashboard/data.js updated successfully with RDDT entry")
