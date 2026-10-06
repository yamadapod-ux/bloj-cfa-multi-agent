# Draft: Business-Type Lane AI/Infra Build-out + TGR capex-cycle alternative

> ร่างโดย Opus 2026-10-06 สำหรับให้ Sonnet นำไปแก้ไฟล์จริง — **อ่านจากไฟล์นี้โดยตรง ห้าม copy จากแชท**
> ไฟล์ที่ต้องแก้: (A) `CLAUDE.md` (B) `.claude/agents/qa.md` (C) `.claude/agents/atlas.md` (D) sync ย่อหน้า TGR exception ใน `CLAUDE.md` ให้ตรงกับ (B)

---

## (A) CLAUDE.md — เพิ่ม section ใหม่ ต่อท้าย "Tier 1.5 — Lane Assignment"

### Business-Type Lane: AI/Infra Build-out (`TRIAL` — เพิ่ม 2026-10-06, review 2026-12-31)

**ที่มา:** Filter A/C/D-Legacy/E2 calibrate มาสำหรับ mature business → คัดทิ้งบริษัทที่อยู่ระหว่าง build-out ทั้งกลุ่มโดยโครงสร้าง (0/155 fast-track). หลักการ CFA: valuation method ต้องเหมาะกับประเภทธุรกิจ. TRIAL lane เดียวก่อน — lane อื่นยังใช้ Filter เดิมทั้งหมด. **ไม่แตะ Return-side locked rules** (conviction gate / Growth MOS reverse-DCF ≤1.2× / 40-30-30 คงเดิม — lane นี้ *เพิ่ม* เกณฑ์ ไม่ได้ลด)

**1. Classification — Atlas เป็นผู้จัด (ไม่ใช่ Emma) โดยต้องจัดให้เสร็จก่อนที่ Emma จะเห็น Data Package และเมื่อจัดแล้วห้ามเปลี่ยนระหว่าง pipeline**

เข้า lane นี้ได้ต้องผ่าน **ครบ 3 ข้อ** (ตัวเลขพร้อม URL):
- Capex/Revenue ≥ 15% (TTM) **หรือ** capex โต ≥ 30% YoY
- Management เปิดเผย build-out program ชัดเจน — ขนาดเงิน + กรอบเวลา
- ≥ 40% ของ revenue growth มาจาก AI / data center / power / network / compute infrastructure

ไม่ผ่านครบ → ใช้ Filter เดิม. Morgan ตรวจ classification ซ้ำ — ถ้าเข้าเกณฑ์ไม่ครบ = `RULE_VIOLATION`

**2. Scout filters ที่แทนของเดิม (เฉพาะ lane นี้)**

| เดิม | แทนด้วย |
|---|---|
| Filter A (ลง ≥20% จาก high) | **ยกเว้น** — แต่ Growth MOS (reverse DCF ≤1.2×) ยังบังคับ |
| Filter C (ROIC ≥ 80% WACC) | **ROIC on in-service capital (หัก CIP) > WACC** **หรือ** **incremental ROIC 3 ปี และ 5 ปี (แสดงทั้งคู่) > WACC** |
| Filter D-Legacy (naive no-growth FV) | ไม่ใช้ — ใช้ข้อ 3 ด้านล่าง |
| Filter E2 (through-cycle ROIC +3pp) | **Runway:** เงินสด + committed financing ≥ 24 เดือนของ net capex burn **หรือ** core business FCF-positive ครอบ capex ได้ · **Dilution** ≤ 3%/ปี (เฉลี่ย 3 ปี) |
| B-Zero, E1 (moat), E3 (overhang) | **คงเดิม — ใช้เหมือน lane ปกติทุกประการ** |

**3. Valuation + MOS (ตัวเลขบังคับ)**
- Quinn ทำ P-W EV 3 scenario พร้อม probability ชัดเจน — **Bear scenario ต้องมี probability ≥ 25%** และต้องรวมกรณี "capex ไม่ได้ผลตอบแทน" (write-down / ROIC ไม่ฟื้น)
- **MOS ≥ 25% เทียบ Blended FV** (สูงกว่า Value 15% เพราะความไม่แน่นอนสูงกว่า) **และ** reverse DCF ≤ 1.2× (เดิม)
- Emma DCF ต้องแสดง **ROIC recovery path รายปี** ในช่วง explicit forecast — TGR ใช้ข้อยกเว้น 3.5–4% ได้ตาม qa.md ทางเลือก capex-cycle เท่านั้น

**4. Position sizing**
- T1 ≤ 4% (ไม่ใช่ 8–10%)
- T2/T3 เพิ่มได้เฉพาะเมื่อ **milestone ที่ระบุไว้ตอน T1 เกิดขึ้นจริงแล้ว** (เช่น capex เริ่มสร้าง revenue ตามที่ guide, margin ขึ้นตาม path)
- Bear ต้องเขียน **Thesis Invalidation ผูก milestone + วันที่** (เช่น "ถ้า Q4 2027 AI revenue < $X → exit")

**5. TRIAL measurement (Vera, review 2026-12-31)**
- บันทึก tag `LANE-AI-INFRA` ใน `portfolio/deployment_log.md`
- Track: จำนวนที่เข้า lane / ผ่านแต่ละด่าน / deploy / 6-month outcome เทียบกับ Filter เดิม
- **ห้ามนับ ticker ที่วิเคราะห์ไปแล้วก่อนวันนี้ (รวมถึง AMZN v1 และ v2) เป็น trial data** — ต้องเป็น scout ใหม่เท่านั้น
- **Calibration ก่อนใช้จริง (แนะนำ):** Vera ลองรันเกณฑ์ข้อ 1–3 ย้อนกับหุ้น AI/infra ที่เคย scout แล้วประมาณ 10 ตัว ดูว่ามีกี่ตัวที่เข้า lane และกี่ตัวที่ผ่าน — ต้องไม่หลวมจนผ่านหมด และไม่ตึงจนไม่มีตัวไหนผ่าน (ผลนี้เป็น calibration เท่านั้น ไม่นับเป็น trial data)

---

## (B) .claude/agents/qa.md — แทนที่เงื่อนไข TGR Conditional Ceiling Exception ทั้งก้อน

Emma อนุญาตให้ใช้ TGR สูงถึง **3.5–4%** (จากเดิม 3% ตายตัว) ได้ **เฉพาะ** เมื่อรายงานมีครบทั้ง 3 ข้อนี้:
1. **จัดเป็น wide-moat ชัดเจน** พร้อมตัวเลข ROIC-WACC spread ที่ยืนยันได้ว่า **>5pp ต่อเนื่อง ≥3 ปี**
   - **ทางเลือก (เพิ่ม 2026-10-06) — สำหรับบริษัทใน heavy-capex/reinvestment cycle:** ถ้า ROIC ปัจจุบันถูกกดจาก capex ที่ยังไม่ mature (J-curve) ให้พิสูจน์ข้อ 1 ด้วย **อย่างน้อย 1 ใน 2 วิธี** แทนได้ — ทั้งสองวิธีใช้ข้อมูลปัจจุบัน ห้ามใช้ ROIC ของปีในอดีตแทน:
     - **(a) ROIC on in-service capital:** invested capital **หัก** Construction-in-Progress / assets not yet placed in service (ตัวเลขจาก 10-K/10-Q ล่าสุด พร้อม URL) → spread ต้อง **>5pp**
     - **(b) Incremental ROIC:** ΔNOPAT ÷ ΔInvested Capital → ต้อง **> WACC +5pp** — คำนวณทั้งช่วง 3 ปี และ 5 ปี แสดงคู่กันเสมอ
   - **เงื่อนไขบังคับของทางเลือกนี้:** (i) capex cycle ต้องเปิดเผยชัดเจนโดย management พร้อมขนาดเงินและกรอบเวลา (ii) DCF ช่วง explicit forecast ต้องแสดง **ROIC recovery path รายปี** ให้เห็นว่าฟื้นถึงระดับไหนเมื่อไหร่ — TGR สะท้อน steady state หลัง cycle จบ ไม่ใช่ใช้ TGR สูงชดเชยช่วงลงทุน (iii) Bear ต้องแยก ROIC gap เป็นส่วน temporary (capex) vs structural — **ใช้ทางเลือกนี้ได้เฉพาะส่วน temporary**
2. **Sub-industry/segment ที่ growth มาจากนั้นมี secular growth >15% ต่อเนื่อง ≥3 ปี** โดยอ้างอิงแหล่งข้อมูลอิสระ (industry research เช่น Synergy Research, Gartner) **ไม่ใช่แค่ guidance ของบริษัทเอง**
3. Emma ต้อง **flag ชัดเจนในรายงานว่า "TGR เกินเพดานมาตรฐาน 3%, justification แบบมีเงื่อนไขอยู่ด้านล่าง"** เพื่อให้ Morgan ตรวจสอบได้ — **ถ้าใช้ทางเลือกข้อ 1 ต้อง flag เพิ่ม "ใช้ capex-cycle alternative วิธี (a)/(b)" + แสดงตัวเลขทั้งสองวิธีที่คำนวณได้ (ไม่ใช่แค่วิธีที่ผ่าน) + ROIC แบบปกติ (TTM) คู่กันเสมอ**

**Morgan check (ทางเลือกข้อ 1):** ตัวเลข CIP/ΔIC มี source URL · incremental ROIC แสดงทั้ง 3 ปี และ 5 ปี (กันเลือกช่วงที่ดีที่สุด) · มี ROIC recovery path ใน DCF · ถ้าไม่ครบ = `RULE_VIOLATION` → กลับไปใช้ TGR 3%

**เพิ่มใน checklist ของ Morgan (สำหรับ lane ใหม่):** ถ้ารายงานอยู่ใน lane `LANE-AI-INFRA` → ตรวจว่า Atlas classification ผ่านครบ 3 ข้อ (มี URL) และจัดก่อน Emma เริ่ม · MOS ≥ 25% · Bear scenario probability ≥ 25% · position T1 ≤ 4% — ข้อใดไม่ครบ = `RULE_VIOLATION`

---

## (C) .claude/agents/atlas.md — เพิ่มขั้นตอนใน Phase 2 Data Package (ก่อนส่งให้ Emma/Quinn)

**Business-Type Classification (บังคับ — เพิ่ม 2026-10-06 TRIAL):** ก่อนส่ง Data Package ให้ Emma/Quinn ทุกครั้ง Atlas ต้องเขียน block "🏷️ Lane Classification" ไว้ต้น Data Package:
- Capex/Revenue TTM = X% (URL) · Capex YoY = Y% (URL)
- Build-out program ที่ management เปิดเผย: ขนาด $ + กรอบเวลา (URL) หรือ "ไม่มี"
- สัดส่วน revenue growth จาก AI/data center/power/network/compute = Z% (URL)
- **ผล: `LANE-AI-INFRA` (ผ่านครบ 3/3) หรือ `STANDARD` (ไม่ครบ)**

Classification นี้ล็อกตลอด pipeline — Emma/Quinn/Bear ห้ามเปลี่ยน ถ้าไม่เห็นด้วยให้ flag ใน notes ให้ Morgan ตัดสิน

---

*Opus — 2026-10-06 | Draft only, not applied*
