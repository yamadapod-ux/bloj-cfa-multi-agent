# Rule Draft: Segment / SOTP Consistency (Morgan QA + Emma)

> ร่างโดย Opus 2026-10-07 — CIO approved · Sonnet อ่านจากไฟล์นี้โดยตรง ห้าม copy จากแชท
> ใส่ใน 2–3 ที่ ข้อความเดียวกัน: (1) `CLAUDE.md` § Morgan QA Protocol → เพิ่ม subsection ใหม่ต่อจาก "Source Annotation" (2) `.claude/agents/morgan.md` (checklist) (3) `.claude/agents/emma.md` (หลักการทำ DCF/SOTP) ถ้ามีส่วน valuation method
> **ไม่ใช่ Return-side rule** — ไม่แตะ 40/30/30, MOS threshold, conviction gate · เป็น QA/methodology consistency เท่านั้น

## ที่มา
AMZN v3.1 (`eb115ac`): consolidated DCF EV $669.7B < AWS-only DCF EV $1,247.8B → implied retail+ads NOPAT 2035 ≈ −$39B (เป็นไปไม่ได้). Emma เฉลี่ย DCF $68 กับ SOTP $191 (ห่าง ~2.8x) โดยไม่ reconcile, Morgan ให้ PASS. ข้อผิดประเภทนี้เกิดซ้ำได้กับทุกบริษัทหลายธุรกิจ (AMZN, GOOGL, MSFT, conglomerates)

## ข้อความที่เพิ่ม

### Multi-Segment Consistency (บังคับ — เมื่อ report มีทั้ง SOTP และ consolidated DCF หรือมี segment model ใดๆ)
1. **Bottom-up ก่อน:** ถ้ามี segment model (เช่น segment DCF) อยู่ใน report → consolidated DCF ต้องสร้างจากผลรวมของ segment (revenue, EBIT, capex, D&A) หรือ reconcile ได้กับผลรวมนั้นทุกปีของ forecast — consolidated margin เป็น **ผลลัพธ์** ไม่ใช่ input อิสระ
2. **Sanity:** ห้ามมี segment ที่ implied NOPAT/EBIT ติดลบใน forecast โดยไม่มีเหตุผล + source (เช่น guidance ว่าจะขาดทุน) · consolidated EV ต้องไม่ต่ำกว่า segment ใดๆ เพียงส่วนเดียวเว้นแต่ส่วนอื่นมีมูลค่าติดลบที่อธิบายได้
3. **ห้ามเฉลี่ยก่อน reconcile:** ถ้า 2 วิธีของ analyst คนเดียวกัน (เช่น DCF vs SOTP) ห่าง ≥ 25% → reconciliation table (สาเหตุของ gap ทีละรายการ) ก่อนเฉลี่ยหรือเลือก — ขยายหลักเดียวกับ DCF Cash Flow Consistency Rule ข้อ 4 (ซึ่งครอบคลุมแค่ Emma vs Quinn)
4. **Independence ของ Blended FV:** Quinn P-W EV scenario และ Bear FV ต้องเป็น valuation ของผู้นั้นเอง (assumption ระบุชัด) — ห้ามใช้ FV สุดท้ายของ analyst อื่นเป็น scenario โดยตรง เพราะทำให้ตัวเลขเดียวกันถูกนับซ้ำใน 40/30/30
5. **Bear floor sanity:** ถ้า FV ใดต่ำกว่า no-growth value (NOPAT ปัจจุบัน ÷ WACC) → ต้องอธิบายว่า assumption ไหนทำให้การลงทุนใหม่ได้ RONIC < WACC และต้องสอดคล้องกับ Bear Discount Classification (Temporary vs Structural) ของรายงานเดียวกัน

**Morgan reject type:** ข้อ 1–2 ไม่ผ่าน = `SANITY_FAIL` · ข้อ 3–5 ไม่ผ่าน = `RULE_VIOLATION`

## งานตามมา
- Commit ไฟล์นี้พร้อมการแก้ · ข้อความ commit อ้าง `segment-consistency rule`

*Opus — 2026-10-07 | Draft only, not applied*
