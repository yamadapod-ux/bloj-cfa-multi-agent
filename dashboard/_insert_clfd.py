#!/usr/bin/env python3
# Script: insert CLFD entry into data.js REPORTS array
# Run: python dashboard/_insert_clfd.py
# Safe method: find last "}," or "}" before "];" and insert new object

import re

DATA_JS = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

with open(DATA_JS, "rb") as f:
    content = f.read().decode("utf-8")

# The CLFD object to insert (no Windows backslashes in JS strings)
clfd_object = r"""  ,
  {
    ticker: "CLFD",
    company: "Clearfield, Inc.",
    date: "2026-05-22",
    version: "v1",
    sector: "Fiber Optic / Telecom Infrastructure",
    price: 42.71,
    recommendation: "HOLD/WAIT",
    blendedFV: 24.15,
    esgAdjFV: 23.67,
    targetBull: 40.00,
    targetBase: 24.15,
    stopLoss: 19.32,
    convictionEmma: 6,
    convictionQuinn: 5,
    convictionBear: 7,
    convictionAvg: 6.0,
    mosPct: -43.4,
    pwEV: 22.29,
    beta: 1.90,
    sharpe1Y: -0.50,
    maxDrawdown: -0.49,
    moat: "Narrow",
    esgRating: "Low-Medium",
    esgScore: 7.2,
    macroRegime: "RISK-ON",
    sp500Reference: 7433,
    keyThesis: "BEAD $42.45B federal program tailwind + fiber recovery story แต่ราคา $42.71 เกิน Blended FV $24.15 ถึง 43.4% — 84% Sensitivity scenarios ให้ negative return ณ ราคาปัจจุบัน; รอ pullback สู่ $20-26",
    topRisk: "BEAD timing delay (40% prob) + H2 FY2026 ต้องทำ +83% จาก Q2 run rate + Corning FlexNAP competition เข้า niche + Gross Margin 37% ต่ำกว่า peers",
    entryZone: "$22-26 (T1) / $18-22 (T2)",
    positionSize: "5% (Value bucket, RISK-ON 1.0x — เมื่อ entry zone ถึง)",
    maxDrawdown: -0.49,
    reportFile: "../reports/CLFD_2026-05-22.md",
    businessSummary: {
      oneLiner: "Clearfield ผลิตและขายอุปกรณ์ fiber optic enclosures และ connectors ให้ ISPs ขนาดเล็ก-กลางในการ deploy fiber broadband ในพื้นที่ชนบทและชานเมืองของสหรัฐฯ",
      analogy: "เหมือน 'ผู้ขายพลั่วในยุคตื่นทองของ fiber broadband' — ไม่ได้วิ่ง network เอง แต่ขายอุปกรณ์ให้คนวิ่ง โดยเฉพาะ ISPs ขนาดเล็กที่ Corning ไม่ได้ focus",
      moneyFlow: [
        "ผลิต fiber enclosures/connectors → ขายผ่าน distributors (Anixter, ScanSource) → contractors → rural ISPs",
        "BEAD funding flow: Federal → State → ISP award → ISP สั่ง equipment จาก Clearfield",
        "FCF positive TTM $14.44M แม้ revenue ยังอยู่ใน down cycle = business viable ไม่ถึงขั้น distress"
      ]
    },
    thesisBullets: [
      { title: "BEAD Program $42.45B = Multi-Year Demand Tail", why: "Federal funding ที่ยังอยู่ใน pipeline → FY2027 เป็นต้นไปควรเริ่ม flow เข้า rural ISP community ที่เป็นลูกค้า CLFD หลัก" },
      { title: "Post-Inventory Correction Recovery", why: "FY2024 -44% = inventory correction รุนแรงที่สุดในประวัติศาสตร์ → ใกล้จบ → organic demand กลับมา; FY2026 guidance $160-170M = +7-13% growth" },
      { title: "FCF Positive = Surviving Power", why: "แม้รายได้ลง CLFD ยังสร้าง FCF $14.44M TTM = ไม่จำเป็นต้อง dilute หรือยืมเงินหนัก; Net Debt ~$1.5M เท่านั้น" },
      { title: "Pure-play US Infrastructure / No China Risk", why: "Revenue ~98% US domestic; ไม่มี geopolitical binary เหมือน QCOM/AMD; BEAD = bipartisan political support" }
    ],
    esgBreakdown: { e: 7, s: 8, g: 6.5, overall: 7.2 },
    revenueSegments: [
      { label: "Fiber Enclosures / FieldSmart", value: 65 },
      { label: "Connectors / Adapters", value: 20 },
      { label: "ClosetMount / Accessories", value: 15 }
    ],
    competitorData: [
      { ticker: "GLW",  company: "Corning Inc.",       revenueGrowth: 8,  operatingMargin: 10, marketCap: 38000 },
      { ticker: "COMM", company: "CommScope",           revenueGrowth: -5, operatingMargin: -8, marketCap: 600  },
      { ticker: "ADTN", company: "ADTRAN",              revenueGrowth: -15, operatingMargin: -10, marketCap: 500 },
      { ticker: "CALX", company: "Calix Inc.",          revenueGrowth: 5,  operatingMargin: 5, marketCap: 2000  },
      { ticker: "DGII", company: "Digi International",  revenueGrowth: 12, operatingMargin: 10, marketCap: 700  }
    ],
    geographyRevenue: {
      unitedStates: "~98%",
      international: "<2%",
      chinaExposure: "Negligible — no geopolitical binary risk"
    },
    bullFlipTriggers: [
      "Q3 FY2026 Revenue >= $50M (single quarter) = H2 inflection confirmed",
      "BEAD Contract Awards >= $500M ถึง rural ISPs in CLFD territory",
      "Gross Margin Recovery >= 40% สองไตรมาสติดกัน",
      "Price Pullback สู่ $20-26 (entry zone) ขณะ thesis ยังแข็ง",
      "FY2027 Analyst Consensus Revenue upgraded >= $220M"
    ],
    bearFlipTriggers: [
      "FY2026 Full Year Revenue < $155M (miss guidance low-end)",
      "Gross Margin < 35% สองไตรมาสติดกัน",
      "BEAD Program Funding Cut / Delay > 12 months",
      "Corning / Calix ชนะ major BEAD ISP contracts แทน CLFD",
      "Cash < $5M + no credit facility"
    ],
    thesisInvalidation: "FY2027 Revenue < $170M (ต่ำกว่า FY2026 guidance) = recovery ไม่เกิด thesis หัก; หรือ Gross Margin < 33% sustained = structural SELL"
  }"""

# Find the last occurrence of "}\n\n];" or "  }\n\n];" or "  }\n];"
# The file ends with:
#     thesisInvalidation: "..."
#   }
#
# ];
# We'll insert before "\n];\n"

# Find position of "\n];\n" (the end of REPORTS array)
end_marker = "\n];\n"
pos = content.rfind(end_marker)

if pos == -1:
    print("ERROR: Could not find end of REPORTS array")
    exit(1)

print(f"Found end marker at position {pos}")
print(f"Context around marker: {repr(content[pos-50:pos+20])}")

# Insert CLFD object before the "];\n"
new_content = content[:pos] + clfd_object + content[pos:]

with open(DATA_JS, "wb") as f:
    f.write(new_content.encode("utf-8"))

print("SUCCESS: CLFD object inserted into data.js")
print(f"File size: {len(new_content)} chars")

# Verify by checking the file ends correctly
with open(DATA_JS, "rb") as f:
    verify = f.read().decode("utf-8")
if "CLFD" in verify and "Clearfield" in verify:
    print("VERIFICATION: CLFD found in data.js ✓")
else:
    print("VERIFICATION FAILED: CLFD not found")
