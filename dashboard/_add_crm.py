#!/usr/bin/env python3
"""
Leo's dashboard updater script — CRM 2026-05-29
ใช้ binary read/write เพื่อป้องกัน encoding issues
"""
import sys
import os

DATA_JS = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

# Read file as text
with open(DATA_JS, "r", encoding="utf-8") as f:
    content = f.read()

# Update LAST_UPDATED
content = content.replace('const LAST_UPDATED = "2026-05-22";', 'const LAST_UPDATED = "2026-05-29";')

# New CRM entry (no trailing comma — it will be the last element, trailing comma is valid in JS but keeping clean)
crm_entry = r"""  {
    ticker: "CRM",
    company: "Salesforce, Inc.",
    date: "2026-05-29",
    sector: "Enterprise Software / Cloud CRM",
    price: 181.00,
    recommendation: "BUY",
    blendedFV: 258.00,
    targetBull: 365.00,
    targetBase: 258.00,
    stopLoss: 146.00,
    convictionEmma: 7,
    convictionQuinn: 7,
    convictionBear: 7,
    convictionAvg: 7.0,
    mosPct: 42.5,
    pwEV: 243.50,
    beta: 1.20,
    sharpe1Y: 0.58,
    maxDrawdown: -0.43,
    moat: "Wide",
    esgRating: "Medium",
    esgScore: 6.0,
    keyThesis: "Wide Moat enterprise CRM trade ที่ FCF yield 9.77% + Forward P/E 13x = ถูกที่สุดในประวัติศาสตร์ Agentforce ARR $1.2B +169% YoY = AI catalyst ใหม่",
    topRisk: "ROIC 6.29% < WACC 9.5% (EVA negative) + Microsoft Dynamics structural threat",
    entryZone: "170-195",
    positionSize: "8% (T1 4%, T2 2.5%, T3 1.5%)",
    bucket: "Value",
    bullFlipTriggers: [
      "ROIC > 10% ใน 2 ไตรมาสติดต่อกัน (EVA กลับเป็นบวก)",
      "Agentforce ARR ถึง $2.5B+ ใน FY2027",
      "Revenue growth กลับมา 11%+ ใน 2 ไตรมาสติดต่อกัน",
      "Microsoft ไม่ได้ gain CRM market share (IDC confirm stable)",
      "Goodwill impairment ไม่เกิด + Slack/Tableau synergy improve"
    ],
    bearFlipTriggers: [
      "Revenue growth ต่ำกว่า 5% YoY ติดต่อ 2 ไตรมาส",
      "Agentforce ARR growth rate ลดต่ำกว่า 50% YoY",
      "ROIC ลดต่ำกว่า 5%",
      "NRR ต่ำกว่า 100%",
      "Microsoft ขโมย >= 3% CRM market share ใน 12 เดือน"
    ],
    thesisInvalidation: "Revenue YoY negative growth (RPO $72.4B ยังอยู่แต่ cancellation massive = moat ไม่มีจริง) หรือ FCF ลดต่ำกว่า $8B",
    reportFile: "../reports/CRM_2026-05-29.md",
    businessSummary: {
      oneLiner: "Salesforce ขาย cloud software ให้บริษัทใช้จัดการความสัมพันธ์กับลูกค้า (CRM) — ผู้นำตลาดโลก 17-18% share",
      analogy: "เหมือน ระบบปฏิบัติการ ของทีม sales และ customer service บริษัทใหญ่ — ถ้าเปลี่ยนต้องใช้เวลา 2-3 ปี",
      moneyFlow: [
        "บริษัทสมัครใช้ Salesforce รายปี (subscription) ตามจำนวน users",
        "Salesforce เก็บค่าต่ออายุทุกปีโดยอัตโนมัติ (retention rate >90%)",
        "บริษัทที่ติดแล้วมักซื้อ module เพิ่ม (upsell) เช่น Marketing Cloud, Service Cloud",
        "ล่าสุด: ขาย Agentforce AI agents ที่ทำงานแทน human — per-action pricing ใหม่"
      ],
      whyDifferent: "Data lock-in + ecosystem 7,000+ apps บน AppExchange ทำให้ enterprise เปลี่ยนไปยากมาก — switching cost 18-36 เดือน + cost หลาย$10M",
      simpleRisk: "Microsoft กำลัง bundle CRM ฟรีใน Microsoft 365 ที่ลูกค้าจ่ายอยู่แล้ว"
    },
    thesisBullets: [
      { title: "FCF yield 9.77% มองข้ามโดยตลาด", why: "Enterprise SaaS wide moat ปกติ trade ที่ FCF yield 3-5% — 9.77% แสดงว่าตลาด over-discount growth deceleration มากเกินจริง" },
      { title: "Agentforce ARR $1.2B +169% YoY", why: "New AI revenue layer บน CRM base — ถ้า Agentforce reach $3-5B ใน FY2028 เท่ากับ revenue engine ใหม่เพิ่มขึ้น 8-13% จากฐาน" },
      { title: "RPO $72.4B = 1.9x revenue — Visibility สูงมาก", why: "Contractual backlog ปกป้อง downside ถ้า economy ชะลอ — ลูกค้า commit แล้วหลายปีล่วงหน้า" },
      { title: "Forward P/E 13x = ถูกที่สุดใน enterprise SaaS", why: "52% discount vs sector median 27x — discount ขนาดนี้ผิดปกติสำหรับ Wide Moat company" }
    ],
    esgBreakdown: {
      e: 7,
      s: 6.5,
      g: 4.5,
      overall: 6.0
    },
    customerConcentration: {
      note: "ไม่มีลูกค้าเดี่ยวเกิน 10% (Salesforce 10-K disclosure)",
      base: "150,000+ องค์กรทั่วโลก กระจายดีมาก",
      fortune500: "90%+ ใช้ผลิตภัณฑ์ Salesforce อย่างน้อย 1 อย่าง"
    },
    geographyRevenue: {
      americas: "~65-67%",
      europe: "~20-22%",
      asiaPacific: "~12-13%",
      china: "<1% (ต่ำมาก — ไม่มีความเสี่ยง US-China)"
    },
    competitorData: [
      { ticker: "CRM", company: "Salesforce", revenueGrowth: 8.5, operatingMargin: 15, marketCap: 175 },
      { ticker: "MSFT", company: "Microsoft", revenueGrowth: 14, operatingMargin: 45, marketCap: 3200 },
      { ticker: "NOW", company: "ServiceNow", revenueGrowth: 21, operatingMargin: 20, marketCap: 200 },
      { ticker: "WDAY", company: "Workday", revenueGrowth: 16, operatingMargin: 12, marketCap: 65 },
      { ticker: "SAP", company: "SAP SE", revenueGrowth: 9, operatingMargin: 18, marketCap: 280 }
    ],
    revenueSegments: [
      { label: "Americas", value: 66 },
      { label: "Europe", value: 21 },
      { label: "Asia Pacific", value: 13 }
    ],
    fullContent: `# CRM — Salesforce, Inc. Full Research Report 2026-05-29\n\nSee reports/CRM_2026-05-29.md for full content\n\nBUY | Blended FV $258 | MOS +42.5% | Conviction 7.0/10\nEntry Zone $170-195 | Stop Loss $146 (-20% from entry $182.50)\nFCF yield 9.77% + Forward P/E 13x + Agentforce ARR $1.2B +169% + RPO $72.4B\nValue Bucket: IPS Gate PASS (Conv 7.0 >= 7.0, MOS +42.5% >= 15%)\nRisk: ROIC 6.29% < WACC 9.5% (EVA negative), Microsoft Dynamics structural threat`
  }"""

# Check if CRM already exists
if '"CRM"' in content or 'ticker: "CRM"' in content:
    print("WARNING: CRM entry already exists in data.js — skipping insert")
    sys.exit(0)

# Find insertion point: the last  }  followed by \n];
# We need to add a comma after the last entry's closing brace, then append CRM entry
# Pattern to find: the closing  }\n]; of the last element
insert_before = "];"

# Find the position of final ];
pos = content.rfind(insert_before)
if pos == -1:
    print("ERROR: Could not find '};' in data.js")
    sys.exit(1)

# The character before ];\n should be the closing } of the last entry
# We need to insert a comma after that } and then add the CRM entry
# Find the last } before pos
last_brace_pos = content.rfind("  }", 0, pos)
if last_brace_pos == -1:
    print("ERROR: Could not find last entry closing brace")
    sys.exit(1)

# Verify the text at last_brace_pos is '  }'
if content[last_brace_pos:last_brace_pos+3] != "  }":
    print(f"ERROR: Unexpected text at last brace position: '{content[last_brace_pos:last_brace_pos+10]}'")
    sys.exit(1)

# Insert: replace last "  }" with "  }," and then append CRM entry before ];
# Build new content: everything up to and including the last }, then comma, newline, CRM entry, newline, ];
new_content = (
    content[:last_brace_pos + 3]   # up to and including "  }"
    + ","                           # add comma after last entry
    + "\n"                          # newline
    + crm_entry                     # CRM entry (no trailing comma — it's the new last)
    + "\n"                          # newline before ];
    + content[pos:]                 # ];\n and rest of file
)

# Write back
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(new_content)

print("SUCCESS: CRM entry added to dashboard/data.js")
print(f"File size: {len(new_content)} chars")
print(f"Last entry closed at position: {last_brace_pos}")
print(f"Insertion point (]): {pos}")
