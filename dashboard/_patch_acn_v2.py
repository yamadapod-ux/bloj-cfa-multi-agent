#!/usr/bin/env python3
"""
Patch dashboard/data.js to add ACN entry.
Safe binary insert after REGN entry.
Tested approach: find closing marker and insert before it.
"""
import os
import re

BASE = r"C:\Users\user\Desktop\บลจ\บลจ CFA"
DATA_JS = os.path.join(BASE, "dashboard", "data.js")

# Read file
with open(DATA_JS, "r", encoding="utf-8") as f:
    content = f.read()

# Check if ACN already exists
if 'ticker: "ACN"' in content:
    print("ACN entry already exists in data.js — skipping insertion")
else:
    ACN_ENTRY = """  {
    ticker: "ACN",
    company: "Accenture PLC",
    date: "2026-06-05",
    version: "v1",
    sector: "IT Services / AI Consulting",
    price: 178.16,
    recommendation: "BUY",
    bucket: "Value",
    blendedFV: 252.35,
    esgAdjFV: 239.73,
    targetBull: 320.00,
    targetBase: 252.35,
    stopLoss: 148.00,
    convictionEmma: 8,
    convictionQuinn: 7,
    convictionBear: 6.5,
    convictionAvg: 7.17,
    mosPct: 41.6,
    pwEV: 285.00,
    beta: 0.90,
    sharpe1Y: 0.64,
    maxDrawdown: -0.43,
    moat: "Wide",
    esgRating: "Medium-High",
    esgScore: 6.65,
    macroRegime: "RISK-ON 4/4",
    sp500Ref: 7553.68,
    wacc: 9.5,
    roic: 27.19,
    roe: 24.76,
    pe: 14.54,
    evEbitda: 8.51,
    fcfYield: 11.42,
    revenueGrowth: "+8% USD / +13% LC (Q2 FY26)",
    keyThesis: "Market pricing AI destruction of IT consulting; ACN Bookings ATH $22.1B Q2 FY26 = demand for AI implementation accelerating not declining. ROIC 27.19% >> WACC 9.5% = EVA spread +17.7% = genuine Wide Moat. FCF Yield 11.42% = market pricing 50-60% FCF decline that management rejects (FY26 guide RAISED). P/E 14.54x = 31% discount vs peer median 21x.",
    topRisk: "AI disruption of headcount model (structural, slow-burn); FX headwind -2-3% revenue annually; Hyperscaler bundling (Microsoft/Google); P/E multiple stays compressed at 17-18x",
    entryZone: "$175-192 (T1) / $155-175 (T2) / $140-155 (T3 conditional)",
    positionSize: "8-10% (T1 5%, T2 3%, T3 2%) -- RISK-ON 1.0x multiplier",
    bullFlipTriggers: [
      "Bookings sustain $20B+ for 3 consecutive quarters",
      "AI revenue reaches $10B/year run rate",
      "EBIT margin expands to 17%+ in any quarter",
      "Hyperscaler partnership deepens (partner not compete)",
      "P/E re-rates above 18x"
    ],
    bearFlipTriggers: [
      "Revenue growth falls below 5% for 2+ consecutive quarters",
      "Bookings drop below $18B/quarter",
      "EBIT margin falls below 14%",
      "Hyperscaler bundling at scale confirmed",
      "FCF guide cut significantly"
    ],
    thesisInvalidation: "Bookings fall 3 consecutive quarters + Revenue below 4% simultaneously; OR ACN announces >10% workforce reduction attributed to AI",
    reportFile: "reports/ACN_2026-06-05.md",
    businessSummary: "Accenture PLC -- Global leader in IT Services and AI Consulting. 780,000 employees in 120+ countries. Strategy & Consulting (~25%), Technology Services (~45%), Operations/Managed Services (~30%). Wide Moat: switching costs (multi-year projects), scale (780K employees), client relationships (avg 8-12yr), 200+ alliances with hyperscalers. Revenue Q2 FY26 $18.0B +8% USD. Bookings $22.1B all-time record. FCF Guide FY26 raised to $10.8-11.5B.",
    thesisBullets: [
      "Bookings ATH $22.1B Q2 FY26 = AI implementation demand accelerating, not declining",
      "ROIC 27.19% >> WACC 9.5% = EVA spread +17.7% = genuine Wide Moat confirmed",
      "FCF Yield 11.42% = most attractive in IT Services (fair value yield 4-6%)",
      "P/E 14.54x = 31% discount vs peer median 21x = Best quality at worst valuation",
      "ADBE/CRM pattern: AI fear drives -43% on Wide Moat = buy opportunity"
    ],
    esgBreakdown: {
      e: 6.5,
      s: 6.0,
      g: 7.5,
      overall: 6.65,
      keyRisk: "AI workforce displacement 780K employees (Social risk); Irish tax optimization (Governance ESG flag); Scope 3 travel emissions",
      valuationImpact: "-5% ESG haircut applied"
    },
    revenueSegments: [
      { label: "Technology Services", value: 45, revenue: "~$8.1B/qtr", growth: "+10% LC" },
      { label: "Strategy & Consulting", value: 25, revenue: "~$4.5B/qtr", growth: "+8% LC" },
      { label: "Operations / Managed Services", value: 30, revenue: "~$5.4B/qtr", growth: "+12% LC" }
    ],
    competitorData: [
      { ticker: "ACN", company: "Accenture", pe: 14.54, evEbitda: 8.51, roic: 27.19, revenueGrowth: 8, moat: "Wide" },
      { ticker: "IBM", company: "IBM Corp.", pe: 22.1, evEbitda: 12.3, roic: 8.9, revenueGrowth: 1.5, moat: "Narrow" },
      { ticker: "INFY", company: "Infosys", pe: 22.5, evEbitda: 15.2, roic: 22.1, revenueGrowth: 7.6, moat: "Narrow" },
      { ticker: "TCS", company: "Tata Consultancy", pe: 24.8, evEbitda: 18.1, roic: 36.4, revenueGrowth: 6.2, moat: "Narrow+" }
    ],
    geographyRevenue: {
      northAmerica: "~43% (+10% LC)",
      europe: "~33% (+7% LC)",
      growthMarkets: "~24% (+12% LC)",
      fxImpact: "-5pp USD headwind on USD revenue reporting"
    },
    fullContent: "## ACN - Accenture PLC | BUY Value Bucket\\n### Blended FV $252.35 (Emma $287x40% + Quinn $285x30% + Bear $173.50x30%)\\n### MOS +41.6% | Conviction 7.17/10\\n\\n## Analysis: 2026-06-05 | Price: $178.16 | Stop: $148 (-20%)\\n## Entry Zone: T1 $175-192 (5%) / T2 $155-175 (3%) / T3 $140-155 (2%)\\n\\n## Bull Thesis:\\n1. Bookings ATH $22.1B Q2 FY26 = AI implementation demand accelerating\\n2. ROIC 27% >> WACC 9.5% = EVA spread +17.7% = genuine Wide Moat\\n3. FCF Yield 11.42% = most attractive in IT Services peer group\\n4. P/E 14.54x = 31% discount vs peer median\\n5. Same pattern ADBE/CRM: AI fear drives -43% on Wide Moat = opportunity\\n\\n## Bear Case:\\n1. AI disruption = structural headcount model risk\\n2. Margin expansion assumption backwards (talent war + pricing pressure)\\n3. P/E 17x new normal not 21x mean reversion\\n4. FX headwind -2-3%/year systematically undermodeled\\n\\n## Sensitivity (Revenue CAGR x WACC):\\n96% of 25 scenarios above current price $178\\n72% of 25 scenarios above MOS threshold $205\\n\\nSee full report: reports/ACN_2026-06-05.md"
  },
"""

    # Find the closing ]; of REPORTS array
    # Look for the REGN entry end, then insert ACN after it
    insert_marker = "  },\n];"
    if insert_marker in content:
        insert_pos = content.rfind(insert_marker)
        # Insert ACN before the closing ];
        content = content[:insert_pos + 4] + ACN_ENTRY + content[insert_pos + 4:]
        print(f"ACN entry inserted at position {insert_pos}")
    else:
        print("ERROR: Could not find closing ]; in REPORTS array")
        exit(1)

# Update LAST_UPDATED
content = re.sub(
    r'const LAST_UPDATED = "[^"]*"',
    'const LAST_UPDATED = "2026-06-05"',
    content
)
print("LAST_UPDATED updated to 2026-06-05")

# Write back
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(content)

print("data.js patched successfully")
print(f"File size: {len(content)} chars")

# Quick sanity check
if 'ticker: "ACN"' in content:
    print("VERIFY: ACN entry found in data.js")
else:
    print("ERROR: ACN entry NOT found after insert!")

if 'const LAST_UPDATED = "2026-06-05"' in content:
    print("VERIFY: LAST_UPDATED = 2026-06-05 confirmed")
