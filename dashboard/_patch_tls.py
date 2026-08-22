"""
dashboard/_patch_tls.py
Patch script to insert TLS (Telos Corporation) analysis entry
into dashboard/data.js REPORTS array + update LAST_UPDATED.

Follows Dashboard Write Safety house rule — NEVER full-file Write on data.js,
always a targeted Python script (precedent: _patch_pgr.py, _patch_veev.py).

Run:
    cd "C:\\Users\\user\\Desktop\\บลจ\\บลจ CFA"
    python dashboard/_patch_tls.py
"""

import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DATA_JS_PATH = "dashboard/data.js"
REPORT_MD_PATH = "reports/TLS_2026-08-22.md"
NEW_LAST_UPDATED = "2026-08-22"


def build_entry():
    with open(REPORT_MD_PATH, "r", encoding="utf-8") as f:
        report_md = f.read()

    # Escape for JS template literal
    escaped = report_md.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

    metadata = '''  {
    ticker: "TLS",
    company: "Telos Corporation",
    date: "2026-08-22",
    version: "v1",
    sector: "Federal Cybersecurity / GovIT (Governance-Risk-Compliance software + Identity Verification)",
    price: 4.3950,
    recommendation: "HOLD/WATCH — NO DEPLOY",
    blendedFV: 4.09,
    esgAdjFV: 3.89,
    targetBull: 5.88,
    targetBase: 4.09,
    stopLoss: 2.72,
    convictionEmma: 5.5,
    convictionQuinn: 5.5,
    convictionBear: 6.5,
    convictionAvg: 5.83,
    mosPct: -6.94,
    mosPctEsgAdj: -11.49,
    pwEV: 4.96,
    pwEvBear: 4.00,
    beta: 0.97,
    sharpe1Y: 0.18,
    forwardSharpe: 0.18,
    maxDrawdown: -0.547,
    kelly: "Full-Kelly 38.4% / Half-Kelly 19.2% — เกินเกิน IPS cap (8-10%) มหาศาล — ห้ามใช้กำหนด position size จริง (red flag ว่า scenario probability inputs underestimate ความเสี่ยง)",
    moat: "Narrow",
    esgRating: "Medium",
    esgScore: 6.0,
    macroRegime: "RISK-ON",
    morganQA: "PASS Round 2 (Data Quality 8.3/10) — Round 1 FAIL (HIGH: DCF terminal growth เกินเพดาน 3%) → correction cascade → Round 2 PASS (0 HIGH, 2 MEDIUM data-completeness ที่ Leo แก้แล้วก่อน embed)",
    sp500Reference: null,
    sp500ReferenceNote: "TBD — Vera ต้อง verify (CIO Verified Data Package รอบนี้ไม่มีตัวเลข S&P 500 index level ตรงๆ ให้ ตาม pattern เดียวกับ TDG/VEEV ก่อนหน้าที่ Vera resolve ย้อนหลังภายหลัง)",
    bucket: "Growth",
    entryZone: "$3.20-$3.60 (mid $3.40)",
    positionSize: "0% ตอนนี้ (NO DEPLOY — Growth bucket single-gate-failure: Conviction 5.83/10 < 6.5 gate, แม้ Revenue Growth +65.93% และ Growth MOS จะผ่านทั้งคู่); ถ้า gate ผ่านในอนาคต แนะนำ cap 3-5% (ต่ำกว่า ceiling ปกติ 8-10% เพราะ Beta underestimate idiosyncratic risk + thin-float liquidity + customer concentration binary risk)",
    keyThesis: "TLS เป็น micro-cap ($328.5M) federal cybersecurity/GovIT contractor (Xacta GRC + Telos ID identity verification) ที่มี Revenue Growth TTM +65.93% (segment mix-shift Security Solutions 70.9%→90.8% FY24→FY25) — ผ่าน Growth bucket revenue-growth gate สบายและ Growth MOS ผ่านทางเทคนิค (soft-pass) แต่ Conviction เฉลี่ยทีม 5.83/10 ต่ำกว่าเกณฑ์ 6.5 (single-gate-failure, 3rd instance ต่อจาก VRT/SHOP) เพราะ customer concentration รุนแรง (91% federal government), revenue inflection ที่พิสูจน์ได้แค่บางส่วน (hard evidence มีแค่ 1 ไตรมาส), และยัง GAAP loss-making — HOLD/WATCH รอ Q3 2026 10-Q เปิดเผยข้อมูลเพิ่ม",
    topRisk: "Customer/counterparty concentration 91% ของรายได้จากรัฐบาลกลางสหรัฐฯ ไม่มี single-agency breakdown เปิดเผย — government shutdown/continuing-resolution risk กระทบ contract timing โดยตรง; ร่วมกับ revenue inflection FY24→FY25 ที่หลักฐาน structural mix-shift มีแค่ 1 ไตรมาส (Telos ID +77% YoY) ยังไม่พอสรุปแน่ชัด และ Beta 0.97 underestimate idiosyncratic risk จริง (52W swing -54.7%/+120.9%)",
    reportFile: "../reports/TLS_2026-08-22.md",
    businessSummary: {
      oneLiner: "Telos คือบริษัท cybersecurity/GovIT ที่ขายซอฟต์แวร์ governance-risk-compliance (Xacta) และบริการ identity verification ให้หน่วยงานรัฐบาลกลางสหรัฐฯ เป็นหลัก",
      analogy: "เหมือนบริษัทที่ขาย 'ระบบตรวจสอบความปลอดภัยไซเบอร์แบบต่อเนื่อง' ให้หน่วยงานรัฐ คล้ายบริษัทตรวจสอบบัญชีที่รัฐต้องจ้างประจำเพื่อผ่านมาตรฐานความปลอดภัย (FedRAMP/RMF) — ลูกค้าเปลี่ยนผู้ให้บริการยากเพราะระบบฝังอยู่ใน workflow การอนุมัติของหน่วยงานแล้ว",
      moneyFlow: [
        "หน่วยงานรัฐบาลกลางต้องผ่านมาตรฐานความปลอดภัยไซเบอร์ (RMF/ATO) อย่างต่อเนื่อง",
        "TLS ขาย Xacta (ซอฟต์แวร์ compliance) และ Telos ID (identity verification) ให้หน่วยงานเหล่านี้ผ่านสัญญาราชการ",
        "รายได้ ~91% มาจากรัฐบาลกลางสหรัฐฯ ผ่านสัญญาหลายฉบับ",
        "ธุรกิจเดิม (Secure Networks) กำลังหดตัวลง ขณะที่ Security Solutions (Xacta/Telos ID) ขยายตัวเร็วมาแทน"
      ],
      whyDifferent: "Switching cost สูงเพราะ Xacta ถูกฝังอยู่ใน continuous authorization workflow ของหน่วยงานแล้ว แต่ TLS เป็น micro-cap ที่แข่งกับ prime contractor ขนาดใหญ่กว่ามาก (CACI/SAIC/BAH/LDOS) ที่มี relationship และ scale เหนือกว่า — moat มีจริงแต่แคบและกระจุกอยู่ที่ segment เดียว",
      simpleRisk: "รายได้เกือบทั้งหมดพึ่งพารัฐบาลกลางสหรัฐฯ (91%) — ถ้าเกิด government shutdown หรืองบประมาณล่าช้า จะกระทบรายได้โดยตรง"
    },
    thesisBullets: [
      { title: "Security Solutions scaling จริง", why: "สัดส่วนรายได้จาก Security Solutions (Xacta + Telos ID) เพิ่มจาก 70.9% เป็น 90.8% ของรายได้รวมในปีเดียว สะท้อน structural growth ไม่ใช่แค่ base effect ล้วนๆ" },
      { title: "Secure Networks drag กำลังหมดฤทธิ์", why: "segment เดิมที่หดตัวเหลือแค่ 9.2% ของรายได้ ผลกระทบต่อ growth รวมในอนาคตจะเบาลงเรื่อยๆ" },
      { title: "EV/Revenue ดูไม่แพงเทียบ growth", why: "เทรดที่ 1.47-1.51x EV/Revenue ขณะที่โต TTM +65.93% — Quinn's reverse-analysis ยืนยันตลาด price-in NTM growth เพียง -1.2% ถึง -2.0% เท่านั้น" },
      { title: "Customer concentration เป็นความเสี่ยงหลัก", why: "91% ของรายได้มาจากรัฐบาลกลางสหรัฐฯ — ไม่มี diversification และเสี่ยงต่อ shutdown/budget delay โดยตรง" },
      { title: "Conviction ยังไม่ถึงเกณฑ์ BUY", why: "DCF absolute base case แสดง overvalued (-20.1% MOS หลัง Morgan correction) + data gap 3 จุด (backlog, customer %, multiple history) ทำให้ต้องรอข้อมูลเพิ่มก่อนยกระดับเป็น BUY" }
    ],
    esgBreakdown: {
      e: 8,
      s: 6,
      g: 4,
      overall: 6.0
    },
    customerConcentration: {
      usFederalGovernment: "~91.0% (FY2025, 10-K) — no single-agency % disclosed",
      top2Combined: null
    },
    geographyRevenue: {
      unitedStates: "~100% (inferred — domestic federal contractor, no international revenue found in filing excerpt)"
    },
    revenueSegments: [
      { label: "Security Solutions (Xacta + Telos ID)", value: 90.8 },
      { label: "Secure Networks (legacy)", value: 9.2 }
    ],
    revenueSegmentsNote: "FY2024→FY2025: Security Solutions 70.9%→90.8% (scaling structural), Secure Networks 29.1%→9.2% (shrinking, impairment-driven) — value ด้านบนคือ FY2025",
    competitorData: [
      { ticker: "TLS", company: "Telos Corp (subject)", revenueGrowth: 65.93, operatingMargin: -1.96, marketCap: 328.5 },
      { ticker: "CACI", company: "CACI International", revenueGrowth: 10.89, operatingMargin: 9.86, marketCap: 14310, strengths: "Diversified national security IT prime, scale ใหญ่สุดในกลุ่ม, revenue growth +10.89% เป็นบวก", weaknesses: "ไม่ focus เฉพาะ Xacta-style GRC niche — เป็น broad services player", threatLevel: "MEDIUM" },
      { ticker: "SAIC", company: "Science Applications Intl", revenueGrowth: -2.90, operatingMargin: 8.01, marketCap: 5410, strengths: "ความสัมพันธ์ยาวนานกับ DoD/civilian agencies, scale ที่ established", weaknesses: "Revenue หดตัว (-2.90%), less innovation-focused เทียบ TLS's Xacta automation", threatLevel: "MEDIUM" },
      { ticker: "BAH", company: "Booz Allen Hamilton", revenueGrowth: -7.27, operatingMargin: 9.80, marketCap: 9270, strengths: "Premier consulting brand สำหรับ DoD cybersecurity, margin สูง (9.80%)", weaknesses: "Revenue หดตัวแรงสุดในกลุ่ม (-7.27%), cost structure สูงกว่า", threatLevel: "HIGH" },
      { ticker: "LDOS", company: "Leidos Holdings", revenueGrowth: 3.41, operatingMargin: 11.79, marketCap: 17740, strengths: "ใหญ่สุด+กระจายตัวสุดในกลุ่ม, margin ดีสุด (11.79%), growth เป็นบวก (+3.41%)", weaknesses: "Conglomerate ขนาดใหญ่ less specialized ในงาน continuous-ATO automation เฉพาะทางแบบ Xacta", threatLevel: "MEDIUM" }
    ],
    bullFlipTriggers: [
      "Segment revenue $ จริง (ไม่ใช่แค่ %) เปิดเผยใน 10-Q ถัดไป แสดง Security Solutions organic growth ≥3 ไตรมาสติดต่อกัน ที่ ≥30% YoY",
      "Customer/agency concentration breakdown แสดงว่าไม่มี single agency เกิน 40% ของ 91% federal revenue",
      "GAAP Operating Income เป็นบวก 2 ไตรมาสติดต่อกัน",
      "Contract backlog/book-to-bill ratio เปิดเผยและแสดง backlog โตเร็วกว่า revenue",
      "Sell-side upgrade เป็น Buy พร้อม PT upside >20% ที่ระบุชัดว่า revenue-inflection uncertainty ได้รับการแก้ไข"
    ],
    bearFlipTriggers: [
      "Revenue growth ไตรมาสถัดไปชะลอเหลือ <20% YoY",
      "Goodwill/intangible impairment เพิ่มอีกในปีที่ 3 ติดต่อกัน",
      "Government shutdown/extended CR เกิดขึ้นจริง + TLS ประกาศ guidance cut ที่อ้างถึง contract delay",
      "Insider selling cluster (Form 4 หลายคนภายใน 90 วัน) — ปัจจุบัน unverified",
      "SBC % of revenue เพิ่มขึ้นต่อจาก 11.1% โดยไม่มี margin improvement ควบคู่"
    ],
    thesisInvalidation: "ถ้า FY26 full-year revenue growth normalize ลงเหลือ single-digit หรือติดลบ และ management ยืนยันใน MD&A ว่า FY25 growth ส่วนใหญ่มาจาก non-recurring task order (ไม่ใช่ structural segment mix-shift) → thesis ผิด ต้อง re-analyze ทันทีด้วยมุมมอง AVOID เป็น default",
'''

    full_content_field = "    fullContent: `" + escaped + "`,\n"
    closing = "  },\n"

    return metadata + "\n" + full_content_field + closing


def main():
    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if 'ticker: "TLS"' in content:
        print("TLS entry already exists in data.js — aborting to avoid duplicate.")
        sys.exit(1)

    entry = build_entry()

    # 1. Update LAST_UPDATED
    content, n = re.subn(
        r'const LAST_UPDATED = "[\d-]+";',
        f'const LAST_UPDATED = "{NEW_LAST_UPDATED}";',
        content,
        count=1,
    )
    if n != 1:
        print("WARNING: LAST_UPDATED line not found/replaced — check manually.")

    # 2. Insert TLS entry right after "const REPORTS = [" marker (newest-first convention)
    marker = "const REPORTS = ["
    idx = content.find(marker)
    if idx == -1:
        print("ERROR: 'const REPORTS = [' marker not found. Aborting — no changes written.")
        sys.exit(1)

    insert_at = idx + len(marker) + 1  # +1 for newline right after '['
    new_content = content[:insert_at] + "\n" + entry + content[insert_at:]

    # 3. Basic sanity checks before writing
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

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("TLS entry inserted successfully. LAST_UPDATED set to", NEW_LAST_UPDATED)


if __name__ == "__main__":
    main()
