// ─── THESIS WATCH DATA ───────────────────────────────────
// Managed by Max/Charlie · Thesis health-check for OPEN positions
// อัปเดตแบบ ad-hoc เมื่อมี portfolio review หรือ CIO ขอทบทวน thesis — ไม่ใช่ scheduled job
// อ้างอิง Bear Flip Triggers / Thesis Invalidation จาก reports/ ต้นฉบับของแต่ละ ticker
// currentPrice / MOS / Conviction / Return ดึงสดจาก PORTFOLIO.positions ตอน render — ไม่ duplicate ตัวเลขไว้ที่นี่ (Single Source of Truth)

const THESIS_WATCH_LAST_UPDATED = "2026-11-24"; // roster cleanup only (ลบตำแหน่งที่ exit แล้ว 3 ตัว) — เนื้อหา entry ที่เหลือยังอิง lastReviewDate ของแต่ละตัว (2026-08-09) ไม่ได้ review ใหม่

const THESIS_WATCH = [
  {
    ticker: "REGN",
    healthStatus: "WATCH",
    reportFile: "reports/REGN_2026-06-03.md",
    bearFlipTriggers: [
      { trigger: "IRA เลือก Dupixent เข้า Medicare negotiation FY2027 (ประกาศ Q4 2026)", status: "WATCH", note: "⚠️ Binary overhang ตัวใหญ่สุดของ position — ยังไม่ประกาศผล ถ้าเลือก Dupixent = valuation reset -20-30% ทันที" },
      { trigger: "Eylea revenue ลดลง >50% YoY 2 ไตรมาส", status: "NOT_FIRED", note: "ไม่มีข้อมูลบ่งชี้" },
      { trigger: "Dupixent COPD penetration <5% ที่ 6 เดือน", status: "NOT_FIRED", note: "Dupixent +38% YoY โดยรวม (บวก)" },
      { trigger: "Sanofi ประกาศ strategic review หรือ profit warning", status: "NOT_FIRED" },
      { trigger: "Fianlimab และ Linvoseltamab pipeline ล้มเหลวทั้งคู่", status: "NOT_FIRED", note: "ไม่มีรายงานความล้มเหลว" },
    ],
    thesisInvalidation: [
      { criteria: "IRA หั่นราคา Dupixent 40%+ พร้อม pipeline หลัก 2 ตัวล้มเหลว", status: "NOT_MET" },
      { criteria: "JAK inhibitors ครองส่วนแบ่งตลาด AD 40% ภายในปี 2029", status: "NOT_MET", note: "long-horizon, ยังประเมินไม่ได้ตอนนี้" },
      { criteria: "CEO Schleifer ลาออกโดยไม่มีแผนสืบทอด", status: "NOT_MET" },
    ],
    verdict: "ไม่มี trigger ไหนยิงจริง fundamentals ยังแข็งแกร่ง (Health Canada อนุมัติ Libtayo ใหม่, Guggenheim ปรับ PT ขึ้น) แต่ MOS หดเหลือใกล้ 0% แล้ว (valuation ตึงมาก) และ IRA Q4 2026 decision คือความเสี่ยง binary ตัวใหญ่สุดที่ยังไม่คลี่คลาย",
    nextCatalyst: "IRA Medicare negotiation announcement (Q4 2026) — ตัวชี้ขาดสำคัญสุดของทั้ง position ถ้าไม่เลือก Dupixent = thesis ยืนยันแข็งแกร่งขึ้นอีก",
    lastReviewDate: "2026-08-09",
  },
  {
    ticker: "NOW",
    healthStatus: "WATCH",
    reportFile: "reports/NOW_2026-05-11.md",
    bearFlipTriggers: [
      { trigger: "Revenue growth <15% YoY 2 ไตรมาสติด", status: "NOT_FIRED", note: "Subscription revenue ยังโต +23% YoY" },
      { trigger: "IT budget freeze: hyperscaler customer ≥3 รายตัดสัญญาต่อ", status: "NOT_FIRED", note: "ไม่มีข้อมูลยืนยัน" },
      { trigger: "Microsoft Copilot Studio ชนะดีล ITSM ใหญ่แทน NOW", status: "NOT_FIRED" },
      { trigger: "SBC สูงกว่า 18% ของ revenue", status: "NOT_FIRED", note: "ไม่มีข้อมูลชัดเจน" },
      { trigger: "Gross margin หลุดต่ำกว่า 74%", status: "WATCH", note: "⚠️ Gross margin ปัจจุบัน 74.77% — ใกล้ threshold มาก ควรจับตา" },
    ],
    thesisInvalidation: [
      { criteria: "Revenue growth หลุดต่ำกว่า 10%", status: "NOT_MET", note: "ยังโต +23%" },
      { criteria: "Microsoft bundle ITSM ฟรีใน M365 Enterprise", status: "NOT_MET" },
      { criteria: "CEO Bill McDermott ลาออก", status: "NOT_MET", note: "ยังไม่ลาออก แต่เตือนเรื่อง headcount cut เพิ่มอีก ~700 ตำแหน่งก่อนสิ้นปี" },
    ],
    verdict: "ไม่มี Bear Flip ยิง (fundamentals แข็งแกร่ง) — ปัญหาหลักคือ valuation ไม่ใช่ fundamentals: ราคาทะลุ Blended FV $121.45 แล้ว (MOS -2.82%, STRONG SELL territory ครั้งแรกในพอร์ต) DECISION 2026-08-09: HOLD ไม่ trim เพราะ weight เล็ก (2.45%) + FV อาจ stale (ไม่ re-verify มา ~3 เดือน) Gross margin 74.77% ใกล้ threshold 74% ควรจับตาเพิ่ม. **DECISION 2026-11-25 (CIO-ordered stop-loss breach review, portfolio/decisions.md): HOLD ต่อ — stop-loss ($93.00) breach 5 เซสชัน (11-18→11-23) แต่ narrows ชัดจาก -5.80%→-1.42%, 0/4 Thesis Invalidation, 1/5 Bear Flip (gross margin), position de minimis (0.9-1.4% weight) — ไม่คุ้มรัน full pipeline. Mandatory re-trigger: ถ้า stopDist กลับไปต่ำกว่า -5% อีก หรือยัง breach อยู่ตอน quarterly review 2026-12-31 → ต้อง full pipeline + Charlie consult ทันที ไม่มีข้อยกเว้นซ้ำ.**",
    nextCatalyst: "ส่ง Emma/Charlie re-verify Blended FV รอบวิเคราะห์ถัดไป (ค้างมา ~3 เดือนแล้ว) + จับตา gross margin trend + ติดตาม stopDist ตาม re-trigger condition 2026-12-31",
    lastReviewDate: "2026-11-25",
  },
  {
    ticker: "CRM",
    healthStatus: "INTACT",
    reportFile: "reports/CRM_2026-05-29.md",
    bearFlipTriggers: [
      { trigger: "Revenue growth <5% YoY 2 ไตรมาสติด", status: "NOT_FIRED", note: "Q1 FY27 +13% YoY" },
      { trigger: "Agentforce ARR growth หลุดต่ำกว่า 50% YoY", status: "NOT_FIRED", note: "Agentforce ARR +205% YoY" },
      { trigger: "ROIC หลุดต่ำกว่า 5%", status: "WATCH", note: "ROIC ปัจจุบัน 6.3% < WACC — จุดอ่อนที่ทีมเฝ้าระวังอยู่แล้ว แต่ยังไม่ถึง threshold 5%" },
      { trigger: "NRR หลุดต่ำกว่า 100%", status: "NOT_FIRED", note: "ไม่มีข้อมูลยืนยันปัญหา" },
      { trigger: "Microsoft แย่งส่วนแบ่งตลาด CRM ≥3% ภายใน 12 เดือน", status: "NOT_FIRED" },
    ],
    thesisInvalidation: [
      { criteria: "Revenue YoY ติดลบ", status: "NOT_MET" },
      { criteria: "FCF หลุดต่ำกว่า $8B (จาก $14.4B)", status: "NOT_MET", note: "FCF ยังคง $14.4B" },
    ],
    verdict: "Thesis intact บัฟเฟอร์กว้าง (MOS +30.92%) จุดอ่อนเดียวที่ต้องเฝ้าระวังคือ ROIC 6.3% < WACC (ยังห่างจาก Bear Flip threshold 5%) Executive reshuffle (Tallapragada→advisor, Milano→COO) เป็น governance noise ไม่ใช่ trigger — ตลาดตอบรับบวกหลัง reassess",
    nextCatalyst: "Q2 FY27 earnings (26 ส.ค. 2026) — จับตา ROIC trend และ Agentforce ARR momentum ต่อเนื่อง",
    lastReviewDate: "2026-08-09",
  },
  {
    ticker: "ADBE",
    healthStatus: "INTACT",
    reportFile: "reports/ADBE_2026-05-09.md",
    bearFlipTriggers: [
      { trigger: "Revenue growth ≤8% YoY 2 ไตรมาสติด (AI cannibalization)", status: "NOT_FIRED" },
      { trigger: "Canva/Google ชนะ RFP enterprise Fortune 500 ≥3 ครั้งใน 12 เดือน", status: "NOT_FIRED" },
      { trigger: "FCF margin หลุดต่ำกว่า 35%", status: "NOT_FIRED", note: "FCF margin 42%" },
      { trigger: "DOJ/EU เปิดการสอบสวน antitrust ใหม่", status: "NOT_FIRED" },
      { trigger: "CEO Narayen ลาออกโดยไม่มีแผนสืบทอด", status: "NOT_FIRED", note: "การลาออกเป็น planned transition มีผู้สืบทอดชัดเจน — ไม่เข้าเกณฑ์ trigger" },
    ],
    thesisInvalidation: [
      { criteria: "Firefly ไม่ถึง $200M revenue ภายใน Q2 FY2027", status: "NOT_MET", note: "รอข้อมูลติดตาม" },
      { criteria: "Creative Cloud subscribers ลดลง (absolute) 2 ไตรมาสติด", status: "NOT_MET" },
      { criteria: "ประกาศ M&A ที่ไม่ synergistic ≥$10B", status: "NOT_MET" },
    ],
    verdict: "Thesis intact ไม่มี trigger ไหนใกล้ยิง CEO succession จัดการเรียบร้อย (planned, ไม่ใช่ crisis exit) — ต่างจาก INTU ที่เคย auto-sell ก่อนหน้า CFO Dan Durn ลาออก (มิ.ย.) เพิ่ม governance noise แต่ไม่ใช่ trigger ที่กำหนดไว้",
    nextCatalyst: "Q3 FY2026 earnings (คาด ~10 ก.ย. 2026) — จับตา Firefly ARR progress",
    lastReviewDate: "2026-08-09",
  },
  {
    ticker: "ADSK",
    healthStatus: "INTACT",
    reportFile: "reports/ADSK_2026-06-09.md",
    bearFlipTriggers: [
      { trigger: "Revenue growth <12% YoY 2 ไตรมาสติด", status: "NOT_FIRED", note: "Q1 FY27 +18.4% YoY กำลังเร่งขึ้น" },
      { trigger: "ARR growth ชะลอต่ำกว่า 10%", status: "NOT_FIRED" },
      { trigger: "คู่แข่ง AI เปิดตัว BIM/CAD ฟรี/ถูก ที่ AEC market >15% adoption", status: "NOT_FIRED" },
      { trigger: "NRR หลุดต่ำกว่า 100%", status: "NOT_FIRED" },
      { trigger: "อัตราดอกเบี้ย 'higher for longer' ต่อเนื่องถึง FY2028", status: "WATCH", note: "Fed ยังคงอัตรา 3.50-3.75% ต่อเนื่อง — เป็นความเสี่ยง macro ระยะยาวที่ต้องติดตาม ไม่ใช่ trigger เฉพาะตัวบริษัท" },
    ],
    thesisInvalidation: [
      { criteria: "Subscription churn พุ่ง >5% ต่อปี", status: "NOT_MET" },
      { criteria: "EU Open BIM mandate บังคับย้ายออกจาก DWG format ≥30% ของ revenue base", status: "NOT_MET" },
      { criteria: "AI tool ฟรีคุณภาพสูงถูกใช้เป็น primary workflow โดยบริษัท AEC รายใหญ่", status: "NOT_MET" },
      { criteria: "Scandal ผู้บริหาร / บัญชีผิดปกติ / hostile M&A", status: "NOT_MET", note: "MaintainX เป็น planned acquisition ปิดดีลสำเร็จ — ยืนยัน thesis ไม่ใช่บั่นทอน" },
    ],
    verdict: "แข็งแกร่งสุดในพอร์ต ไม่มี trigger ไหนใกล้ยิงเลย MaintainX integration ปิดดีลสำเร็จยืนยัน FCF-inflection thesis แทนที่จะเป็นความเสี่ยง ความเสี่ยงเดียวที่เหลือคือ macro-level (rates higher for longer) ไม่ใช่ปัญหาเฉพาะบริษัท",
    nextCatalyst: "Q2 FY27 earnings (27 ส.ค. 2026) — จับตา MaintainX integration progress + ARR momentum",
    lastReviewDate: "2026-08-09",
  },
];
