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
  {
    sector: "Software / AI",
    slug: "software-ai",
    stance: "CAUTIOUS",
    cyclePosition: "Mid-cycle",
    headline: "Secular growth ของจริง แต่ ROI-realization overhang กดราคาเป็นระลอก — selective ไม่ broad-avoid",
    thesis: "AI capex ของ hyperscaler ยังโตต่อเนื่องแรงมาก (4 รายใหญ่ guide รวม $670B ปี 2026, US Big Tech investment คาดโต +50% ทะลุ $600B, capex intensity ~23% ของ revenue สูงกว่ายุคก่อน ChatGPT กว่าเท่าตัว) แต่ประเด็นหลักที่ตลาดยังตัดสินใจไม่ได้คือช่องว่างระหว่างเงินที่ลงทุนกับ ROI ที่วัดผลได้จริง — Morgan Stanley เรียกช่วงนี้ว่า 'peak uncertainty' หลัง valuation กลุ่ม software/services ร่วงกลับมาใกล้ระดับที่เคยเห็นตอน disruption scare ครั้งก่อน สอดคล้องกับที่พอร์ตเราเจอเองปีนี้ (ADBE/CRM โดน downgrade เรื่อง capex-ROI overhang ก่อนจะเด้งกลับ, GOOGL stopDist เกือบ breach เพราะตลาด sell-the-news ทุกครั้งที่ capex guide ขึ้น แม้ Cloud growth จริงจะเร่งขึ้นต่อเนื่อง). ทีมยังไม่ avoid ทั้งกลุ่มเพราะ backlog/cloud growth เป็นหลักฐาน ROI ที่จับต้องได้จริงสำหรับผู้ชนะที่ชัดเจน (เช่น GOOGL Cloud +82%) แต่ยังไม่ commit เพิ่มทุนใหม่แบบไม่เลือกหน้า เพราะ mass productive deployment ในระดับ enterprise ยังไม่มาจริงตามที่ capex บอกไว้",
    keyPoints: [
      "4 hyperscaler ใหญ่ guide capex รวม $670B ปี 2026, US Big Tech +50% ทะลุ $600B, capex intensity ~23% ของ revenue",
      "Morgan Stanley: software/services valuation กลับมาใกล้ 'peak uncertainty' ระดับเดียวกับ disruption scare ครั้งก่อน",
      "ช่องว่าง capex-vs-ROI คือ bull/bear pivot หลักของกลุ่มทั้งปี 2026-2027 — mass enterprise deployment ยังไม่มาจริง",
      "หลักฐานเชิงประจักษ์จากพอร์ตเราเอง: ADBE/CRM/GOOGL ทั้งหมดโดน sell-the-news ซ้ำๆ ทุกครั้งที่มีข่าว capex แม้ fundamentals จริงจะแข็งแกร่งขึ้นต่อเนื่อง",
      "Technology sector Q2 2026 earnings +64.6% YoY (เร่งขึ้น) ยืนยันว่า demand ยังจริง ไม่ใช่แค่ hype — แต่ market ยัง discount ด้วย ROI doubt",
    ],
    relatedTickers: ["ADBE", "NOW", "GOOGL", "CRM", "ADSK"],
    sources: [
      { title: "CNBC — AI boom: Big Tech capex now seen topping $1 trillion in 2027", url: "https://www.cnbc.com/2026/04/30/ai-boom-big-tech-capital-expenditures-now-seen-topping-1-trillion-in-2027-.html" },
      { title: "Goldman Sachs — Why AI Companies May Invest More than $500 Billion in 2026", url: "https://www.goldmansachs.com/insights/articles/why-ai-companies-may-invest-more-than-500-billion-in-2026" },
      { title: "PwC — Technology: US Deals 2026 midyear outlook", url: "https://www.pwc.com/us/en/industries/tmt/library/technology-deals-outlook.html" },
      { title: "Forbes — S&P 500 Earnings Outlook Hinges On Tech, Energy And The Fed", url: "https://www.forbes.com/sites/bill_stone/2026/07/05/sp-500-earnings-outlook-hinges-on-tech-energy-and-the-fed/" },
    ],
    lastUpdated: "2026-07-30",
    author: "Atlas",
    trigger: "CIO ad-hoc request — sector coverage expansion (portfolio is 6/8 positions Software/AI-adjacent)",
  },
  {
    sector: "Healthcare",
    slug: "healthcare",
    stance: "CAUTIOUS",
    cyclePosition: "Late-cycle / Defensive rotation",
    headline: "Valuation ถูก + rotation story น่าสนใจ แต่ earnings ยังหดตัวจริง และมี stock-specific risk ในพอร์ตเราเอง",
    thesis: "Sell-side หลายสำนัก (Janus Henderson, BlackRock iShares, Bloomberg) มองปี 2026 เป็นปีที่ healthcare 'กลับมา' ได้ — valuation ยังอยู่ใกล้จุดต่ำสุดในรอบ ~30 ปีจาก policy uncertainty ที่เริ่มคลี่คลาย (drug pricing reform ชัดเจนขึ้น, M&A เริ่มกลับมาคึกคัก) และเป็น sector defensive ที่มักได้ประโยชน์จาก rotation ช่วงปลายวัฏจักร แต่ข้อมูลจริงจาก Q2 2026 earnings season ขัดแย้งกับ narrative นี้บางส่วน — healthcare เป็น sector เดียวใน S&P 500 ที่ earnings หดตัว YoY ไตรมาสนี้ ไม่ใช่แค่ sentiment ที่แย่ ทีมเจอสัญญาณ stock-specific คล้ายกันในพอร์ต/watchlist ของเราเอง: REGN เจอ securities class action lawsuit ใหม่ (Phase 3 melanoma setback), ZTS growth ชะลอเหลือ 2-5% พร้อม analyst PT ถูกหั่นต่อเนื่อง 2 รอบ, DXCM มีประวัติ crash -40% ในไตรมาสเดียวกันเมื่อ 2 ปีก่อน — ทำให้ยังไม่มั่นใจพอจะเรียกทั้ง sector ว่า positive แม้ valuation จะน่าสนใจ",
    keyPoints: [
      "Valuation healthcare ใกล้จุดต่ำสุดรอบ ~30 ปี จาก policy uncertainty ที่เริ่มคลี่คลาย (drug pricing reform, Medicare Advantage rate decision เม.ย.)",
      "แต่ Q2 2026: healthcare เป็น sector เดียวใน S&P 500 ที่ earnings หดตัว YoY — ขัดกับ 'comeback' narrative ของ sell-side บางส่วน",
      "M&A activity เริ่มกลับมาคึกคักขึ้น เป็นสัญญาณบวกเชิง structural",
      "Stock-specific risk ในพอร์ต/watchlist เราเอง: REGN lawsuit ใหม่, ZTS growth deceleration + PT cuts 2 รอบ, DXCM มี crash pattern -40% ประวัติศาสตร์ก่อน earnings",
      "สรุป: เป็น sector ที่ 'น่าดูใกล้ชิด' ไม่ใช่ 'รีบเพิ่มทุน' — รอดู Q3 earnings ว่า decline เป็น trough จริงหรือแค่เริ่มต้น",
    ],
    relatedTickers: ["REGN", "DXCM", "ZTS", "PODD"],
    sources: [
      { title: "Bloomberg — Healthcare Looks Ready to Star in Rotation Trade", url: "https://www.bloomberg.com/news/articles/2026-07-13/healthcare-looks-ready-to-star-in-rotation-trade-taking-stock" },
      { title: "Janus Henderson — Why healthcare stocks could excel in 2026", url: "https://www.janushenderson.com/article/why-healthcare-stocks-could-excel-in-2026/" },
      { title: "BlackRock iShares — Healthcare making a comeback?", url: "https://www.blackrock.com/au/insights/ishares/2026-comeback-year-for-healthcare" },
      { title: "Forbes — S&P 500 Earnings Outlook (healthcare sole YoY earnings decline)", url: "https://www.forbes.com/sites/bill_stone/2026/07/05/sp-500-earnings-outlook-hinges-on-tech-energy-and-the-fed/" },
    ],
    lastUpdated: "2026-07-30",
    author: "Atlas",
    trigger: "CIO ad-hoc request — sector coverage expansion (portfolio holds REGN + DXCM/ZTS/PODD watchlist)",
  },
];
