# -*- coding: utf-8 -*-
"""
Patch FPS object in data.js — add missing dashboard fields.
Safe: reads full file, replaces FPS block only, verifies result.
"""

import re, sys

FILE = "data.js"
content = open(FILE, encoding="utf-8").read()

# ── locate FPS object ──────────────────────────────────────────────────────────
fps_ticker_idx = content.find('ticker: "FPS"')
assert fps_ticker_idx != -1, "FPS ticker not found in data.js"

block_start = content.rfind("{", 0, fps_ticker_idx)
depth, i = 0, block_start
while i < len(content):
    if content[i] == "{":
        depth += 1
    elif content[i] == "}":
        depth -= 1
        if depth == 0:
            block_end = i
            break
    i += 1

old_block = content[block_start : block_end + 1]

# ── new fields to inject (before closing }) ───────────────────────────────────
NEW_FIELDS = """
    maxDrawdown: -49.0,
    reportFile: "../reports/FPS_2026-05-22.md",
    businessSummary: {
      oneLiner: "FPS ออกแบบและผลิตระบบจ่ายไฟฟ้า (switchgear, transformers, UPS) สำหรับ AI Data Centers, Power Grids และ Industrial Facilities",
      analogy: "เหมือน 'ระบบไฟฟ้า' ของ AI Data Center — GPU ของ NVIDIA ทรงพลังแค่ไหนก็ต้องการ power distribution ที่น่าเชื่อถือ FPS คือผู้ส่งพลังงานนั้น",
      moneyFlow: [
        "AI Data Centers (~60% est.) ซื้อ switchgear, transformers, UPS สำหรับ hyperscale facility — project-based $500K–$5M ต่อ unit",
        "Power Grid/Utilities (~25% est.) ซื้อ distribution equipment สำหรับ grid modernization",
        "Industrial Facilities (~15% est.) custom power solutions + after-sales service contracts"
      ]
    },
    thesisBullets: [
      { title: "AI Data Center Power Pure-Play", why: "FPS เป็น pure-play ใน power distribution สำหรับ AI Data Centers — backlog $1.5B + BTB 2.3x = demand visibility ดีมากในระยะ 12-15 เดือน" },
      { title: "Revenue Growth 387% TTM", why: "Revenue TTM $1.196B จาก $245.79M ใน FY2024 — โตเร็วมาก แต่ต้องพิสูจน์ว่า structural ไม่ใช่ cyclical pull-forward" },
      { title: "FY2026 Guidance Raised", why: "FY2026 guidance $1.35-1.39B (+82% YoY midpoint) หลัง Q3 record $378.7M — management confidence สูงและ booking momentum แข็ง" }
    ],
    esgBreakdown: { e: 7, s: 6, g: 6, overall: 6.3 },
    revenueSegments: [
      { label: "AI Data Centers", value: 60 },
      { label: "Power Grid / Utilities", value: 25 },
      { label: "Industrial Facilities", value: 15 }
    ],
    competitorData: [
      { ticker: "FPS",  company: "Forgent Power Solutions", revenueGrowth: 103, operatingMargin: 8.3,  marketCap: 14.92 },
      { ticker: "POWL", company: "Powell Industries",        revenueGrowth: 60,  operatingMargin: 14.0, marketCap: 2.8   },
      { ticker: "ETN",  company: "Eaton Corp",               revenueGrowth: 8,   operatingMargin: 16.5, marketCap: 135   },
      { ticker: "HUBB", company: "Hubbell",                  revenueGrowth: 8,   operatingMargin: 18.0, marketCap: 18    },
      { ticker: "ESE",  company: "ESCO Technologies",        revenueGrowth: 10,  operatingMargin: 11.5, marketCap: 3.8   }
    ],
    geographyRevenue: {
      unitedStates: "~70% est. (domestic industrial + data center)",
      international: "~30% est.",
      chinaExposure: "<5% — LOW (tariff risk minimal vs hardware exporters)"
    },
    bullFlipTriggers: [
      "FCF turns positive — scaling complete CapEx normalizing → FV ขึ้นสู่ $35-45",
      "Net Debt/EBITDA < 2.0x ภายใน 2 ปี — financial risk ลดชัดเจน",
      "Gross Margin ขยายสู่ 38%+ — evidence moat hardening และ pricing power",
      "Book-to-bill > 2.0x ใน FY2027 ต่อเนื่อง — demand structural ไม่ใช่ cyclical",
      "Revenue CAGR >40% ยืนใน 4 quarters ต่อเนื่อง — เปลี่ยน base case assumptions"
    ],
    bearFlipTriggers: [
      "Revenue guidance cut หรือ FY2027 guidance < +15% — growth deceleration signal",
      "Book-to-bill < 1.0x สองไตรมาสติดกัน — demand normalization confirmed",
      "Gross Margin < 30% — competition + commodity pressure materializing",
      "Equity offering ประกาศ — dilution signal management เห็น cash crunch",
      "Hyperscaler CapEx guidance ลด >20% — primary demand driver หาย"
    ],
    thesisInvalidation: "FY2027 revenue < $1,200M (flat vs TTM) = growth cycle จบ thesis ผิดทั้งหมด OR Net Debt/EBITDA > 5.0x = financial distress territory OR covenant breach"
"""

# ── inject before closing } of FPS block ─────────────────────────────────────
# Remove the last closing } and re-add with new fields
new_block = old_block[:-1].rstrip() + ",\n" + NEW_FIELDS.rstrip() + "\n  }"

# ── replace in content ────────────────────────────────────────────────────────
new_content = content[:block_start] + new_block + content[block_end + 1:]

# ── verify ────────────────────────────────────────────────────────────────────
checks = [
    'revenueSegments',
    'competitorData',
    'geographyRevenue',
    'businessSummary',
    'thesisBullets',
    'esgBreakdown',
    'bullFlipTriggers',
    'bearFlipTriggers',
    'thesisInvalidation',
    'reportFile',
    'maxDrawdown',
]
missing = [c for c in checks if c not in new_content]
if missing:
    print("FAIL — missing fields after patch:", missing)
    sys.exit(1)

# ── write ─────────────────────────────────────────────────────────────────────
open(FILE, "w", encoding="utf-8").write(new_content)
print("SUCCESS — FPS patched with", len(checks), "new fields")
print("Total file lines:", new_content.count("\n"))
