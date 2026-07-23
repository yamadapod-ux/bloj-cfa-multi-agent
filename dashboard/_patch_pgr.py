"""
dashboard/_patch_pgr.py
Patch script to insert PGR (The Progressive Corporation) analysis entry
into dashboard/data.js REPORTS array + update LAST_UPDATED.

WHY THIS SCRIPT EXISTS (instead of a direct Write to data.js):
- dashboard/data.js is ~220,000 tokens — far too large to safely read/rewrite
  in full via the Read/Write tools available in the session that produced this
  analysis (2026-07-22). No Bash/Node execution tool was available either.
- Per house rule "Dashboard Write Safety" (memory/feedback_dashboard_write_safety.md):
  NEVER use a full-file Write on data.js — always use a targeted Python script.
- This script follows the same convention as prior patches (_patch_ma.py,
  _temp_insert_rddt.py, _backfill.py) referenced in tracker.md / decisions.md.

HOW TO RUN (in a session with Python execution available):
    cd "C:\\Users\\user\\Desktop\\บลจ\\บลจ CFA"
    python dashboard/_patch_pgr.py

This will:
1. Read dashboard/data.js
2. Insert the PGR_ENTRY object as the first element of the REPORTS array
   (right after "const REPORTS = [")
3. Update LAST_UPDATED to "2026-07-22"
4. Write the file back
5. Run a basic sanity check (balanced braces/brackets, no lone trailing comma)
"""

import re
import sys

DATA_JS_PATH = "dashboard/data.js"
NEW_LAST_UPDATED = "2026-07-22"

PGR_ENTRY = r"""  {
    ticker: "PGR",
    company: "The Progressive Corporation",
    date: "2026-07-22",
    version: "v1",
    sector: "Financials / Insurance - Personal Auto & Property P&C (Digital/Telematics-driven)",
    price: 205.90,
    recommendation: "HOLD/WAIT FOR PULLBACK",
    blendedFV: 208.00,
    esgAdjFV: 202.00,
    targetBull: 260.00,
    targetBase: 208.00,
    stopLoss: 144.00,
    convictionEmma: 7,
    convictionQuinn: 6,
    convictionBear: 7,
    convictionAvg: 6.67,
    mosPct: 1.0,
    pwEV: 206.00,
    pwEvBear: 183.00,
    beta: 0.25,
    forwardSharpe: -0.26,
    sharpe1Y: -0.26,
    maxDrawdown: -0.1924,
    kelly: "~0% (NEGATIVE edge at current price)",
    moat: "Narrow+",
    esgRating: "Medium",
    esgScore: 6.0,
    bucket: "Value",
    entryZone: "$175-185 (T1, MOS >=15% at entry mid $180)",
    positionSize: "5% (when price enters zone and conviction gate passes)",
    reportFile: "../reports/PGR_2026-07-22.md",
    keyThesis: "Digital/telematics-driven personal auto & property insurer - highest revenue growth in peer group (+10.49% TTM) via 20+yr Snapshot telematics data moat, ROE 34.94%, combined ratio 87.1% still profitable. BUT operating margin (16.56%) is LOWEST among named peers (ALL 21.03% / TRV 22.03% / CB 23.71% / ACGL 28.94%) despite fastest growth - underwriting discipline gap. Stock fell twice in one week (-9% June premium growth deceleration, -2.98% post-Q2-earnings margin concern) - Bear treats as confirmed signal, not noise. Blended FV $208 barely above price $205.90 = MOS +1.0%, essentially none. Conviction 6.67 < 7.0 Value gate. Both Value bucket gates fail simultaneously (pattern matches WPM 2026-07-12) -> HOLD/WAIT, no deploy.",
    topRisk: "Underwriting margin gap vs entire peer group (lowest operating margin despite highest growth) + two confirmed negative signals in one week (growth deceleration + margin deterioration) + structural component to rising loss costs (severe weather trend + auto repair cost inflation) + Fed hawkish pivot risk to float income valuation (beta 0.25 does not capture this tail)",
    businessSummary: {
      oneLiner: "Progressive เป็นผู้นำ personal auto/property insurer ที่ใช้ telematics (Snapshot) เก็บพฤติกรรมขับขี่จริงมา 20+ ปี เพื่อตั้งราคาเบี้ยประกันแม่นยำกว่าคู่แข่งที่ใช้ demographic proxy",
      analogy: "เหมือนบริษัทประกันที่ใช้ 'black box' วัดพฤติกรรมขับรถจริงแทนการเดาจากอายุ/เพศ/ที่อยู่ - ยิ่งขับดี ยิ่งจ่ายถูก และบริษัทยิ่งรู้ต้นทุนความเสี่ยงแม่นยำกว่าคู่แข่ง",
      moneyFlow: [
        "Personal Auto Insurance (segment ใหญ่สุด): เก็บเบี้ยจากผู้ขับขี่ จ่ายเคลมเมื่อเกิดอุบัติเหตุ กำไรจากส่วนต่าง (underwriting profit) เมื่อ combined ratio <100 - Q2 2026 combined ratio 87.1-87.3",
        "Commercial Auto: ประกันรถเพื่อธุรกิจ margin สูงกว่า personal lines",
        "Property Insurance: กำลังโตผ่านการ bundle กับ auto (cross-sell) - segment ใหม่ที่กำลังขยาย",
        "Telematics (Snapshot) + Investment income (float): pricing แม่นยำกว่าคู่แข่ง + เงินเบี้ยที่เก็บก่อนจ่ายเคลมไปลงทุนได้ผลตอบแทนเพิ่ม"
      ]
    },
    thesisBullets: [
      { title: "Telematics data moat 20+ ปี", why: "Snapshot เก็บข้อมูลพฤติกรรมขับขี่จริงสะสมมานาน - pricing precision ที่คู่แข่งใหม่ตามไม่ทัน, เป็น data moat ที่ลอกยากในระยะสั้น" },
      { title: "Growth leadership ในกลุ่ม peer", why: "Revenue TTM +10.49% สูงสุดในกลุ่ม ALL/TRV/CB/ACGL - policies in force +7% YoY = market share gain โดยตรง" },
      { title: "ROE 34.94% + ROIC 28.70% extraordinary", why: "แม้จะเป็น cyclical elevated level ที่ต้อง normalize ลงบ้าง ก็ยังสูงกว่า cost of equity (9.0% floor) มาก" }
    ],
    esgBreakdown: { e: 5, s: 6, g: 7, overall: 6.0 },
    revenueSegments: [
      { label: "Personal Auto (est. - not in verified data package)", value: 82 },
      { label: "Commercial Lines (est.)", value: 10 },
      { label: "Property (est.)", value: 8 }
    ],
    competitorData: [
      { ticker: "PGR", company: "Progressive (subject)", revenueGrowth: 10.49, operatingMargin: 16.56, marketCap: 119710 },
      { ticker: "ALL", company: "Allstate", revenueGrowth: 4.40, operatingMargin: 21.03, marketCap: 64800 },
      { ticker: "TRV", company: "Travelers", revenueGrowth: 2.38, operatingMargin: 22.03, marketCap: 77100 },
      { ticker: "CB", company: "Chubb", revenueGrowth: -4.10, operatingMargin: 23.71, marketCap: 137610 },
      { ticker: "ACGL", company: "Arch Capital", revenueGrowth: 8.83, operatingMargin: 28.94, marketCap: 34990 }
    ],
    geographyRevenue: { unitedStates: 100, international: 0, notes: "US-only per verified data package - no international/FX exposure disclosed" },
    bullFlipTriggers: [
      "Combined ratio กลับ <=86% ติดต่อกัน 2 เดือน (PGR รายงานผลรายเดือน - disclosure เร็วกว่า insurer อื่น)",
      "Net premium written growth reaccelerates >=6-7% YoY (reverse การชะลอ June +3%)",
      "ราคา pullback สู่ $175-185 -> MOS >=15% ทันที",
      "Conviction re-rate >=7.0 หลังยืนยัน 1-2 ไตรมาสว่า margin stabilize",
      "Wall Street sentiment shift - analyst upgrade พลิกจาก 15/25 Hold ปัจจุบัน"
    ],
    bearFlipTriggers: [
      "Combined ratio เกิน 90% ต่อเนื่อง 2+ เดือน - margin erosion กลายเป็น structural",
      "Net premium written growth ชะลอต่ำกว่า 3% YoY ต่อเนื่อง - growth story แตก",
      "Policies in force growth stall <3% YoY (จาก +7% ปัจจุบัน) - market share losses",
      "Severe weather/loss cost trend เร่งตัวต่อเนื่อง 2+ ไตรมาส (adverse reserve development)",
      "Fed hikes 3 ครั้งจริงตามที่ price ไว้ (Sep/Oct/Dec 2026) - CoE เพิ่ม กด equity multiple ทั้งตลาด"
    ],
    thesisInvalidation: "ถ้า combined ratio เกิน 92-93% ต่อเนื่อง 2 ไตรมาส พร้อมกับ premium growth deceleration ต่อเนื่อง (break ต่ำกว่า 3%) = underwriting discipline moat หายไป และ digital/telematics advantage ไม่ translate เป็น profitable growth อีกต่อไป -> re-analysis required ทั้งหมด"
  },
"""


def main():
    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if '"ticker": "PGR"' in content or 'ticker: "PGR"' in content:
        print("PGR entry already exists in data.js — aborting to avoid duplicate.")
        sys.exit(1)

    # 1. Update LAST_UPDATED
    content, n = re.subn(
        r'const LAST_UPDATED = "[\d-]+";',
        f'const LAST_UPDATED = "{NEW_LAST_UPDATED}";',
        content,
        count=1,
    )
    if n != 1:
        print("WARNING: LAST_UPDATED line not found/replaced — check manually.")

    # 2. Insert PGR_ENTRY right after "const REPORTS = [" marker
    marker = "const REPORTS = ["
    idx = content.find(marker)
    if idx == -1:
        print("ERROR: 'const REPORTS = [' marker not found. Aborting — no changes written.")
        sys.exit(1)

    insert_at = idx + len(marker) + 1  # +1 for the newline right after '['
    new_content = content[:insert_at] + "\n" + PGR_ENTRY + content[insert_at:]

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

    print("PGR entry inserted successfully. LAST_UPDATED set to", NEW_LAST_UPDATED)
    print("Run `node -e \"require('./dashboard/data.js')\"` or open dashboard/index.html to verify.")


if __name__ == "__main__":
    main()
