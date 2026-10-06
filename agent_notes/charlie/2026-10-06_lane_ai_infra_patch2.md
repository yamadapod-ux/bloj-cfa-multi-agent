# Patch 2: LANE-AI-INFRA classification fixes (หลัง Vera calibration faa04d2)

> ร่างโดย Opus 2026-10-06 — Sonnet อ่านจากไฟล์นี้โดยตรง ห้าม copy จากแชท
> แก้ 2 ไฟล์: `CLAUDE.md` (section Business-Type Lane ข้อ 1) และ `.claude/agents/atlas.md` (Lane Classification block) — ข้อความเกณฑ์ต้องตรงกันทั้งสองไฟล์

## เหตุผล
1. **Calibration 3/10 ที่เข้า lane เป็น REIT ทั้งหมด (EQIX, DLR, IRM)** — REIT ทำ capex หนักเป็นธุรกิจปกติ จึงผ่านเกณฑ์ capex ได้โดยธรรมชาติ แต่ REIT ควรวัดด้วย P/AFFO / NAV ไม่ใช่ ROIC recovery path → lane จับผิดประเภทธุรกิจ (ปัญหาเดียวกับที่ lane นี้ตั้งใจแก้)
2. **Capex growth ≥30% ไม่มีพื้นขั้นต่ำ** → บริษัทที่ capex ฐานเล็กมาก (เช่น equipment supplier อย่าง AMAT) ผ่านเกณฑ์ข้อ 1 ได้ แม้จะถูกข้อ 2/3 กรองออกในรอบนี้

## (A) แก้เกณฑ์ bullet แรกของ Classification

**BEFORE:**
- Capex/Revenue ≥ 15% (TTM) **หรือ** capex โต ≥ 30% YoY

**AFTER:**
- Capex/Revenue ≥ 15% (TTM) **หรือ** (capex โต ≥ 30% YoY **และ** Capex/Revenue ≥ 8% TTM)

## (B) เพิ่มบรรทัดใหม่ ต่อจาก "ไม่ผ่านครบ → ใช้ Filter เดิม"

**ไม่รวม (exclusion):** REIT และ regulated utilities ไม่เข้า lane นี้แม้ผ่านครบ 3 ข้อ — ธุรกิจเหล่านี้ capex หนักโดยโครงสร้างและมีวิธีวัดเฉพาะของตัวเอง (REIT: P/AFFO, NAV · Utilities: DDM, rate base growth, allowed ROE) → ใช้ Filter เดิมไปก่อนจนกว่าจะมี lane ของตัวเอง

## (C) Open question — บันทึกเท่านั้น ห้ามแก้กฎ

เพิ่มท้ายไฟล์ calibration ของ Vera (commit faa04d2) ใต้หัวข้อ "Open Questions for 2026-12-31 review":

- **Segment-level vs consolidated-level (เกณฑ์ข้อ 3):** บริษัทหลาย segment (เช่น AMZN: AWS ~33.5% ของ revenue growth) ไม่ถึง 40% ที่ระดับบริษัท. **ไม่แก้เกณฑ์ตอนนี้** เพราะ AMZN คือ ticker ต้นเรื่อง — แก้เพื่อให้มันเข้า lane = goal-seeking. ทางที่ถูกหลักคือ **SOTP** (segment build-out วัดด้วยเครื่องมือ lane นี้, segment อื่นวัดแบบมาตรฐาน, รวม FV) ไม่ใช่ลดเกณฑ์ทั้งบริษัท. **พิจารณาเพิ่มกฎ SOTP เฉพาะเมื่อ scout รอบใหม่เจอบริษัทหลาย segment ที่ไม่ใช่ AMZN ≥ 2 ตัว** ที่ติดเกณฑ์ข้อ 3 แบบเดียวกัน

## หลังแก้
- ไม่ต้องรัน calibration ใหม่ทั้งหมด — แค่ระบุใน commit message ว่า EQIX/DLR/IRM จะกลายเป็น `STANDARD` ตาม exclusion ใหม่ (lane ใน calibration set เหลือ 0/10 เข้า — ถือว่าคาดได้ เพราะ set เดิมไม่ได้คัดมาสำหรับ lane นี้; การวัดจริงคือ scout รอบใหม่)
- Commit ไฟล์นี้พร้อมการแก้

*Opus — 2026-10-06 | Draft only, not applied*
