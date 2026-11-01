// ─── CRASH RESPONSE PLAYBOOK DATA ───────────────────────────────
// Managed by Max (PM) · CIO-directed 2026-11-01 · แผนตอบสนองล่วงหน้าเมื่อตลาดย่อ/correction/crash
// เป็น sizing + priority guide เสริมเท่านั้น — ไม่แก้กฎใดใน CLAUDE.md (Return-side ล็อก, Macro Regime Gate ใช้ตามเดิม)
// cash / totalValue / cashPct ดึงสดจาก PORTFOLIO.summary ตอน render — ไม่ duplicate ไว้ที่นี่ (Single Source of Truth)
// trigger price ทั้งหมดมาจาก portfolio/watchlist.md § AI Selloff Watch + § Quality Compounder Watchlist (Oct 30 close)
//   และ § Pending Analysis (MMS/NBIX/BYD, Oct 16 close) — เป็น screen-level ไม่ใช่ team Blended FV
// อัปเดต: Max re-score คอลัมน์ T (ระยะห่างจาก trigger) ทุกครั้งที่ tier ใด activate + ทุก Portfolio Review ระหว่าง drawdown

const CRASH_PLAYBOOK_LAST_UPDATED = "2026-11-02";

const CRASH_PLAYBOOK = {
  asOf: "2026-11-02 (ราคาอ้างอิง Oct 30 close)",
  regimeRecord: "RISK-ON 3/4 — agent_notes/atlas/2026-10-27_regime.md (VIX 17.52 ณ วันนั้น)",
  regimeWarning: "VIX ปิด 21.03 (Oct 30) = ระดับ TC แล้ว + Fed Stance เป็น RISK-OFF อยู่ก่อน (~73–77% odds hike Dec 9) → เหลือ RISK-ON แค่ 2/4 (Yield Curve, HY) = ไม่มี majority 3/4 — Atlas ต้อง re-call ก่อนใช้ playbook นี้ครั้งแรก. ถ้าไม่มี record ใหม่ Max ถือว่า TC ตาม CLAUDE.md",
  readyToDeploy: 0,
  readyNote: "ยังไม่มีชื่อใดผ่าน full VS2 pipeline + Morgan PASS + Blind Re-derivation (1.7) ที่ราคา trigger — playbook นี้จึงกำหนด 'ลำดับส่ง pipeline' และ 'ขนาดเมื่อผ่าน' ไม่ใช่สัญญาณซื้อ",

  // ── C. Severity tiers ─────────────────────────────────────────
  // tier = สัญญาณที่รุนแรงที่สุดในบรรดา (S&P drawdown จาก closing high, VIX, HY spread) — ไม่ใช่ index อย่างเดียว
  severityTiers: [
    {
      tier: 1,
      name: "ย่อปกติ (Pullback)",
      health: "INTACT",
      signal: "S&P 500 −10% ถึง −15% จาก closing high (Atlas บันทึก reference high + 2 sources) · VIX 20–25 · HY < 400bps",
      expectedRegime: "RISK-ON น่าจะคงอยู่ — แต่ปัจจุบัน Fed เป็น RISK-OFF แล้ว ถ้า VIX >20 ด้วย majority จะหลุด → Atlas re-call ก่อนทุก deploy",
      deployBudget: "ใช้ได้ ≤ 20% ของ cash ที่ deploy ได้ (เหนือ floor) · ชื่อใหม่ไม่เกิน 2 ตัว",
      actions: [
        "Deploy T1 (4% ของพอร์ต) เฉพาะชื่อที่ผ่าน conviction gate + MOS gate แล้วจริงจาก full VS2 pipeline + Morgan PASS + 1.7 blind — ห้ามซื้อที่ screen trigger",
        "Charlie ส่ง pipeline ชื่อ priority อันดับ 1–3 ที่แตะ early-warning (Quality: Trigger @WACC−1pp · AI: stress trigger ระยะ ≤10%) — เตรียมไว้ก่อน Tier 2",
        "ห้าม T2/T3 add ใน tier นี้ — รอ price confirm + FV re-verify",
      ],
    },
    {
      tier: 2,
      name: "Correction",
      health: "WATCH",
      signal: "S&P 500 −15% ถึง −25% · หรือ VIX 25–30 · หรือ HY 400–600bps",
      expectedRegime: "มีโอกาสสูงที่จะเป็น TC (VIX + HY + Fed ไม่ใช่ RISK-ON) → ห้าม open ใหม่ตาม Macro Regime Gate จนกว่า Atlas re-call RISK-ON",
      deployBudget: "ถ้ายัง RISK-ON: สะสม ≤ 50% ของ cash ที่ deploy ได้ · ชื่อใหม่สะสมไม่เกิน 4 ตัว · ถ้า TC: 0 ชื่อใหม่",
      actions: [
        "RISK-ON: deploy T1 ตาม Priority Ranking (คะแนนสูงก่อน) — 1 ชื่อต่อ session, เว้นอย่างน้อย 2 session ระหว่างชื่อที่อยู่ factor เดียวกัน (AI-megacap)",
        "T2 (+3%) ได้เฉพาะชื่อจาก Tier 1 ที่ re-verify FV หลังราคาลงแล้ว MOS ยังผ่าน (FV ไม่ได้ลงตามราคา)",
        "TC: เปลี่ยนเป็นโหมดเตรียม — รัน full pipeline ชื่อ priority 1–5 ให้ Morgan PASS ค้างไว้ พร้อม execute ทันทีที่ Atlas re-call RISK-ON",
        "Force Deploy (cash >30% >2 สัปดาห์ + RISK-ON + มี candidate ผ่าน gate) = บังคับ ≥1 position ตามเดิม — playbook ไม่ override",
      ],
    },
    {
      tier: 3,
      name: "Crash",
      health: "FIRING",
      signal: "S&P 500 ลง > −25% · หรือ VIX > 30 · หรือ HY > 600bps (ระดับ RISK-OFF ใน Macro Regime Gate)",
      expectedRegime: "เกือบแน่นอนว่าเป็น TC หรือ RISK-OFF → Macro Regime Gate ห้าม open ใหม่ทั้งหมด (cash floor 25% / 35%, multiplier 0.75x / 0.5x)",
      deployBudget: "ระหว่าง TC/RISK-OFF: ชื่อใหม่ 0 · add ได้เฉพาะ position เดิมที่ผ่าน gate (ดู guardrail ข้อ 4) ไม่ต่ำกว่า floor ของ regime · หลัง Atlas re-call RISK-ON: deploy ได้ถึง 100% ของ cash เหนือ floor 10% แบ่ง 3 จังหวะ",
      actions: [
        "ระหว่าง crash: ไม่ใช่ 'ซื้อก้นเหว' — กฎปัจจุบันให้ซื้อตอนฟื้น. Pipeline ชื่อ priority 1–8 ให้ Morgan PASS ครบ + re-compute trigger ด้วย Rf/ERP ใหม่ (FV เปลี่ยนตาม WACC)",
        "วันที่ Atlas re-call RISK-ON: จังหวะ 1 = 40% ของ budget (T1 ชื่อ top-3 ที่ MOS ยังผ่าน) · จังหวะ 2 = 30% หลัง ≥10 trading days · จังหวะ 3 = 30% หลัง FV re-verify รอบถัดไป",
        "Drawdown halt −35% ของพอร์ต (Risk Rule 1) มาก่อนทุกอย่าง — ถ้าโดน หยุด trade ทั้งหมด",
        "ทางเลือกให้ CIO ตัดสิน (ไม่ทำเอง): แก้แถว TC/RISK-OFF ให้เปิด T1 ได้จำกัด — เป็น Risk-side rule แก้ก่อน 8Q ได้ ดู Open Decision ด้านล่าง",
      ],
    },
  ],

  // ── B. Position sizing ────────────────────────────────────────
  regimeFloors: [
    { regime: "RISK-ON", floorPct: 10, multiplier: 1.0, newPositions: "ได้", note: "Force Deploy active" },
    { regime: "TRANSITIONAL-CAUTIOUS", floorPct: 25, multiplier: 0.75, newPositions: "ห้าม", note: "รักษา position เดิมได้" },
    { regime: "RISK-OFF", floorPct: 35, multiplier: 0.5, newPositions: "ห้าม", note: "Force Deploy suspend" },
  ],
  sizing: [
    { item: "Full position target", rule: "8–10% ของพอร์ต × regime multiplier · ห้ามเกิน 10%", source: "IPS + Deployment Rule 5" },
    { item: "T1 (เข้าครั้งแรก)", rule: "4% ของพอร์ต (ครึ่งหนึ่งของ 8%) · ต่ำสุด 3% ตาม minimum rule", source: "Deployment Rule 5 (min 3% เมื่อ conv ≥6.5)" },
    { item: "T2 (add)", rule: "+3% เมื่อ FV re-verify หลังราคาลงแล้ว MOS ยังผ่าน gate", source: "Max Consultation Rule (tranche add ต้อง consult)" },
    { item: "T3 (add)", rule: "+2–3% จนถึง cap 10%", source: "IPS single position ≤10%" },
    { item: "AI/Infra lane", rule: "T1 ≤ 4% · T2/T3 ได้เฉพาะเมื่อ milestone ที่ระบุตอน T1 เกิดจริง · MOS ≥25%", source: "Business-Type Lane: AI/Infra" },
    { item: "Thesis-valid, no MOS", rule: "½ ของขนาดปกติ (4–5%) · บันทึก 'thesis-valid entry, no MOS' ใน trade-log", source: "Deployment Rule 3" },
    { item: "Factor cap: AI-megacap", rule: "รวมไม่เกิน 2 ชื่อ / ≤15% ของพอร์ต — META/GOOGL/MSFT/AMZN/NVDA มี factor AI-capex เดียวกัน", source: "Max assessment #5 (AI Selloff Watch)" },
    { item: "Factor cap: Software", rule: "ไม่เพิ่มชื่อ software ใหม่ — พอร์ตมี ADBE/NOW/CRM/ADSK อยู่แล้ว", source: "Concentration judgment (ไม่ใช่กฎใหม่)" },
    { item: "จำนวน position", rule: "เปิดอยู่ 5 → เพิ่มได้สูงสุด 5 (รวม ≤10, เพดาน 12)", source: "IPS max positions" },
  ],
  tierBudgetPct: { 1: 20, 2: 50, 3: 100 }, // % สะสมของ cash เหนือ floor ที่ใช้ได้ (คำนวณสดตอน render)

  // ── A. Priority ranking ───────────────────────────────────────
  // Score = R + 2×M + G + T + D (สูงสุด 18) — moat ถ่วง 2 เท่าตามโจทย์ CIO
  // R Readiness: 3 team VS2 FV สด · 2 มี team/lightweight FV แต่เก่าหรือ learning-queue · 1 screen-level เท่านั้น · 0 ต้อง re-classify ก่อน
  // M Moat: 3 Wide · 2 Narrow+ · 1 ยังไม่ยืนยัน
  // G Gate passability: 3 Growth gate (conv ≥6.5) ไม่มี lane เพิ่ม · 2 Value gate (conv ≥7.0, MOS ≥15%) หรือ lane ยังไม่จัด · 1 lane AI/Infra (MOS ≥25%) หรือ conviction เดิมห่าง gate ≥1 จุด · 0 มี methodology blocker
  // T ระยะถึง trigger (official): 3 ≤10% · 2 10–20% · 1 20–35% · 0 >35%
  // D Diversification vs พอร์ต (software-heavy + REGN): 3 sector ใหม่ non-AI · 2 healthcare · 1 AI-megacap factor
  priority: [
    { ticker: "MMS",  group: "Pending (learning-queue)", price: "$61.47*", trigger: "Entry $55–61 · Stop $48", drop: "≈0%",     R: 2, M: 2, G: 2, T: 3, D: 3, blocker: "E 1/3 (ROIC spread +2–2.7pp, federal overhang) · Tier 1.5 target 2026-11-20 หลัง FY26 Q4 (Nov 19)", fit: "Fed shock / AI" },
    { ticker: "NBIX", group: "Pending (learning-queue)", price: "$135.77*", trigger: "Entry $122–135 · Stop $108", drop: "≈0–10%", R: 2, M: 2, G: 3, T: 3, D: 2, blocker: "D-V1 'methods disagree' · IRA Medicare 2027–29 ยังไม่ quantify · Q3 print Nov 2 → Tier 1.5 2026-11-03", fit: "AI / Credit (net cash)" },
    { ticker: "PAYX", group: "Quality Compounder", price: "$112.12", trigger: "$78.84 (early-warn $100.39)", drop: "−29.7%", R: 1, M: 3, G: 2, T: 1, D: 3, blocker: "Screen FV เดียว ไม่มี 40/30/30 · SMB employment / Paycor integration", fit: "AI / War" },
    { ticker: "ORLY", group: "Quality Compounder", price: "$88.12",  trigger: "$59.63 (early-warn $78.39)", drop: "−32.3%", R: 1, M: 3, G: 2, T: 1, D: 3, blocker: "Leases ไม่อยู่ใน screen → FV สูงเกินจริง · ROIC 72→54%", fit: "Recession-defensive" },
    { ticker: "GOOGL", group: "AI Megacap", price: "$279.84", trigger: "$230 stress (base $267.47)", drop: "−17.7%", R: 1, M: 3, G: 2, T: 2, D: 1, blocker: "Exit 2026-09-12 ด้วย Thesis Invalidation (capex >$100B/yr) — re-entry ต้องมี thesis ใหม่ + FY27 capex guide · AI/Infra lane ยังไม่จัด", fit: "AI selloff" },
    { ticker: "META", group: "AI Megacap", price: "$614.99", trigger: "$501 stress (base ผ่านแล้ว)", drop: "−18.5%", R: 1, M: 3, G: 2, T: 2, D: 1, blocker: "Capex/Rev 43% → น่าจะเข้า AI/Infra lane (MOS ≥25%, T1 ≤4%) · FCF ติดลบ", fit: "AI selloff" },
    { ticker: "RMD",  group: "Quality Compounder", price: "$229.94", trigger: "$161.14 (early-warn $197.74)", drop: "−29.9%", R: 1, M: 3, G: 2, T: 1, D: 2, blocker: "GLP-1 bear thesis · 5Y ROIC ~22% ขอบ 20%", fit: "AI / Recession" },
    { ticker: "BYD",  group: "Pending (learning-queue)", price: "$70.04*", trigger: "Entry $63–70 · Stop $56", drop: "≈0–10%", R: 2, M: 1, G: 2, T: 3, D: 3, blocker: "Moat ยังไม่ยืนยัน (E1 ❓) · D 0.87×/1.06× ขึ้นกับ FCF basis · leverage → แพ้ใน credit event", fit: "AI / Fed shock (ไม่ใช่ war/credit)" },
    { ticker: "AMZN", group: "AI Megacap (Value gate)", price: "$240.35", trigger: "$171.25 (zone $161–171)", drop: "−28.7%", R: 2, M: 3, G: 1, T: 1, D: 1, blocker: "Conviction ล่าสุด 5.67 vs gate 7.0 · team FV v3.4 ก่อน Q3 miss (Oct 29) — ต้อง re-verify", fit: "AI selloff" },
    { ticker: "MSFT", group: "AI Megacap (Value gate)", price: "$521.91", trigger: "$383 proxy (stress $300)", drop: "−27%",   R: 1, M: 3, G: 2, T: 1, D: 1, blocker: "ไม่มี team Blended FV — proxy 0.85× screen DCF · rev +17.9% <20% → Growth gate ปิด", fit: "AI selloff" },
    { ticker: "ROL",  group: "Quality Compounder", price: "$34.66",  trigger: "$18.59 (early-warn $23.52)", drop: "−46.4%", R: 1, M: 3, G: 2, T: 0, D: 3, blocker: "Q2 miss + law-firm investigation (E3 overhang)", fit: "Recession-defensive" },
    { ticker: "KNSL", group: "Quality Compounder", price: "$365.71", trigger: "$182.70 (early-warn $213.63)", drop: "−50.0%", R: 1, M: 3, G: 2, T: 0, D: 3, blocker: "E&S cycle softening · RI model simplified", fit: "Fed shock (float ได้ประโยชน์)" },
    { ticker: "ITW",  group: "Quality Compounder", price: "$278.55", trigger: "$138.20 (early-warn $175.30)", drop: "−50.4%", R: 1, M: 3, G: 2, T: 0, D: 3, blocker: "โตช้า 3.6–4.9%", fit: "Fed shock (duration สั้น)" },
    { ticker: "MNST", group: "Quality Compounder", price: "$47.34",  trigger: "$24.23 (early-warn $30.75)", drop: "−48.8%", R: 1, M: 3, G: 2, T: 0, D: 3, blocker: "EV/Rev 95th pctile", fit: "Credit event (net cash $3.4B)" },
    { ticker: "GWW",  group: "Quality Compounder", price: "$1,359.17", trigger: "$626.17 (early-warn $768.53)", drop: "−53.9%", R: 1, M: 3, G: 2, T: 0, D: 3, blocker: "EV/Rev 95th pctile", fit: "Crash only" },
    { ticker: "FAST", group: "Quality Compounder", price: "$51.91",  trigger: "$23.87 (early-warn $29.98)", drop: "−54.0%", R: 1, M: 3, G: 2, T: 0, D: 3, blocker: "EV/Rev 95th pctile", fit: "Crash only" },
    { ticker: "SHW",  group: "Quality Compounder", price: "$332.61", trigger: "$141.60 (early-warn $181.59)", drop: "−57.4%", R: 1, M: 3, G: 2, T: 0, D: 3, blocker: "Net debt $11.5B → แพ้ใน credit event", fit: "Crash only" },
    { ticker: "MSI",  group: "Quality Compounder", price: "$491.53", trigger: "$202.82 (early-warn $265.31)", drop: "−58.7%", R: 1, M: 3, G: 2, T: 0, D: 3, blocker: "ROIC ลงเหลือ 22% (M&A)", fit: "War (public-safety demand)" },
    { ticker: "RACE", group: "Quality Compounder", price: "$395.99", trigger: "$155.23 (early-warn $192.21)", drop: "−60.8%", R: 1, M: 3, G: 2, T: 0, D: 3, blocker: "20-F ไม่มี TTM · captive-finance debt", fit: "Crash only" },
    { ticker: "CTAS", group: "Quality Compounder", price: "$219.82", trigger: "$79.52 (early-warn $98.78)", drop: "−63.8%", R: 1, M: 3, G: 2, T: 0, D: 3, blocker: "Implied k 3.3× · long-duration → แพ้ Fed shock", fit: "Crash only" },
    { ticker: "TT",   group: "Quality Compounder", price: "$410.00", trigger: "$213.20 (early-warn $260.26)", drop: "−48.0%", R: 1, M: 3, G: 2, T: 0, D: 2, blocker: "บางส่วนผูก DC cooling (AI capex)", fit: "Crash only" },
    { ticker: "IDXX", group: "Quality Compounder", price: "$551.21", trigger: "$185.74 (early-warn $215.63)", drop: "−66.3%", R: 1, M: 3, G: 2, T: 0, D: 2, blocker: "WACC 10.6% (β 1.54) · long-duration", fit: "Crash only" },
    { ticker: "WST",  group: "Quality Compounder", price: "$412.62", trigger: "$116.12 (early-warn $138.05)", drop: "−71.9%", R: 1, M: 3, G: 2, T: 0, D: 2, blocker: "ROIC 35→18% ขาลง · P/FV 3.0×", fit: "Crash only" },
    { ticker: "NVDA", group: "AI Megacap", price: "$204.64", trigger: "ยังไม่มี — ต้องรัน VS2 แบบ Cyclical (mid-cycle) ก่อน", drop: "n/a",   R: 0, M: 3, G: 0, T: 0, D: 1, blocker: "Screen 'ผ่าน' ด้วยเหตุผลผิด (hypergrowth extrapolation) · team FV $149 (2026-05-16) เก่า 5 เดือน", fit: "AI selloff (หลัง re-classify)" },
  ],
  priorityNote: "* MMS/NBIX/BYD ราคา Oct 16 (เก่ากว่า 7 วัน) — ต้อง re-verify ≥2 sources ก่อนใช้ตาม Scout→Analysis SLA. ราคาอื่น Oct 30 close. ห้ามซื้อที่ trigger โดยตรง: ชื่อที่แตะ early-warning → Charlie ส่ง full VS2 pipeline ตามลำดับคะแนน (ต้นทุน ~200–255K token/ชื่อ จึงต้องเรียงลำดับ)",

  // ── D. Scenarios (AI vs non-AI) ───────────────────────────────
  scenarios: [
    {
      name: "AI-capex unwind (baseline ของ watchlist เดิม)",
      health: "WATCH",
      signals: "Hyperscaler หั่น capex guide · NVDA guide miss · AI-lab funding/IPO ล้ม · Nasdaq แย่กว่า S&P ≥5pp ใน 1 เดือน",
      hits: "AI megacaps + AI-power/E&C trade (VST/PWR/MTZ ฯลฯ) — software ในพอร์ตเคย decouple (Oct 22, Oct 30)",
      response: "ใช้ Priority Ranking ตามเดิม · AI megacap ทีละชื่อ ไม่เกิน factor cap · contagion victim ต้องผ่าน A–E ใหม่ (Part B พบว่า non-AI utilities ลงไม่ถึง 20% — contagion ไม่ได้เกิดจริง)",
    },
    {
      name: "Fed hawkish shock",
      health: "FIRING",
      signals: "10Y UST ปิด > 5.00% ติดกัน 10 trading days หรือปิด > 5.25% วันใดก็ได้ (ตอนนี้ 4.93–5.00%) · Fed funds futures price hike ≥2 ครั้งใน 12M · 2Y ขึ้นเร็วกว่า 10Y (curve flatten เข้า 0)",
      hits: "ทุก FV ลดลงพร้อมราคา (Rf เป็น input WACC) — long-duration/high P-FV โดนหนักสุด: IDXX, WST, CTAS, GWW, FAST และ software ในพอร์ต",
      response: "ห้ามใช้ trigger เดิม — Atlas รัน Macro Scenario Stress Test #1/#5 แล้ว re-compute trigger ด้วย Rf ใหม่ก่อน (−1pp WACC = FV +15–45% ทิศกลับกันก็จริง) · เลื่อน priority ไปชื่อ duration สั้น/เงินสดแรง: MMS, ITW, BYD, KNSL (float ได้ดอกเบี้ยสูงขึ้น) · cash yield ของพอร์ตเพิ่มตาม Cash Yield Rule = รอได้ถูกลง",
    },
    {
      name: "War / geopolitical escalation",
      health: "FIRING",
      signals: "น้ำมัน > $110 ยืน ≥5 วัน (Oct 23 แตะ >$100 จาก US-Iran) · VIX กระโดด > 30 ใน ≤3 วันโดย HY ยัง < 450bps · shipping/insurance spike",
      hits: "Consumer discretionary + ต้นทุนพลังงาน/ขนส่ง: RACE, BYD, ORLY (บางส่วน), airlines · ไม่ใช่ AI-megacap เป็นหลัก",
      response: "Shock ที่ credit ไม่ตาม = Tier ตาม VIX แต่รอ Atlas re-call ก่อน (VIX spike อาจหลุด majority สั้นๆ) · priority: ชื่อที่รายได้ไม่ผูกพลังงาน/การเดินทาง (PAYX, MSI, NBIX, MMS) · ไม่ใช้ข่าวสงครามเป็น catalyst ซื้อชื่อ defense/energy นอก pipeline",
    },
    {
      name: "Credit event (non-AI)",
      health: "FIRING",
      signals: "HY spread > 500bps และขยายต่อเนื่อง 2 สัปดาห์ (> 600 = RISK-OFF) · private credit/BDC redemption gate · regional bank stress · leveraged-loan default ข่าวใหญ่",
      hits: "บริษัทหนี้สูง/refinance ใกล้: BYD, SHW (net debt $11.5B), utilities ที่ leverage สูง · financials",
      response: "B-Zero มาก่อน: priority ชื่อ net cash / ND/EBITDA ต่ำ (MNST, NBIX, IDXX, PAYX) · ตัด BYD/SHW ออกจากลำดับจนกว่า spread กลับ < 400 · regime มักเป็น RISK-OFF เร็ว → โหมดเตรียมตาม Tier 3",
    },
  ],

  // ── Guardrails (สิ่งที่ playbook นี้ไม่ทำ) ─────────────────────
  guardrails: [
    "ไม่แก้ Return-side rule ใด (MOS 15%/Growth reverse-DCF 1.2×, conviction 6.5/7.0, 40/30/30, position 8–10%) — trigger/ranking เป็น screen-level ใช้จัดลำดับงานเท่านั้น",
    "ทุก BUY ต้องผ่าน: Atlas regime record ใหม่ → full VS2 pipeline → Morgan QA PASS → VS2 1.7 Blind Re-derivation (trigger ก) → Max execute",
    "Tranche add (T2/T3) และ BUY นอก pipeline ต้องผ่าน Max Consultation Rule (Max × Charlie) ก่อน — BUY จาก fresh pipeline นับว่า consult แล้ว",
    "Add position เดิมระหว่าง TC: CLAUDE.md เขียน 'รักษา positions ที่มีอยู่ได้' ไม่ได้ระบุ add ชัด → ครั้งแรกที่จะใช้ต้อง Max×Charlie consult + flag CIO · RISK-OFF: ไม่ add",
    "Stop loss −20% / drawdown halt −35% / thesis invalidation exit ทำงานตามปกติระหว่าง crash — ไม่เลื่อนเพราะ 'ราคาถูกลง'",
  ],
  openDecision: "CIO ตัดสิน (Risk-side rule, แก้ก่อน 8Q ได้): ปัจจุบัน Tier 3 แปลว่า 'ซื้อตอนฟื้น' เพราะ TC/RISK-OFF ห้าม open ใหม่. ทางเลือก (ก) คงเดิม · (ข) เปิด T1 ได้เฉพาะ priority top-3 ที่ Morgan PASS แล้ว ขนาด T1 4% × multiplier ของ regime (TC = 3% · RISK-OFF = 2% ซึ่งต่ำกว่า minimum 3% → ต้องเลือกว่าใช้ 3% หรือไม่เข้าเลย) ไม่ต่ำกว่า cash floor. Max ไม่แก้เอง — เสนอเท่านั้น",
};
