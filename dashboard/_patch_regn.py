#!/usr/bin/env python3
"""
Leo's patch script — REGN entry for dashboard/data.js
Run: python dashboard/_patch_regn.py
Adds REGN entry and updates LAST_UPDATED to 2026-06-03
"""

import os
import re

DATAJS = os.path.join(os.path.dirname(__file__), "data.js")

REGN_ENTRY = r"""  {
    ticker: "REGN",
    company: "Regeneron Pharmaceuticals, Inc.",
    date: "2026-06-03",
    version: "v1",
    sector: "Healthcare / Pharma-Biotech",
    price: 602.00,
    recommendation: "BUY",
    blendedFV: 792.00,
    targetBull: 945.00,
    targetBase: 737.00,
    stopLoss: 482.00,
    convictionEmma: 7.5,
    convictionQuinn: 7.0,
    convictionBear: 7.0,
    convictionAvg: 7.2,
    mosPct: 31.6,
    pwEV: 787.50,
    beta: 0.70,
    sharpe1Y: 0.50,
    maxDrawdown: -0.38,
    moat: "Wide",
    esgRating: "Medium-High",
    esgScore: 6.4,
    keyThesis: "Wide Moat Pharma ราคา Discount — Dupixent COPD ramp ยังไม่ถูก price in อย่างเต็มที่ P/E 14-15x ต่ำสุดใน peer group สำหรับ Wide Moat + 19% growth + 85% gross margin",
    topRisk: "IRA Medicare Drug Negotiation (Dupixent FY2027 prob 25-30%) + Eylea biosimilar Q3 2026 negative surprise",
    entryZone: "$575-625 (T1), $510-570 (T2), $460-510 (T3)",
    positionSize: "T1 4-5%, Max 8%",
    businessSummary: {
      oneLiner: "Regeneron สร้าง Dupixent ซึ่งเป็น biologic ที่รักษา inflammatory diseases 8 indications รวมถึง COPD ที่เพิ่งได้รับอนุมัติ Sep 2024 — 37M US COPD patients = TAM ใหม่ขนาดมหึมา",
      analogy: "เหมือน Humira ในยุคของ AbbVie แต่ Dupixent มีข้อได้เปรียบด้าน mechanism ที่ broader และ safer profile — platform drug ไม่ใช่ single-indication",
      moneyFlow: [
        "Dupixent (~70%) — IL-4/IL-13 dual blockade biologic ร่วมกับ Sanofi (REGN รับ ~50% profit); US+Global",
        "Eylea (~18%) — VEGF inhibitor ophthalmic; declining ด้วย biosimilar แต่ Eylea HD (8mg) ช่วย offset",
        "Other Products (~7%) — Kevzara, Praluent, Pozelimab, Inmazeb",
        "Technology Licensing (~5%) — VelociGene/VelocImmune platform; milestone payments"
      ],
      whyDifferent: "Dupixent เป็น rare 'platform drug' ที่มี 8 approved indications — COPD approval Sep 2024 เปิด TAM 37M patients ซึ่ง market ยังไม่ได้ให้มูลค่าอย่างเต็มที่ ขณะที่ P/E ต่ำสุดใน peer group"
    },
    thesisBullets: [
      { title: "Dupixent COPD = Missed Opportunity", why: "37M US COPD patients; penetration <5% หลัง 1+ ปีที่ approve = 3-5 ปีของ ramp curve ยังอยู่ข้างหน้า; peak COPD contribution $4-8B/yr ยังไม่ได้ price in" },
      { title: "P/E 14-15x ต่ำผิดปกติสำหรับ Wide Moat", why: "ABBV P/E 16-17x, LLY 40-50x แต่ REGN Wide Moat + 19% growth + 85% gross margin ได้ P/E ต่ำสุดในกลุ่ม = Eylea discount over-punishes Dupixent quality" },
      { title: "FCF Fortress + Net Cash $11-13B", why: "FCF Yield ~7% + Net Cash มากกว่า Debt = buyback capacity + pipeline M&A optionality; ผู้ถือหุ้นได้ประโยชน์จาก capital return ระหว่างรอ pipeline" },
      { title: "R&D Platform Moat (VelociGene/VelocImmune)", why: "Proprietary antibody discovery platform ที่ผลิต best-in-class candidates ได้เร็ว = structural advantage ที่ยากจะลอกเลียน; moat source ที่ 2 รองจาก Dupixent" },
      { title: "No China/Tariff Risk", why: "US-based manufacturing (Tarrytown, NY) + revenue majority US = immune จาก US-China tariff headwinds ที่กระทบ portfolio names อื่นๆ" }
    ],
    esgBreakdown: { e: 7, s: 5.5, g: 6.5, overall: 6.4 },
    revenueSegments: [
      { label: "Dupixent Collaboration", value: 68, revenue: "~$9.7B TTM (share)", growth: "+25-30% YoY", margin: "~70%" },
      { label: "Eylea (Original + HD)",  value: 18, revenue: "~$2.6B TTM", growth: "-15% (Original) / +HD offset", margin: "~75%" },
      { label: "Other Products",         value:  9, revenue: "~$1.3B", growth: "+5-10%", margin: "~65%" },
      { label: "Tech Licensing + Other", value:  5, revenue: "~$0.7B", growth: "+Milestones", margin: "~90%" }
    ],
    geographyRevenue: {
      unitedStates: "~70%",
      international: "~30% (via Sanofi global commercialization — Dupixent)",
      china: "<2% (not a key market — minimal tariff risk)",
      europe: "~15% (via Sanofi EU distribution)"
    },
    competitorData: [
      { ticker: "REGN", revenueGrowth: 19, operatingMargin: 32, marketCap: 64,
        strengths: "Dupixent 8 indications, COPD TAM, R&D platform moat, No China risk", weaknesses: "Eylea biosimilar, Sanofi 50% dependency, Founder key-person", threatLevel: "SUBJECT" },
      { ticker: "AMGN", revenueGrowth: 10, operatingMargin: 35, marketCap: 140,
        strengths: "Diversified biologics, Biosimilar business, Rare disease portfolio", weaknesses: "Lower growth vs REGN, legacy revenue issues", threatLevel: "LOW" },
      { ticker: "ABBV", revenueGrowth: 20, operatingMargin: 30, marketCap: 310,
        strengths: "Skyrizi/Rinvoq (replacing Humira), P/E inline, dividend", weaknesses: "Humira cliff past peak, Rinvoq regulatory risk", threatLevel: "LOW" },
      { ticker: "BMY", revenueGrowth: 0, operatingMargin: 20, marketCap: 135,
        strengths: "Eliquis, Opdivo oncology franchise", weaknesses: "Pipeline underperformance, revenue declining", threatLevel: "LOW" }
    ],
    customerConcentration: {
      sanofi: "~65-70% (Dupixent profit partner — key relationship)",
      usMedicaid: "~10-15% (IRA risk)",
      usMedicare: "~10-15% (IRA negotiation eligible)",
      international: "~30% via Sanofi"
    },
    bullFlipTriggers: [
      "Dupixent Q3 2026 Growth ≥ 30% YoY = COPD ramp confirmed, add T2",
      "IRA Exempts Dupixent from FY2027 Negotiation = largest risk removed, add T2/T3",
      "Fianlimab Phase 3 Positive (Melanoma) = $2-4B pipeline validated",
      "Eylea HD Quarterly Revenue ≥ $800M = biosimilar defense confirmed",
      "Stock ≤ $500 = MOS ≥ 50% even vs Bear DCF $560"
    ],
    bearFlipTriggers: [
      "IRA Selects Dupixent for FY2027 Negotiation (Q4 2026) = valuation reset -20-25%, review",
      "Eylea Revenue Decline > 50% YoY for 2 consecutive quarters = transition failure",
      "Dupixent COPD Penetration < 5% at 6 months = COPD narrative collapses",
      "Sanofi Strategic Review or Profit Warning = collaboration risk",
      "Fianlimab + Linvoseltamab Both Fail = pipeline optionality gone"
    ],
    thesisInvalidation: "IRA cuts Dupixent 40%+ AND major pipeline drugs fail → DCF FV $350-400 = thesis wrong; OR CEO Schleifer departs without succession → 30-day re-analysis required",
    reportFile: "../reports/REGN_2026-06-03.md",
    maxDrawdown: -0.38,
    fullContent: `# REGN — Regeneron Pharmaceuticals, Inc. (BUY)\n\nBlended FV $792 | MOS +31.6% | Conviction 7.2/10\n\nWide Moat Pharma at unwarranted discount. Dupixent COPD ramp = missed by market. P/E 14-15x lowest in peer group. FCF Yield ~7%. Value Bucket: MOS ≥ 15% ✅ + Conv ≥ 7.0 ✅\n\nTop Risk: IRA Medicare Drug Negotiation (25-30% prob FY2027) + Eylea Q3 2026 biosimilar negative surprise\n\nSee full report: reports/REGN_2026-06-03.md`
  },
"""

def patch():
    with open(DATAJS, "rb") as f:
        content = f.read().decode("utf-8")

    # Check if REGN already exists
    if '"REGN"' in content:
        print("REGN already exists in data.js — skipping to avoid duplicate")
        return

    # Find insertion point: before the closing ];
    # Pattern: last },\n]; or },\n\n];
    insert_marker = "];"
    idx = content.rfind(insert_marker)
    if idx == -1:
        print("ERROR: Could not find ]; in data.js")
        return

    # Find the last } before ];
    # Insert REGN entry before ];
    new_content = content[:idx] + REGN_ENTRY + content[idx:]

    # Update LAST_UPDATED
    new_content = re.sub(
        r'const LAST_UPDATED = "[^"]*";',
        'const LAST_UPDATED = "2026-06-03";',
        new_content
    )

    with open(DATAJS, "wb") as f:
        f.write(new_content.encode("utf-8"))

    print("SUCCESS: REGN entry added to data.js")
    print("LAST_UPDATED updated to 2026-06-03")

if __name__ == "__main__":
    patch()
