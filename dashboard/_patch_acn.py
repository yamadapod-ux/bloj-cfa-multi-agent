#!/usr/bin/env python3
"""
Patch dashboard/data.js to add ACN entry.
Safe binary insert — does NOT rewrite whole file.
"""
import os
import re

BASE = r"C:\Users\user\Desktop\บลจ\บลจ CFA"
DATA_JS = os.path.join(BASE, "dashboard", "data.js")

ACN_ENTRY = r"""  {
    ticker: "ACN",
    company: "Accenture PLC",
    date: "2026-06-05",
    recommendation: "BUY",
    bucket: "Value",
    price: 178.16,
    blendedFV: 252.35,
    esgAdjFV: 239.73,
    mos: 41.6,
    conviction: 7.17,
    stopLoss: 148,
    entryZone: "$175-192 (T1) / $155-175 (T2)",
    maxPosition: "8-10%",
    horizon: "3-5 years",
    regime: "RISK-ON 4/4",
    sector: "IT Services / AI Consulting",
    moat: "Wide",
    beta: 0.90,
    roic: 27.19,
    roe: 24.76,
    pe: 14.54,
    evEbitda: 8.51,
    fcfYield: 11.42,
    revenueGrowth: "+8% USD / +13% LC (Q2 FY26)",
    reportFile: "reports/ACN_2026-06-05.md",
    maxDrawdown: -43,
    businessSummary: "Accenture PLC — Global leader in IT Services, Strategy, Consulting, Technology, and Operations. 780,000 employees across 120+ countries. Wide Moat through switching costs, scale, client relationships (avg 8-12yr), and 200+ hyperscaler alliances. Revenue Q2 FY26 $18.0B +8% USD. Bookings $22.1B all-time record.",
    thesisBullets: [
      "Market pricing AI destruction; data shows AI acceleration — Bookings ATH $22.1B Q2 FY26",
      "ROIC 27.19% >> WACC 9.5% = EVA spread +17.7% = genuine Wide Moat confirmed",
      "FCF Yield 11.42% = market pricing 50-60% FCF decline that management rejects (FY26 guide raised)",
      "P/E 14.54x = 31% discount vs peer median 21x = Best quality at worst valuation in IT Services",
      "Same pattern as ADBE/CRM: AI fear drives -43% drawdown on Wide Moat company = buy opportunity"
    ],
    esgBreakdown: {
      e: 6.5,
      s: 6.0,
      g: 7.5,
      overall: 6.65,
      materialRisks: "AI workforce displacement 780K employees (S risk); Irish tax structure (G ESG flag); Scope 3 travel emissions",
      valuationImpact: "-5% ESG haircut"
    },
    revenueSegments: {
      "Strategy & Consulting": "25%",
      "Technology Services": "45%",
      "Operations / Managed Services": "30%"
    },
    competitorData: [
      { name: "IBM", pe: 22.1, evEbitda: 12.3, roic: 8.9, revenueGrowth: "+1.5%", moat: "NARROW" },
      { name: "Infosys", pe: 22.5, evEbitda: 15.2, roic: 22.1, revenueGrowth: "+7.6%", moat: "NARROW" },
      { name: "TCS", pe: 24.8, evEbitda: 18.1, roic: 36.4, revenueGrowth: "+6.2%", moat: "NARROW+" },
      { name: "Capgemini", pe: 15.2, evEbitda: 9.8, roic: 16.2, revenueGrowth: "+5.1%", moat: "NARROW" }
    ],
    geographyRevenue: {
      "North America": "43%",
      "Europe": "33%",
      "Growth Markets": "24%"
    },
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
    thesisInvalidation: "Bookings fall 3 consecutive quarters + Revenue below 4% simultaneously; OR ACN announces >10% workforce reduction attributed to AI"
  },
"""

# Read file as bytes to preserve all formatting
with open(DATA_JS, "rb") as f:
    raw = f.read()

content = raw.decode("utf-8")

# Check if ACN already exists
if '"ACN"' in content and 'ticker: "ACN"' in content:
    print("ACN entry already exists in data.js — skipping")
else:
    # Find the insert position: before the closing ];
    # Look for the last },\n]; pattern
    insert_target = b"  },\n];"
    if insert_target in raw:
        insert_pos = raw.rfind(insert_target) + len(insert_target) - 2  # before ];
        new_entry_bytes = ACN_ENTRY.encode("utf-8")
        raw = raw[:insert_pos] + new_entry_bytes + raw[insert_pos:]
        print(f"ACN entry inserted at position {insert_pos}")
    else:
        # Try alternative: find ];\n at end
        alt_target = b"];"
        insert_pos = raw.rfind(alt_target)
        if insert_pos > 0:
            new_entry_bytes = ACN_ENTRY.encode("utf-8")
            raw = raw[:insert_pos] + new_entry_bytes + raw[insert_pos:]
            print(f"ACN entry inserted (alt method) at position {insert_pos}")
        else:
            print("ERROR: Could not find insert position in data.js")
            exit(1)

    # Update LAST_UPDATED
    content = raw.decode("utf-8")
    # Replace old date
    import re
    content = re.sub(
        r'const LAST_UPDATED = "[^"]*"',
        'const LAST_UPDATED = "2026-06-05"',
        content
    )

    with open(DATA_JS, "w", encoding="utf-8") as f:
        f.write(content)

    print("data.js updated successfully with ACN entry")
    print(f"File size: {len(content)} chars")

# Verify with node --check
import subprocess
result = subprocess.run(
    ["node", "--check", DATA_JS],
    capture_output=True, text=True
)
if result.returncode == 0:
    print("node --check PASSED — data.js syntax valid")
else:
    print("node --check FAILED:")
    print(result.stderr)
