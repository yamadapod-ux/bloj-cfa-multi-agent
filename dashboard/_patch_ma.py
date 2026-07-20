#!/usr/bin/env python3
"""
_patch_ma.py — Add MA (Mastercard) entry to dashboard/data.js
Run: python dashboard/_patch_ma.py
"""

import re, sys, os

DATA_JS = os.path.join(os.path.dirname(__file__), "data.js")

MA_ENTRY = r"""  {
    ticker: "MA",
    company: "Mastercard Incorporated",
    date: "2026-06-07",
    version: "v1",
    sector: "Financial Services / Payment Networks",
    bucket: "Value",
    price: 484.00,
    recommendation: "HOLD/WAIT",
    blendedFV: 430.00,
    esgAdjFV: 409.00,
    targetBull: 580.00,
    targetBase: 500.00,
    stopLoss: 387.00,
    convictionEmma: 7.0,
    convictionQuinn: 6.5,
    convictionBear: 7.5,
    convictionAvg: 7.0,
    mosPct: -11.6,
    pwEV: 480.00,
    beta: 0.95,
    sharpe1Y: 0.90,
    maxDrawdown: -0.32,
    moat: "Wide",
    esgRating: "Medium-High",
    esgScore: 6.8,
    entryZone: "$410–440 (T1) / $380–410 (T2)",
    maxPosition: "5%",
    macroRegime: "RISK-ON 4/4",
    forwardSharpe: -0.20,
    kellyPct: 0.0,
    wacc: 9.5,
    roic: 95.0,
    revenueGrowth: 11.0,
    emmaFV: 427.00,
    quinnFV: 480.00,
    bearFV: 385.00,
    sp500Ref: "~7,600-7,700 (est. June 6)",
    reportFile: "reports/MA_2026-06-07.md",
    maxDrawdown: -0.32,
    businessSummary: "Mastercard คือ Global Payment Network Duopoly — Toll Road บน Global Commerce. MA ประมวลผล transactions ผ่าน 3.3B+ cards ใน 210+ ประเทศ โดยไม่รับ credit risk = ROIC 95% = สูงที่สุดใน Value bucket",
    thesisBullets: [
      "Network Effect Moat (Irreplaceable) — 3.3B cards × 90M merchants × 210 countries = ไม่มีใครสร้างซ้ำได้ใน 10+ ปี",
      "Cross-Border Premium Revenue — international volume ~65% of revenue; travel recovery = structural tailwind",
      "Value-Added Services Growth Engine — Cyber/Data Analytics >20% YoY = P/E re-rating opportunity"
    ],
    esgBreakdown: { e: 8, s: 5, g: 7.5, overall: 6.8 },
    revenueSegments: [
      { name: "Service Fees", pct: 33 },
      { name: "Assessment/Domestic Fees", pct: 39 },
      { name: "Cross-Border Volume", pct: 20 },
      { name: "Processing Fees", pct: 8 }
    ],
    competitorData: [
      { ticker: "V", company: "Visa Inc.", pe: 30, evEbitda: 24, roic: 50, revGrowth: 10, moat: "Wide" },
      { ticker: "AXP", company: "American Express", pe: 18, evEbitda: 13, roic: 30, revGrowth: 9, moat: "Wide" },
      { ticker: "PYPL", company: "PayPal Holdings", pe: 15, evEbitda: 11, roic: 15, revGrowth: 6, moat: "Narrow" },
      { ticker: "FI", company: "Fiserv Inc.", pe: 16, evEbitda: 14, roic: 12, revGrowth: 11, moat: "Narrow" }
    ],
    geographyRevenue: [
      { region: "United States", pct: 35 },
      { region: "Europe", pct: 23 },
      { region: "Asia Pacific", pct: 20 },
      { region: "Latin America", pct: 11 },
      { region: "Other (MEA)", pct: 11 }
    ],
    bullFlipTriggers: [
      "Price pullback to $410-430 (MOS ≥ 8% vs Blended FV $430)",
      "Revenue growth re-accelerating >14% for 2 consecutive quarters",
      "Stablecoin legislation = MA integration model (MA earns from stablecoin rails)",
      "VAS Revenue >25% of total revenue (platform re-rating)",
      "India government digital payment contract won by MA"
    ],
    bearFlipTriggers: [
      "GENIUS Act or equivalent stablecoin bill passes in adverse form",
      "EU PSD3 mandates open banking at scale (Europe 23% revenue at risk)",
      "Revenue growth <9% for 2 consecutive quarters",
      "FedNow bank adoption >10% of bank-to-bank transactions",
      "Major data breach (100M+ cards)"
    ],
    thesisInvalidation: "Stablecoin regulation mandates interchange-free digital payments at scale → Exit immediately; thesis permanently broken"
  }"""

def patch():
    with open(DATA_JS, "rb") as f:
        content = f.read().decode("utf-8")

    # Check MA not already present
    if '"MA"' in content and 'ticker: "MA"' in content:
        print("MA entry already exists — skipping to avoid duplicate")
        return

    # Find insertion point: before last "];" in REPORTS array
    # Pattern: find "}," followed eventually by "];"
    insert_marker = "};\n];"
    alt_marker = "  }\n];"

    if insert_marker in content:
        idx = content.rfind(insert_marker)
        new_content = content[:idx + len("};")] + ",\n" + MA_ENTRY + "\n];"
    elif alt_marker in content:
        idx = content.rfind(alt_marker)
        new_content = content[:idx + len("  }")] + ",\n" + MA_ENTRY + "\n];"
    else:
        # Fallback: find last "};" before "];"
        idx = content.rfind("];")
        if idx == -1:
            print("ERROR: Could not find REPORTS array end marker")
            sys.exit(1)
        # Find the closing brace before ];
        brace_idx = content.rfind("}", 0, idx)
        new_content = content[:brace_idx + 1] + ",\n" + MA_ENTRY + "\n" + content[idx:]

    # Update LAST_UPDATED
    new_content = re.sub(
        r'const LAST_UPDATED = "[^"]*";',
        'const LAST_UPDATED = "2026-06-07";',
        new_content
    )

    with open(DATA_JS, "wb") as f:
        f.write(new_content.encode("utf-8"))

    print("SUCCESS: MA entry added to dashboard/data.js")
    print(f"File size: {len(new_content)} bytes")

if __name__ == "__main__":
    patch()
