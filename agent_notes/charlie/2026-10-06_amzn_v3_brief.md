# AMZN v3 — Business-Type-Correct Re-run (Learning run, CIO approved 2026-10-06)

> ร่างโดย Opus 2026-10-06 — Sonnet อ่านจากไฟล์นี้โดยตรง ห้าม copy จากแชท
> **ไม่ใช่ trial data ของ LANE-AI-INFRA** (CLAUDE.md § Lane ข้อ 5 — ห้ามนับ AMZN) · เป็นงานเรียนรู้: "ถ้าใช้เครื่องมือที่ถูกกับธุรกิจประเภทนี้ ผลต่างจาก v1/v2 แค่ไหน และเพราะอะไร"
> Re-analysis file rule (กฎเหล็ก 11): append Update Log ใน `reports/AMZN_2026-10-06_v2_rerun.md` หรือสร้างไฟล์ v3 ตาม precedent v2 — เลือกแบบเดียวกับ v2 เพื่อให้เทียบกันได้ · dashboard/data.js แทนที่ object เดิม ห้ามซ้อน

## ทำไมต้องรันใหม่ (จุดอ่อนของ v1/v2)
1. TGR exception ใน v2 ทดสอบด้วย **trailing company-level ROIC vs WACC** — v2 รัน 14:04 ก่อนกฎ in-service/incremental ROIC (`e167bfb` 15:22) → ใช้เกณฑ์ที่เรายอมรับแล้วว่าผิดสำหรับ build-out
2. Bear ข้อหลัก "ROIC ครึ่งหนึ่งของ GOOGL/MSFT ทั้งที่ capex 2x" = วงกลม: capex หนัก → CIP อยู่ในตัวหาร → ROIC ต่ำ → ถูกลงโทษซ้ำ
3. ROIC/margin รวมบริษัทเอา AWS (op margin ~39%) ปนกับ retail (margin บาง) → ควรแยกประเมิน
4. WACC 11.2% (β 1.44) อยู่นอกกรอบ mega-cap 7–9% ใน CLAUDE.md — ไม่เคยถูก challenge

## ⚠️ Anti-goal-seeking (บังคับ — อ่านก่อนเริ่ม)
- **ล็อกวิธีการทั้งหมดในไฟล์นี้ก่อนดูผล** — ห้ามเปลี่ยนวิธี/peer/ตัวเลขหลังเห็น FV
- CIO มีความเห็นว่า AMZN ระยะยาวไม่น่าอยู่แค่ $200 — **นั่นคือ hypothesis ที่ v3 ทดสอบ ไม่ใช่คำตอบที่ต้องได้** ถ้า v3 ยังได้ FV ใกล้ $200 → รายงานตามจริงพร้อมเหตุผล
- Peer/segment multiple ต้องเลือกก่อนคำนวณ (ตาม peer-selection guideline B-V1) และบันทึกเหตุผล
- Return-side locked rules ไม่เปลี่ยน (40/30/30, MOS threshold, conviction gate)

## Pipeline: Atlas → Emma ∥ Quinn → Bear → Charlie → Morgan (ตามปกติ, ราคาสด ≥2 sources)

### Atlas — Data Package เพิ่มเติม
- Segment reporting จาก 10-K/10-Q ล่าสุด: revenue, operating income, **capex และ assets ต่อ segment** (AWS / North America / International; ads ถ้าแยกเปิดเผยได้ — ถ้าไม่มีให้ระบุว่าเป็น estimate พร้อมที่มา)
- PP&E แยก **construction in progress (CIP)** vs in-service (10-K PP&E note)
- Beta จาก ≥3 แหล่ง (เช่น stockanalysis, Yahoo, Morningstar/GuruFocus) + 10Y Treasury + ERP source
- Classification เข้า LANE-AI-INFRA หรือไม่ (รายงาน PASS/FAIL/DATA_INSUFFICIENT ตาม patch3) — ใช้เพื่อเลือกเครื่องมือเท่านั้น ไม่นับ trial

### Emma — วัดด้วยเครื่องมือของ build-out
1. **ROIC บน in-service capital** (หัก CIP ออกจาก invested capital) — company-level และ AWS-level
2. **Incremental ROIC 3 ปี และ 5 ปี** (ΔNOPAT ÷ Δinvested capital) แสดงทั้งคู่
3. **Sum-of-the-parts:** AWS (DCF แยก หรือ EV/EBIT จาก peer cloud ที่เลือกก่อน) + Retail NA/Intl (EV/Sales หรือ EV/EBIT จาก peer retail) + Ads (ถ้าแยกได้) − net debt
4. Consolidated DCF แสดง **ROIC recovery path รายปี** + capex/revenue path ที่ normalize ลงเมื่อ build-out จบ
5. **WACC reconciliation:** แสดง WACC จาก β ทั้ง 3 แหล่ง + bottom-up β (peer unlevered) → เลือก 1 ค่าพร้อมเหตุผล; ถ้ายังอยู่นอก 7–9% ต้องอธิบายว่าทำไม
6. TGR: ทดสอบ capex-cycle exception ใหม่ด้วยเกณฑ์ `e167bfb` (in-service + incremental ROIC)

### Quinn
- Sensitivity 5×5: **WACC × AWS growth** (แทน Yr1 growth × WACC เดิม)
- **Reverse DCF:** ที่ราคาปัจจุบัน ตลาด price-in growth/margin/WACC เท่าไหร่
- **Forward value path:** FV ณ ปี 2027 / 2029 / 2031 (ใน base case) — ตอบคำถาม "ระยะยาวมูลค่าไปถึงไหน" แยกจาก "วันนี้ควรจ่ายเท่าไหร่"
- P-W EV 3 scenario; Bear scenario ≥25% และรวมกรณี capex ไม่ได้ผลตอบแทน

### Bear
- แยก Temporary/reinvestment vs Structural ทุกข้อ (กฎ Bear Discount Classification)
- ห้ามใช้ trailing ROIC รวมบริษัทเป็นหลักฐาน impairment — ถ้าจะแย้งเรื่องผลตอบแทน capex ต้องใช้ incremental/in-service ROIC
- Thesis Invalidation ผูก milestone + วันที่ (เช่น AWS growth / AWS margin / backlog ในไตรมาสที่ระบุ)
- Bear ยังต้องแย้งจริง — เช่น AWS share loss, antitrust, capex overbuild ทั้งอุตสาหกรรม

### Charlie — ส่วนบังคับใน report
**ตารางเทียบ v1 / v2 / v3:**

| | v1 (เช้า) | v2 (14:04) | v3 | Δ v3 vs v2 | สาเหตุ |
|---|---|---|---|---|---|
| Emma FV | $230.63 | $230.63 | | | |
| Quinn P-W EV | $203.50 | $203.50 | | | |
| Bear FV | $159.72 | $156.27 | | | |
| Blended FV | $201.22 | $200.18 | | | |
| MOS | -20.3% | -21.4% | | | |
| WACC | 11.2% | 11.2% | | | |
| TGR | 3.0% | 3.0% | | | |
| Conviction avg | 5.33 | 5.40 | | | |
| Verdict | NO BUY | NO BUY | | | |

**Attribution:** แยกว่า Δ มาจากแต่ละการเปลี่ยนแปลงเท่าไหร่ (in-service ROIC/TGR · SOTP · WACC · Bear reclassification) — ทำทีละตัวแบบ step-by-step

**"มูลค่าวันนี้ vs ราคาระยะยาว":** อธิบายภาษาง่ายว่า Blended FV = ราคาที่ควรจ่ายวันนี้เพื่อได้ผลตอบแทน = WACC ไม่ใช่ราคาเป้าระยะยาว + แสดง forward value path ของ Quinn

### Morgan
- ตรวจ anti-goal-seeking: วิธี/peer ตรงกับไฟล์นี้, ไม่มีการเปลี่ยนหลังเห็นผล
- ตรวจ segment numbers + CIP กับ 10-K
- ตรวจ WACC reconciliation

## ผลลัพธ์
- ถ้า v3 ผ่าน gate → ไม่ deploy อัตโนมัติ — Max ต้องปฏิบัติตาม Regime Gate + Max Consultation Rule ปกติ และ flag ให้ CIO เห็นก่อน (เพราะเป็น learning run บน CIO-override ticker)
- ไม่ว่าผลเป็นอย่างไร → Leo บันทึก lesson สั้นๆ ใน learning-log.md: "เครื่องมือแบบไหนเปลี่ยนผลแค่ไหน"
- Commit + push · รายงานกลับ: ตาราง v1/v2/v3 + attribution + verdict

*Opus — 2026-10-06 | AMZN v3 brief, CIO approved item 1*
