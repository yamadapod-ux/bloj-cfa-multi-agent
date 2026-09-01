# -*- coding: utf-8 -*-
"""
dashboard/_patch_zeta.py
Insert ZETA (Zeta Global Holdings Corp.) analysis entry into dashboard/data.js
REPORTS array + update LAST_UPDATED.

Dashboard Write Safety: targeted script, never full-file Write on data.js
(precedent: _patch_chym.py, _patch_meli.py, _patch_adi.py).

Run:
    python dashboard/_patch_zeta.py
"""
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DATA_JS_PATH = "dashboard/data.js"
REPORT_MD_PATH = "reports/ZETA_2026-09-01.md"
NEW_LAST_UPDATED = "2026-09-01"


def build_entry():
    with open(REPORT_MD_PATH, "r", encoding="utf-8") as f:
        report_md = f.read()
    escaped = report_md.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

    metadata = r'''  {
    ticker: "ZETA",
    company: "Zeta Global Holdings Corp.",
    date: "2026-09-01",
    version: "v1 (Morgan QA CONDITIONAL PASS — Data Quality 8.0/10)",
    sector: "US Adtech / Martech — data + AI + omnichannel activation platform สำหรับ enterprise CMO",
    bucket: "GROWTH",
    price: 30.88,
    recommendation: "AVOID / HOLD-WAIT FOR PULLBACK — NO DEPLOY",
    blendedFV: 19.16,
    esgAdjFV: 17.53,
    mos: "-38.0%",
    mosPct: -38.0,
    mosPctEsgAdj: -43.2,
    conviction: 5.5,
    convictionEmma: 4.5,
    convictionQuinn: 5.0,
    convictionBear: 7.0,
    convictionAvg: 5.5,
    targetBull: 37,
    targetBase: 19,
    stopLoss: 14.80,
    pwEV: 19.58,
    pwEvBear: 13.50,
    beta: 1.39,
    sharpe1Y: -0.32,
    forwardSharpe: -0.32,
    maxDrawdown: "-62% historical peak-to-trough ($38.20→$14.37); -34% single-event (Culper day, Nov 2024); est. -40% ถึง -55% forward 12M stress",
    kelly: "0% ทุก fraction (Full / Half / Quarter). Forward E[R] 12M ≈ -12.8%, ≈ 25pp ต่ำกว่า CAPM hurdle; Forward Sharpe -0.32; Treynor -12.6%. Kelly พลิกบวกที่ราคา ~$19–20",
    moat: "NARROW · durability ~7–10 ปี (Emma NARROW / Bear NARROW-capped / Quinn implicit NARROW). data network effect (partial — opt-in base จริง ~110M ไม่ใช่ 240M+ ตาม marketing material) + switching cost (real ไม่ absolute — NRR ~120%, super-scaled tenure 56 เดือน) — แต่ gross margin 59.5% ต่ำกว่า TTD ~16 จุด = ไม่มี structural cost edge; M&A-assisted growth = moat 'ซื้อมา' ไม่ใช่ compound organically",
    esgRating: "Medium-High",
    esgScore: 4.0,
    macroRegime: "TRANSITIONAL-CAUTIOUS",
    morganQA: "CONDITIONAL PASS (Data Quality 8.0/10, 0 HIGH / 3 MEDIUM / 4 LOW, reject type FORMAT). Price gate PASS ($30.88 Stockanalysis + $30.92 Yahoo + Morgan independent live $30.54, Δ < 5%). Market cap sanity 250.4M × $30.88 = $7,732M ✓. Blended FV 40/30/30 canonical verified — Charlie ปฏิเสธ fabricated 'IPS 2026-05-15 → 40/35/25' ใน base-prompt (Error #8/#9 prevention instance ต่อเนื่อง: ADI→GCT→MELI→CHYM→ZETA). DCF Cash Flow Consistency Rule: SBC 12.4% > 10% → ยิง; ทั้ง 3 analysts NOPAT-based FCFF; Emma single FV $21.50 vs Quinn $21.71 gap +1.0% << 25% → reconciliation table ไม่บังคับ (Emma flag methodology band ภายใน framework ตัวเอง ~40% — disclosed). M-1 (Competitor Profiles subsection) + M-3 (CFA footnotes 5 headings) → Charlie แก้แล้ว. M-2 (Emma esgBreakdown block stale {e:8,s:4,g:3,overall:4.3}) + L-1 (competitorData array) → Leo embed reconciled {e:7.5,s:3.5,g:2.75,overall:4.0} + build competitorData. ไม่มีข้อไหนเปลี่ยน verdict.",
    sp500Reference: 7688.39,
    sp500ReferenceNote: "7,688.39 (2026-08-31 close — last completed session; agent_notes/atlas/2026-09-01_regime.md § Single Source of Truth; Yahoo Finance -23.37/-0.30% + TradingEconomics 7,688.30 cross-check; prior close 7,711.76 Aug 28. Sept 1 close ยังไม่มี ณ analysis time)",
    revenueGrowthYoY: 35,
    revenueGrowthNote: "+35% total YoY (TTM) / +25% organic (ex-M&A ex-political candidate revenue). ~10pp ของ total growth มาจาก M&A (LiveIntent/Marigold). FY2026 guide +39% total / +25% organic ex-political",
    entryZone: "$17–20 (mid $18.50) — ต้องได้ MOS ≥ 15% vs Blended FV $19.16 AND Bull Flip Trigger ยืนยัน (Davoodi settle ≤ $75M / GAAP op margin > 10% 2Q / Regime กลับ RISK-ON). จาก entry mid $18.50 → Blended FV $19.16 = CAGR +1.2%/ปี (ต่ำกว่า risk-free — ต้องรอราคา ≤ $16.30 หรือ bull-flip)",
    positionSize: "0% — FAIL Growth conviction gate (avg 5.5 < 6.5) + FAIL Growth MOS Gate (Method 1 Reverse DCF implied CAGR ~1.3–1.5× consensus > 1.2×; Method 2 EV/Rev percentile split-fail Emma 85th / Quinn 55–65th) + absolute MOS -38.0% + **Regime TRANSITIONAL-CAUTIOUS → Force Deploy SUSPENDED, ห้าม open new position ทั้งหมด** (Atlas judgment override — US-Iran strike / oil spike / Fed hike priced Sept FOMC)",
    keyThesis: "ZETA = enterprise marketing platform (proprietary Identity Graph + AI/agentic layer + omnichannel activation) — ธุรกิจ execute ได้จริง (20 ไตรมาสติด beat-and-raise, organic +25%, NRR ~120%, adj EBITDA margin 20.7% +170bps, Q2'26 GAAP-positive ไตรมาสแรก). แต่ราคา $30.88 (YTD +52%, ห่าง 52W high 0.5%, EV/Revenue 4.9x = premium สูงสุดในกลุ่ม independent adtech/martech) price in ทศวรรษของการโต ≥ 17% + operating margin 18–21% ที่ ZETA ไม่เคยทำได้ (GAAP op margin TTM 3.4%, gross margin ลดจาก 63% → 59.5%). SBC TTM $194.5M = 12.4% ของรายได้ (+19% YoY) → GAAP breakeven — owner FCF จริง ~$30M ไม่ใช่ reported $224M (overstate 6–7×). Q2'26 GAAP EPS $0.03 พลาด consensus ~$0.20. Davoodi v. Zeta class action — MTD DENIED 8 ก.ค. 2026 → discovery active; บริษัทถอนคำว่า 'opted-in' ออกจาก filings เอง. Growth MOS Gate FAIL + Conviction 5.5 < 6.5 + Regime TC. 7th consecutive 'priced-for-perfection' NO-DEPLOY (MU/CRCL/ADI/MELI/GCT/CHYM→ZETA). ไม่ใช่ hard AVOID — net cash + FCF+ + execution track record จริง = 'great business, wrong price, wrong macro window'. Scout Round 26 price ($23.50 '2.8x P/S discount') STALE — ราคาจริง $30.88 near-ATH, thesis เปลี่ยนทั้งหมด",
    topRisk: "Quality of earnings + valuation-priced-for-perfection — SBC $194.5M (12.4% rev, +19% YoY H1) >> Operating Income $53.4M >> Net Income -$2.17M; owner FCF จริง ~$30M ไม่ใช่ reported $224M. Reverse DCF ที่ $30.88 = implied 10-yr revenue CAGR 17.6–19.5% + terminal EBIT margin 18% ที่ ZETA ไม่เคยแตะ. Sensitivity Matrix (10-yr Rev CAGR × Terminal EBIT margin): 7/25 cells (28%) เท่านั้นที่ justify $30.88 — ต้องการ margin ≥ 18% (peak) AND CAGR ≥ 17% sustained 10 ปี พร้อมกัน. Bear P-W EV $13.50 (MOS -56.3%). Davoodi discovery: settlement estimate $125–175M + moat-impairment tail (opt-in base จริง ~110M vs claimed '240M+'). Severe scenario (systemic data-sourcing problem + settlement > $200M) → $6–7",
    reportFile: "../reports/ZETA_2026-09-01.md",
    businessSummary: {
      oneLiner: "Enterprise marketing platform — รวม proprietary consumer Identity Graph + AI + omnichannel activation (email/CTV/social/search/display) ขายให้ CMO องค์กรเป็นสัญญารายปี + media pass-through",
      analogy: "เหมือน Adobe/Salesforce Marketing Cloud แต่เน้น first-party identity data + ซื้อ media inventory มา activate เอง (เก็บ margin บางๆ บนยอดที่ไหลผ่าน — revenue โตเร็วแต่ gross margin เจือจาง)",
      moneyFlow: [
        "Subscription / platform fees — CMO องค์กรจ่ายค่าเข้าใช้ Zeta Marketing Platform เป็นสัญญารายปี (data + AI + campaign orchestration)",
        "Media & data pass-through — ZETA ซื้อ ad inventory/data แล้ว activate เก็บ margin บางๆ บนยอดที่ไหลผ่าน — ทำให้ headline growth สูงแต่ gross margin เจือจาง (59.5%)",
        "Identity Graph licensing — ขายการเข้าถึง/enrichment ของ consumer identity data (~110M opt-in email + device/behavioral signals)",
        "Outcome/usage-based pricing — บางสัญญาผูกกับ consumption (56% ของ CMO shift ไป consumption pricing)",
        "M&A roll-up — LiveIntent 2024 (~$250M), Marigold — เพิ่ม scale + headline growth"
      ],
      whyDifferent: "ต่างจาก pure DSP (TTD) — มี first-party Identity Graph + AI/agentic layer + OpenAI/Snowflake/Palantir partnerships; NRR ~120%, super-scaled tenure 56 เดือน = switching cost จริง — แต่ opt-in base จริง ~110M ไม่ใช่ 240M+ ที่โฆษณา",
      simpleRisk: "ราคา near-ATH price in ความสมบูรณ์แบบ (7/25 cells) — SBC 12.4% รายได้ทำให้ GAAP breakeven แม้ adj EBITDA 'กำไร'; owner FCF จริง ~$30M; Davoodi class action เข้า discovery (opt-in scope misrepresent); gross margin ลด 63%→59.5% = mix shift ไป lower-margin pass-through; Regime TRANSITIONAL-CAUTIOUS"
    },
    thesisBullets: [
      { title: "ราคา price in ความสมบูรณ์แบบ", why: "Reverse DCF ที่ $30.88 = implied 10-yr revenue CAGR 17.6–19.5% + terminal EBIT margin 18% ที่ ZETA ไม่เคยแตะ (GAAP op margin TTM 3.4%). Sensitivity 7/25 cells (28%) justify — ต้อง margin ≥ 18% AND CAGR ≥ 17% sustained พร้อมกัน" },
      { title: "Quality of earnings — SBC wedge", why: "SBC TTM $194.5M = 12.4% ของรายได้ (+19% YoY) >> Operating Income $53.4M >> Net Income -$2.17M. Q2'26 GAAP EPS $0.03 พลาด consensus ~$0.20. owner FCF จริง ~$30M ไม่ใช่ reported $224M (overstate 6–7×). 'Rule of 64' = company metric ใช้ M&A-inflated 44% growth ไม่ใช่ organic 25%" },
      { title: "Davoodi v. Zeta — MTD DENIED, discovery active", why: "8 ก.ค. 2026 Judge Ho ปฏิเสธ motion to dismiss (29 หน้า) → discovery. Allegation ที่ survived = misrepresent scope ของ opt-in consent เบื้องหลัง '240M+' (จริง ~110M); บริษัทถอนคำว่า 'opted-in' ออกจาก filings เอง. Settlement estimate $125–175M + moat-impairment tail" },
      { title: "M&A-boosted headline + goodwill 57% equity", why: "~10pp ของ +35% total growth มาจาก M&A (LiveIntent/Marigold). goodwill $524.7M = 57% ของ equity. 2027 organic comps (ex-M&A ex-political) เสี่ยง decel → 18–20% → Growth-bucket gate pressure" },
      { title: "Asymmetry แย่ — near-ATH, Street upside ~0–13%", why: "YTD +52%, ห่าง 52W high 0.5%. Street avg 12M PT ~+6% เหนือราคา (BofA $34 / Citi $35 = ปลายบน fair range); Freedom Broker downgrade Buy→Hold (5 ส.ค.). Regime TRANSITIONAL-CAUTIOUS + Fed hike priced Sept = multiple compression ต่อ high-P/E growth" }
    ],
    esgBreakdown: { e: 7.5, s: 3.5, g: 2.75, overall: 4.0 },
    esgBreakdownNote: "Reconciled จาก report §ESG (Emma / Bear → Reconciled): Environmental 8 / 7 → 7.5 (asset-light; compute/data-center energy indirect เท่านั้น). Social 4 / 3 → 3.5 (consumer-consent litigation = data-ethics issue ที่ core asset ตั้งอยู่บน consent basis ที่กำลังถูกฟ้อง; privacy-regulatory TAM risk). Governance 3 / 2.5 → 2.75 (dual-class controlled company — Steinberg > 50% voting; active securities class action Davoodi v. Zeta [MTD DENIED → discovery, C-suite defendants]; aggressive non-GAAP 'Rule of 64'; goodwill $524.7M = 57% ของ equity; SBC 12.4% rev + rising). Overall 4.3 / 3.5 → 4.0/10 (MEDIUM–HIGH RISK). Valuation impact reconciled -8.5% (Emma -6% / Bear -11%) → ESG-adj Blended FV $17.53 → MOS -43.2%. Emma structured-data block ยัง stale {e:8,s:4,g:3,overall:4.3} — Leo embed จาก reconciled report ตาม Morgan M-2 (ESG structured-block staleness ซ้ำต่อจาก TLS/CRCL/ADI/MELI/GCT/CHYM — instance ที่ 7)",
    customerConcentration: {
      note: "ไม่มี single customer > 10% flag ใน 10-Q (Emma notes). ZETA report scaled (>$100K/yr) + super-scaled (>$1M/yr) customer counts เท่านั้น; largest vertical ~22% ของ revenue = diversified ไม่ใช่ single-account risk. Supplier concentration: พึ่ง walled-garden inventory (Meta/Google) + third-party data source ที่ถูก privacy regulation กดดัน"
    },
    geographyRevenue: {
      unitedStates: "~90%+ — US-centric enterprise martech (Atlas Section K estimate — ไม่มี exact breakdown ใน filing)",
      international: "~<10%",
      china: "~0% — ไม่มี exposure"
    },
    revenueSegments: [
      { label: "Subscription / platform fees + Identity Graph licensing (est.)", value: 58 },
      { label: "Media & data pass-through (est.)", value: 42 }
    ],
    revenueSegmentsNote: "ZETA ไม่ disclose software-vs-media split ชัดเจนใน filing — ตัวเลข est. จาก gross margin trajectory (59.5% TTM, ลดจาก 63% = mix shift ไป pass-through) + Emma peer work. Political candidate revenue ~$15M (~1% ของ revenue, 2026 midterm) — immaterial ต่อตัวเลขแต่เป็น 2027 comp headwind เล็กน้อย",
    competitorData: [
      { ticker: "ZETA", company: "Zeta Global (subject)", revenueGrowth: 35, operatingMargin: 3.4, marketCap: 7750 },
      { ticker: "TTD", company: "The Trade Desk", revenueGrowth: 11.6, operatingMargin: 19.6, marketCap: 6220, strengths: "independent DSP ที่ใหญ่สุด, buy-side transparency, CTV programmatic leadership, GAAP op margin 19.6% + gross margin ~80% (สูงกว่า ZETA ~20pp)", weaknesses: "growth ชะลอเหลือ +11.6%, 'shrinking addressable market' narrative, ไม่มี first-party identity asset ระดับ ZETA; market cap เคย ~$140B → ~$6.2B = template ของ multiple compression", threatLevel: "MEDIUM" },
      { ticker: "CRTO", company: "Criteo", revenueGrowth: -4.2, operatingMargin: 9.3, marketCap: 865, strengths: "retail media network pivot, commerce media heritage, GAAP op margin 9.3% (positive)", weaknesses: "revenue หด -4.2%, cookie-deprecation legacy exposure, brand เก่า — cautionary tale ของ adtech ที่ไม่ปรับตัว", threatLevel: "LOW-MEDIUM" },
      { ticker: "BRZE", company: "Braze", revenueGrowth: 27.0, operatingMargin: -15.3, marketCap: 3840, strengths: "customer engagement / lifecycle messaging ชั้นนำ, developer-friendly, NRR สูง, growth +27% — direct comp ที่ CDP/engagement budget ของ CMO เดียวกัน", weaknesses: "GAAP operating margin -15.3% (เผาเงินหนัก), scope แคบกว่า (messaging ไม่ใช่ full-stack data+media)", threatLevel: "MEDIUM-HIGH" },
      { ticker: "APP", company: "AppLovin", revenueGrowth: 60.6, operatingMargin: 77.4, marketCap: 104450, strengths: "mobile ad monetization + AI engine (AXON), GAAP op margin 77.4% + growth +60.6% = best-in-class ทั้งสองมิติ — พิสูจน์ว่า AI-driven adtech ทำ margin 70%+ ได้", weaknesses: "concentrated ใน mobile gaming/app-install, ไม่เล่นใน enterprise CMO / omnichannel space — different arena (แต่ยกมาตรฐานที่ตลาดคาดหวัง)", threatLevel: "LOW" }
    ],
    bullFlipTriggers: [
      "ราคา ≤ $19–20 — MOS ≥ 15% บน Blended FV + downside-protected",
      "Davoodi settle ≤ $75M + discovery ไม่เจอ knowing-misrepresentation docs + ไม่มี FTC/regulator action",
      "GAAP operating margin > 10% TTM 2 ไตรมาสติด + organic growth ยังคง ≥ 25%",
      "SBC < 9% ของ revenue + share count flat YoY (dilution หยุด)",
      "Gross margin re-expand ≥ 62% + Regime กลับ RISK-ON"
    ],
    bearFlipTriggers: [
      "Discovery เปิดเผย knowing-misrepresentation docs / settlement > $200M / FTC enforcement action",
      "Organic revenue growth < 20% (ไตรมาสใดๆ)",
      "Guidance cut หรือ revenue miss > 5%",
      "Gross margin < 57%",
      "Goodwill impairment หรือ debt-funded M&A > $300M / NRR < 105%"
    ],
    thesisInvalidation: "Bull thesis invalid ถ้า ZETA ไม่สามารถ sustain ≥ 20% organic growth + ≥ 15% GAAP operating margin ภายใน 8 ไตรมาส. Bear thesis invalid ถ้า Davoodi dismissed หรือ settled < $50M โดยไม่มี admission AND GAAP op margin ทะลุ 12%+ sustained → re-analysis required",
    unitEconomics: {
      ruleOf40: "~64 ('Rule of 64' company metric: rev growth +44% M&A-inflated + adj EBITDA margin 20.7%) / ~46 ถ้าใช้ organic +25% + adj EBITDA margin 20.7% / ~39 ถ้าใช้ organic +25% + FCF margin 14.3%",
      nrr: "~120% (super-scaled cohort)",
      ltvCac: "N/A — ไม่ disclose",
      cacPayback: "N/A",
      sbcPctRevenue: "12.4% (SBC TTM $194.5M, +19% YoY H1) — HIGH, DCF Cash Flow Consistency Rule ยิง; net dilution ~1.5–2%/yr",
      note: "20 ไตรมาสติด beat-and-raise; super-scaled customer tenure 56 เดือน; Gross Margin TTM 59.5% (ลดจาก 63% — mix shift ไป pass-through); GAAP Operating Margin 3.4% (vs TTD 19.6%); Net Income TTM -$2.17M (SBC wedge); FCF TTM $224M reported แต่ owner FCF ≈ $30M หลังหัก SBC. ความเสี่ยง = valuation + regime + litigation-overhang — ไม่ใช่ broken business"
    },
    fvVerifiedDate: "2026-09-01",
    priceUpdated: "2026-09-01",
'''

    full_content_field = "    fullContent: `" + escaped + "`,\n"
    closing = "  },\n"
    return metadata + "\n" + full_content_field + closing


def main():
    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if 'ticker: "ZETA"' in content:
        print("ZETA entry already exists in data.js — aborting to avoid duplicate.")
        sys.exit(1)

    entry = build_entry()

    content, n = re.subn(r'const LAST_UPDATED = "[\d-]+";',
                         f'const LAST_UPDATED = "{NEW_LAST_UPDATED}";', content, count=1)
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
        print(f"ERROR: brace mismatch {ob} vs {cb} — aborting."); sys.exit(1)
    if obr != cbr:
        print(f"ERROR: bracket mismatch {obr} vs {cbr} — aborting."); sys.exit(1)
    if re.search(r'\[\s*,', new_content) or re.search(r',\s*,', new_content):
        print("ERROR: lone/double comma detected — aborting."); sys.exit(1)

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("ZETA entry inserted. LAST_UPDATED =", NEW_LAST_UPDATED)


if __name__ == "__main__":
    main()
