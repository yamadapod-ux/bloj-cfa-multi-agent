"""
Leo's data.js insert script for MCO — 2026-06-10
"""

data_js_path = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

mco_entry = '''  {
    ticker: "MCO",
    company: "Moody's Corporation",
    date: "2026-06-10",
    sector: "Financial Data Infrastructure / Credit Ratings",
    price: 448.00,
    recommendation: "HOLD/WAIT",
    blendedFV: 429.00,
    targetBull: 540.00,
    targetBase: 445.00,
    stopLoss: 359.00,
    convictionEmma: 7.5,
    convictionQuinn: 7.0,
    convictionBear: 6.5,
    convictionAvg: 7.0,
    mosPct: -4.2,
    pwEV: 441.00,
    beta: 0.90,
    sharpe1Y: 0.55,
    maxDrawdown: -0.25,
    moat: "Wide",
    esgRating: "Medium",
    esgScore: 6.0,
    keyThesis: "Oligopoly bond ratings (MCO+SPGI 80-85% global share) + NRSRO regulatory moat + MA Analytics recurring 47% revenue. Bond issuance Q1 2026 >$2T first time ever. MOS -4.2% at $448 = HOLD. Entry zone $390-415.",
    topRisk: "May CPI 4.2% (3-year high) — if beat = HY spread widens = MIS revenue at risk H2 2026. Cyclicality + issuer-pays governance model.",
    entryZone: "$390-415",
    positionSize: "5-7% (at entry zone only)",
    businessSummary: {
      oneLiner: "Moody's เป็นผู้ออกใบรับรองความน่าเชื่อถือของตลาดตราสารหนี้ทั่วโลก — ใครจะออก bond ต้องผ่านเราก่อน",
      analogy: "เหมือน credit score agency ระดับสถาบัน — เหมือน FICO แต่สำหรับ bond ของรัฐบาลและบริษัทยักษ์ใหญ่ทั่วโลก",
      moneyFlow: [
        "บริษัท/รัฐบาลที่จะออก bond มาจ้าง Moody's ประเมิน creditworthiness และจ่าย fee $100K-$500K",
        "Moody's ออก rating (Aaa/Baa) ที่ institutional investors ต้องอ่านก่อนซื้อ bond",
        "MA Analytics: ธนาคาร/ประกันภัยทั่วโลกจ่าย subscription รายปีเพื่อใช้ระบบ credit risk",
        "ยิ่งมี bond ออก (IPO, M&A, refinancing) MCO ยิ่งได้ fee — SpaceX IPO June 12 = direct catalyst"
      ],
      whyDifferent: "NRSRO designation จาก SEC ทำให้ institutional investor หลายประเภทต้องใช้ Moody's ตามกฎหมาย — คู่แข่งใหม่ต้องใช้เวลา 20+ ปี",
      simpleRisk: "ถ้าเศรษฐกิจเข้าสู่ recession = บริษัทหยุดออก bond = Moody's สูญรายได้จาก ratings ทันที"
    },
    thesisBullets: [
      { title: "Bond Issuance Record Q1 2026", why: "Bond issuance >$2T Q1 2026 first time ever — MCO gets fee on every deal" },
      { title: "Oligopoly Moat 60+ years", why: "MCO+SPGI control 80-85% global bond ratings — new entrant needs 20+ years" },
      { title: "MA Analytics Recession Buffer", why: "47% of revenue is recurring subscription analytics — protects against cyclical MIS downturn" },
      { title: "SpaceX IPO June 12 Catalyst", why: "Every bond/equity deal requires MCO rating — direct fee income immediately" },
      { title: "ROIC 30% = Value Creation", why: "ROIC 30% >> WACC 9.3% = EVA spread +21% — quality compounding business" }
    ],
    esgBreakdown: {
      e: 8,
      s: 6,
      g: 4.5,
      overall: 6.0
    },
    revenueSegments: [
      { label: "MIS (Ratings)", value: 53 },
      { label: "MA (Analytics)", value: 47 }
    ],
    competitorData: [
      { ticker: "MCO", company: "Moody's Corporation", revenueGrowth: 15, operatingMargin: 47, marketCap: 82 },
      { ticker: "SPGI", company: "S&P Global", revenueGrowth: 13, operatingMargin: 44, marketCap: 140 },
      { ticker: "MSCI", company: "MSCI Inc.", revenueGrowth: 11, operatingMargin: 55, marketCap: 48 },
      { ticker: "ICE", company: "Intercontinental Exchange", revenueGrowth: 7, operatingMargin: 32, marketCap: 85 },
      { ticker: "FDS", company: "FactSet Research", revenueGrowth: 7, operatingMargin: 35, marketCap: 16 }
    ],
    customerConcentration: {
      bondIssuers: "no single issuer >5% — thousands of issuers",
      maAnalytics: ">2,000 subscribers globally",
      concentrationRisk: "LOW"
    },
    geographyRevenue: {
      unitedStates: "~55%",
      europe: "~28-30%",
      asiaPacific: "~10-12%",
      restOfWorld: "~5%"
    },
    bullFlipTriggers: [
      "MCO price pullback to $390-410 (Kelly positive + 72% sensitivity cells support)",
      "May CPI <= 3.8% miss (Fed cut path -> HY spread <300 bps)",
      "MA ARR growth >15% sustained (true SaaS premium)"
    ],
    bearFlipTriggers: [
      "May CPI >4.5% (Fed hike -> credit spread spike -> MIS revenue risk H2)",
      "Q2 2026 MIS revenue growth <5% (Q1 was one-time)",
      "HY Credit Spread widens above 500 bps (junk bond issuance halt)"
    ],
    thesisInvalidation: "Recession + HY Spread >600 bps + MIS revenue down >20% two quarters = pure cyclical not compounder",
    reportFile: "../reports/MCO_2026-06-10.md",
    fullContent: "MCO HOLD/WAIT | Price ~$448 | Blended FV $429 (Emma $445x40% + Quinn $441x35% + Bear $386x25%) | MOS -4.2% | Conviction 7.0/10 | Value Bucket | NRSRO oligopoly moat | Bond issuance Q1 2026 >$2T | MA Analytics 47% recurring | Entry zone $390-415 | Stop $359 (-20%) | Forward Sharpe -0.28 = no deploy at $448 | Kelly negative at $448 | Sector: Financial Data Infrastructure (NEW) | Morgan CONDITIONAL PASS | 2026-06-10"
  },
'''

# Read file in binary to preserve encoding
with open(data_js_path, 'rb') as f:
    raw = f.read()

content = raw.decode('utf-8')

# Update LAST_UPDATED
content = content.replace('const LAST_UPDATED = "2026-06-09";', 'const LAST_UPDATED = "2026-06-10";')

# Check if MCO already exists
if '"MCO"' in content:
    print("MCO entry already exists in data.js — no duplicate insert")
    # Still update LAST_UPDATED
    with open(data_js_path, 'wb') as f:
        f.write(content.encode('utf-8'))
    print("LAST_UPDATED updated to 2026-06-10")
else:
    # Find insertion point: before last ];
    # Find the closing ]; of REPORTS array
    closing = '\n];\n'
    idx = content.rfind(closing)
    if idx == -1:
        closing = '\n];'
        idx = content.rfind(closing)

    if idx == -1:
        print("ERROR: Cannot find closing ]; in data.js")
    else:
        new_content = content[:idx] + '\n' + mco_entry + content[idx:]
        with open(data_js_path, 'wb') as f:
            f.write(new_content.encode('utf-8'))
        print("SUCCESS: MCO entry inserted into data.js")
        print(f"Insertion point at index: {idx}")

# Verify
with open(data_js_path, 'rb') as f:
    verify = f.read().decode('utf-8')

if '"MCO"' in verify and '2026-06-10' in verify:
    print("VERIFY: MCO found + LAST_UPDATED 2026-06-10 confirmed ✓")
    mco_pos = verify.find('"MCO"')
    print(f"MCO ticker found at character position: {mco_pos}")
else:
    print("VERIFY FAILED")
