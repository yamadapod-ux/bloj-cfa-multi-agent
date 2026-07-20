"""
Script: Update GOOGL entry in dashboard/data.js
Date: 2026-05-20 (Price Verification Fix)
Uses binary read/write to preserve encoding and newlines
"""

import re
import subprocess
import os

BASE = r"C:\Users\user\Desktop\บลจ\บลจ CFA"
data_js_path = os.path.join(BASE, "dashboard", "data.js")

# Read file as binary then decode
with open(data_js_path, "rb") as f:
    raw = f.read()
content = raw.decode("utf-8")

# Build the new GOOGL entry
# Use triple backtick for fullContent — must escape carefully
# fullContent uses backtick template literal in JS

new_googl_entry = r"""  {
    ticker: "GOOGL",
    company: "Alphabet Inc. Class A",
    date: "2026-05-20",
    version: "v2 (Price Verification Fix — 2026-05-20)",
    sector: "Communication Services / Technology",
    price: 165.44,
    recommendation: "HOLD/WAIT",
    blendedFV: 170.00,
    targetBull: 223.00,
    targetBase: 178.00,
    stopLoss: 132.00,
    convictionEmma: 6.5,
    convictionQuinn: 6.0,
    convictionBear: 6.5,
    convictionAvg: 6.33,
    mosPct: 2.7,
    pwEV: 170.00,
    beta: 1.07,
    sharpe1Y: 0.09,
    maxDrawdown: -0.45,
    moat: "Wide",
    esgRating: "Medium-High",
    esgScore: 5.0,
    keyThesis: "Wide Moat Search + GCP + YouTube. Q1 2026 beat (Rev $90.2B +12.1%, EPS $2.81 +48.7%, GCP $12.3B +28.1%). Blended FV $170 (Emma $175x40% + Quinn $177x30% + Bear $157x30%). MOS +2.7% at $165.44. Growth MOS PASS. DOJ remedy phase 2026 = BINARY RISK (Structural 35% prob). Conviction 6.33 < 6.5 Growth gate. TC regime = no new positions. GOOGL > GOOG (voting rights + S&P 500 tracking). Price verified: Yahoo Finance + Google Finance.",
    topRisk: "DOJ structural separation (Chrome/Android) → FV $85-115 (-50%). AI Search substitution (Perplexity/ChatGPT) eroding informational queries. CapEx spiral if GCP ROI disappoints.",
    entryZone: "$140-155 (normal) or $155-165 post DOJ clarity",
    positionSize: "6% max (TC x 0.75)",
    priceSource: "Yahoo Finance https://finance.yahoo.com/quote/GOOGL/ + Google Finance (2026-05-19 close)",
    q1_2026: "Revenue $90.2B +12.1% YoY, EPS $2.81 +48.7%, GCP $12.3B +28.1%, Op.Margin 34.4% — Beat consensus",
    businessSummary: {
      oneLiner: "Alphabet คือบริษัทแม่ของ Google — ทำเงินจากโฆษณา Search และ YouTube ($234B/ปี), Cloud (GCP $43B), และกำลัง expand ไป AI",
      analogy: "Google Search คือทางด่วนข้อมูลที่ทุกคนต้องผ่าน ใครอยากโฆษณาบนทางด่วนนี้ต้องจ่ายเงิน Google",
      moneyFlow: [
        "ผู้ใช้ค้นหาบน Google หรือดู YouTube → Google รวบรวม intent data",
        "Advertisers จ่าย Google เพื่อแสดงโฆษณาต่อคนที่มี intent นั้น (Cost-per-Click)",
        "Google Cloud เก็บ subscription fee จาก enterprises ที่ใช้ cloud computing + AI services",
        "Net margin ~29% → FCF $73B/ปี → ส่งคืน shareholders ผ่าน buyback $62B/ปี"
      ],
      whyDifferent: "25 ปีของ search data + advertiser relationships + Android (3B devices) + Chrome (65% browser share) = ecosystem ที่คู่แข่งใช้เวลา decades กว่าจะสร้างเทียบได้",
      simpleRisk: "ถ้า ChatGPT/Perplexity เปลี่ยน habit ผู้ใช้ให้ค้นหาผ่าน AI chatbot แทน Google Search ได้สำเร็จ รายได้โฆษณา $198B/ปีอาจหดตัว"
    },
    thesisBullets: [
      { title: "Search Monopoly ยังไม่พัง", why: "90% market share ใน 25 ปี — AI Overviews (SGE) ยัง monetize ได้; commercial queries (ที่ทำเงิน) ยังคงอยู่" },
      { title: "GCP = Next Revenue Engine", why: "Cloud +28.1% Q1 2026 กับ operating margin 17% = path to #2 cloud; Q1 2026 $12.3B beat consensus" },
      { title: "Cheapest Mega-cap ใน Universe", why: "Forward P/E 17-18x vs peers 22-30x แม้ ROIC 26% สูงกว่า sector median — DOJ overhang over-punish valuation" },
      { title: "Capital Returns Machine", why: "$62.5B buyback + dividend new in 2024 = $100B+ capital return potential; net cash $98B" },
      { title: "Waymo Optionality", why: "200K+ rides/week; autonomous vehicle TAM ขนาดใหญ่ = free option ที่ตลาดยังไม่ price in" }
    ],
    esgBreakdown: { e: 7, s: 4.5, g: 3.5, overall: 5.0 },
    customerConcentration: {
      advertisers: "Millions — no single customer >1%",
      appleRisk: "Apple Distribution Deal ~$20B/yr = DOJ target",
      topCustomers: "No concentration risk (millions of SMBs)"
    },
    geographyRevenue: {
      unitedStates: "~47%",
      emea: "~29%",
      apac: "~17%",
      otherAmericas: "~7%",
      chinaExposure: "<3% indirect — LOW geopolitical risk"
    },
    revenueSegments: [
      { label: "Search Advertising", value: 57, revenue: "~$198B (FY2024)", growth: "+9.8% Q1 2026", margin: "~40%" },
      { label: "YouTube Ads", value: 10, revenue: "~$36B (FY2024)", growth: "+12.3% Q1 2026", margin: "~35%" },
      { label: "Google Cloud (GCP)", value: 12, revenue: "$43B (FY2024) / $12.3B Q1 2026", growth: "+28.1% Q1 2026", margin: "~17%" },
      { label: "Google Network (AdSense)", value: 9, revenue: "~$32B (FY2024)", growth: "Declining", margin: "~30%" },
      { label: "Subscriptions & Devices", value: 4, revenue: "~$14B (FY2024)", growth: "+10%", margin: "~20%" },
      { label: "Other Bets (Waymo etc.)", value: 1, revenue: "<$2B (FY2024)", growth: "N/A", margin: "Negative" },
    ],
    competitorData: [
      { ticker: "GOOGL", revenueGrowth: 12, operatingMargin: 34.4, marketCap: 2010,
        strengths: "Search monopoly 90%+, GCP +28%, Wide Moat (data+brand+Android), Net cash $98B", weaknesses: "DOJ ruling already guilty, AI threat to search, CapEx $52.5B", threatLevel: "SUBJECT" },
      { ticker: "META", revenueGrowth: 33, operatingMargin: 42, marketCap: 1500,
        strengths: "Social graph 3.3B users, AI ad targeting, ROAS competitive", weaknesses: "No search intent, FTC antitrust risk, teen safety concerns", threatLevel: "MEDIUM" },
      { ticker: "MSFT", revenueGrowth: 17, operatingMargin: 45, marketCap: 3100,
        strengths: "OpenAI partnership, Azure #2 cloud, Copilot in Office 365", weaknesses: "Bing ~3-4% search share, P/E 28-30x premium", threatLevel: "HIGH" },
      { ticker: "AMZN", revenueGrowth: 11, operatingMargin: 11, marketCap: 2300,
        strengths: "40% product searches start at Amazon, AWS #1 cloud, Prime ecosystem", weaknesses: "No general search, thin retail margins", threatLevel: "MEDIUM-HIGH" },
    ],
    sensitivityMatrix: {
      v1Label: "Revenue CAGR",
      v2Label: "WACC",
      v1Values: ["5%", "8%", "11%", "14%", "17%"],
      v2Values: ["8.0%", "8.75%", "9.5%", "10.25%", "11.0%"],
      cells: [
        [118, 105, 94, 85, 77],
        [152, 136, 122, 111, 101],
        [192, 173, 156, 142, 130],
        [238, 215, 195, 178, 163],
        [292, 265, 241, 220, 202]
      ],
      baseCase: { v1: "11%", v2: "9.5%", fv: 156 },
      currentPrice: 165.44,
      cellsJustifyCount: "9-10/25 (~38%)"
    },
    dojScenarios: {
      behavioralOnly: { prob: 30, fv: 225, description: "Fines + prohibition, no structural separation" },
      terminateAppleDeal: { prob: 35, fv: 130, description: "DOJ forces end of Apple distribution deal $20B/yr" },
      structuralSeparation: { prob: 25, fv: 90, description: "Chrome or Android forced divestiture" },
      forcedDivestiture: { prob: 10, fv: 75, description: "Major asset separation ordered" }
    }
  }"""

# Pattern to find and replace the existing GOOGL entry
# Match from { (with whitespace) followed by ticker: "GOOGL" to the closing }
old_pattern = r'\{\s*\n\s*ticker:\s*"GOOGL".*?\n\s*\}'

match = re.search(old_pattern, content, flags=re.DOTALL)
if match:
    print(f"Found GOOGL entry at position {match.start()}-{match.end()}")
    content_new = content[:match.start()] + new_googl_entry.strip() + content[match.end():]
    print("Replaced GOOGL entry")
else:
    print("WARNING: GOOGL entry not found — will append at end of REPORTS array")
    # Insert before closing bracket of REPORTS array
    insert_pos = content.rfind("];")
    if insert_pos > 0:
        content_new = content[:insert_pos] + ",\n" + new_googl_entry.strip() + "\n" + content[insert_pos:]
    else:
        content_new = content

# Update LAST_UPDATED
content_new = re.sub(
    r'const LAST_UPDATED = "[^"]*";',
    'const LAST_UPDATED = "2026-05-20";',
    content_new
)

# Write as binary
with open(data_js_path, "wb") as f:
    f.write(content_new.encode("utf-8"))

print("data.js written successfully")

# Validate with node
result = subprocess.run(
    ["node", "-e", "try{require('./data.js');console.log('OK')}catch(e){console.log('ERR:',e.message)}"],
    capture_output=True,
    text=True,
    encoding="utf-8",
    cwd=os.path.join(BASE, "dashboard")
)
print("Node validation:", result.stdout.strip())
if result.stderr:
    print("STDERR:", result.stderr.strip())
