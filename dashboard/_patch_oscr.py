# -*- coding: utf-8 -*-
"""
dashboard/_patch_oscr.py
Insert OSCR (Oscar Health, Inc.) analysis entry into dashboard/data.js
REPORTS array + update LAST_UPDATED.

Dashboard Write Safety: targeted script, never full-file Write on data.js
(precedent: _patch_zeta.py, _patch_chym.py, _patch_meli.py).

Run:  python dashboard/_patch_oscr.py
"""
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DATA_JS_PATH = "dashboard/data.js"
REPORT_MD_PATH = "reports/OSCR_2026-09-01.md"
NEW_LAST_UPDATED = "2026-09-01"


def build_entry():
    with open(REPORT_MD_PATH, "r", encoding="utf-8") as f:
        report_md = f.read()
    escaped = report_md.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

    metadata = r'''  {
    ticker: "OSCR",
    company: "Oscar Health, Inc.",
    date: "2026-09-01",
    version: "v1 (Morgan QA CONDITIONAL PASS — Data Quality 8.0/10)",
    sector: "US Health Insurance — pure-play ACA individual marketplace (98% net premium) + +Oscar B2B platform licensing + Oscar Medical Group",
    bucket: "GROWTH",
    price: 29.96,
    recommendation: "AVOID / HOLD-WAIT FOR PULLBACK — NO DEPLOY",
    blendedFV: 21.10,
    esgAdjFV: 19.20,
    mos: "-29.6%",
    mosPct: -29.6,
    mosPctEsgAdj: -35.9,
    conviction: 4.83,
    convictionEmma: 5.0,
    convictionQuinn: 4.5,
    convictionBear: 5.0,
    convictionAvg: 4.83,
    targetBull: 42,
    targetBase: 22,
    stopLoss: 14.00,
    pwEV: 21.43,
    pwEvBear: 19.50,
    beta: 2.38,
    sharpe1Y: 0.20,
    forwardSharpe: 0.20,
    maxDrawdown: "-68.1% (52W $33.55 -> $10.69); IPO-era directional ~-94%; forward-stress est. -55% to -75% (cliff scenario FV $7.29 = -75.7%; beta 2.38 + binary = gap risk เกิน -20% stop)",
    kelly: "0% ทุก fraction (f* -4.42 / -2.21 / -1.11 — negative edge). Kelly พลิกบวกที่ราคา ~$21 (P-W EV) หรือเมื่อ ACA subsidy binary resolve toward extension",
    moat: "NARROW-fragile · durability 5–10 ปี, contingent (Emma Narrow-fragile / Quinn implicit Narrow / Bear Narrow-capped). Moat sources: tech platform (partial — admin-cost advantage แต่ MLR 80% floor caps benefit), cost advantage (partial), switching cost ~0 (ACA re-shop ทุก open enrollment), network effect ไม่มี, efficient scale ไม่มี (CNC #1, Blues, MOH, Aetna แข่งในตลาดเดียวกัน). Paired moat FV: Bull $32–38 / Bear $9–13",
    esgRating: "Medium-High",
    esgScore: 4.8,
    macroRegime: "TRANSITIONAL-CAUTIOUS",
    morganQA: "CONDITIONAL PASS (Data Quality 8.0/10, 0 HIGH / 3 MEDIUM / 4 LOW, reject type FORMAT). Price gate PASS ($29.96 × 2 sources, Δ 0%). Market cap sanity 308.33M × $29.96 = $9,235M ✓. **Atlas Q2 2026 data correction verified** — scout package 'Q2 rev +29% / membership +28% / >2.0M' ผิด; Atlas corrected จาก 10-Q oscr-20260630: Q2 revenue $4.88B (+70% YoY), membership 2,963,002 (~2.96M, +46% YoY), Q2 net income $362M. TTM ($15,319M / +42.8% / EPS $1.91) ถูกต้อง = valuation basis. Blended FV 40/30/30 canonical verified — Charlie ปฏิเสธ fabricated 'IPS 2026-05-15 → 40/35/25' (Error #8/#9 prevention instance ต่อเนื่อง ADI→GCT→MELI→CHYM→ZETA→OSCR). SBC 0.49% rev → DCF Cash Flow Consistency Rule ไม่ยิง; ทั้ง 3 analysts NOPAT-based FCFF, strip premium-float ΔNWC, treat risk-adj payable $4.94B non-operating, ไม่ extrapolate reported OCF/FCF $4,380M. Growth MOS Gate: Emma PASS 2/2 vs Quinn FAIL 2/2 → Bear reconciled FAIL 0/2 (Emma PASS = methodology artifact — generous WACC + non-informative EV/Revenue metric สำหรับ premium-pass-through insurer; NET 2026-08-10 precedent). Emma-Quinn single-FV gap +2.3% << 25% → reconciliation table ไม่บังคับ. 3 MEDIUM = ESG structured-block (Leo embed reconciled {e:8,s:4.5,g:3,overall:4.8}) + competitorData array (Leo build) + Q2 corrected figures embed. ไม่มีข้อไหนเปลี่ยน verdict.",
    sp500Reference: 7688.39,
    sp500ReferenceNote: "7,688.39 (2026-08-31 close — reuse agent_notes/atlas/2026-09-01_regime.md § Single Source of Truth [same session as ZETA]; Yahoo Finance -0.30% + TradingEconomics 7,688.30 cross-check; prior close 7,711.76 Aug 28; Sept 1 close ยังไม่มี ณ analysis time)",
    revenueGrowthYoY: 42.8,
    revenueGrowthNote: "Revenue TTM +42.8% ($15,319M) — แต่ growth ไม่ structural: subsidy-era one-time membership surge (2026 special pricing year). Q2 2026 (Atlas-corrected): revenue $4.88B (+70% YoY), membership 2,963,002 (~2.96M, +46% YoY), net income $362M. Rev history: FY22 $3,964M → FY23 $5,863M (+48%) → FY24 $9,178M (+57%) → FY25 $11,701M (+28%). 2026 enrollment แล้ว -21% ถึง -26% (market-wide); analyst คาด 2027 -10% ถึง -20% เพิ่ม",
    entryZone: "$16–19 (mid $17.50) — ต้องได้ MOS ≥ 15% vs Blended FV $21.10 AND Bull Flip Trigger ยืนยัน (multi-yr ePTC extension signed / CARE Act ผ่านชัดเจน + stock ยังไม่ re-rate / 2027 open-enrollment membership decline ≤ 5%). จาก entry mid $17.50 → Blended FV $21.10 = +6.44% CAGR ≈ +20.6% total 3 ปี (สมเหตุสมผลที่ entry zone แต่ยังต่ำกว่า S&P Good target + binary tail risk)",
    positionSize: "0% — FAIL Growth conviction gate (avg 4.83 < 6.5) + FAIL Growth MOS Gate 0/2 (Bear-reconciled: Method 1 Reverse DCF implied heroic near-term execution; Method 2 P/B 4.5x ~90th pctile + fwd P/E 19.2x top of managed-care range) + absolute MOS -29.6% + **Regime TRANSITIONAL-CAUTIOUS → Force Deploy SUSPENDED, ห้าม open new position ทั้งหมด** (Atlas judgment override — US strikes on Iran 8/31, Fed 25bp hike priced Sept FOMC). Beta 2.38 + regulatory binary + thin volatile margin = profile ที่ regime TC penalize หนักที่สุด",
    keyThesis: "Oscar Health = full-stack tech-enabled health insurer, pure-play ACA individual marketplace (98% net premium), ~100% revenue พึ่ง federal subsidy framework. **Execution outlier จริง** — เจอ 'market reset' ก่อนคู่แข่งตั้งแต่ 2025 (FY2025 op loss -$396M), re-priced aggressive สำหรับ 2026, กำลังเก็บ benefit ของ favorable pricing year ขณะที่ CNC/MOH/ELV เพิ่งโดน cost shock (net loss TTM). Q2 2026 MLR 79.2% (vs 91.1% YoY), swung to GAAP profit, raised FY2026 earnings-from-ops guide $500-700M, gaining ACA share 6.3% → 9.2% ใน 2 ปี. Positive outlier ใน sub-sector ที่กำลังแย่. **แต่** ที่ราคา $29.96 (fwd P/E ~19x, P/B 4.5x = 2-3 เท่าของ insurer ปกติ) ราคา price-in benign subsidy outcome + beat-management-target execution โดยไม่มี margin of safety — ในขณะที่ **enhanced premium tax credits หมดอายุจริงแล้ว 1 ม.ค. 2026** (Senate S.3385 failed ธ.ค. 2025; House ผ่านร่าง 3 ปี ม.ค. 2026 stalled Senate; CARE Act 2-yr compromise unvoted; 'do nothing' default = bearish; midterm พ.ย. 2026 = forcing catalyst). Triple-gate fail: Conviction 4.83 < 6.5 + Growth MOS Gate FAIL 0/2 + MOS -29.6% (เหมือน CHYM 2026-08-31). **8th consecutive 'priced-for-perfection' NO-DEPLOY** (MU/CRCL/ADI/MELI/GCT/CHYM/ZETA→OSCR) — เพิ่ม dimension = explicit legislative binary. **ไม่ใช่ hard AVOID** — GAAP-profitable + net cash (float) + raised guide + genuine share gains = downside floor จริง. 'Great execution, wrong price, unresolved legislative binary, wrong macro window.' **ถ้า regime flip กลับ RISK-ON — ยังไม่ใช่ BUY** (ทุก gate เป็น regime-independent)",
    topRisk: "ACA subsidy legislation binary (UNRESOLVED) — enhanced PTCs หมดอายุ 1 ม.ค. 2026, Senate ไม่ต่อ, CARE Act stalled, 'do nothing' default = bearish. Single largest driver ของ thesis. Scenario tree: (a) no clean extension / cliff ~37% → FV $7-14 (2027 rev -25-30%, MLR 84-86%, operating deleverage บน pure-play ACA); (b) CARE Act 2-yr w/ guardrails ~41% → FV $23-28; (c) clean multi-yr extension ~17% → FV $40-48. Bear P-W EV $19.50 (MOS -34.9%). Sensitivity Matrix (2027 rev Δ × normalized op margin): 4/25 cells (16%) justify $29.96 — ต้องการ flat-or-growing 2027 revenue AND op margin ≥ 5.5% (peak) AND multiple ≥ 13x พร้อมกัน. เพิ่มความเสี่ยง: P&L cyclicality (op margin -4% → +0.6% → -3.4% → +4.1% ใน 4 ปี; MLR 6M 2026 75% ต่ำกว่า 80% floor = favorable peak + rebate risk); Florida 57.8% membership concentration; premium-to-surplus 7.4x (thin capitalization); risk-adj payable $4.94B = 54% ของ liabilities; beta 2.38 + regime TC; dual-class governance (Kushner/Schlosser ~75% voting) + political-conflict optics",
    reportFile: "../reports/OSCR_2026-09-01.md",
    businessSummary: {
      oneLiner: "ประกันสุขภาพรายบุคคลผ่าน ACA marketplace — full-stack tech-enabled insurer ที่รายได้ ~100% พึ่ง federal subsidy framework; กำไร = premium − claims (MLR)",
      analogy: "เหมือน neo-insurer (tech-first) ที่ขายประกัน Obamacare ให้คนที่ไม่มีประกันจากนายจ้าง — รัฐบาลจ่าย subsidy ตรงให้ Oscar; ถ้า subsidy หด ลูกค้าหาย",
      moneyFlow: [
        "Premium รายเดือนจาก >2.0M สมาชิก ACA marketplace (98% ของ revenue) — รัฐบาลกลางจ่าย APTC ตรงให้ Oscar แทนสมาชิกส่วนใหญ่",
        "กำไร = premium ที่เก็บ − ค่ารักษา (claims); MLR = claims/premium; ถ้า MLR < 80% ต้องคืนเงิน (rebate) ตามกฎ ACA",
        "Risk-adjustment transfers ผ่าน CMS — Oscar จ่ายออก (payable $4.94B) เพราะ risk pool ค่อนข้างสุขภาพดี",
        "+Oscar (B2B) — license เทคโนโลยี (claims platform, Campaign Builder) ให้ payor/provider รายอื่น (~2%, margin สูงกว่า, ไม่แบก insurance risk)",
        "Oscar Medical Group — telehealth / virtual primary care ลด claims cost",
        "เงินสด + investments $10.2B — float หนุน policyholder reserves + risk-adj payable (ไม่ใช่ excess cash); investment income จาก rate สูง"
      ],
      whyDifferent: "tech-driven admin-cost advantage → gaining ACA share (6.3% → 9.2% ใน 2 ปี); เจอ market-reset ก่อนคู่แข่ง (2025) → favorable pricing year ขณะ CNC/MOH/ELV โดน cost shock; ICHRA early-mover (employer-funded individual coverage = structural offset ต่อ subsidy cliff); +Oscar B2B optionality — แต่ทั้งหมดยัง contingent",
      simpleRisk: "รายได้ ~100% พึ่ง ACA marketplace + federal subsidy — enhanced premium tax credits หมดอายุจริงแล้ว 1 ม.ค. 2026, Congress ยัง stalled, 2026 enrollment แล้ว -21-26%. Pure-play (ไม่มี Medicaid/MA buffer). P&L ผันผวนสุดขั้ว (op margin -4% ถึง +4% ใน 4 ปี), MLR 6M 2026 75% = favorable peak จะ normalize ขึ้น, P/B 4.5x แพงมากสำหรับ insterr, Florida 57.8% ของสมาชิก, beta 2.38"
    },
    thesisBullets: [
      { title: "ACA subsidy binary — UNRESOLVED, 'do nothing' default = bearish", why: "enhanced premium tax credits หมดอายุจริงแล้ว 1 ม.ค. 2026 (ไม่ใช่ความเสี่ยงอนาคต). Senate S.3385 failed ธ.ค. 2025; House ผ่านร่าง 3 ปี 230–196 (8 ม.ค. 2026) แต่สมาชิกยอมรับ 'likely to fail Senate'; CARE Act 2-yr compromise (income cap 700% FPL + $25 min premium) unvoted/unsigned. Government shutdown 43 วัน จบโดยไม่ต่อ. Midterm พ.ย. 2026 = political forcing catalyst. Scenario: cliff ~37% → FV $7-14 / CARE Act ~41% → $23-28 / clean ext ~17% → $40-48" },
      { title: "ราคา price-in benign outcome — P/B 4.5x, fwd P/E 19x", why: "insurer ปกติ trade 1-2x P/B; OSCR 4.5x = premium 125-200% vs sub-sector median. Through-cycle ROE 16-18% → justified P/B 1.2-2.1x (Gordon). Favorable-year ROE 26.8% = leverage artifact (premium-to-surplus 7.4x = thin capitalization). Justified normalized P/E ~11-13x (base). Beta 2.38 → Ke ~16.5% = mechanical reason ที่ต้อง trade low multiple. 4/25 sensitivity cells justify ราคา" },
      { title: "TTM = favorable-MLR peak, cherry-picked", why: "MLR 6M 2026 = 75.0% (ต่ำกว่า ACA 80% floor → rebate risk + H2 catch-up); FY2026 guide MLR 81.5-82.5% = normalize กลับขึ้น. Op margin 4 ปีล่าสุด: -4.02% → +0.62% → -3.39% → +4.11% = extreme cyclicality — management ไม่เคยพิสูจน์ว่า hit through-cycle target 5% ได้" },
      { title: "Pure-play ACA — เปราะบาง, concentrated, leveraged", why: "98% net premium = ACA individual; zero Medicaid/MA diversification → operating-deleverage tail หนักกว่า diversified peers เมื่อ enrollment หด. Florida = 57.8% ของสมาชิก (single-state single-point-of-failure); top-3 states 86%. Equity เพียง $2.05B หนุน revenue $15.3B; risk-adj payable $4.94B = 54% ของ liabilities" },
      { title: "Regime TC + beta 2.38 = worst-case profile + Street 'Hold'", why: "Regime TRANSITIONAL-CAUTIOUS (Force Deploy suspended); Fed 25bp hike priced Sept FOMC; beta 2.38 (สูงสุดในกลุ่ม peer) + thin volatile margin + regulatory-binary = profile ที่ regime TC penalize หนักสุด. Street rating 'Hold' (ไม่ใช่ Buy), avg PT $30.57 — ทุก PT ถูกยกขึ้นหลังหุ้นวิ่ง (herding to price). Kelly 0% ทุก fraction, Forward Sharpe 0.20 < S&P 0.30. 8th consecutive priced-for-perfection NO-DEPLOY" }
    ],
    esgBreakdown: { e: 8, s: 4.5, g: 3, overall: 4.8 },
    esgBreakdownNote: "Reconciled จาก report §🌱 (Emma / Bear → Reconciled): Environmental 8 / 8 → 8 (health insurer, direct footprint ต่ำ, immaterial). Social 5 / 4-5 → 4.5 (positive: mission = affordability/access; negative: claims-denial / prior-auth scrutiny post-UNH environment, member-complaint history, narrow networks, aggressive membership growth ในตลาด subsidized = 'growth at what cost' + adverse-selection; impact -3%). Governance 3 / 3 → 3 (dual-class — Class B 20 votes/share, Thrive Capital [Josh Kushner] + co-founder Schlosser ~75% voting; political-conflict optics — Kushner family ties ↔ federal healthcare policy ที่ขับ ~100% revenue; CMS risk-adj methodology risk [$4.94B payable]; data privacy/cyber ของ 2.0M members' health data [Emma พลาด, Bear จับ]; offset: Bertolini ex-Aetna CEO = governance positive, board refreshed 2026; impact -5% ถึง -6%). Overall 4.95 / ~3.5 → 4.8/10 (MEDIUM-HIGH RISK). Total valuation overlay -9% (Emma -8% / Bear -10%) → ESG-adj Blended FV $19.20 → MOS -35.9%. ESG = legitimate materiality — governance discount (political-entanglement + dual-class) เป็นเหตุผลจริงที่ investors เรียก multiple discount",
    customerConcentration: {
      note: "ไม่มี single commercial customer — DTC insurer, revenue = premium จาก 2.96M individual members (Q2 2026). **De facto single point of failure: ~100% dependency ต่อ ACA marketplace + federal subsidy framework** (APTC pass-through + risk-adjustment via CMS; enhanced PTC หมดอายุ 1 ม.ค. 2026). ⚠️ flag > 20% — treat 'ACA policy' = single customer. State-level: Florida 1,179,934 (57.8%) / Texas 358,910 (17.6%) / Georgia 218,746 (10.7%) / other ~17 states ~13.9% (SEC 10-K FY2025). ไม่มี Medicaid/MA diversification (ต่างจาก CNC/ELV/MOH)"
    },
    geographyRevenue: {
      unitedStates: "100% — pure US ACA individual marketplace; ไม่มี geopolitical/FX/China exposure (relative positive ใน regime TC)",
      international: "0%",
      china: "0% — แต่ intra-US state concentration HIGH: Florida = 57.8% ของสมาชิก = single-state single-point-of-failure (rate review, market-exit rules, state exchange decisions)"
    },
    revenueSegments: [
      { label: "Net premium — ACA individual marketplace + small-group", value: 98 },
      { label: "+Oscar B2B platform licensing + Oscar Medical Group", value: 2 }
    ],
    revenueSegmentsNote: "TTM: Net Premium $15,041M (98% ของ revenue $15,319M) / +Oscar B2B + Oscar Medical Group ~2%. +Oscar B2B = higher-margin, ไม่แบก insurance risk — แต่ยัง unproven scale (ไม่ใช่ reportable segment). MLR (medical loss ratio) เป็น P&L driver หลัก — 6M 2026 = 75.0%, FY2026 guide 81.5-82.5%",
    competitorData: [
      { ticker: "OSCR", company: "Oscar Health (subject)", revenueGrowth: 42.8, operatingMargin: 4.11, marketCap: 9240 },
      { ticker: "CNC", company: "Centene (Ambetter — #1 ACA individual)", revenueGrowth: 12.9, operatingMargin: 1.86, marketCap: 31784, strengths: "scale มหาศาล (~$160B revenue), diversified (Medicaid + MA + ACA), historically P/E 10-12x, ACA leadership via Ambetter", weaknesses: "TTM net margin -2.83% (loss) — MLR blowout; slow-moving; ACA leadership = exposure ไม่ใช่ moat ตอนนี้", threatLevel: "HIGH" },
      { ticker: "MOH", company: "Molina Healthcare", revenueGrowth: 1.8, operatingMargin: 0.70, marketCap: 10376, strengths: "~$40B revenue, government-focused, long profit track record, disciplined underwriting", weaknesses: "net margin -0.02% (near breakeven) — เพิ่งโดน cost shock; growth +1.8% เท่านั้น", threatLevel: "MEDIUM" },
      { ticker: "ELV", company: "Elevance Health", revenueGrowth: 6.3, operatingMargin: 3.79, marketCap: 85130, strengths: "large diversified managed care ($199B revenue), net margin +2.47%, P/E 10-14x, brand (Blues licensee)", weaknesses: "Health Benefits op margin 5.0% → 3.6% YoY (จุดชนวน sector selloff); slow growth +6.3% — OSCR normalized op margin จะ 'ใกล้ ELV' ไม่ dominant", threatLevel: "MEDIUM" },
      { ticker: "ALHC", company: "Alignment Healthcare (Medicare Advantage insurtech)", revenueGrowth: 37.2, operatingMargin: 1.22, marketCap: 2780, strengths: "closest growth comp (+37.2%), insurtech model, recently profitable (net margin +0.89%)", weaknesses: "Medicare Advantage (ต่าง sub-market จาก OSCR's ACA); op margin 1.22% thin; small ($2.78B); ไม่ได้ premium P/B แบบ OSCR", threatLevel: "LOW-MEDIUM" }
    ],
    bullFlipTriggers: [
      "Multi-year (≥3yr) clean ePTC extension signed into law — ไม่มี $25 min premium, ไม่มี aggressive FPL cap → base case shift, FV → $28-32",
      "2027 open-enrollment actuals (ธ.ค. 2026 – ม.ค. 2027): Oscar membership decline ≤ 5% YoY (vs -15-25% feared) → ICHRA + share gains offset cliff เป็นจริง",
      "ราคา ≤ $18-20 — MOS ≥ 15% บน Blended FV + Kelly turns positive + downside-protected",
      "Sept 16 Investor Day: FY2027 guide op margin ≥ 5.0% AND H2 2026 MLR ≤ 82% → through-cycle margin structural, justify 13x",
      "+Oscar B2B disclosed เป็น reportable segment ที่ ≥ $500M revenue run-rate + ≥ 20% operating margin → real software moat, re-rate justified"
    ],
    bearFlipTriggers: [
      "ไม่มี ePTC legislation ผ่านเป็นกฎหมายภายใน Nov 1, 2026 (เริ่ม 2027 open enrollment) → full-cliff probability → FV → $12-15",
      "H2 2026 MLR prints > 86% (CNC/ELV-style cost shock) → re-pricing discipline ล้มเหลว → FV → $13-16",
      "2027 membership guidance (Sept 16 Investor Day หรือ Q3 call) implies ≥ 15% enrollment decline → revenue deleverage → FV → $14",
      "MLR rebate accrual หรือ risk-adjustment payable dispute/restatement ตัด FY2026 net income > 15%",
      "Florida regulatory action — mandated rate cut / market-conduct action (57.8% membership exposure)"
    ],
    thesisInvalidation: "Oscar posts a GAAP operating loss ในไตรมาสใดๆ ของ FY2026-2027 แม้เป็น favorable 2026 pricing year → premise 'MLR discipline เป็น structural' ผิด → กลับสู่ pre-2025 volatility, P/B 4.5x invalidated ทั้งหมด → FV → book ~$7 → re-analysis required. OR (upside invalidation): clean permanent ePTC extension + Oscar sustains > 5% op margin 4+ ไตรมาสติดต่อกัน → bear thesis (policy-binary + not-structural-growth) ผิดทางบวก → re-rate $35+ → re-analysis required",
    unitEconomics: {
      ruleOf40: "N/A — insurer ไม่ใช้ Rule of 40 (SaaS metric). Insurer-relevant: MLR 6M 2026 75.0% / FY guide 81.5-82.5%; SG&A ratio ต่ำกว่า legacy Blues (tech advantage); combined ratio ~96-100% through-cycle",
      nrr: "N/A — ACA re-shop ทุก open enrollment, switching cost ~0",
      ltvCac: "N/A",
      cacPayback: "N/A",
      sbcPctRevenue: "0.49% (SBC TTM $75.2M) — LOW, DCF Cash Flow Consistency Rule ไม่ยิง",
      note: "Membership 2,963,002 Q2 2026 (~2.96M, +46% YoY, Atlas-corrected); ACA share 6.3% → 9.2% ใน 2 ปี (gaining, แต่ total-market pie หด -21-26%). Premium-to-surplus 7.4x (vs normal insurer 3-5x = thin capitalization); equity multiplier 5.46x; through-cycle ROE 16-18% (favorable-year 26.8% = artifact). risk-adjustment payable $4.94B = 54% ของ total liabilities. ความเสี่ยง = policy binary + P&L cyclicality + valuation — ไม่ใช่ accounting fraud"
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

    if 'ticker: "OSCR"' in content:
        print("OSCR entry already exists in data.js — aborting to avoid duplicate.")
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
    print("OSCR entry inserted. LAST_UPDATED =", NEW_LAST_UPDATED)


if __name__ == "__main__":
    main()
