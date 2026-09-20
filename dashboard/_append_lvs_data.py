#!/usr/bin/env python3
"""
Leo's dashboard patch script — LVS 2026-09-20
Adds LVS entry to dashboard/data.js REPORTS array (append before closing '];')
Run: python dashboard/_append_lvs_data.py
"""
import re
import json

DATA_JS_PATH = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
REPORT_MD_PATH = r"C:\Users\user\Desktop\บลจ\บลจ CFA\reports\LVS_2026-09-20.md"

with open(REPORT_MD_PATH, "r", encoding="utf-8") as f:
    report_md = f.read()

# Escape for JS template literal: backslash, backtick, ${
escaped = report_md.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

full_content_literal = "`" + escaped + "`"

entry = """  {
    ticker: "LVS",
    company: "Las Vegas Sands Corp.",
    date: "2026-09-20",
    version: "v1",
    sector: "Gaming/Leisure/Travel (Casino & Integrated Resorts)",
    bucket: "Value",
    price: 39.98,
    recommendation: "WATCH",
    blendedFV: 47.58,
    mosPct: 16.0,
    conviction: 6.33,
    convictionEmma: 7,
    convictionQuinn: 6,
    convictionBear: 6,
    convictionAvg: 6.33,
    targetBull: 54.55,
    targetBase: 47.58,
    stopLoss: 31.60,
    pwEV: 47.17,
    beta: 0.82,
    sharpe1Y: 0.137,
    maxDrawdown: -0.432,
    moat: "Narrow-Wide",
    esgRating: "Medium",
    esgScore: 5.0,
    macroRegime: "TRANSITIONAL-CAUTIOUS",
    sp500Reference: 7650.50,
    sp500ReferenceNote: "7,650.50 (2026-09-18 close — Yahoo Finance + TheStreet ✅ 2 sources cross-check per Single Source of Truth Rule; verified by Atlas 2026-09-20)",
    revenueGrowthYoY: 18.1,
    revenueGrowthNote: "Revenue TTM +18.1% YoY — เร็วสุดใน peer group (MGM +3.2% / WYNN +6.4% / MLCO +6.0%) แต่ยังจัดเป็น Value bucket (DCF/FCFF-based, mature FCF-positive business) ไม่ใช่ Growth bucket ตาม CLAUDE.md",
    entryZone: "$38.00–$41.00 (mid $39.50) — future watch only, ไม่ deploy ที่ราคาปัจจุบัน",
    positionSize: "0% ตอนนี้ (Conviction 6.33 < 7.0 gate + Regime TC suspends Force Deploy) — ถ้า gate ผ่านในอนาคต: 3-5% pre-multiplier × 0.75x TC ≈ 2.25-3.75%",
    keyThesis: "LVS เทรดที่ discount ~20% เทียบ peer median ทั้ง P/E และ EV/EBITDA ทั้งที่ growth (+18.1%)/margin (23.3%)/ROIC (19.8%) สูงสุดในกลุ่ม — Wide-ish regulatory-scarcity moat (Macau 6-concession cap ถึง 2033, Singapore duopoly) แต่ MOS หัวข่าว 16.0% พึ่งพาสมมติฐานเดียว (EV/EBITDA multiple re-rate 8.21x→9.0x ที่ไม่มี catalyst ยืนยัน) — ถ้าไม่ re-rate MOS จริงเหลือ ~1.75%. Conviction เฉลี่ย 6.33/10 ไม่ถึงเกณฑ์ Value bucket gate (≥7.0) และ Regime TRANSITIONAL-CAUTIOUS ห้าม open new positions — WATCH ไม่ BUY, เก็บเข้า buy_list รอ Q3 earnings (21 ต.ค. 2026) เป็นตัวยืนยัน",
    topRisk: "Multiple re-rating dependency (MOS ทั้งหมดพึ่งพา 8.21x→9.0x assumption ที่ไม่มี hard catalyst) | 100% geography concentration ใน Macau+Singapore, 74.8% China-linked visitor | China outbound-investment rules (ก.ค. 2026) ที่ CLSA เตือนว่าเป็น persistent sentiment risk | MBS $8B expansion มีประวัติ overrun +142% และเลื่อนมาแล้ว 1 ครั้ง (2029→2031)",
    reportFile: "../reports/LVS_2026-09-20.md",
    businessSummary: {
      oneLiner: "Las Vegas Sands เป็นเจ้าของและผู้ดำเนินการ integrated resort ขนาดใหญ่ที่สุดในมาเก๊าและสิงคโปร์ ทำเงินจาก casino gaming, โรงแรม, MICE/convention, retail และ F&B",
      analogy: "เหมือนเป็นเจ้าของ 'เมืองในเมือง' สำหรับนักท่องเที่ยว — คาสิโน + โรงแรมหรู + ห้างสรรพสินค้า + ศูนย์ประชุมรวมอยู่ในที่เดียว ดึงคนมาใช้จ่ายทุกอย่างในที่เดียวกัน",
      moneyFlow: [
        "นักท่องเที่ยว (ส่วนใหญ่จากจีนแผ่นดินใหญ่) เดินทางมามาเก๊า/สิงคโปร์",
        "ใช้จ่ายใน casino gaming (VIP rolling + mass market) เป็นรายได้หลัก",
        "บวกรายได้เสริมจากโรงแรม, retail mall, MICE/convention, F&B ที่ cross-sell กันในระบบนิเวศเดียว",
        "กำไรถูกจำกัดคู่แข่งด้วยใบอนุญาตที่รัฐบาลควบคุม (Macau 6 ราย, Singapore 2 ราย) ทำให้ margin สูงกว่าธุรกิจทั่วไป"
      ],
      whyDifferent: "รัฐบาลมาเก๊าและสิงคโปร์จำกัดจำนวนใบอนุญาต casino ตามกฎหมาย (Macau 6 concessions ถึง 2033, Singapore duopoly 2 ราย) — คู่แข่งใหม่เข้าตลาดแทบเป็นไปไม่ได้ ต่างจาก moat แบบ brand/switching cost ทั่วไปที่ยังพอแข่งขันได้",
      simpleRisk: "รายได้ 100% ผูกกับมาเก๊า+สิงคโปร์และนักท่องเที่ยวจีน — ถ้าจีนคุมเข้มการเดินทางออกนอกประเทศหรือกฎระเบียบมาเก๊าเปลี่ยน จะกระทบบริษัททั้งหมดโดยตรง ไม่มีตลาดอื่นมาช่วยกระจายความเสี่ยง"
    },
    thesisBullets: [
      { title: "Wide-ish Moat จาก Regulatory Scarcity", why: "Macau concession ล็อกถึง 2033 + Singapore duopoly (2 ใบอนุญาตเท่านั้น) — government-controlled barrier ที่แข็งแกร่งกว่า brand moat ทั่วไป แต่ Bear challenge ให้เป็น Narrow-to-Wide เพราะ Macau เป็น 6-operator oligopoly ที่แข่งขัน amenity arms race ต่อเนื่อง" },
      { title: "Valuation Mismatch ชัดเจน", why: "เทรดที่ discount ~20% เทียบ P/E และ EV/EBITDA ของ peer median ทั้งที่ growth/margin/ROIC สูงสุดในกลุ่มทุกตัว" },
      { title: "Beaten-down เพราะ Cyclical ไม่ใช่ Structural (แต่ Bear ตั้งคำถาม)", why: "Macau VIP hold softness + World Cup 2026 ดึง visitation ชั่วคราว, market share ยังเพิ่มขึ้นต่อเนื่อง (24.5%→26.2%) — แต่ Bear ชี้ว่า 'temporary' narrative ยังไม่ verify อิสระ อาจเป็น credit-tightening structural ก็ได้" },
      { title: "MOS 16.0% headline แต่ fragile", why: "Blended FV $47.58 vs ราคา $39.98 — MOS ผ่านเกณฑ์ 15% แบบเฉียดฉิว แต่พึ่งพา multiple re-rating assumption เดียว (8.21x→9.0x); no-rerate scenario เหลือ MOS ~1.75% เท่านั้น" },
      { title: "China/Geography Concentration เป็นความเสี่ยงหลัก", why: "100% revenue จาก Macau+Singapore, 74.8% visitor mix เป็นจีนแผ่นดินใหญ่ — ไม่มี diversification buffer ถ้า China policy เปลี่ยน" }
    ],
    bearRisks: [
      { title: "Multiple re-rating คือ MOS ทั้งหมด", why: "ที่ multiple ปัจจุบัน 8.21x MOS แท้จริงมีแค่ +3.0% — headline 16.0%/15.24% ทั้งหมดคือการ bet ว่าตลาด re-rate กลับ 9.0x ซึ่งไม่มี hard catalyst; UBS เองใช้ blended multiple ใกล้ราคาตลาดปัจจุบัน ไม่ใช่ 9.0x+" },
      { title: "MBS $8B expansion มีประวัติ slip", why: "Budget เดิม $3.3B (2019) → $8.0B ปัจจุบัน (+142% overrun) และเลื่อนมาแล้ว 1 ครั้ง (2029→2031) — Emma's terminal value assume clean landing 2031 ซึ่งขัดกับ track record ของ project เอง" }
    ],
    esgBreakdown: { e: 6, s: 5, g: 4, overall: 5.0 },
    esgBreakdownNote: "Medium Risk (Sustainalytics 20.7). ค่านี้คือค่าที่ปรับแล้วหลัง Bear challenge (Governance 5→4 จาก insider selling ~$174.5M ใน 90 วันต้นปี 2026 รวม former CEO 1.2M หุ้น; Overall 5.3→5.0) — Morgan QA caveat: ใช้ค่านี้ไม่ใช่ Emma's raw structured-data block (g:5, overall:5.3)",
    customerConcentration: {
      sandsChina: "~56.5% (Macau properties, Q2 2026)",
      marinaBaySands: "~43.5% (Singapore, Q2 2026)",
      top2Combined: "~100% (no US operations remaining — Las Vegas properties divested 2021-2022)"
    },
    geographyRevenue: {
      unitedStates: 0,
      international: 100,
      macau: 56.5,
      singapore: 43.5,
      chinaExposure: "74.8% ของ Macau visitor arrivals เป็น mainland China (Q1 2026)"
    },
    revenueSegments: [
      { label: "Macau (Sands China)", value: 56.5 },
      { label: "Singapore (Marina Bay Sands)", value: 43.5 },
      { label: "US/Other", value: 0 }
    ],
    competitorData: [
      { ticker: "LVS", company: "Las Vegas Sands", revenueGrowth: 18.1, operatingMargin: 23.3, marketCap: 25895 },
      { ticker: "MGM", company: "MGM Resorts", revenueGrowth: 3.2, operatingMargin: 6.5, marketCap: 9510 },
      { ticker: "WYNN", company: "Wynn Resorts", revenueGrowth: 6.4, operatingMargin: 16.0, marketCap: 8290 },
      { ticker: "MLCO", company: "Melco Resorts", revenueGrowth: 6.0, operatingMargin: 13.4, marketCap: 1760 }
    ],
    bullFlipTriggers: [
      "EV/EBITDA multiple re-rate จริงถึง ≥9.0x บน verified market data (ไม่ใช่แค่ consensus PT) ภายใน 1-2 ไตรมาส",
      "Q3 2026 earnings (21 ต.ค.) ยืนยัน VIP hold normalize กลับสู่ค่าเฉลี่ย + Macau market share รักษา ≥26%",
      "China ออกคำชี้แจง/carve-out ยืนยันว่ากฎ outbound-investment (ก.ค. 2026) ไม่กระทบ gaming-related travel spend",
      "MBS expansion ยืนยัน completion date 2031 ไม่มี budget revision เพิ่มเติมอีก ≥2 ไตรมาสติด"
    ],
    bearFlipTriggers: [
      "Multiple ค้างที่ ≤8.21x ผ่าน Q1 2027 (อีก 2 ไตรมาส) โดยไม่มี re-rating catalyst",
      "China capital-control action ที่กระทบ GGR จริง (ไม่ใช่แค่ sentiment)",
      "MBS expansion ประกาศเลื่อนเพิ่มเติม (เกิน 2031) หรือ cost revision เกิน $8.0B",
      "Macau market share หลุดต่ำกว่า 25% สองไตรมาสติด",
      "Insider selling เร่งขึ้นหลัง CEO transition settle แล้ว"
    ],
    thesisInvalidation: "Macau/Singapore government เปลี่ยนจำนวน concession/license ในทางที่ทำลาย regulatory-scarcity moat หรือ ยืนยัน GGR-level impact (ไม่ใช่แค่ sentiment) จาก China capital controls ต่อ outbound gaming spend",
    fullContent: FULL_CONTENT_PLACEHOLDER
  }
"""

entry = entry.replace("FULL_CONTENT_PLACEHOLDER", full_content_literal)

with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
    content = f.read()

marker = "\n];"
idx = content.rfind(marker)
if idx == -1:
    raise SystemExit("Could not find closing '];' for REPORTS array")

# Find the last '}' before the marker (end of previous object) to insert comma
before = content[:idx]
after = content[idx:]

# before ends with "  }\n\n" (last object closing) - add comma after that '}'
before_stripped = before.rstrip("\n")
if not before_stripped.endswith("}"):
    raise SystemExit("Unexpected structure: previous entry does not end with '}'")

new_content = before_stripped + ",\n\n" + entry + after

with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print("LVS entry appended successfully.")
