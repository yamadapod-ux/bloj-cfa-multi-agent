// ─── SECTOR VIEWS DATA ───────────────────────────────────────────
// Managed by Atlas · เขียนแบบ ad-hoc เมื่อทีมเกิด/ทบทวน view ระดับ sector เท่านั้น
// (ไม่ใช่ scheduled job แบบ /news-scan — ดู CLAUDE.md § Sector Views Protocol)
// กฎการเขียน: ห้ามแก้/ลบ entry เดิม — push entry ใหม่เข้า array เท่านั้น (append-only)
// เหตุผล: entry เก่าคือ audit trail ว่าทีมเคยคิดอะไรมาก่อน ณ วันไหน — การแก้ทับจะทำลายหลักฐานนั้น

const SECTOR_VIEWS_LAST_UPDATED = "2026-07-30 09:00";

const SECTOR_VIEWS = [
  {
    sector: "Energy",
    slug: "energy",
    stance: "NEGATIVE",
    cyclePosition: "Late-cycle",
    headline: "Late-cycle plateau เงินทุนใหม่เสี่ยงจ่ายที่จุดพีค — รอ de-escalation ก่อน",
    thesis: "พลังงานอยู่ช่วง late-cycle ที่ราคาถูกดันขึ้นด้วย geopolitical risk premium (Iran conflict, oil +5% แตะ $83+ วันเดียว) มากกว่า fundamental scarcity — สัญญาณชัดที่สุดคือ S&P 500 Energy earnings คาดโต +57% ปี 2026 แต่ consensus คาดหดตัว -5% ปี 2027 (pattern peak-then-decline ที่ตลาด price-in แล้ว) ประกอบกับ XLE พุ่ง +32-40% YTD ทิ้งห่าง S&P 500 และ Tech จนถูกมองว่า valuation ตึงเกินไปแล้ว ขณะที่ EIA/ING คาด oversupply 2.0-2.26 ล้านบาร์เรล/วันปี 2026 ซึ่งขัดแย้งกับราคาที่พุ่งอยู่ตอนนี้ — capex ยังมีวินัย (upstream ลดต่อเนื่องปีที่ 2) และ rig count ยังต่ำเทียบ shale-boom era จึงยังไม่ใช่ bubble-top แบบสุดขั้ว แต่การซื้อตอนนี้เท่ากับจ่ายที่ earnings peak + valuation แพง + geopolitical premium พร้อมกันทั้งสามอย่าง ซึ่งเสี่ยงเกินไปสำหรับ time horizon 3-5 ปีของกองทุน",
    keyPoints: [
      "S&P 500 Energy earnings: +57% (2026F) แล้วพลิกหด -5% (2027F) — สัญญาณ peak-then-decline จากตลาดเอง",
      "XLE +32-40% YTD 2026 (ทิ้งห่าง S&P 500 +8.8% และ Tech +23%) — valuation ตึงแล้ว, risk/reward tilted downside ตาม analyst",
      "EIA/ING คาด oversupply 2.0-2.26 ล้านบาร์เรล/วันปี 2026 — ราคาปัจจุบันขับเคลื่อนด้วย Iran conflict premium ไม่ใช่ scarcity จริง",
      "Upstream capex ลดต่อเนื่องปีที่ 2 (-2-3% YoY) + rig count ยังต่ำเทียบ shale-boom — ยังไม่ใช่ euphoria-style bubble top",
      "ถ้าจะพิจารณาจริง: integrated majors (XOM/CVX) หรือ midstream/pipeline (FCF นิ่งกว่า) ดีกว่า pure-play E&P ที่จะโดนแรงสุดถ้า cycle หัน",
    ],
    relatedTickers: [],
    sources: [
      { title: "Forbes — S&P 500 Earnings Outlook Hinges On Tech, Energy And The Fed", url: "https://www.forbes.com/sites/bill_stone/2026/07/05/sp-500-earnings-outlook-hinges-on-tech-energy-and-the-fed/" },
      { title: "GuruFocus — Energy Sector Insights: Key Pivot Points for XLE", url: "https://www.gurufocus.com/news/8980339/energy-sector-insights-key-pivot-points-for-xle" },
      { title: "ING Think — Bearish oil outlook, but upside risks abound", url: "https://think.ing.com/articles/bearish-oil-outlook-but-clear-upside-risks/" },
      { title: "Bloomberg — OPEC Keeps 2026 Oil Supply, Demand Outlook Steady", url: "https://www.bloomberg.com/news/articles/2025-12-11/opec-data-point-to-balanced-global-oil-market-in-2026" },
      { title: "OilPrice — Global Upstream Capex Set To Fall Again In 2026 Amid Low Oil Prices", url: "https://oilprice.com/Energy/Crude-Oil/Global-Upstream-Capex-Set-To-Fall-Again-In-2026-Amid-Low-Oil-Prices.html" },
      { title: "Bloomberg — US Oil Rig Count Rises for 12th Week, Longest Streak Since 2022", url: "https://www.bloomberg.com/news/articles/2026-07-17/us-oil-rig-count-notches-longest-streak-without-drop-since-2022" },
      { title: "EIA — Weekly Petroleum Status Report (crude inventories)", url: "https://www.eia.gov/todayinenergy/detail.php?id=67868" },
    ],
    lastUpdated: "2026-07-30",
    author: "Atlas",
    trigger: "CIO ad-hoc request — energy sector cycle analysis",
  },
];
