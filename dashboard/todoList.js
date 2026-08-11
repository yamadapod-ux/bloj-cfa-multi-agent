// ─── TODO / IDEAS LIST ───────────────────────────────────
// Personal ideas board — ไม่เกี่ยวกับ portfolio/investment decisions โดยตรง
// เก็บไว้ที่นี่เพราะ CIO เปิด dashboard ค้างไว้ตลอด — ใช้เป็นที่จดไอเดียที่คุยกับ Claude ระหว่างรอ agent ทำงาน
// อัปเดตแบบ ad-hoc — ไม่มี agent ไหนดูแลไฟล์นี้เป็นทางการ (ต่างจากไฟล์อื่นในโฟลเดอร์นี้)

const TODO_LAST_UPDATED = "2026-08-11";

const TODO_LIST = [
  {
    id: "content-case-study",
    title: "เอา บลจ. CFA มาทำเป็น case study / content เกี่ยวกับการลงทุน",
    category: "Career / Content",
    status: "IDEA",
    priority: "HIGH",
    dateAdded: "2026-08-11",
    summary: "ไม่เริ่ม project ใหม่ — เอา project นี้ที่ทำอยู่แล้ว 90% มาเล่าใหม่เป็น content สาธารณะ แทนที่จะทำ 'TikTok หุ้น' แบบทั่วไป",
    context: "เกิดจากบทสนทนาเรื่องความไม่แน่ใจเรื่องสายอาชีพ — ตอนนี้ทำงาน CX ให้แอปลงทุน (ไม่ทรมานแต่ก็ไม่ใช่สิ่งที่ตื่นเต้นที่สุด) เรียนจบภาพยนตร์มา ชอบช่วงเวลาที่ได้หาข้อมูลหุ้นมากที่สุดในบรรดางานทั้งหมดที่เคยทำ",
    keyInsights: [
      "Pattern ที่สังเกตเห็นจากการทำงานร่วมกันตลอด session: เป็น 'director brain' — ไม่เขียนโค้ดเอง ไม่คำนวณ DCF เอง ไม่หาข้อมูลทุกตัวเอง แต่รู้เสมอว่าอะไรถูกอะไรผิดอะไรขาด (จับได้ว่า ETN ตกหล่นจาก watchlist prune, จับได้ว่า Vera sync-check note ผิดพลาดจาก race condition) — ตรงกับพื้นฐานภาพยนตร์ที่บอกว่า รู้ทฤษฎีจัดแสง/มุมกล้อง/ตัดต่อหมด แต่ไม่เคยลงมือทำเองจริงจัง",
      "AI tools ตอนนี้กำลังลดช่องว่างระหว่าง 'รู้ว่าอะไรดี' กับ 'ทำเองไม่เป็น' ลงเร็วมาก — พอดีกับ pattern การทำงานที่ใช้กับ Claude Code อยู่แล้ว (สั่งงาน ตรวจ QA ไม่ต้อง execute เอง) ใช้หลักการเดียวกันกับ video editing ได้ (AI-assisted editing tools)",
      "TikTok/YouTube แนว 'บอกให้คนซื้อหุ้นตัวไหน' ถูกตัดออกตั้งแต่ต้น เพราะ (1) skill mismatch — ต้องการ short-form/personality-driven ซึ่งต่างจาก deep-research ที่ชอบจริง (2) ตลาดอิ่มตัวมาก มีช่องแนวนี้เยอะแล้ว (3) ประเด็นกฎหมาย/compliance เรื่องให้คำแนะนำการลงทุนส่วนบุคคลโดยไม่มีใบอนุญาต",
      "มุมที่ differentiate จริง: เล่าเรื่อง 'กระบวนการ' ไม่ใช่ 'คำแนะนำ' — เช่น AI agent orchestration + investment discipline framework (CFA-based) + narrative structure จากพื้นฐานภาพยนตร์ ไม่มีคนทำ niche นี้จริงจัง",
    ],
    contentHooks: [
      "'Gate ปฏิเสธหุ้น 9 ตัวติดกัน — และนั่นคือฟีเจอร์ ไม่ใช่บั๊ก' (เล่าเรื่อง dual-gate-fail 9 instances ในไตรมาสนี้ ว่าทำไม cash ค้าง 60%+ ไม่ deploy คือ discipline ทำงานถูกต้อง)",
      "'ผมสร้างทีมนักวิเคราะห์ AI 9 ตัว ให้เถียงกันเองก่อนตัดสินใจซื้อหุ้น' (แนะนำทีม Charlie/Atlas/Emma/Quinn/Bear/Morgan/Leo/Vera/Max และวิธีที่แต่ละตัวมี checks-and-balances ต่อกัน)",
      "'AI จับได้ว่า AI อีกตัวคำนวณผิด' (เล่าเคส Morgan QA จับ Blended FV formula ผิดใน ICE analysis — 2-round correction cycle)",
      "'ผมเขียน constitution ให้ทีม AI ของตัวเอง' (แนะนำ CLAUDE.md เป็น 'show bible' ที่กำหนดกฎเหล็กทั้งหมด)",
    ],
    openQuestions: [
      "รูปแบบเริ่มต้น: newsletter/blog (ต้นทุนต่ำ ทดสอบว่ายัง enjoy อยู่ไหมตอนต้อง publish ให้คนอื่นอ่าน) vs. video ตรงๆ (ใช้ film background เต็มที่กว่าแต่ต้นทุนสูงกว่ามาก)",
      "รู้สึกยังไงกับการเอา 'งานอดิเรกที่ทำเพื่อตัวเอง' มา expose ให้คนอื่นเห็น — จะเปลี่ยนความรู้สึกกับ project นี้ไปทางไหน",
      "ถ้าจะทำ video ต้องหาทางแก้ execution gap (ไม่เคยตัดต่อเอง) — ใช้ AI-assisted tool เอง หรือหา partner/editor",
      "ยังไม่ได้ตัดสินใจว่าจะเริ่มเมื่อไหร่ / เริ่มยังไง — รอคุยต่อ",
    ],
    nextStep: "ยังไม่ได้เริ่มลงมือ — บันทึกไอเดียไว้ก่อน รอตัดสินใจเรื่อง format + ความพร้อมที่จะ publish ให้คนอื่นเห็น",
  },
];
