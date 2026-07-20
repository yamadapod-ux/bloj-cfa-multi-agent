#!/usr/bin/env python3
"""
Leo's dashboard patch script — ADSK 2026-06-09
Adds ADSK entry to dashboard/data.js
Run: python dashboard/_patch_adsk.py
"""

import re

DATA_JS_PATH = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

ADSK_ENTRY = '''  {
    ticker: "ADSK",
    company: "Autodesk, Inc.",
    date: "2026-06-09",
    version: "v1",
    sector: "Technology / Design Software / AEC",
    price: 229.00,
    recommendation: "BUY",
    blendedFV: 290.00,
    targetBull: 400.00,
    targetBase: 310.00,
    stopLoss: 183.00,
    convictionEmma: 7.5,
    convictionQuinn: 7.0,
    convictionBear: 6.5,
    convictionAvg: 7.0,
    mosPct: 26.6,
    pwEV: 264.00,
    beta: 1.02,
    sharpe1Y: 0.70,
    maxDrawdown: -0.54,
    moat: "Wide",
    esgRating: "Good",
    esgScore: 6.7,
    keyThesis: "ADSK = ADBE 2022-2023 FCF inflection pattern. Subscription transition complete. DWG/Revit format 40-year moat. ROIC 49.15%. Q1 FY27 revenue +18% YoY = acceleration. Blended FV $290 = MOS 26.6%.",
    topRisk: "AEC construction cyclicality (near-term, 30% prob); AI generative design disruption (25% prob 3-5yr); ROIC inflation methodology (adjusted 35-45%)",
    entryZone: "$220-235 (T1) / $200-218 (T2)",
    positionSize: "8% max (T1: 4%, T2: 3%, T3: 1%)",
    businessSummary: {
      oneLiner: "Autodesk ขาย subscription software สำหรับ architect, engineer, manufacturer ทั่วโลก — AutoCAD และ Revit เป็น industry standard มา 40+ ปี",
      analogy: "ถ้า Adobe เป็น design OS สำหรับ creative professionals, Autodesk เป็น design OS สำหรับ architect และ engineer ทั่วโลก — switching ทำไม่ได้เพราะทั้งอุตสาหกรรมใช้ไฟล์รูปแบบเดียวกัน",
      moneyFlow: [
        "ลูกค้าจ่าย subscription รายปี $400-2,000+/seat สำหรับ AutoCAD, Revit, Fusion 360, Inventor",
        "Product Collections (bundle) เพิ่ม ARPU — AEC Collection, Manufacturing Collection",
        "Autodesk Construction Cloud (ACC) เป็น SaaS overlay บน construction workflow = Cloud ARR growing",
        "Forma AI premium tier = emerging upsell ยังไม่ถูก price in"
      ],
      whyDifferent: "DWG file format เป็น ISO standard (ISO 19500) และ Revit = BIM standard ระดับโลกที่ใช้ใน major construction project ทุกที่ — switching cost ไม่ใช่แค่ราคา software แต่ team recertification + workflow rebuild ทั้งองค์กร"
    },
    thesisBullets: [
      { title: "FCF Inflection Post-Subscription (ADBE Pattern)", why: "ADSK completed subscription transition ~FY2022 เหมือน ADBE ที่ทำใน 2013-2017 — หลัง transition FCF margin expand จาก ~20% → ~45-48%; FCF Yield 5.62% ที่ $229 = real cash" },
      { title: "DWG/Revit = 40-Year Unbreakable Moat", why: "ISO standard format + professional certification ecosystem + contractor interoperability = switching cost ที่ทำลายได้ยากที่สุดใน enterprise software" },
      { title: "AI Integration Genuine — Premium Upsell Not Priced In", why: "Forma BIM AI และ Fusion 360 Generative Design integrate AI เข้า core workflow ไม่ใช่แค่ UI overlay — premium tier upsell ยังไม่ถูก price in ที่ $229" }
    ],
    esgBreakdown: { e: 6.5, s: 6.5, g: 7.0, overall: 6.7, notes: "Low E footprint (SaaS); S concern: pricing accessibility for developing world architects; G: standard, no dual-class" },
    revenueSegments: [
      { name: "AEC (Architecture/Engineering/Construction)", pct: 50 },
      { name: "Manufacturing (Fusion 360/Inventor)", pct: 30 },
      { name: "Media & Entertainment", pct: 10 },
      { name: "AutoCAD/Other", pct: 10 }
    ],
    competitorData: [
      { name: "Adobe (ADBE)", metric: "P/E ~25x, ROIC 37%, Rev Growth +10%", position: "Closest SaaS peer" },
      { name: "PTC Inc.", metric: "P/E ~35x, ROIC 25%, Rev Growth +13%", position: "CAD/PLM competitor" },
      { name: "Bentley Systems (BSY)", metric: "P/E ~38x, ROIC 20%, Rev Growth +11%", position: "AEC engineering peer" },
      { name: "Dassault Systemes", metric: "EU listed, 3DEXPERIENCE platform", position: "Enterprise direct competitor" }
    ],
    geographyRevenue: [
      { region: "Americas", pct: 52 },
      { region: "EMEA", pct: 31 },
      { region: "APAC", pct: 17 }
    ],
    bullFlipTriggers: [
      "ARR growth >= 16% for 2+ consecutive quarters",
      "Forma/Fusion AI ARR > $200M",
      "AEC construction recovery (housing starts >= 1.4M/yr)",
      "Rate cut >= 100bps by end 2026",
      "Net Revenue Retention >= 113%"
    ],
    bearFlipTriggers: [
      "Revenue growth < 12% for 2 consecutive quarters",
      "ARR growth decelerates below 10%",
      "Major AI competitor launches free/cheap BIM/CAD with >15% enterprise adoption",
      "Net Revenue Retention falls below 100%",
      "Rate higher-for-longer through FY2028"
    ],
    thesisInvalidation: [
      "Subscription churn spike >5% annual",
      "EU Open BIM mandate forces DWG migration",
      "Free AI design tool adopted by top AEC firms for primary workflow"
    ],
    reportFile: "reports/ADSK_2026-06-09.md",
    maxDrawdown: -0.54
  },
'''

def patch_data_js():
    with open(DATA_JS_PATH, 'rb') as f:
        content = f.read().decode('utf-8')

    # Check if ADSK already exists
    if '"ADSK"' in content:
        print("ADSK entry already exists in data.js — skipping")
        return

    # Find insertion point: before the closing ];
    # Look for the last },\n]; pattern
    insert_marker = '},'
    close_marker = '\n];'

    # Find last occurrence of },  followed by \n];
    last_entry_end = content.rfind('},\n];')
    if last_entry_end == -1:
        # Try alternate format
        last_entry_end = content.rfind('},\n]')
        if last_entry_end == -1:
            print("ERROR: Could not find insertion point in data.js")
            return

    # Insert after the last },
    insert_pos = last_entry_end + 2  # after },
    new_content = content[:insert_pos] + '\n' + ADSK_ENTRY + content[insert_pos:]

    # Update LAST_UPDATED
    new_content = re.sub(
        r'const LAST_UPDATED = "[^"]*";',
        'const LAST_UPDATED = "2026-06-09";',
        new_content
    )

    with open(DATA_JS_PATH, 'wb') as f:
        f.write(new_content.encode('utf-8'))

    print("SUCCESS: ADSK entry added to dashboard/data.js")
    print("LAST_UPDATED set to 2026-06-09")

if __name__ == '__main__':
    patch_data_js()
