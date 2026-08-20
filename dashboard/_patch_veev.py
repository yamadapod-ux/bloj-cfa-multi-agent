"""
dashboard/_patch_veev.py
Patch script to REPLACE the existing VEEV (Veeva Systems Inc.) v1 entry
in dashboard/data.js REPORTS array with the v2 re-analysis entry (2026-08-20)
+ update LAST_UPDATED.

WHY THIS SCRIPT EXISTS (instead of a direct Write to data.js):
- dashboard/data.js is far too large to safely read/rewrite in full via the
  Read/Write tools in a single call.
- Per house rule "Dashboard Write Safety": NEVER use a full-file Write on
  data.js — always use a targeted Python script.
- Per CLAUDE.md Rule 11 (Re-analysis handling): REPLACE the existing VEEV
  object entirely — do NOT append a duplicate entry.

HOW TO RUN:
    cd "C:\\Users\\user\\Desktop\\บลจ\\บลจ CFA"
    python dashboard/_patch_veev.py
"""

import re
import sys
import io

DATA_JS_PATH = "dashboard/data.js"
REPORT_MD_PATH = "reports/VEEV_2026-05-11.md"
NEW_LAST_UPDATED = "2026-08-20"


def js_escape_template_literal(text: str) -> str:
    """Escape a string for safe embedding inside a JS template literal (backtick string)."""
    text = text.replace("\\", "\\\\")
    text = text.replace("`", "\\`")
    text = text.replace("${", "\\${")
    return text


def main():
    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    with open(REPORT_MD_PATH, "r", encoding="utf-8") as f:
        report_content = f.read()

    escaped_report = js_escape_template_literal(report_content)

    # 1. Update LAST_UPDATED
    content, n = re.subn(
        r'const LAST_UPDATED = "[\d-]+";',
        f'const LAST_UPDATED = "{NEW_LAST_UPDATED}";',
        content,
        count=1,
    )
    if n != 1:
        print("WARNING: LAST_UPDATED line not found/replaced — check manually.")

    # 2. Locate the existing VEEV object boundaries.
    #    Pattern: a line "  {" followed eventually by a line containing
    #    ticker: "VEEV", ending at the matching "  },\n" right before the
    #    next "  {" (next report entry).
    veev_marker = '    ticker: "VEEV",'
    marker_idx = content.find(veev_marker)
    if marker_idx == -1:
        print("ERROR: VEEV entry not found in data.js. Aborting — no changes written.")
        sys.exit(1)

    # Walk backwards from marker_idx to find the start of this object: "  {\n"
    obj_start = content.rfind("\n  {\n", 0, marker_idx)
    if obj_start == -1:
        print("ERROR: could not locate start of VEEV object. Aborting.")
        sys.exit(1)
    obj_start += 1  # move past the leading \n so we start at "  {"

    # Walk forward from marker_idx to find the end of this object: "\n  },\n"
    # followed by the next "  {" (start of next report) — find first "\n  },\n"
    obj_end_marker = content.find("\n  },\n", marker_idx)
    if obj_end_marker == -1:
        print("ERROR: could not locate end of VEEV object. Aborting.")
        sys.exit(1)
    obj_end = obj_end_marker + len("\n  },\n")

    old_block = content[obj_start:obj_end]
    if 'ticker: "VEEV"' not in old_block:
        print("ERROR: sanity check failed — extracted block does not contain VEEV ticker. Aborting.")
        sys.exit(1)
    if 'ticker: "FICO"' in old_block or 'ticker: "LDOS"' in old_block:
        print("ERROR: sanity check failed — extracted block spans beyond VEEV entry. Aborting.")
        sys.exit(1)

    print(f"Old VEEV block located: {len(old_block)} chars, lines approx "
          f"{content[:obj_start].count(chr(10))+1} to {content[:obj_end].count(chr(10))+1}")

    # 3. Build new VEEV v2 entry
    new_block = "  {\n" + VEEV_ENTRY_BODY + "\n    fullContent: `" + escaped_report + "`,\n  },\n"

    new_content = content[:obj_start] + new_block + content[obj_end:]

    # 4. Basic sanity checks before writing
    open_braces = new_content.count("{")
    close_braces = new_content.count("}")
    open_brackets = new_content.count("[")
    close_brackets = new_content.count("]")
    if open_braces != close_braces:
        print(f"ERROR: Brace mismatch after patch ({{ {open_braces} vs }} {close_braces}) — aborting write.")
        sys.exit(1)
    if open_brackets != close_brackets:
        print(f"ERROR: Bracket mismatch after patch ([ {open_brackets} vs ] {close_brackets}) — aborting write.")
        sys.exit(1)

    # Ensure only ONE "VEEV" ticker entry exists after patch
    veev_count = new_content.count('    ticker: "VEEV",')
    if veev_count != 1:
        print(f"ERROR: expected exactly 1 VEEV ticker entry after patch, found {veev_count}. Aborting write.")
        sys.exit(1)

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("VEEV entry replaced successfully (v1 -> v2). LAST_UPDATED set to", NEW_LAST_UPDATED)
    print("Run `node -e \"require('./dashboard/data.js')\"` or open dashboard/index.html to verify.")


VEEV_ENTRY_BODY = r'''    ticker: "VEEV",
    company: "Veeva Systems Inc.",
    date: "2026-08-20",
    version: "v2",
    sector: "Healthcare Technology / Life Sciences SaaS",
    price: 251.00,
    recommendation: "HOLD/WAIT FOR PULLBACK — NO DEPLOY",
    blendedFV: 192.66,
    esgAdjFV: 188.81,
    targetBull: 245.00,
    targetBase: 188.81,
    stopLoss: 160.00,
    convictionEmma: 7.0,
    convictionQuinn: 5.5,
    convictionBear: 7.0,
    convictionAvg: 6.5,
    mosPct: -23.24,
    mosPctEsgAdj: -24.78,
    pwEV: 231.88,
    pwEvBear: 173.00,
    beta: 0.92,
    sharpe1Y: 0.53,
    maxDrawdown: -0.6374,
    moat: "Wide",
    esgRating: "Low-Medium",
    esgScore: 7.35,
    macroRegime: "RISK-ON",
    morganQA: "PASS (Data Quality 8.7/10)",
    sp500Reference: null,
    sp500ReferenceNote: "TBD — CIO data package ไม่มีตัวเลข index level ตรงๆ วันนี้ (มีแต่ P/E/earnings-yield context) — Vera ต้อง verify ย้อนหลังก่อนใช้ alpha calculation",
    bucket: "Value",
    entryZone: "T1 $185-200 (watch zone) / T2 $150-167 (target zone, MOS >=15%)",
    positionSize: "0% (NO DEPLOY — MOS gate FAIL -24.78% << 15% required, แม้ Conviction 6.5 PASS gate >=6 — single-gate failure, ต่างจาก dual-gate-failure pattern เดิม)",
    keyThesis: "Vault CRM migration win rate >80% เทียบ Salesforce พิสูจน์ moat จริงในสถานการณ์แข่งขันเต็มที่ (top-20 pharma 10-6 favoring Veeva), FCF +38.3% YoY สู่ $1,640M (margin 49.4%), Rule of 40 = 65.65% — คุณภาพธุรกิจสูงสุดตัวหนึ่งในพอร์ต แต่ราคา $251 แพงกว่าแม้แต่ Bull-case DCF ของ Emma ($245). Reclassified เป็น Value bucket (revenue growth 16.25% < 20% threshold) — Blended FV (ESG-adj) $188.81 ให้ MOS -24.78%, ล้มเหลว Value gate (>=15%) หนักมาก แม้ Conviction 6.5/10 ผ่านเกณฑ์ (>=6) สบายๆ — 'great company, priced beyond even bull-case DCF'",
    topRisk: "Fed hawkish pivot ต่อเนื่อง (2 hikes priced Sept+Dec 2026) กดดัน premium multiple (P/E TTM 43-44.5x) โดยตรง — ถ้า WACC ดันขึ้นสู่ 11.5-12% FV ร่วงสู่ $190-207; ประกอบกับ Emma-Quinn DCF base-case divergence ที่ยังไม่ reconcile ($145 vs $261.5, 80% gap จาก FCF-conversion/deferred-revenue methodology) เพิ่ม uncertainty band ให้ negative-MOS signal",
    reportFile: "../reports/VEEV_2026-05-11.md",
    businessSummary: {
      oneLiner: "Veeva ขายซอฟต์แวร์ cloud subscription เฉพาะทางให้บริษัทยา/ไบโอเทค ใช้บริหารตั้งแต่ขายยา ทดลองยา จนถึงควบคุมคุณภาพ ภายใต้กฎ FDA",
      analogy: "เหมือน Salesforce แต่สร้างมาเฉพาะสำหรับอุตสาหกรรมยา — ลูกค้าเปลี่ยนออกยากมากเพราะต้องผ่านการตรวจสอบใหม่จาก FDA ใช้เวลา 18-24 เดือน",
      moneyFlow: [
        "บริษัทยาซื้อ subscription รายปี (สัญญา 3-5 ปี) เพื่อใช้ Commercial Cloud (ขายยา) และ Vault platform (ทดลอง/กฎระเบียบ/คุณภาพ/ความปลอดภัย) — ~80% ของรายได้",
        "ลูกค้าซื้อ module เพิ่มเรื่อยๆ ภายใน customer base เดิม (เฉลี่ย 5-7 module ต่อลูกค้า จาก 2-3 module ในปี 2020) — cross-sell ไม่ต้องหาลูกค้าใหม่",
        "ค่า implementation/validation (ที่จำเป็นตามกฎ FDA) เป็นรายได้เสริมอีก ~20%",
        "กำลังย้ายลูกค้าเก่าจาก Salesforce-based CRM ไปแพลตฟอร์มตัวเอง (Vault CRM) — ล่าสุดชนะ competitive evaluation ไปแล้ว >80% ของ decisions"
      ],
      whyDifferent: "Switching cost สูงที่สุดในกลุ่ม software เพราะระบบต้องผ่านการรับรอง FDA (21 CFR Part 11) — เปลี่ยนระบบต้อง re-validate ใหม่ 18-24 เดือนและเสี่ยงตรวจสอบล้มเหลว ล่าสุดพิสูจน์แล้วจริงในการแข่งขันกับ Salesforce (win rate >80%) แม้ลูกค้าเปิดให้แข่งขันเต็มที่",
      simpleRisk: "ราคาหุ้นวิ่งขึ้นเร็วกว่าการเติบโตของธุรกิจมาก (+51% ใน 3.5 เดือน) ทำให้ตอนนี้ valuation แพงเกินกว่าที่ DCF จะ justify ได้ แม้ธุรกิจจะยังดีขึ้นจริง"
    },
    thesisBullets: [
      { title: "Vault CRM Migration สำเร็จเกินคาด", why: "Win rate >80% เทียบ Salesforce ในการแข่งขัน, ชนะ top-20 pharma decisions 10-6 — พิสูจน์ switching-cost moat ในสถานการณ์จริง (self-reported stat, 4/20 ยัง pending)" },
      { title: "FCF เร่งตัวแรง", why: "FCF +38.3% YoY สู่ $1,640M, FCF margin 49.4% — Rule of 40 = 65.65% (สูงกว่าเกณฑ์ 40% เกือบเท่าตัว)" },
      { title: "ราคาแพงกว่า fundamentals มาก", why: "P/E premium +107% เหนือ sector median, EV/EBITDA premium +164%, ราคาปัจจุบันเหนือแม้กระทั่ง Bull-case DCF ($245) — MOS ติดลบ -24.78% เทียบ Blended FV (ESG-adj) $188.81" },
      { title: "จัดกลุ่มใหม่เป็น Value bucket", why: "Revenue growth TTM 16.25% ต่ำกว่าเกณฑ์ Growth bucket 20% แล้ว — ต้องใช้ MOS gate ที่เข้มงวดกว่า (>=15%) ซึ่งปัจจุบัน fail อย่างชัดเจน" },
      { title: "S&P 500 inclusion catalyst หมดอายุแล้ว", why: "Effective May 19, 2026 realized แล้ว — Bear v1's call ว่า 'priced in' ถูกยืนยัน ไม่มี forward flow-driven upside เหลืออยู่" }
    ],
    esgBreakdown: { e: 7.5, s: 6.75, g: 7.85, overall: 7.35 },
    customerConcentration: {
      top10Combined: "~28% (SEC 10-K FY2023 — ข้อมูลเก่าที่สุดที่หาได้ ไม่ใช่ FY2027 ปัจจุบัน, ใช้เป็น directional)",
      singleCustomerMax: "ไม่มีลูกค้ารายเดียวเกิน 10% ของ revenue"
    },
    geographyRevenue: { unitedStates: 60.94, europe: 30.09, asiaPacific: 8.97, note: "North America รวม 60.94% (SEC 10-K FY2026 aggregator, TradingView) — China ไม่ระบุแยก ไม่ใช่สัดส่วนที่มีนัยสำคัญ" },
    revenueSegments: [
      { label: "North America", value: 60.94 },
      { label: "Europe", value: 30.09 },
      { label: "Asia Pacific", value: 8.97 }
    ],
    revenueSegmentsNote: "ไม่มี business-segment revenue breakdown แยกใน data package — ใช้ geography breakdown แทนตาม house rule",
    unitEconomics: {
      ruleOf40: "65.65% (16.25% rev growth + 49.4% FCF margin) — Pass เกณฑ์ >=40% อย่างมาก",
      nrr: "N/A — ไม่มี disclosure",
      ltvCac: "N/A — ไม่มี disclosure",
      sbcPctRevenue: "13.5% (Q1 FY2027, SEC 10-Q)"
    },
    competitorData: [
      { ticker: "VEEV", company: "Veeva Systems (subject)", revenueGrowth: 16.25, operatingMargin: 29.5, marketCap: 40770 },
      { ticker: "IQV", company: "IQVIA Holdings", revenueGrowth: 8.17, operatingMargin: 13.95, marketCap: 67060 },
      { ticker: "CERT", company: "Certara", revenueGrowth: 11.09, operatingMargin: 4.27, marketCap: 1280 },
      { ticker: "DOCS", company: "Doximity", revenueGrowth: 11.18, operatingMargin: 30.57, marketCap: 4590 },
      { ticker: "HCAT", company: "Health Catalyst", revenueGrowth: -7.54, operatingMargin: -8.05, marketCap: 127 }
    ],
    competitorDataNote: "operatingMargin ใช้ net margin เป็น proxy (ไม่มี operating margin แยกในข้อมูลที่ verify ได้สำหรับ peers); IQV marketCap คำนวณจาก Revenue $15.9B x Net Margin 13.95% x P/E 30.22x (derived จากตัวเลข verified 2 ค่า ไม่ใช่ training-knowledge estimate)",
    bullFlipTriggers: [
      "ราคาย่อกลับมาที่ $190-210 (MOS เข้าใกล้ 0% ถึงบวกเทียบ Bear P-W EV $173)",
      "FY2027 full-year revenue guidance ยกระดับเป็น >=18%",
      "Veeva เปิดเผยรายได้จาก AI/agentic labor product line >=$100-150M annualized",
      "4 top-20 pharma decisions ที่เหลือปิดครบในทาง Veeva พร้อม retention >=90% independently-verified",
      "Fed พลิกกลับมา dovish (ยกเลิก hikes ที่ priced) -> WACC ลดสู่ 9.5-10%"
    ],
    bearFlipTriggers: [
      "Fed hike ทั้ง 2 ครั้ง (Sept+Dec 2026) แล้ว signal ต่อเนื่อง 2027 -> WACC ดันสู่ 11.5-12%",
      "Revenue growth หลุดต่ำกว่า 14% สำหรับ 2 ไตรมาสติดต่อกัน",
      "4 top-20 decisions ที่เหลือพลิกไป Salesforce ทั้งหมด หรือ win-rate ไตรมาสหน้า <70%",
      "Forward P/E ไม่ compress แม้ growth ชะลอ (ยังเทรดเกิน 35x)",
      "Insider selling เปลี่ยนจาก scheduled 10b5-1 เป็น opportunistic (โดยเฉพาะ Gassner)"
    ],
    thesisInvalidation: "Revenue growth หลุดต่ำกว่า 10% full fiscal year ใดๆ, หรือ Peter Gassner ลาออกจากตำแหน่ง CEO, หรือ VEEV ถูก acquired, หรือ FDA CSA modernization ยกเลิก 21 CFR Part 11 validation requirement จริง -> re-analysis required ทันที",
'''


if __name__ == "__main__":
    main()
