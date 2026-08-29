"""
dashboard/_patch_adi.py
Insert ADI (Analog Devices, Inc.) analysis entry into dashboard/data.js
REPORTS array + update LAST_UPDATED.

Dashboard Write Safety: targeted script, never full-file Write on data.js
(precedent: _patch_tls.py, _patch_pgr.py, _patch_veev.py).

Run:
    cd "C:\\Users\\user\\Desktop\\บลจ\\บลจ CFA"
    python dashboard/_patch_adi.py
"""

import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DATA_JS_PATH = "dashboard/data.js"
REPORT_MD_PATH = "reports/ADI_2026-08-29.md"
NEW_LAST_UPDATED = "2026-08-29"


def build_entry():
    with open(REPORT_MD_PATH, "r", encoding="utf-8") as f:
        report_md = f.read()

    escaped = report_md.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

    metadata = '''  {
    ticker: "ADI",
    company: "Analog Devices, Inc.",
    date: "2026-08-29",
    version: "v1 (Morgan QA CONDITIONAL PASS)",
    sector: "Semiconductors / Analog & Mixed-Signal",
    bucket: "Value",
    price: 361.78,
    recommendation: "HOLD / WAIT — NO DEPLOY",
    blendedFV: 229,
    esgAdjFV: 218,
    targetBull: 301,
    targetBase: 233,
    stopLoss: 156,
    convictionEmma: 6.5,
    convictionQuinn: 5.0,
    convictionBear: 6.0,
    convictionAvg: 5.83,
    mosPct: -36.7,
    mosPctEsgAdj: -39.7,
    pwEV: 267.29,
    pwEvBear: 195,
    beta: 1.21,
    sharpe1Y: 0.15,
    forwardSharpe: 0.15,
    maxDrawdown: -0.499,
    kelly: "Full −174% / Half −87% / Quarter −44% — ติดลบทุกระดับ ไม่มี long position ที่ mathematically justified ที่ $361.78",
    moat: "Wide (core) / Narrow catalog periphery — Bear reconciled: Wide ที่ high-performance/precision signal-chain core (10-20yr switching cost) / Narrow ที่ general-purpose catalog tier (TXN 300mm cost advantage) / M&A ที่สร้าง wide catalog ทำที่ราคาที่ ROIC incl-goodwill 10.5% ≈ WACC 9.7%",
    esgRating: "Medium",
    esgScore: 6.1,
    macroRegime: "RISK-ON",
    morganQA: "CONDITIONAL PASS (Data Quality 9/10, 0 HIGH · 1 MEDIUM · 2 LOW, reject type FORMAT) — MEDIUM: Emma structured-data block ESG ค้าง pre-reconciliation (g:7, overall:6.7) → Leo embed reconciled E6/S7/G5.5/Overall 6.1. LOW: EV/EBITDA percentile cosmetic (~72-78th) + Growth Test 1 synthesis observation. Blended FV weight 40/30/30 verified เป๊ะ + report จับ fabricated rule 'IPS 2026-05-15 40/35/25' ได้เอง",
    sp500Reference: 7711.76,
    sp500ReferenceNote: "7,711.76 (2026-08-28 close — Atlas Yahoo Finance ^GSPC; 2nd source 7,711.48 delta 0.004% — Atlas flag low-risk เพราะ 2nd source ไม่ independent เต็มที่ CNBC fetch 403'd)",
    revenueGrowthYoY: 33.65,
    entryZone: "$185-205 (mid $195) — MOS ≥ 15% vs Blended FV $229; พิจารณาหลัง Sept FOMC 16 ก.ย. + MOFCOM ruling ~13 ก.ย.",
    positionSize: "0% — ไม่ผ่าน Value gate ทั้ง 2 เงื่อน (MOS −36.7% << +15% · Conviction 5.83 < 7.0). Growth cross-check ก็ FAIL (Growth MOS 0/2 · Conviction 5.83 < 6.5). Force Deploy active (RISK-ON) แต่ไม่มี candidate ผ่าน gate — Force Deploy ไม่ override gate",
    keyThesis: "ADI = wide-moat analog FCF machine ตัวจริง (รอด FY2024 downcycle −23.4% revenue โดยยัง gross margin 60%+ และมีกำไร ต่างจาก MU FY2023 op margin −37%) แต่ราคา $361.78 ไม่เหลือ margin of safety — DCF ทั้ง 3 scenario ($153/$233/$301) + Blended FV $229 (MOS −36.7%) ต่ำกว่าราคาทั้งหมด แม้ bull case ยัง −16.7%. เทรดที่ 43x P/E / 26x EV/EBITDA (~78-80th pctile ของ 10Y ตัวเอง) บน revenue สูงกว่า prior cyclical peak +13% + margin/multiple ที่ระดับ peak. cyclical/rate-peak analog #3 ต่อจาก MU/CRCL",
    topRisk: "Valuation / no-MOS — implied exit EV/EBITDA ใน DCF แค่ 11.6x vs current 26.3x = cyclical-peak multiple ที่ไม่ sustainable; multiple re-rate ไป median = −30% ถึง −40% โดยไม่ต้อง earnings miss. ซ้อนด้วย MOFCOM anti-dumping ruling ~13 ก.ย. 2026 ที่ระบุชื่อ ADI ตรงๆ (duty ≥25% → Bear FV ~$110) + Sept FOMC 16 ก.ย. hike coin-flip กด high-multiple cyclical โดยตรง",
    reportFile: "../reports/ADI_2026-08-29.md",
    businessSummary: {
      oneLiner: "Analog Devices ออกแบบและขายชิป analog/mixed-signal และ power-management หลายหมื่นรุ่น ที่แปลงสัญญาณโลกจริง (อุณหภูมิ แรงดัน การเคลื่อนไหว) เป็นข้อมูลดิจิทัล ให้ลูกค้าอุตสาหกรรม รถยนต์ และศูนย์ข้อมูล AI",
      analogy: "เหมือน 'ประสาทสัมผัส' ของอุปกรณ์อิเล็กทรอนิกส์ — ถ้า CPU/GPU คือสมอง ADI คือหู ตา ผิวหนัง ที่รับรู้โลกจริงแล้วส่งข้อมูลเข้าสมอง; ชิปแต่ละตัวถูกฝังเข้าไปในเครื่องจักร/รถ แล้วอยู่ยาว 10-20 ปี",
      moneyFlow: [
        "ลูกค้า (โรงงาน ผู้ผลิตรถ ผู้ผลิต AI infra) ออกแบบชิป ADI ฝังเข้าไปในผลิตภัณฑ์ — ผ่าน design-win ที่ใช้เวลาหลายเดือน",
        "เมื่อ design-in แล้ว ADI ขายชิปนั้นซ้ำตลอดอายุผลิตภัณฑ์ (10-20 ปี) — ~75% เป็น sole-sourced เปลี่ยนยาก",
        "ผลิตแบบ fab-lite (โรงงานเก่าที่คุ้มทุนแล้ว + จ้าง TSMC) → capex แค่ 4.4% ของรายได้ → gross margin 66% GAAP / 72% adjusted",
        "กระแสเงินสดเหลือ ~$5B/ปี → คืนผู้ถือหุ้น >100% ผ่านปันผล (ขึ้น 22 ปีติด) + ซื้อหุ้นคืน"
      ],
      whyDifferent: "Switching cost มหาศาล — ชิป ADI ราคาแค่ ~$2-3 แต่ถูก qualify เข้าระบบลูกค้าและอยู่ยาว 10-20 ปี การเปลี่ยนไปคู่แข่งต้องทดสอบทั้งระบบใหม่เพื่อประหยัด BOM เล็กน้อย → ลูกค้าไม่ทำ; บวก catalog IP หลายทศวรรษจาก Linear + Maxim ที่ไม่ต้องแข่ง leading-edge node",
      simpleRisk: "หุ้นเทรดที่ ~43x P/E / 26x EV/EBITDA บนกำไรที่เพิ่งเด้งขึ้นแรงจาก cyclical trough — ราคาสะท้อน recovery ที่ต่อเนื่องไปเรื่อยๆ ถ้า 2027 comps เริ่มโหดหรือ Fed ขึ้นดอกเบี้ย multiple อาจหดตัวแรง"
    },
    thesisBullets: [
      { title: "No margin of safety at $362", why: "DCF ทั้ง Bear/Base/Bull ($153/$233/$301) ต่ำกว่าราคาตลาดทั้งหมด; prob-weighted FV $226 = MOS -37.5%; แม้ bull case ยัง -17%; Blended FV $229 (MOS -36.7%)" },
      { title: "Wide moat พิสูจน์แล้วจริง", why: "FY2024 revenue -23.4% แต่ gross margin ยัง 60%+ และ profitable (ต่างจาก MU FY2023 op margin -37%); ROIC ex-goodwill 34-45% vs WACC 9.7%" },
      { title: "Cyclically-peak multiple", why: "EV/Revenue ~78-80th percentile ของ 10Y range; EV/EBITDA 26x vs median 22x; implied exit multiple ใน DCF แค่ 11.6x = current multiple ไม่ sustainable" },
      { title: "China 26% ของรายได้ + MOFCOM anti-dumping ruling ~13 ก.ย. 2026", why: "investigation ระบุชื่อ ADI ตรงๆ; China +34% YoY = revenue ที่เสี่ยงสุดคือที่โตเร็วสุด; duty ≥25% → Bear FV ~$110; DXY strength (Fed hawkish) compounds" },
      { title: "2027 comp wall", why: "Q3 +40% YoY / Comms +84% เป็น trough-comp math ไม่ใช่ run-rate; die-bank inventory +$83M sequentially = late-cycle behavior; ถ้า channel restocking > sell-through, 2027 decelerates sharply" }
    ],
    esgBreakdown: {
      e: 6,
      s: 7,
      g: 5.5,
      overall: 6.1
    },
    esgBreakdownNote: "Reconciled (Bear challenge applied): Governance 7 → 5.5 (serial M&A goodwill 83% ของ equity + ROIC incl-GW ≈ WACC + buyback >100% FCF funded จาก balance sheet ซื้อที่ 43x P/E ใกล้ ATH ขณะ CEO/CFO ขายหุ้นส่วนตัว + distributor concentration disclosure ไม่ชัด). Overall 6.7 → 6.1. Valuation impact −3.5% → −5%. MSCI BBB (Average) · Sustainalytics ESG Risk 24 (Medium)",
    customerConcentration: {
      largestDistributor: "~25% ของ net revenues (FY2023 10-K; distributor Arrow/WPG-type ไม่ใช่ end customer — underlying demand กระจายหลายหมื่น OEM)",
      secondDistributor: "~10% ของ net revenues (FY2023)",
      distributorChannelTotal: "~56% ของ FY2025 revenue (FY2024 58%)",
      note: "🚩 >20% flag แต่เป็น channel ไม่ใช่ end-customer → concentration risk ที่แท้จริงต่ำกว่าตัวเลข 25% มาก; risk จริง = channel inventory stocking/destocking amplifies cycle. FY2025 disclosure ไม่ชัด (ต้องใช้ FY2023 10-K) = disclosure demerit → ESG Governance"
    },
    geographyRevenue: {
      unitedStates: "29% (~$3.2B)",
      china: "26% (~$2.9B, +34% YoY $2.14B→$2.86B) — geopolitical exposure สูงสุด, MOFCOM anti-dumping + export-control + local-substitution (SG Micro/3Peak) risk; สูงกว่า MU's 7% มาก",
      europe: "21% (industrial-heavy)",
      restOfAsia: "13%",
      japan: "9% (-9% YoY, auto softness)",
      restOfAmericas: "1% (+161% YoY, small base)"
    },
    revenueSegments: [
      { label: "Industrial", value: 49 },
      { label: "Automotive", value: 25 },
      { label: "Communications / AI data-center", value: 16 },
      { label: "Consumer", value: 10 }
    ],
    revenueSegmentsNote: "Q3 FY2026 end-market mix: Industrial +53% YoY (mid-cycle restock, highest margin), Auto +16% (slowest leg), Comms +84% (AI data-center content step-up), Consumer +6% (stabilizing)",
    competitorData: [
      { ticker: "ADI", company: "Analog Devices (subject)", revenueGrowth: 33.65, operatingMargin: 35.67, marketCap: 175310 },
      { ticker: "TXN", company: "Texas Instruments", revenueGrowth: 16.66, operatingMargin: 38.03, marketCap: 236200, strengths: "Analog leader scale #1, in-house 300mm fab = ต้นทุน/หน่วยต่ำสุดในกลุ่ม, ROIC 25.5% / ROE 35.2% (ไม่มี goodwill drag), direct-sales relationship", weaknesses: "gross margin 58.3% ต่ำกว่า ADI (65.8%), capex cycle 300mm หนัก กด FCF 2022-2026, growth +16.7% ช้ากว่า ADI", threatLevel: "MEDIUM" },
      { ticker: "NXPI", company: "NXP Semiconductors", revenueGrowth: 8.77, operatingMargin: 32.94, marketCap: 56380, strengths: "auto/industrial analog + MCU + connectivity leader, valuation ถูกสุดในกลุ่ม (fwd P/E 13.4x, EV/EBITDA 12.7x), ROE 27.9% — closest value alternative", weaknesses: "growth +8.8% ช้าสุด (ยกเว้น ON), China exposure สูง, moat แคบกว่า, leverage สูงกว่า ADI", threatLevel: "MEDIUM" },
      { ticker: "MCHP", company: "Microchip Technology", revenueGrowth: 20.93, operatingMargin: 16.23, marketCap: 39600, strengths: "MCU + analog + FPGA broad portfolio, cross-sell engine, กำลังฟื้นจาก downcycle (guidance raised)", weaknesses: "cyclical ลึกสุดในกลุ่ม — P/E 112x (earnings depressed), ROIC 5.9% ต่ำสุด, EBIT margin 10.6% vs ADI 35.7%, leverage สูง", threatLevel: "LOW" },
      { ticker: "ON", company: "ON Semiconductor", revenueGrowth: -3.14, operatingMargin: 23.19, marketCap: 28270, strengths: "power semiconductor leader (SiC สำหรับ EV traction inverter), image sensor สำหรับ ADAS, structural EV content story", weaknesses: "ยังอยู่ใน downturn (revenue -3.1%), gross margin 42.8% ต่ำสุด (commodity power discrete), ROE 8.3%, SiC demand ชะลอ, capital intensive", threatLevel: "LOW" }
    ],
    bullFlipTriggers: [
      "ราคา ≤ $210 โดย thesis ไม่แย่ลง → MOS ≥ ~15% vs Bear Base $220 / ~10% vs Emma Base $233",
      "China MOFCOM anti-dumping investigation ปิดคดีแบบไม่มี duty หรือ < 10% (ruling ครบกำหนด ~13 ก.ย. 2026) — ลบ ~$2.9B China revenue tail",
      "2 ไตรมาสติดที่ distributor sell-through (POS) growth ≥ shipment growth AND book-to-bill > 1.0 — พิสูจน์ว่า recovery = end-demand ไม่ใช่ channel restock",
      "Fed ให้ Sept cut หรือประกาศจบ hiking cycle AND 10Y < 4.0% — ลบ multiple-compression overhang บน 43x P/E name",
      "Normalized adj operating margin ยืน ≥ 47% เป็น 3+ ไตรมาส พร้อม TXN pricing นิ่ง — validate Emma Base margin; lift Bear Base สู่ ~$250"
    ],
    bearFlipTriggers: [
      "China ตั้ง anti-dumping duty ≥ 25% บน ADI analog imports → ≥ $1.0-1.5B revenue เสี่ยงใน 2 ปี → Bear FV สู่ ~$110",
      "ไตรมาสใดมี QoQ revenue decline + guidance cut ก่อน FY2027 (channel double-order unwind confirmed)",
      "Sept FOMC hike AND VIX ปิด > 20 → Atlas regime → TRANSITIONAL-CAUTIOUS; historical −30% ถึง −40% สำหรับ high-P/E cyclicals",
      "Adj gross margin ลด ≥ 200 bps ใน 2 ไตรมาส (TXN 300mm pricing pressure กัด catalog tier)",
      "Goodwill impairment charge ประกาศ หรือ net-debt/EBITDA > 2.0x เพื่อ fund buyback/M&A เข้า downturn"
    ],
    thesisInvalidation: "\\"No-MOS\\" thesis ผิด ถ้า: ADI compound revenue ≥ 12%/ปี ถึง FY2029 โดยไม่มีปีติดลบ + adj op margin ≥ 48% sustained + China revenue โตแม้มี probe + forward multiple ยืน ≥ 22x → Q3 trajectory เป็น structural เต็มตัว $362 ถูกจริง. | Team HOLD → AVOID/SELL ถ้า: 2027 global industrial recession + China duties ยิงพร้อมกัน → revenue สู่ระดับ FY2024 absolute (~$9.4-10.6B) + margin < 38% → FV $85-100",
    unitEconomics: null,
'''

    full_content_field = "    fullContent: `" + escaped + "`,\n"
    closing = "  },\n"
    return metadata + "\n" + full_content_field + closing


def main():
    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if 'ticker: "ADI"' in content:
        print("ADI entry already exists in data.js — aborting to avoid duplicate.")
        sys.exit(1)

    entry = build_entry()

    content, n = re.subn(
        r'const LAST_UPDATED = "[\d-]+";',
        f'const LAST_UPDATED = "{NEW_LAST_UPDATED}";',
        content,
        count=1,
    )
    if n != 1:
        print("WARNING: LAST_UPDATED not replaced.")

    marker = "const REPORTS = ["
    idx = content.find(marker)
    if idx == -1:
        print("ERROR: REPORTS marker not found. Aborting.")
        sys.exit(1)
    insert_at = idx + len(marker) + 1
    new_content = content[:insert_at] + "\n" + entry + content[insert_at:]

    ob, cb = new_content.count("{"), new_content.count("}")
    obr, cbr = new_content.count("["), new_content.count("]")
    if ob != cb:
        print(f"ERROR: brace mismatch {ob} vs {cb} — aborting.")
        sys.exit(1)
    if obr != cbr:
        print(f"ERROR: bracket mismatch {obr} vs {cbr} — aborting.")
        sys.exit(1)

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("ADI entry inserted. LAST_UPDATED =", NEW_LAST_UPDATED)


if __name__ == "__main__":
    main()
