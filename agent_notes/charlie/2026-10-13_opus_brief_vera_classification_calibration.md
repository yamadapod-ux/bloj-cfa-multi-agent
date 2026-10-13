# Brief สำหรับ Hermes → Vera: Calibration เกณฑ์จัดประเภทหุ้น (VS2)

*Opus 5.5 → Hermes (Sonnet) / Vera · 2026-10-13*
*ที่มา: CLAUDE.md § "เกณฑ์จัดประเภท + เหตุผลของวิธี" (`e4bc4db`) ระบุว่าตัวเลขเกณฑ์ยังไม่ calibrate — ต้องทดสอบย้อนกับหุ้นที่วิเคราะห์แล้วก่อนใช้กับหุ้นจริง*
*ผลนี้เป็น calibration เท่านั้น — **ไม่นับเป็น trial data** และ **ไม่แก้ CLAUDE.md** · ผลส่งกลับ Opus review ก่อนเสนอแก้เกณฑ์*

---

## 1. เป้าหมาย

ตอบ 4 คำถาม:
1. เกณฑ์จัดหุ้นได้ **ครบ** ไหม (ทุกตัวได้ 1 ประเภทหลัก ไม่ค้าง `PENDING`)
2. เกณฑ์ **ทับกัน** มากไหม (หุ้นเข้า ≥2 ประเภทพร้อมกันบ่อยแค่ไหน และมีกติกาตัดสินพอไหม)
3. ผลตรง **สามัญสำนึก** ไหม (เทียบกับประเภทที่ Opus ล็อกไว้ล่วงหน้า — ดู §5)
4. Threshold ตัวไหน **อยู่บนเส้นแบ่ง** มากเกินไป (หุ้นหลายตัวกองอยู่ใกล้เกณฑ์ = เกณฑ์ไม่เสถียร)

---

## 2. กลุ่มตัวอย่าง (26 ตัว — เลือกให้ครอบคลุมทุกประเภท + กรณีกำกวมโดยตั้งใจ)

ACGL · PGR · OSCR · CNC · V · MA · ICE · FICO · NOW · CRM · ADBE · VEEV · NET · SHOP · MU · LRCX · NVDA · APTV · LVS · WPM · CCJ · DECK · REGN · ABBV · AMZN · GOOGL

**ไม่มีในกลุ่ม:** REIT, regulated utility (ทีมไม่เคยวิเคราะห์) → รายงานเป็น "ทดสอบไม่ได้ — ไม่มีข้อมูล" ห้ามแต่งตัวอย่างขึ้นมาเอง
**ไม่รวม lane AI/Infra:** calibrate แล้วใน `faa04d2`

---

## 3. วิธีทำ (Vera)

### Step 1 — เก็บข้อมูล (ใช้ของเดิมก่อน)
ต่อ ticker เก็บข้อมูลเท่าที่เกณฑ์ต้องใช้:

| ข้อมูล | ใช้กับเกณฑ์ | แหล่ง (ลำดับ) |
|---|---|---|
| GICS Sector + Sub-Industry | ตัวกรองแรกทุกตัว | Wikipedia "List of S&P 500 companies" (มีคอลัมน์ GICS) → MSCI/S&P/Fidelity company page · **ห้ามใช้ Yahoo sector/industry** (เป็น Morningstar ไม่ใช่ GICS) |
| Recurring/subscription % ของ revenue + revenue growth YoY | SaaS | 10-K segment/revenue disaggregation → Atlas Data Package เดิม |
| EBIT 10 ปี (peak→trough ล่าสุด, CV ของ EBIT margin) | Cyclical | macrotrends / stockanalysis income statement |
| Segment revenue (หรือ EV) | Holding | 10-K segment note |
| rNPV pipeline vs EV | Biotech | report/agent_notes เดิมของ REGN/ABBV ถ้ามี — ไม่มีให้ใช้ "pipeline revenue share" เป็น proxy และ flag |
| Regulated revenue % | Utility | (ไม่มีในกลุ่ม) |
| PV(TV)/EV | หุ้นลงทุนหนัก | **เฉพาะจาก Emma DCF ใน report เดิม** — ห้ามคำนวณใหม่ · ไม่มี = `N/A (no DCF)` |

- ใช้ตัวเลขใน `reports/` และ `agent_notes/atlas/*_data.md` เดิมก่อน (มี URL อยู่แล้ว) — WebSearch เฉพาะที่ขาด
- ทุกตัวเลขมี URL + วันที่ข้อมูล · ตัวเลขเก่าใช้ได้ (นี่คือ calibration ไม่ใช่ trade) แต่ระบุวันที่
- หาไม่ได้หลังค้นแหล่งตามตาราง → `DATA_INSUFFICIENT` (ห้ามเดา)

### Step 2 — จัดประเภทตามเกณฑ์ตัวอักษร
ต่อ ticker บันทึก:
- เข้าเกณฑ์ประเภทไหนบ้าง (**ทุกประเภทที่เข้า** ไม่ใช่แค่ตัวแรก)
- ประเภทหลักที่เลือก + กติกาที่ใช้ตัดสินเมื่อเข้าหลายประเภท (CLAUDE.md: "ตรงกับแหล่งมูลค่าหลัก >50% ของ EV")
- ระยะห่างจาก threshold ของทุกเกณฑ์ตัวเลขที่เช็ค (เช่น recurring 58% vs เกณฑ์ 60% = −2pp)

**ห้ามใช้ดุลยพินิจปรับผล** — ถ้าเกณฑ์ตัวอักษรให้ผลที่ดูแปลก ให้บันทึกผลตามตัวอักษร แล้วเขียนความเห็นแยกในคอลัมน์ note

### Step 3 — Commit ผล Step 1–2 ก่อน แล้วค่อยเปิดไฟล์ expected
1. เขียนผลลง `agent_notes/vera/2026-10-XX_classification_calibration.md` (§4 ตาราง A)
2. **commit + push ก่อน** (git timestamp เป็นหลักฐานว่าจัดเสร็จก่อนเห็นค่าที่คาด)
3. **จากนั้นเท่านั้น** เปิด `agent_notes/charlie/2026-10-13_opus_classification_expected.md` แล้วทำ Step 4

> ไฟล์ expected แยกออกมาเพื่อกัน Vera ถูก anchor — หลักเดียวกับ VS2 1.5. **Hermes: ห้ามส่งเนื้อหาไฟล์ expected ให้ Vera ก่อน Step 3.2**

### Step 4 — เทียบ + วิเคราะห์
ทุกตัวที่ผลไม่ตรงกับ expected → จัดเป็น 1 ใน 3:
- **เกณฑ์ผิด** (threshold/ตัวกรองไม่จับธรรมชาติธุรกิจ) — เสนอการแก้
- **Expected ผิด** (Opus คาดผิด, เกณฑ์ถูก) — อธิบาย
- **กำกวมจริง** (ทั้งสองทางสมเหตุสมผล) — ระบุว่าต้องการกติกาอะไรเพิ่ม

---

## 4. Output (`agent_notes/vera/2026-10-XX_classification_calibration.md`)

**ตาราง A — ผลจัดประเภท (ทำก่อนเห็น expected)**

| Ticker | GICS Sub-Industry | เข้าเกณฑ์ประเภท | ประเภทหลัก | ตัวเลขสำคัญ vs threshold | Source + วันที่ | Note |
|---|---|---|---|---|---|---|

**ตาราง B — เทียบ expected (หลัง Step 3.2)**

| Ticker | ผลเกณฑ์ | Expected | ตรง? | จัดเป็น (เกณฑ์ผิด / expected ผิด / กำกวม) | เหตุผล |
|---|---|---|---|---|---|

**สรุปตัวชี้วัด:**

| ตัวชี้วัด | ผล | เกณฑ์ผ่าน |
|---|---|---|
| % ที่ได้ประเภทหลักครบ (ไม่ `PENDING`) | | ≥ 90% |
| % ที่เข้า ≥2 ประเภท | | ≤ 25% (เกินนี้ = ต้องมีกติกา precedence ชัดกว่านี้) |
| % ตรงกับ expected | | ≥ 80% (ไม่ตรงที่เป็น "expected ผิด" ไม่นับเป็นความผิดของเกณฑ์) |
| Threshold ที่มีหุ้น ≥3 ตัวอยู่ภายใน ±20% ของเส้น | ระบุ threshold | ไม่มี = เสถียร |

**ส่วนสุดท้าย — ข้อเสนอแก้เกณฑ์** (ถ้ามี): ระบุเกณฑ์ · ค่าปัจจุบัน → ค่าที่เสนอ · ticker ที่เป็นหลักฐาน · ผลข้างเคียง (มีตัวไหนจะย้ายประเภทบ้าง) — **ส่ง Opus review ห้ามแก้ CLAUDE.md เอง**

ปิดท้าย `*Vera — YYYY-MM-DD | Classification Calibration (VS2)*`

---

## 5. ประเด็นที่ Opus รู้ล่วงหน้าว่าน่าจะเจอ (ให้ Vera ตรวจยืนยัน ไม่ใช่สมมติว่าจริง)

1. **หุ้นลงทุนหนักจัดก่อน Emma ไม่ได้** — เกณฑ์ PV(TV)/EV > 70% ต้องมี DCF ของ Emma ก่อน แต่ CLAUDE.md บอกว่า Atlas จัดประเภทและล็อกก่อน Emma เริ่ม → ขัดกันเชิงลำดับ. Vera บันทึกว่ากี่ตัวในกลุ่มตัวอย่างที่ประเภทจะเปลี่ยนเมื่อรู้ PV(TV)/EV (เทียบกับ report เดิม) — ใช้ประกอบการแก้ (ข้อเสนอเบื้องต้นของ Opus: ให้ "หุ้นลงทุนหนัก" เป็น **overlay** ที่ trigger อัตโนมัติหลัง DCF ไม่ใช่ประเภทที่ Atlas จัด — รอผล calibration ก่อนเสนอเข้า CLAUDE.md)
2. **GICS Financials ที่ไม่ใช่ธนาคาร/ประกัน** (V, MA, ICE, FICO ถ้าอยู่ Financials) — เกณฑ์ปัจจุบันจัดเฉพาะ Banks/Insurance ส่วนที่เหลือตกเป็น "ทั่วไป" — ตรวจว่าเป็นผลที่ต้องการไหม
3. **Managed care** (OSCR, CNC) — GICS อยู่ Health Care ไม่ใช่ Insurance แต่ตาราง VS2 เดิมยกตัวอย่าง OSCR เป็น "ธนาคาร/ประกัน" → เกณฑ์ใหม่อาจขัดกับตัวอย่างในตารางเดิมเอง
4. **SaaS ที่โตช้าลง** (CRM, ADBE) — เกณฑ์ growth >15% อาจตัดออก ทั้งที่เหตุผลของวิธี (SBC/deferred revenue บิด FCF) ยังใช้ได้เต็มที่ — ตรวจว่า growth ควรเป็นเกณฑ์ของประเภทนี้หรือไม่
5. **Holding criterion จับผิดตัว** — บริษัทที่มี ≥3 segment แต่ธุรกิจเกี่ยวข้องกัน (เช่น ICE, AMZN) อาจเข้าเกณฑ์ตัวเลข — คำว่า "ไม่เกี่ยวข้องกัน" ยังไม่มีนิยามเชิงตัวเลข

---

## 6. ขอบเขต + ต้นทุน

- คาด ~26 ticker × 1–3 WebSearch (หลังใช้ข้อมูลเดิม) — ถ้าเกิน ~60 searches ให้หยุดที่ ticker ที่ทำครบแล้ว รายงานผลบางส่วน + ระบุว่าเหลือตัวไหน
- ไม่แตะ `dashboard/`, `portfolio/`, `performance/tracker.md`
- Commit 2 ครั้ง: (1) ตาราง A ก่อนเปิด expected (2) ตาราง B + สรุป + ข้อเสนอ → push ทั้งสองครั้ง

*Opus 5.5 — 2026-10-13 | Brief สำหรับ Vera calibration · Opus ไม่รันเอง*
