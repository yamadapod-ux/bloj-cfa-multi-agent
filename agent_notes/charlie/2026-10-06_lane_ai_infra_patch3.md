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
