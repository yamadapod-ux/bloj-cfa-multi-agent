// ─── THESIS WATCH DATA ───────────────────────────────────
// Managed by Max/Charlie · Thesis health-check for OPEN positions
// อัปเดตแบบ ad-hoc เมื่อมี portfolio review หรือ CIO ขอทบทวน thesis — ไม่ใช่ scheduled job
// อ้างอิง Bear Flip Triggers / Thesis Invalidation จาก reports/ ต้นฉบับของแต่ละ ticker
// currentPrice / MOS / Conviction / Return ดึงสดจาก PORTFOLIO.positions ตอน render — ไม่ duplicate ตัวเลขไว้ที่นี่ (Single Source of Truth)

const THESIS_WATCH_LAST_UPDATED = "2026-08-09";

const THESIS_WATCH = [
  {
    ticker: "ACN",
    healthStatus: "FIRING",
    reportFile: "reports/ACN_2026-06-05.md",
    bearFlipTriggers: [
      { trigger: "Revenue growth <5% YoY 2+ ไตรมาสติด", status: "FIRED", note: "FY26 guide หั่นเหลือ 3-4% (Q3 FY26, June18)" },
      { trigger: "Bookings หลุดต่ำกว่า $18B/ไตรมาส", status: "FIRED", note: "Bookings -13% sequential" },
      { trigger: "EBIT margin หลุดต่ำกว่า 14%", status: "NOT_FIRED", note: "Margin ขยายเป็น 17% แล้ว" },
      { trigger: "Hyperscaler bundling แทนที่ ACN ในวงกว้าง", status: "NOT_FIRED", note: "ไม่มีข้อมูลยืนยัน" },
      { trigger: "FCF guidance ถูกหั่นอย่างมีนัยสำคัญ", status: "NOT_FIRED", note: "FCF $3.6B ยังแข็งแกร่ง" },
    ],
    thesisInvalidation: [
      { criteria: "บุ๊กกิ้งลดติดต่อกัน 3 ไตรมาส + revenue growth <4%", status: "PARTIAL", note: "มีแล้ว 1 ใน 3 ไตรมาสที่ต้องการ" },
      { criteria: "เลิกจ้าง >10% ของพนักงานที่อ้างเหตุผล AI", status: "NOT_MET" },
      { criteria: "ลูกค้ารายใหญ่ (>3% revenue) ยกเลิกสัญญาไปหา AI alternative", status: "NOT_MET" },
    ],
    verdict: "2 ใน 5 Bear Flip Triggers ยิงแล้ว (revenue + bookings) — เป็นเหตุผลที่ trim 50% ไปแล้วเมื่อ 2026-06-22. Thesis Invalidation ต้องการบุ๊กกิ้งลดติดกัน 3 ไตรมาส ตอนนี้มีแค่ 1 ไตรมาส — ตำแหน่งเสี่ยงสุดของพอร์ตตอนนี้",
    nextCatalyst: "Q4 FY26 earnings (คาด ~ก.ย. 2026) — ตัวชี้ขาดว่าจะครบเงื่อนไข Thesis Invalidation (exit เต็มรูปแบบ) หรือบุ๊กกิ้งเริ่มทรงตัว",
    lastReviewDate: "2026-08-09",
  },
  {
    ticker: "GOOGL",
    healthStatus: "WATCH",
    reportFile: "reports/GOOGL_2026-05-21.md",
    bearFlipTriggers: [
      { trigger: "DOJ สั่ง structural separation (Chrome/Android/Search)", status: "NOT_FIRED", note: "ยังไม่มีคำสั่ง อยู่ระหว่าง remedies phase" },
      { trigger: "Cloud growth <25% YoY 2 ไตรมาส", status: "NOT_FIRED", note: "Cloud เร่งขึ้นเป็น +82% YoY (Q2 2026)" },
      { trigger: "CapEx ยืนยัน >$85B FY2026 โดยไม่มี plateau guidance", status: "WATCH", note: "⚠️ CapEx guide ปัจจุบัน $195-205B ทะลุ threshold เดิมไปไกลมาก — threshold เดิมตั้งไว้ต่ำเกินไปเทียบกับที่เกิดจริง แต่ Cloud growth offset ไว้จึงยังไม่ประกาศยิงอย่างเป็นทางการ" },
      { trigger: "Search market share ยืนยันต่ำกว่า 87%", status: "NOT_FIRED", note: "ไม่มีข้อมูลยืนยัน" },
      { trigger: "Apple distribution deal ถูกยกเลิก", status: "NOT_FIRED", note: "ตรงข้าม — WWDC ยืนยัน Siri 2.0 ใช้ Gemini เสริมความสัมพันธ์" },
    ],
    thesisInvalidation: [
      { criteria: "Chrome/Android ถูกสั่ง divest", status: "NOT_MET" },
      { criteria: "Search revenue ลดลง YoY 3 ไตรมาสติด", status: "NOT_MET", note: "Search ยังโตต่อเนื่อง" },
      { criteria: "GCP operating margin หลุดต่ำกว่า 20%", status: "NOT_MET", note: "ไม่มีข้อมูลชัดเจน แต่ Cloud growth แข็งแกร่ง" },
      { criteria: "CapEx >$100B/ปี ต่อเนื่อง (sustained)", status: "WATCH", note: "⚠️ $195-205B guide ทะลุ threshold นี้ไปแล้วเช่นกัน — ควร re-calibrate threshold เดิมที่ตั้งไว้ตั้งแต่พ.ค. ให้สอดคล้องกับ AI capex era ปัจจุบัน" },
    ],
    verdict: "CapEx guide ($195-205B) ทะลุทั้ง Bear Flip threshold (>$85B) และ Thesis Invalidation threshold (>$100B) ที่ตั้งไว้เดิมไปไกลมาก — ทีมยังไม่เคยประกาศยิงอย่างเป็นทางการเพราะ Cloud growth +82% ยัง offset ไว้ แต่ threshold เดิมน่าจะหลวมเกินไปเทียบกับสภาพตลาดปัจจุบัน (ทุก mega-cap AI capex วิ่งเกิน $100B แล้ว) ✅ Q2 beat (Cloud +82%, EPS $9.11 record) ยืนยัน core thesis แต่ 🔴 ความเสี่ยงใหม่ที่ไม่มีใน trigger list เดิม — AI talent exodus (Jeff Dean/Hassabis exit 5-6 ส.ค.) กัดกร่อน AI-model-leadership narrative แม้ยังไม่ถึงระดับ Invalidation",
    nextCatalyst: "Bear/Quinn ควร re-calibrate CapEx threshold ให้ทันยุค AI capex ปัจจุบัน (threshold เดิมล้าสมัยไปแล้ว) + จับตา Q3 2026 earnings ว่า Cloud growth ยังคง offset capex concern ได้ต่อเนื่องหรือไม่",
    lastReviewDate: "2026-08-09",
  },
  {
    ticker: "RDDT",
    healthStatus: "WATCH",
    reportFile: "reports/RDDT_2026-05-30.md",
    bearFlipTriggers: [
      { trigger: "DAU growth <10% YoY 2 ไตรมาสติด", status: "WATCH", note: "US DAU +6% YoY เป็นไตรมาสแรกแล้ว (Q2 2026) — ต้องรอไตรมาสหน้ายืนยันว่าจะครบ 2 ไตรมาสติดหรือไม่ (Intl DAU +28% ยังแรงมาก offset)" },
      { trigger: "ARPU growth <20% YoY", status: "NOT_FIRED", note: "Global ARPU +36% YoY ห่างไกลเกณฑ์มาก" },
      { trigger: "Google AI Overview ลด traffic วัดได้ >15%", status: "WATCH", note: "Management เตือน 'search referrals choppy' — ยังเป็น qualitative ไม่ถูก quantify >15% ตามเกณฑ์" },
      { trigger: "Meta Forum DAU ทะลุ 50M ภายใน 18 เดือน", status: "NOT_FIRED", note: "ไม่มีข้อมูลยืนยัน" },
      { trigger: "Q3 2026 revenue พลาด guidance >5%", status: "NOT_FIRED", note: "รอผล Q3 — Q2 guide ที่ให้ไว้ ($860-870M) เหนือ consensus" },
    ],
    thesisInvalidation: [
      { criteria: "Google ยกเลิกดีล AI licensing พร้อม DAU <10%", status: "NOT_MET", note: "ดีลยังเจรจาต่อเนื่อง ไม่ terminate" },
      { criteria: "Revenue growth <20% + EBITDA margin <25% พร้อมกัน", status: "NOT_MET", note: "Revenue ยังโต +61% YoY" },
      { criteria: "EU GDPR สั่งแบน AI data licensing", status: "NOT_MET" },
    ],
    verdict: "ไม่มี trigger ไหนยิงจริง แต่ DAU trigger ต้องการอีกแค่ 1 ไตรมาสยืนยัน (US DAU +6% เป็นไตรมาสแรกแล้ว) และ Google AI Overview traffic impact ยังเป็นคำเตือนเชิงคุณภาพที่ยังไม่ถูก quantify — ทั้งสองจุดจะชัดเจนขึ้นมากใน Q3 earnings",
    nextCatalyst: "Q3 2026 earnings (คาด ~ต.ค./พ.ย.) — ตัวชี้ขาด DAU trigger (จะครบ 2 ไตรมาสติดหรือไม่) และ revenue vs guidance",
    lastReviewDate: "2026-08-09",
  },
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
    verdict: "ไม่มี Bear Flip ยิง (fundamentals แข็งแกร่ง) — ปัญหาหลักคือ valuation ไม่ใช่ fundamentals: ราคาทะลุ Blended FV $121.45 แล้ว (MOS -2.82%, STRONG SELL territory ครั้งแรกในพอร์ต) DECISION 2026-08-09: HOLD ไม่ trim เพราะ weight เล็ก (2.45%) + FV อาจ stale (ไม่ re-verify มา ~3 เดือน) Gross margin 74.77% ใกล้ threshold 74% ควรจับตาเพิ่ม",
    nextCatalyst: "ส่ง Emma/Charlie re-verify Blended FV รอบวิเคราะห์ถัดไป (ค้างมา ~3 เดือนแล้ว) + จับตา gross margin trend",
    lastReviewDate: "2026-08-09",
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
