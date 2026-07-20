"""Append ALAB entry to dashboard/data.js — Leo script 2026-05-20
Binary mode write to prevent newline collapse.
"""
import os, subprocess

BASE = r'C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard'
filepath = os.path.join(BASE, 'data.js')

# Full content of research report (condensed for fullContent)
full_content = r"""# AI ALAB — Astera Labs, Inc.
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

**Recommendation:** HOLD / WAIT FOR PULLBACK | **Blended FV:** $48.5 | **Entry Zone:** $41–50 | **Stop Loss:** $36

**TL;DR:**
- Verdict: HOLD/WAIT — ALAB เป็น best-in-class AI connectivity pure-play แต่ราคา ~$60 แพงกว่า Blended FV $48.5 ถึง 19%
- ทำไม: CXL/PCIe pioneer + Revenue +244% FY2024 + Gross Margin 70% แต่ Marvell/Broadcom entering + concentration risk
- Downside: Bear FV $37 = -38% จากราคาปัจจุบัน

**Sensitivity Matrix (Revenue CAGR x EV/Revenue):** 24% of 25 cells justify $60; 6/25 cells justify current price.
**Customer Concentration:** Top 2 (Microsoft+Google) ~50%+ = primary binary risk.
**Regime:** TRANSITIONAL-CAUTIOUS — Force Deploy suspended."""

entry = '''  {
    ticker: "ALAB",
    company: "Astera Labs, Inc.",
    date: "2026-05-20",
    version: "v1",
    sector: "Semiconductors / AI Connectivity",
    price: 60.00,
    recommendation: "HOLD/WAIT",
    blendedFV: 48.50,
    targetBull: 83.80,
    targetBase: 52.80,
    stopLoss: 36.00,
    convictionEmma: 7,
    convictionQuinn: 6,
    convictionBear: 7,
    convictionAvg: 6.7,
    mosPct: -19.2,
    pwEV: 52.40,
    beta: 2.00,
    sharpe1Y: 0.30,
    maxDrawdown: -0.45,
    moat: "Narrow",
    esgRating: "Medium",
    esgScore: 5.8,
    keyThesis: "CXL/PCIe pure-play pioneer พร้อม revenue +244% FY2024 แต่ราคา $60 เกิน Blended FV $48.5 ถึง 19% รอ pullback $41-50",
    topRisk: "Customer concentration Top 2 ~50%+ (Microsoft+Google) = hyperscaler capex binary risk + Marvell/Broadcom entering CXL",
    entryZone: "$41–50 (T1: $45-50 / T2: $41-45)",
    positionSize: "Max 3% (TRANSITIONAL-CAUTIOUS ×0.75)",
    bullFlipTriggers: [
      "Q1 FY2025 revenue >$150M + operating breakeven",
      "Customer concentration drops <35% top-2",
      "Price pullback to $41-48 (MOS 5-15%)",
      "Marvell fails to win hyperscaler CXL design wins FY2025",
      "CXL 3.0 spec mandatory standard confirmed"
    ],
    bearFlipTriggers: [
      "Revenue miss 2 quarters consecutive (<$120M/Q)",
      "Microsoft or Google order cut >20% (10-Q)",
      "Marvell wins disclosed hyperscaler CXL design win",
      "FY2025 guidance cut <$500M",
      "Insider selling >5% float in 90 days"
    ],
    thesisInvalidation: "Hyperscaler สร้าง in-house CXL chip เอง OR AI capex reverse เกิน 40%",
    reportFile: "../reports/ALAB_2026-05-20.md",
    fullContent: `''' + full_content.replace('`', r'\`') + '''`,
    businessSummary: {
      oneLiner: "Astera Labs ทำชิปเชื่อมต่อ AI server — GPU และ Memory คุยกันได้เร็วขึ้นด้วย CXL/PCIe technology",
      analogy: "เหมือน highway on-ramp ระหว่าง GPU และ Memory ใน AI data center",
      moneyFlow: [
        "Hyperscalers (Microsoft/Google/Meta) สั่งซื้อ AI server rack ใหม่ทุกปี",
        "ทุก rack ต้องการ PCIe/CXL retimer chip เพื่อ connect GPU กับ Memory",
        "ALAB design ชิป ส่งให้ TSMC ผลิต ขายในราคา premium margin ~70%",
        "ยิ่ง hyperscaler ลงทุน AI capex มาก ALAB ได้ revenue มาก"
      ],
      whyDifferent: "Pure-play CXL/PCIe pioneer — ชิปถูก design in ลึกใน server architecture ทำให้ switching ยาก + 2 ปีที่โตกับ hyperscaler ทำให้มี relationship ที่ Marvell/Broadcom ต้องใช้เวลา 2-3 ปีสร้างใหม่",
      simpleRisk: "ถ้า Microsoft หรือ Google ลด AI capex หรือสร้าง in-house chip เอง revenue ลดทันที"
    },
    thesisBullets: [
      { title: "CXL Pure-Play Pioneer", why: "First-mover ใน hyperscaler rack generation นี้ switching cost สูง 12-18 เดือนใน cycle ปัจจุบัน" },
      { title: "Revenue +244% FY2024", why: "Direct beneficiary ของ AI data center buildout โดยไม่ต้อง compete กับ NVIDIA" },
      { title: "Gross Margin ~70%", why: "Fabless model + IP value = structural high margin เทียบ NVDA" },
      { title: "Path to Profitability FY2025", why: "Operating leverage เริ่มที่ $500-600M revenue scale" }
    ],
    esgBreakdown: { e: 7, s: 6, g: 4.5, overall: 5.8 },
    customerConcentration: {
      microsoft: "~25-35% (est., largest, flag >20%)",
      google: "~20-25% (est., second)",
      top2Combined: "~50%+ (CRITICAL concentration)",
      meta: "~15-20% (est.)",
      amazonAws: "~10-15% (est.)"
    },
    geographyRevenue: {
      unitedStates: "~90-95%",
      international: "~5-10%",
      china: "~0-3% (minimal)"
    },
    competitorData: [
      { ticker: "ALAB", company: "Astera Labs", revenueGrowth: 244, operatingMargin: -10, marketCap: 9.6 },
      { ticker: "MRVL", company: "Marvell Technology", revenueGrowth: 28, operatingMargin: 15, marketCap: 70 },
      { ticker: "NVDA", company: "NVIDIA", revenueGrowth: 122, operatingMargin: 55, marketCap: 1100 },
      { ticker: "AVGO", company: "Broadcom", revenueGrowth: 50, operatingMargin: 35, marketCap: 1000 },
      { ticker: "AMD", company: "AMD", revenueGrowth: 20, operatingMargin: 5, marketCap: 160 }
    ],
    revenueSegments: [
      { label: "PCIe/CXL Retimers (Aries)", value: 60 },
      { label: "Ethernet Smart Cable (Taurus)", value: 25 },
      { label: "CXL Memory (Leo)", value: 15 }
    ],
  }'''

with open(filepath, 'rb') as f:
    raw = f.read()

# Find the closing bracket of REPORTS array
marker = b'\n];'
idx = raw.rfind(marker)
if idx == -1:
    print('ERROR: Could not find ]; marker in data.js')
    exit(1)

insert = (',\n' + entry + '\n').encode('utf-8')
raw = raw[:idx] + insert + raw[idx:]

# Update LAST_UPDATED
raw = raw.replace(
    b'const LAST_UPDATED = "2026-05-20";',
    b'const LAST_UPDATED = "2026-05-20";'
)

with open(filepath, 'wb') as f:
    f.write(raw)

print('ALAB entry appended to data.js')

# Validate
result = subprocess.run(
    ['node', '-e', "try{require('./data.js');console.log('OK')}catch(e){console.log('ERR:',e.message)}"],
    capture_output=True, text=True, encoding='utf-8',
    cwd=BASE
)
print('Node validation:', result.stdout.strip(), result.stderr.strip())
