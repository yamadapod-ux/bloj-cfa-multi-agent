"""
One-shot: add AVGO entry into dashboard/data.js (Charlie/Leo session 2026-04-25)
Run: python dashboard/_add_avgo.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JS = os.path.join(ROOT, "dashboard", "data.js")
REPORT_MD = os.path.join(ROOT, "reports", "AVGO_2026-04-25.md")

with open(REPORT_MD, "r", encoding="utf-8") as f:
    md = f.read()

def escape(s):
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

content_esc = escape(md)

avgo_entry = '''  {
    ticker: "AVGO",
    company: "Broadcom Inc.",
    date: "2026-04-25",
    sector: "Technology / Semiconductors & Infrastructure Software",
    price: 172.40,
    recommendation: "BUY",
    blendedFV: 220.00,
    targetBull: 290.00,
    targetBase: 215.00,
    stopLoss: 130.00,
    convictionEmma: 8,
    convictionQuinn: 7.5,
    convictionBear: 6,
    convictionAvg: 7.2,
    pwEV: 212.00,
    beta: 1.18,
    sharpe1Y: 1.05,
    maxDrawdown: -0.31,
    moat: "Wide",
    esgRating: "Medium",
    esgScore: 5.4,
    keyThesis: "AI ASIC tailwind (Google TPU/Meta MTIA) + VMware margin re-rating + Hock Tan capital discipline — premium quality at discount valuation, MOS +21.6%",
    topRisk: "Google ASIC concentration >40% (Alchip multi-sourcing threat) + VMware churn cycle FY27 + Hock Tan key-person (73yrs, no succession)",
    entryZone: "$138–172",
    positionSize: "5% (3 tranches: $170/40%, $155/35%, $138/25%)",
    bullFlipTriggers: [
      "Custom ASIC customers ขยายเป็น ≥5 hyperscalers (AWS/MSFT/Oracle) ใน 12 เดือน",
      "VMware net retention >115% หลัง 2-year renewal cohort แรก (FY27 H1)",
      "Hock Tan ประกาศ succession plan + designated successor",
      "AI ASIC revenue >$25B FY26 actual (vs guidance $20–22B)",
      "Operating margin sustained ≥65% สำหรับ 4 ไตรมาสติด"
    ],
    bearFlipTriggers: [
      "Google ประกาศ multi-source TPU กับ Alchip/Marvell (loss >20% custom ASIC pipeline)",
      "VMware ARR growth <5% YoY 2 ไตรมาสติด",
      "Operating margin compression >300bps QoQ unexplained",
      "EU/US antitrust formal action vs VMware pricing → forced rollback",
      "Hock Tan unexpected exit / health event without ready successor"
    ],
    thesisInvalidation: "Custom ASIC SAM revised down >30%, VMware GAAP revenue declining YoY 2Q ติด, AI capex peak confirmed (≥3 hyperscalers cut 2026 guidance >15%), หรือ Net debt/EBITDA >3x sustained while buyback continues",
    reportFile: "../reports/AVGO_2026-04-25.md",
    fullContent: `''' + content_esc + '''`
  }'''

with open(DATA_JS, "r", encoding="utf-8") as f:
    js = f.read()

# already present? skip
if 'ticker: "AVGO"' in js:
    print("[skip] AVGO already in data.js — replacing")
    # remove existing AVGO block
    pat = re.compile(r',?\s*\{\s*\n?\s*ticker:\s*"AVGO"[\s\S]*?\n\s{2}\}', re.MULTILINE)
    js = pat.sub("", js)

# Insert before the closing `\n];` of REPORTS array
# Find pattern: `\n  }\n];`
new_js = js.replace("\n  }\n];", "\n  },\n" + avgo_entry + "\n];", 1)

# update LAST_UPDATED
new_js = re.sub(
    r'const LAST_UPDATED\s*=\s*"[^"]*";',
    'const LAST_UPDATED = "2026-04-25";',
    new_js
)

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(new_js)

# verify
with open(DATA_JS, "r", encoding="utf-8") as f:
    final = f.read()
print(f"[ok] AVGO added — {len(md):,} chars embedded")
print(f"[ok] data.js total: {len(final):,} chars")
avgo_count = final.count('ticker: "AVGO"')
fc_count = final.count('fullContent:')
print(f"[ok] AVGO ticker count: {avgo_count}")
print(f"[ok] fullContent count: {fc_count}")
