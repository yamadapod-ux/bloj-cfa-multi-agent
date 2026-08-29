"""
dashboard/_patch_meli.py
Insert MELI (MercadoLibre, Inc.) analysis entry into dashboard/data.js
REPORTS array + update LAST_UPDATED.

Dashboard Write Safety: targeted script, never full-file Write on data.js
(precedent: _patch_adi.py, _patch_tls.py, _patch_pgr.py).

Run:
    cd "C:\\Users\\user\\Desktop\\บลจ\\บลจ CFA"
    python dashboard/_patch_meli.py
"""

import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DATA_JS_PATH = "dashboard/data.js"
REPORT_MD_PATH = "reports/MELI_2026-08-29.md"
NEW_LAST_UPDATED = "2026-08-29"


def build_entry():
    with open(REPORT_MD_PATH, "r", encoding="utf-8") as f:
        report_md = f.read()

    escaped = report_md.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

    metadata = '''  {
    ticker: "MELI",
    company: "MercadoLibre, Inc.",
    date: "2026-08-29",
    version: "v1 (Morgan QA Round 2 PASS)",
    sector: "LatAm E-commerce + Fintech (Consumer Discretionary / Financials hybrid)",
    bucket: "Growth",
    price: 1966.25,
    recommendation: "HOLD / WAIT — NO DEPLOY",
    blendedFV: 1207,
    esgAdjFV: 1085,
    targetBull: 2350,
    targetBase: 1163,
    stopLoss: 940,
    convictionEmma: 5,
    convictionQuinn: 5,
    convictionBear: 6,
    convictionAvg: 5.33,
    mosPct: -38.6,
    mosPctEsgAdj: -44.8,
    pwEV: 1240,
    pwEvBear: 1158,
    beta: 1.31,
    sharpe1Y: 0.24,
    forwardSharpe: 0.24,
    maxDrawdown: -41.3,
    kelly: "Full −186% / Half −93% / Quarter −47% — ติดลบทุกระดับ ไม่มี long position ที่ mathematically justified ที่ $1,966.25",
    moat: "Wide franchise / Narrow economic moat — Bear reconciled: Wide logistics moat (Mercado Envios >90% in-network, same/next-day metros, 15-20yr durability) / Marketplace network effects Medium-contested (Shopee +$6B Brazil GMV ปีเดียว) / Fintech Narrow (NU op margin 52% แข่งตรง underwriting เหนือกว่า) / Data-underwriting Unproven (NPL near lows ขณะ book +75% = ยังไม่ผ่าน full LatAm credit cycle). ROIC 14.2% ≈ WACC 13% = zero economic profit ตอนนี้ — 'Narrow economic' เป็น forward bet ไม่ใช่ current reality",
    esgRating: "Medium-High",
    esgScore: 5.6,
    macroRegime: "RISK-ON",
    morganQA: "Round 2 PASS (Data Quality 9/10, HIGH 0 / MEDIUM 0 / LOW 0 outstanding). Round 1 soft FAIL (FORMAT, 3 MEDIUM + 4 LOW) → Charlie แก้ v1.1 (ESG structured-block sync note, Peer table +EV/EBITDA/ROE/Gross Margin, CFA footnotes 16/16, credit-book reconcile definitive, Porter's New Entrants High, Sensitivity axes align Quinn) → Round 2 cleared ทั้งหมด. Blended FV weight 40/30/30 canonical verified — report จับ + ปฏิเสธ fabricated rule 'IPS 2026-05-15 → 40/35/25' ที่ฝังใน Bear system prompt + task (Error #8 prevention ครั้งที่ 2 ต่อจาก ADI). DCF Cash Flow Consistency: Emma+Quinn NOPAT-based FCFF, gap 1.6% < 25% → ไม่ต้อง reconciliation table (process win — Atlas บังคับ cash-flow basis ใน Data Package)",
    sp500Reference: 7711.76,
    sp500ReferenceNote: "7,711.76 (2026-08-28 close — reuse agent_notes/atlas/2026-08-29_regime.md, Yahoo Finance ^GSPC; 2nd source 7,711.48 delta 0.004%)",
    revenueGrowthYoY: 46.0,
    entryZone: "$1,050–1,300 (mid $1,175) — เข้าได้เมื่อ price pullback ≤ $1,450 หรือ 2 ไตรมาส op-margin recovery ≥ 10% + ads segment disclosure ≥ $5B run-rate (Bull-flip conditional)",
    positionSize: "0% — Growth bucket single-gate-failure: Revenue Growth +46% PASS · Growth MOS marginal PASS (Method 2 EV/Rev 3.05x 5Y low เท่านั้น — optical) · Conviction 5.33 < 6.5 FAIL. Kelly ติดลบทุกระดับ. Force Deploy active (RISK-ON) แต่ไม่มี candidate ผ่าน gate — Force Deploy ไม่ override gate",
    keyThesis: "MELI = wide-moat LatAm super-app (logistics >90% in-network + Mercado Pago TPV $101B/Q + Mercado Crédito $16.4B book + ads), 30 ไตรมาสติด revenue growth >30%, dominant ~35% Brazil e-commerce GMV — แต่ราคา $1,966 อยู่เหนือ FV ของทั้ง 3 analyst (Emma $1,220 / Quinn $1,240 / Bear $1,158) 38–41%. op margin ยุบเหลือ 6.7% (Q2'26, −550bps YoY = deliberate anti-Shopee investment, ไม่มี guidance); WACC ~13% (US CAPM 9.76% + blended EM country risk premium ~4pp) ≈ ROIC 14.2% = zero economic profit ตอนนี้; reported FCF $12.4B = mirage (fintech float +$7.7B, owner FCF ~$1.9B). ไม่ใช่ AVOID — margin trough ไม่ใช่ peak, EV/Rev 5Y low, secular ไม่ใช่ cyclical, credible Bull $2,250+ exists. cyclical/rate-peak analog #4 ต่อจาก MU/CRCL/ADI แต่ setup ตรงข้าม (trough)",
    topRisk: "Valuation / no-MOS — Blended FV $1,207 (MOS −38.6%) ต่ำกว่าราคาทั้ง 3 framework; 1/25 sensitivity cells justify ราคา; Base cell $1,143 = −42%. Downside (Bear + Extreme-Bear, 38% prob) → FV $300–$620 = −68% ถึง −84% (credit book $16.4B +75% YoY NPL 7.0% = late-cycle setup + Argentina mid-terms ต.ค. 2026 + Fed-hawkish DXY). Best realistic upside (Bull 20%) = $2,250 = แค่ +14%. Asymmetry ไม่ดีที่ราคานี้. Terminal operating margin (6.7% วันนี้ → 13-15% Base assumption) เป็น invisible management choice ที่ไม่มี guidance",
    reportFile: "../reports/MELI_2026-08-29.md",
    businessSummary: {
      oneLiner: "ตลาดอีคอมเมิร์ซ + ระบบชำระเงิน + ธนาคารดิจิทัล + เครือข่ายโลจิสติกส์ ที่ครองตลาดละตินอเมริกา (บราซิล เม็กซิโก อาร์เจนตินา)",
      analogy: "Amazon + PayPal + ธนาคาร + Kerry Express รวมกันในบริษัทเดียว แต่สำหรับละตินอเมริกา",
      moneyFlow: [
        "ผู้บริโภคซื้อของบนแอป MELI — บริษัทเก็บค่าคอมมิชชั่น + ค่าโฆษณา + ค่าส่ง ~26% ของมูลค่าสินค้า (GMV $22B/ไตรมาส)",
        "จ่ายเงินผ่าน Mercado Pago — เก็บค่าธรรมเนียมรูดบัตร ~1% ของ TPV $101B/ไตรมาส + net interest margin จาก float",
        "ปล่อยกู้ผ่าน Mercado Crédito — credit book $16.4B (+75% YoY), กินส่วนต่างดอกเบี้ยหลังหักหนี้เสีย (NIMAL 20.7%) แต่แบก credit risk (NPL 7.0%)",
        "รายได้รวมเป็นกำไร: แต่ตอนนี้ op margin แค่ 6.7% (จาก ~13-16%) เพราะจงใจอุดหนุน free shipping + credit card + PIX discounts สู้ Shopee"
      ],
      whyDifferent: "เครือข่ายโลจิสติกส์ที่ใหญ่ที่สุดในละตินอเมริกา (>90% ส่งเอง same/next-day ในเมืองใหญ่) + ecosystem 3-in-1 (ขายของ+จ่ายเงิน+กู้เงิน) + ข้อมูลธุรกรรมที่ใช้ underwrite สินเชื่อ — คู่แข่งต้องใช้ทุนและเวลาหลายปีจึงจะ replicate ได้",
      simpleRisk: "จงใจกดกำไรเพื่อสู้ Shopee/Amazon/Shein และไม่มีใครรู้ว่ากำไรจะฟื้นเมื่อไหร่ (ไม่มี management guidance) + พอร์ตสินเชื่อโต 75%/ปี = เสี่ยงหนี้เสีย + 100% รายได้จาก EM (ไม่มี DM diversification)"
    },
    thesisBullets: [
      { title: "Margin recovery = ทั้ง thesis", why: "op margin 6.7% Q2'26 (−550bps YoY) เป็น management choice; terminal margin 10% vs 13% vs 16% ทำ FV swing $640-$2,290 และไม่มี guidance timeline" },
      { title: "ราคาแพงเทียบมูลค่า", why: "Emma DCF $1,220 / Quinn P-W EV $1,240 / Bear P-W EV $1,158 vs ราคา $1,966 = MOS −38 ถึง −41%; Blended FV $1,207 (−38.6%); reverse DCF imply ~1.24× consensus growth = stretched" },
      { title: "EV/Revenue 5Y low เป็นภาพลวง", why: "3.05x = ต่ำสุด 5 ปี (vs 5.24x FY23 / 4.13x FY24 / 3.66x FY25) เพราะ margin trough ไม่ใช่ราคาถูก; EV/EBIT 37x, EV/EBITDA 27.5x = ไม่ถูกบน earnings basis" },
      { title: "Credit book = quasi-bank risk", why: "$16.4B +75% YoY, NPL 7.0%, provisioning $1.24B/ไตรมาส; MELI กลายเป็นธนาคารแต่ยัง valued แบบ growth-tech + เสี่ยง rate-cap regulation (Brazil card cap enacted 2024)" },
      { title: "Moat แข็งแต่ไม่สร้างมูลค่า", why: "franchise Wide (logistics durable 15-20 ปี) แต่ ROIC ยุบ 63.75%→14.2% ≈ WACC 13% = zero economic profit; MELI จ่าย margin 550bps ป้องกัน Shopee และยัง lose marginal share" }
    ],
    esgBreakdown: {
      e: 6,
      s: 4.5,
      g: 6.5,
      overall: 5.6
    },
    esgBreakdownNote: "Reconciled (Bear challenge applied): Social 5 → 4.5 (responsible-lending บน credit book +75-91%/yr ให้ underbanked ในเศรษฐกิจเงินเฟ้อสูง, NPL 7% = setup เดียวกับที่ทำให้เกิด regulatory backlash ทั่วโลก; gig-worker reclassification Brazil 'PL dos Aplicativos'; LGPD บน 88M fintech users). Governance 7 → 6.5 (complex cross-border fintech entity structure Brazil/Argentina/Mexico/Cayman; credit book $16B external banking oversight จำกัด). Overall 6.0 → 5.6 (Medium-High Risk). Valuation impact −10% → ESG-adj Blended FV $1,085. ⚠️ Emma structured-data block ค้างค่า pre-Bear {e:6,s:5,g:7,overall:6.0} — ESG structured-block staleness ซ้ำครั้งที่ 5 (TLS/CRCL/ADI/...)",
    customerConcentration: {
      note: "ไม่มี concentration risk — fragmented marketplace (ล้าน SMB sellers + 60M+ consumers + 88M fintech MAU + 100M+ ecosystem users), single customer <<1% revenue. Risk = platform/seller ecosystem health + regulatory ไม่ใช่ key-account loss"
    },
    geographyRevenue: {
      brazil: "54.4% (~$5,530M Q2'26) — single-country concentration risk (BRL/USD ~5.19, fiscal, Selic 14% easing path); Q2'26 reported +59% มี FX tailwind vs +40% FX-neutral commerce",
      mexico: "23.0% (~$2,337M) — +38% FX-neutral, กำลัง scale",
      argentina: "18.1% (~$1,839M) — elevated tail risk (ARS step-devaluation, ~$20B external maturities 2026, mid-term elections ต.ค. 2026); reported +20% แต่ FX-neutral GMV +38% = underlying แข็ง",
      otherLatAm: "~4.6% (~$463M — Chile, Colombia)",
      china: "~0% — ไม่มี China exposure; 100% LatAm/EM, zero DM diversification. Fed hawkish + strong USD = direct translation drag ทุก segment"
    },
    revenueSegments: [
      { label: "Commerce", value: 57 },
      { label: "Fintech (Mercado Pago + Crédito)", value: 43 }
    ],
    revenueSegmentsNote: "ประมาณจาก Q2'26 commerce revenue $5.8B vs total net revenues & financial income $10.17B (~57% commerce / ~43% fintech). MELI ไม่ disclose segment operating margin แยกประเทศ",
    competitorData: [
      { ticker: "MELI", company: "MercadoLibre (subject)", revenueGrowth: 46.0, operatingMargin: 8.26, marketCap: 99680 },
      { ticker: "SE", company: "Sea Limited", revenueGrowth: 43.06, operatingMargin: 8.24, marketCap: 73110, strengths: "closest structural analog (super-app: e-comm Shopee + fintech SeaMoney + gaming Garena); Garena gaming = cash cow อุด e-comm losses; Shopee บุก Brazil สำเร็จ (GMV ~$10B ≈ 40% ของ MELI, added ~$6B ปีเดียว); asset-lighter logistics", weaknesses: "Garena revenue เสี่ยง concentration (Free Fire single-title); ไม่มี logistics moat ลึกแบบ MELI; fintech (SeaMoney) เล็กกว่า Mercado Pago มาก", threatLevel: "HIGH" },
      { ticker: "NU", company: "Nu Holdings", revenueGrowth: 44.33, operatingMargin: 52.02, marketCap: 69080, strengths: "pure-play LatAm neobank, op margin 52%, 100M+ ลูกค้า, low CAC, credit underwriting ชั้นเยี่ยม — proof point ว่า mature LatAm fintech ทำ margin 50%+ ได้; แข่งตรงกับ Mercado Pago/Crédito ใน banking layer", weaknesses: "ไม่มี e-commerce/logistics; Brazil concentration; NIM เสี่ยงเมื่อ credit cycle turn", threatLevel: "MEDIUM" },
      { ticker: "CPNG", company: "Coupang", revenueGrowth: 9.92, operatingMargin: -1.70, marketCap: 29690, strengths: "logistics execution ระดับโลก (Rocket Delivery), Korea dominance, เริ่มขยาย Taiwan", weaknesses: "growth หมดแล้ว (+9.9% TTM), op margin −1.7%, ไม่มี fintech engine, ไม่ได้อยู่ LatAm; cautionary tale — e-comm-only ที่ growth หมด → P/E 82x เปราะมาก", threatLevel: "LOW" },
      { ticker: "STNE", company: "StoneCo", revenueGrowth: 1.6, operatingMargin: 51.3, marketCap: 3900, strengths: "Brazil payments/fintech, op margin ~51%, mature profitability, merchant relationships ลึก — benchmark margin ของ Brazil payments", weaknesses: "growth หยุด (+1.6% Q2'26), market cap หด $3.9B (จาก peak >$30B), โดน MELI + NU + PIX กินส่วนแบ่ง — เป็นเหยื่อมากกว่าเป็นภัย", threatLevel: "LOW" }
    ],
    bullFlipTriggers: [
      "Op margin recovery: op margin ≥ 2 ไตรมาสติดกลับเหนือ 10.0% (จาก 6.7%) AND management ออก explicit margin-trajectory guidance เป้า ≥ 13%",
      "Price: ราคาย่อ ≤ $1,450 (ใกล้ 52W low $1,495 + Base FV) → MOS เป็นบวกบน Base",
      "Advertising disclosure: MELI เปิดเผย ads เป็น segment + run-rate ≥ $5B annualized ที่ incremental margin ≥ 50% → validate structural margin lever (FV → $1,900–2,200)",
      "CRP compression confirmed: Argentina sovereign upgrade ถึง B+ ขึ้นไป AND Brazil Selic < 12% + fiscal stable → blended CRP < 2%, WACC ~12%, Base FV → ~$1,450+",
      "Competitive intensity peak passed: Shopee Brazil GMV growth ชะลอ < 20% YoY 2 ไตรมาสติด (จาก ~50%+)"
    ],
    bearFlipTriggers: [
      "Credit deterioration: 15–90 day NPL เหนือ 9.0% (จาก 7.0%) หรือ provisions/originations แย่ลง 2 ไตรมาสติด",
      "Margin capitulation: op margin หลุดต่ำกว่า 6.0% ในไตรมาสใดก็ตาม",
      "Secular growth break: revenue growth (FX-neutral) ของ segment ใดก็ตาม decel ต่ำกว่า 20%",
      "Rate-cap enacted: Brazil หรือ Mexico ออก consumer-credit interest-rate cap applicable กับ Mercado Crédito → −10 ถึง −15% FV",
      "Argentina break: Milei coalition แพ้ mid-term ต.ค. 2026 decisively AND ARS หลุด crawling band (step-devaluation > 25%)"
    ],
    thesisInvalidation: "Thesis ผิดทั้งหมด (re-analysis required) ถ้า: (1) ไตรมาสที่ GMV FX-neutral growth ติดลบ หรือ fintech TPV growth < 15% → premise 'secular LatAm digitization + dominant share' ตาย | (2) Credit-book stress ที่ต้อง equity raise หรือ write-down > $2B → MELI คือ lender ที่บริหารพลาด, re-underwrite ตั้งแต่ต้น | (3) MELI เสียตำแหน่ง #1 GMV ใน Brazil ให้ Shopee/Amazon 2 ไตรมาสติด → logistics moat ไม่ translate เป็น durable marketplace dominance",
    unitEconomics: null,
'''

    full_content_field = "    fullContent: `" + escaped + "`,\n"
    closing = "  },\n"
    return metadata + "\n" + full_content_field + closing


def main():
    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if 'ticker: "MELI"' in content:
        print("MELI entry already exists in data.js — aborting to avoid duplicate.")
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

    # lone-comma / undefined-slot guard
    if re.search(r'\[\s*,', new_content) or re.search(r',\s*,', new_content):
        print("ERROR: lone/double comma detected — aborting.")
        sys.exit(1)

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("MELI entry inserted. LAST_UPDATED =", NEW_LAST_UPDATED)


if __name__ == "__main__":
    main()
