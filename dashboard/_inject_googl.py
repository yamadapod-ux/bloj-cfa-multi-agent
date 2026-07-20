#!/usr/bin/env python3
"""
_inject_googl.py — Leo: inject GOOGL object into dashboard/data.js REPORTS array
Run: python dashboard/_inject_googl.py
Created: 2026-05-21
"""

import re, sys

DATA_FILE = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

GOOGL_OBJECT = r"""  {
    ticker: "GOOGL",
    company: "Alphabet Inc. Class A",
    date: "2026-05-21",
    version: "v3 (Re-Analysis — Q1 2026 Beat + Conviction Gate PASSED)",
    previousDate: "2026-05-20",
    previousRating: "HOLD/WAIT @ $165.44 | FV $170",
    sector: "Communication Services / Technology",
    bucket: "Growth",
    price: 166.91,
    recommendation: "HOLD",
    blendedFV: 173.00,
    esgAdjFV: 164.00,
    targetBull: 215.00,
    targetBase: 173.00,
    stopLoss: 132.00,
    convictionEmma: 7.0,
    convictionQuinn: 6.5,
    convictionBear: 6.5,
    convictionAvg: 6.67,
    pwEV: 173.00,
    beta: 1.07,
    forwardSharpe: -0.02,
    maxDrawdown: -0.45,
    mos: 0.037,
    mosPct: 3.7,
    kelly: "NEGATIVE at $166.91; POSITIVE ≥ $130",
    moat: "Wide",
    esgRating: "Medium-High Risk",
    esgScore: 5.0,
    esgBreakdown: { e: 7, s: 4.5, g: 3.25, overall: 5.0 },
    macroRegime: "TRANSITIONAL-CAUTIOUS",
    sp500Reference: 5840,
    wacc: "9.1% (Rf 4.45% + β 1.07 × ERP 4.5%)",
    sensitivityCellsJustify: "10-12/25 = 40-48%",
    entryZone: "$140–155 (base) หรือ DOJ behavioral ruling (ใดก็ได้ ≤ $175)",
    positionSize: "6% เมื่อ Regime RISK-ON (Conviction 6.67 × 0.75 TC suspended now)",
    ratingChangeNote: "v2 (2026-05-20) Price Fix $165.44 | FV $170 → v3 (2026-05-21) Full Pipeline | FV $173 | Conviction Gate FLIPPED 6.33→6.67 PASSED",
    keyThesis: "Cheapest Quality Mega-cap — Conviction Gate CLEARED. Q1 2026 op margin 34.4% (+470bps) structural; AI Overviews ไม่กระทบ Search revenue (Search +9.8%); GCP $12.3B +28.1% run rate $49B. Blended FV $173 vs price $167 = MOS +3.7%. DOJ binary = largest overhang (25% structural remedy probability). TC Regime = only blocker. ถ้า regime เปลี่ยน RISK-ON → BUY ทันที 6%.",
    topRisk: "DOJ structural separation ruling (forced divestiture Chrome/Android) → FV $75-90; CapEx $75-85B FY2026 (+43-62% vs FY2024) = FCF compression $55B→$23-33B; AI Search substitution acceleration Q2-Q3 2026 data",
    bullFlipTriggers: [
      "DOJ final remedy = behavioral only → FV re-rates $200+; BUY ทันที ≤ $180",
      "GCP market share ≥ 14% global ใน Q2 2026 → Cloud acceleration confirmed",
      "Search revenue +12%+ YoY ใน Q2 2026 → AI Overviews definitively safe",
      "CapEx guidance revised downward ($75-85B → $60-65B) = FCF upgrade",
      "ราคา ≤ $140 + no new negative catalyst → Kelly positive; BUY"
    ],
    bearFlipTriggers: [
      "DOJ structural separation ruling → SELL ทันที; FV $75-90",
      "Search market share < 88% ใน 2 consecutive reports → AI substitution confirmed",
      "GCP growth < 15% YoY ใน Q2 หรือ Q3 2026 → Cloud story disappointing",
      "CapEx > $85B FY2026 actual + no FCF recovery guidance → capital spiral",
      "Apple distribution deal terminated → Search revenue -10-15% structural"
    ],
    thesisInvalidation: "Chrome/Android forced divestiture OR Search share < 80% rolling 12M OR 3 consecutive quarters Search revenue YoY decline",
    businessSummary: {
      oneLiner: "Alphabet คือเจ้าของ Google Search, YouTube, และ Google Cloud — บริษัทโฆษณาดิจิทัลและ cloud ที่ใหญ่ที่สุดในโลก",
      analogy: "เหมือนเป็นเจ้าของทางด่วนทุกเส้นบนอินเทอร์เน็ต — ใครก็ตามที่ต้องการพาคนไปที่ไหนต้องจ่ายเงินผ่าน Google",
      moneyFlow: [
        "ผู้ใช้ค้นหาสิ่งต้องการบน Google (2 ล้านล้านครั้ง/ปี)",
        "ผู้ลงโฆษณาจ่ายเงินเพื่อให้โฆษณาปรากฏข้างผลการค้นหา (CPC model)",
        "GCP ให้บริษัทต่างๆ เช่า cloud + AI infrastructure แบบ subscription",
        "YouTube ads + premium subscriptions + Google One = diversified revenue streams"
      ],
      whyDifferent: "25 ปีของข้อมูลการค้นหา + network effect ของ advertisers + Android 3B devices = ecosystem ที่คู่แข่งไม่สามารถ replicate ได้ในระยะสั้น",
      simpleRisk: "ถ้า DOJ บังคับแยกบริษัท (Chrome/Android) หรือ AI search เปลี่ยน habit ผู้ใช้ได้จริง — thesis พัง"
    },
    thesisBullets: [
      { title: "Search Monopoly ยังแข็ง", why: "90%+ global share; AI Overviews Q1 2026 ไม่กระทบ ad revenue (Search +9.8% YoY) = worry ที่ใหญ่ที่สุดไม่เป็นจริง" },
      { title: "GCP = Next Revenue Engine", why: "Q1 2026 $12.3B +28.1% YoY; run rate $49B; margin expanding 9%→17%+; path to #2 cloud realistic" },
      { title: "Valuation Discount ผิดปกติ", why: "P/E ~18x = 22-25% discount vs peers (META ~19x, MSFT ~28x); ROIC 26% > sector; discount = DOJ overhang" },
      { title: "Operating Margin Expansion", why: "Q1 2026: 34.4% (+470bps YoY) = structural improvement; GCP scale leverage + cost efficiency" },
      { title: "Capital Return Machine", why: "$62.5B buyback FY2024 + net cash $98B; FCF $55B/yr; no leverage = fortress" }
    ],
    customerConcentration: {
      noSingleCustomerAbove1pct: "<1% each — millions of advertisers worldwide",
      appleDistributionDeal: "~$20B/yr cost item (TAC); DOJ target — if terminated = short-term headwind"
    },
    geographyRevenue: {
      unitedStates: "~47%",
      emea: "~29%",
      apac: "~17%",
      otherAmericas: "~7%",
      chinaDirectExposure: "<3% — low geopolitical risk; DXY weak = FX tailwind on 53% non-US"
    },
    revenueSegments: [
      { label: "Google Search & Other (~57%)", value: 57, revenue: "~$198B+ ann.", growth: "+9.8% Q1 2026", margin: "~55-60%" },
      { label: "YouTube Ads (~10%)", value: 10, revenue: "~$36B+ ann.", growth: "+12.3% Q1 2026", margin: "~35-40%" },
      { label: "Google Cloud (GCP ~14%)", value: 14, revenue: "$49B ann. (run rate)", growth: "+28.1% Q1 2026", margin: "~17%" },
      { label: "Google Network (~9%)", value: 9, revenue: "~$31B ann.", growth: "-1% Q1 2026", margin: "~15-20%" },
      { label: "Other (~10%)", value: 10, revenue: "~$35B ann.", growth: "+15% Q1 2026", margin: "~10-20%" }
    ],
    competitorData: [
      { ticker: "GOOGL", revenueGrowth: 12, operatingMargin: 34.4, marketCap: 2030,
        strengths: "Search monopoly 90%+, GCP accelerating, Wide Moat, Net Cash $98B, ROIC 26%", weaknesses: "DOJ antitrust binary, CapEx $75-85B FY2026 FCF compression, Dual-class governance", threatLevel: "SUBJECT" },
      { ticker: "META", revenueGrowth: 33, operatingMargin: 41, marketCap: 1550,
        strengths: "Digital ads moat, AI Advantage+, Social graph 3.35B, Revenue growing faster", weaknesses: "FTC antitrust, no search, no cloud, Reality Labs burning cash", threatLevel: "HIGH" },
      { ticker: "MSFT", revenueGrowth: 17, operatingMargin: 45, marketCap: 3200,
        strengths: "Azure #2 cloud, OpenAI partnership, Enterprise relationships, Copilot", weaknesses: "Bing < 4% search share, consumer brand weak vs Google", threatLevel: "HIGH" },
      { ticker: "AMZN", revenueGrowth: 11, operatingMargin: 11, marketCap: 2100,
        strengths: "AWS #1 cloud, Amazon Ads growing, e-commerce product search 40%", weaknesses: "No general search, margins lower, no AI search consumer product", threatLevel: "MEDIUM" }
    ],
    reportFile: "../reports/GOOGL_2026-05-20.md",
    fullContent: `# GOOGL — Alphabet Inc. Class A (v3 Re-Analysis)
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

## Update Log (v3 — 2026-05-21)
| Version | วันที่ | ราคา | Blended FV | Conviction | Rating | สาเหตุ |
|---------|--------|------|-----------|-----------|--------|--------|
| v3 | 2026-05-21 | $166.91 | $173 | 6.67 ✅ | HOLD/WAIT (TC) | Full pipeline Q1 2026 beat; conviction gate PASSED |
| v2 | 2026-05-20 | $165.44 | $170 | 6.33 | HOLD/WAIT (TC) | Price verification fix; Q1 2026 actuals |
| v1 | original | ~$170 | $170 | 6.33 | HOLD/WAIT (TC) | First analysis |

## คำแนะนำ v3: HOLD/WAIT (TC Regime) — Conviction Gate PASSED ✅

| รายการ | ค่า |
|--------|-----|
| Blended FV | $173 (Emma $178×40% + Quinn $180×35% + Bear $155×25%) |
| ESG-adj FV | $164 (-5% ESG penalty) |
| MOS | +3.7% (ราคา $166.91 vs FV $173) |
| Entry Zone | $140–155 หรือ DOJ behavioral ruling |
| Stop Loss | $132 (-20% จาก entry $165.44) |
| Conviction | 6.67/10 ✅ Growth gate 6.5 PASSED |
| Regime | TRANSITIONAL-CAUTIOUS → suspend new positions |

## TL;DR
- Verdict: HOLD/WAIT (TC regime) — Conviction gate ผ่านแล้ว (6.67 ≥ 6.5) แต่ TRANSITIONAL-CAUTIOUS ห้าม open new positions
- ทำไม v3 ดีขึ้น: Q1 2026 op margin 34.4% (+470bps) structural; AI Overviews ไม่กระทบ Search; GCP run rate $49B; Blended FV $173
- Downside Risk ใหม่: CapEx guidance $75-85B FY2026 (+43-62%) = FCF compression; DOJ remedy order ยังค้าง

## Conviction Bar
Emma   ███████░░░  7.0/10  — Structural margin expansion confirmed; AI Overviews OK; FV $178
Quinn  ██████▌░░░  6.5/10  — P-W EV $180; Sharpe still marginal negative; Kelly negative at $167
Bear   ██████▌░░░  6.5/10  — FV $155 (CapEx concern); DOJ binary; structural tail raised 5%→10%
─────────────────────────────────────────────────────
Avg    ██████▌░░░  6.67/10 ✅ Growth gate 6.5 PASSED | TC regime suspends deployment

## Blended FV Triangulation (IPS 2026-05-15)
Emma (Fundamental/DCF): $178 × 40% = $71.20
Quinn (Quant/P-W EV): $180 × 35% = $63.00
Bear (Downside/P-W EV): $155 × 25% = $38.75
Blended FV = $172.95 ≈ $173

MOS = ($173 / $166.91 - 1) × 100 = +3.7%

## Recommendation
HOLD/WAIT (TC Regime) — ถ้า Regime เปลี่ยน RISK-ON → BUY T1 6% ทันที (Conviction 6.67 ≥ 6.5 gate)

Deploy triggers:
1. Macro regime เปลี่ยน RISK-ON → BUY T1 6% ทันที
2. DOJ behavioral remedy → BUY T1 6-7% ณ ราคาใดก็ได้ ≤ $180
3. ราคาลงมา $140-155 → WATCH → BUY T1 4.5% เมื่อ regime shift

Stop Loss: $132 (-20% จาก entry $165.44)

*รายงานเต็มอยู่ใน: reports/GOOGL_2026-05-20.md (อัปเดต in-place v3)*
*QA: Morgan ✅ PASS | Executed: Leo | 2026-05-21*
`
  },"""

# Read the data file
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if GOOGL already exists
if '"GOOGL"' in content and 'ticker: "GOOGL"' in content:
    print("GOOGL already exists in data.js — checking if update needed...")
    # Find the GOOGL object and check its version
    if '2026-05-21' in content and 'ticker: "GOOGL"' in content:
        # Check context around GOOGL
        idx = content.find('ticker: "GOOGL"')
        context = content[max(0, idx-50):idx+200]
        print(f"Current GOOGL context: {context}")
        print("GOOGL v3 appears to already be present. Verify manually.")
        sys.exit(0)

# Find the end of REPORTS array (before the closing ];)
# Insert GOOGL before the closing of the array
pattern = r'(\s*\},\s*\n\];)'
replacement = f'\n{GOOGL_OBJECT}\n];\n'

# Try to insert before the final ]; of REPORTS array
# Find the last }  before ];
last_brace_pos = content.rfind('\n  },\n\n];')
if last_brace_pos == -1:
    # Try alternative pattern
    last_brace_pos = content.rfind('\n  }\n\n];')

if last_brace_pos == -1:
    # Try simpler pattern
    last_brace_pos = content.rfind('];')
    if last_brace_pos == -1:
        print("ERROR: Could not find insertion point in data.js")
        sys.exit(1)
    # Insert before ];
    new_content = content[:last_brace_pos] + GOOGL_OBJECT + '\n\n];\n' + content[last_brace_pos+2:]
else:
    # Insert after last },
    insert_point = last_brace_pos + len('\n  },\n\n')
    new_content = content[:insert_point] + GOOGL_OBJECT + '\n\n' + content[insert_point:]

# Update LAST_UPDATED
new_content = re.sub(r'const LAST_UPDATED = "[^"]+";', 'const LAST_UPDATED = "2026-05-21";', new_content)

# Write back
with open(DATA_FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SUCCESS: GOOGL object injected into dashboard/data.js")
print(f"LAST_UPDATED set to 2026-05-21")
print("Please verify dashboard loads correctly at file:// path")
