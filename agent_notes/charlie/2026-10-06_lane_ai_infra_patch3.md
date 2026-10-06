# Patch 3: LANE-AI-INFRA — DATA_INSUFFICIENT ≠ FAIL (reporting clarification)

> ร่างโดย Opus 2026-10-06 — Sonnet อ่านจากไฟล์นี้โดยตรง ห้าม copy จากแชท
> แก้ 2 ไฟล์ ข้อความเดียวกัน: `CLAUDE.md` (Business-Type Lane ข้อ 1 Classification — ต่อจากบรรทัด exclusion REIT/utility) และ `.claude/agents/atlas.md` (Lane Classification block)
> ไม่เปลี่ยนตัวเกณฑ์ 3 ข้อ — แค่กำหนดวิธีรายงานเมื่อหาข้อมูลไม่ได้

## ที่มา
Scout รอบแรกของ lane (2026-10-06): FLNC และ CIEN ถูกตัดออกโดยไม่มีตัวเลข capex ยืนยันเกณฑ์ข้อ 1 — ตัวที่ใช้ตัดสินจริงคือ "owner-operator vs equipment-seller" ซึ่งไม่มีในเกณฑ์ลายลักษณ์อักษร (judgment เพิ่มเอง)

## ข้อความที่เพิ่ม

**สถานะผลเกณฑ์แต่ละข้อ (บังคับ — เพิ่ม 2026-10-06):** ทุกเกณฑ์ต้องรายงานเป็น 1 ใน 3 สถานะเท่านั้น:
- `PASS` — มีตัวเลข + URL และผ่าน
- `FAIL` — มีตัวเลข + URL และไม่ผ่าน
- `DATA_INSUFFICIENT` — หาตัวเลขไม่ได้ **หลังจาก**ค้นจากแหล่งบังคับแล้ว

**แหล่งบังคับก่อนจะใช้ `DATA_INSUFFICIENT` ได้:** Capex และ Revenue มีอยู่ในงบการเงินของบริษัทจดทะเบียนทุกแห่ง → ต้องค้นจาก **SEC 10-K/10-Q (cash flow statement: "Purchases of property and equipment")** หรือ stockanalysis.com / macrotrends cash-flow page ก่อน — ห้ามใช้ `DATA_INSUFFICIENT` กับ capex/revenue ถ้ายังไม่ได้ลองแหล่งเหล่านี้

**ผลของ `DATA_INSUFFICIENT`:** classification ยังไม่สรุป (`PENDING`) — ห้ามนับเป็น `STANDARD` หรือ reject. ต้อง resolve ภายใน scout รอบเดียวกัน หรือบันทึกเป็น pending ใน watchlist.md พร้อมระบุว่าขาดข้อมูลอะไร

**ห้ามใช้เกณฑ์นอกลายลักษณ์อักษร:** การตัดสิน lane ใช้เฉพาะ 3 เกณฑ์ตัวเลข + exclusion REIT/utility เท่านั้น. ถ้า Atlas/Max เห็นว่ามีปัจจัยอื่นควรพิจารณา (เช่น owner-operator vs equipment-seller) → เขียนเป็น **note แยก** ให้ Bear/Morgan ใช้ประกอบ ห้ามใช้เป็นเหตุผลจัด lane

**Morgan check:** ถ้า classification ใช้เหตุผลที่ไม่อยู่ใน 3 เกณฑ์ + exclusion = `RULE_VIOLATION`

## งานตามมา (ไม่ใช่การแก้กฎ)
- Re-check FLNC และ CIEN: ดึง capex/revenue TTM จาก 10-K/10-Q แล้วรายงานสถานะ PASS/FAIL ตัวเลขจริง (คาดว่า FAIL ข้อ 1 แต่ต้องมีตัวเลขยืนยัน)
- IREN entry ใน deployment_log: ระบุให้ชัดว่าเป็น **scout-level screen (ไม่มี Blended FV)** ไม่ใช่ full pipeline — กัน Vera นับผิดใน Funnel Health
- Commit ไฟล์นี้พร้อมการแก้

*Opus — 2026-10-06 | Draft only, not applied*

---

## Follow-up หลังตรวจ commit `97e5938` (Opus — 2026-10-06)

> Sonnet อ่านจากไฟล์นี้โดยตรง — แก้ข้อความเท่านั้น **ไม่เปลี่ยนผลใดๆ** (IREN = NO BUY, BE/FLNC/CIEN/CWEN = REJECT คงเดิม) · ใช้ targeted Edit ห้าม Write ทับทั้งไฟล์

**ที่ทำถูกแล้ว (ไม่ต้องแตะ):** CLAUDE.md/atlas.md ตรงร่าง · แถว FLNC/CIEN มีตัวเลขจริง + ถอด ownership-structure ออกแล้ว · แถว IREN `deployment_log.md:921` · CWEN (ตกข้อ 3 ด้วยตัวเลข $0 — อยู่ในเกณฑ์)

### 1. IREN ยังถูกเรียก "full pipeline" อีก 3 จุด (Vera จะนับผิด)
- `portfolio/watchlist.md:6738` heading `## IREN Full Pipeline Result ...` → เปลี่ยนเป็น `## IREN Scout-Level Screen Result ...`
- `portfolio/deployment_log.md:928` (Rationale all 6) — "run through the full lane pipeline (Atlas-lock classification -> scout-filter-equivalent -> Bear -> Morgan QA)" → เขียนให้ตรงกับที่ทำจริง = scout-level screen, ไม่มี Blended FV
- `portfolio/deployment_log.md:930` (Max signature) — "IREN fast-tracked through full pipeline" → "IREN scout-level screen"
- ถ้าเจออ้าง "full pipeline" ของ IREN ที่อื่นใน watchlist.md § Round 74 / buy_list.md → แก้แบบเดียวกัน

### 2. เหตุผลนอกเกณฑ์ (equipment-seller / owner-operator) ยังเหลือ — ขัด Patch 3 ตรงๆ
- **BE** `deployment_log.md:923` และ `watchlist.md:6722` — ลบท่อน "Also fails the 'owns/operates own build-out' structural test ..." / คอลัมน์ "FAIL (โครงสร้าง...)" ออกจากเหตุผล reject → ย้ายไปเป็น note แยก (เช่น `Note for Bear/Morgan (ไม่ใช่เหตุผลจัด lane): ...`)
- บรรทัดสรุป `watchlist.md:6727`, `watchlist.md:6733`, `deployment_log.md:928` — "equipment-seller/capex-light pattern x3" → "ตกเกณฑ์ข้อ 1 (capex/revenue: BE ~4.7%, CIEN ~4.0%, FLNC ~0.55% — ต่ำกว่า 15% และ 8% floor)" · CWEN คงเดิม (ตกข้อ 3)
- หลักการ: เหตุผล reject ต้องอ้างได้แค่ 3 เกณฑ์ตัวเลข + exclusion REIT/utility

### 3. BE ตัวเลขไม่ใช่ TTM + แหล่งไม่ตรงแหล่งบังคับ
- ปัจจุบัน: Q2 2026 capex $0.05B ÷ Q2 revenue $1.065B (ไตรมาสเดียว แต่เขียนว่า TTM) จาก frontier.eninvs.com
- แก้: ดึง capex TTM + revenue TTM จาก stockanalysis.com cash-flow statement (หรือ SEC 10-Q) ให้เหมือน FLNC/CIEN แล้วแทนตัวเลขทั้ง 2 ไฟล์ — คาดว่ายัง FAIL ห่างเกณฑ์มาก ถ้าผลกลับเป็น PASS → หยุดและแจ้ง CIO ก่อน ห้ามเปลี่ยนผลเอง

### เมื่อเสร็จ
- Commit + push ข้อความ commit อ้าง `patch3 follow-up`
- รายงานกลับ: list จุดที่แก้ (file:line) + ตัวเลข BE TTM ใหม่พร้อม URL

*Opus — 2026-10-06 | Follow-up instructions for Sonnet, post-review of 97e5938*
