# Brief สำหรับ Hermes (Sonnet): แก้ agent files ตาม Validation Framework

*Opus 5.5 → Hermes (Sonnet) · 2026-10-13*
*ต่อจาก: CLAUDE.md commit `e4bc4db` (VS2 ข้อ 1.5–1.7, เกณฑ์จัดประเภท, Vera ข้อ 7, Multi-Segment 5 rename, reconcile ตัวตรวจ) — brief เดิม `2026-10-13_opus_brief_validation_framework_claudemd.md`*
*เป้าหมาย: ให้ agent ทำตามกฎใหม่จริง — ตอนนี้กฎอยู่ใน CLAUDE.md แต่ไม่มี agent file ไหนสั่งให้ทำ*

---

## หลักการแก้ (ทุกจุด)

- **targeted Edit เท่านั้น** ห้าม Write ทับทั้งไฟล์ (เคยเสีย tracker.md 75% จาก Write ทับมาแล้ว)
- **ยึดรูปแบบเดิม:** agent files ใช้บรรทัด `**VS2:** ...` สั้นๆ ชี้กลับ CLAUDE.md — ทำแบบเดียวกัน ไม่คัดลอกกฎเต็มมาซ้ำ (กันสองที่ขัดกันในอนาคต)
- ทุกจุดที่เพิ่มติด `TRIAL` — review 2026-12-31
- **ไม่แตะ:** 40/30/30, MOS threshold, conviction gate, TGR ceiling, Lane AI/Infra block เดิมใน atlas.md
- Morgan = ไฟล์ `.claude/agents/qa.md` (ไม่มี morgan.md)

---

## จุดออกแบบที่ต้องเข้าใจก่อนแก้ (ลำดับของ 1.7 ใน pipeline)

CLAUDE.md ข้อ 1.7 trigger (ก) เขียนว่า "ก่อน Max execute BUY จริง" — brief นี้วาง 1.7 ไว้ **หลัง Charlie เขียน report แล้ว ก่อน Morgan QA** (เฉพาะ report ที่ recommendation = BUY) เหตุผล: ถ้ารันหลัง Morgan PASS, Morgan จะตรวจผล 1.7 ไม่ได้ และถ้าผลห่าง >10% ต้องย้อนแก้ report ที่ PASS ไปแล้ว. ยังสอดคล้องกับ CLAUDE.md เพราะเกิดก่อน Max execute อยู่ดี

Trigger (ข) (หุ้นถืออยู่ที่ re-verify แล้ว MOS พลิกเครื่องหมาย) — Max ตรวจพบใน Re-Analysis Trigger Check → ขอ Charlie dispatch 1.7 ก่อนเสนอ sell/trim ใดๆ

---

## การแก้ 9 จุด

### A1 — `atlas.md`: block Business-Type Classification + Pre-registration (ใหม่)

**ตำแหน่ง:** หลังบรรทัด `**VS2 Data Package (บังคับ):** WACC package ...` (บรรทัด ~454) ก่อน `---` / `## I. Data Quality Notes`

**ข้อความ:**
```markdown
**VS2 Business-Type Classification (บังคับ `TRIAL` — ดู CLAUDE.md § เกณฑ์จัดประเภท + เหตุผลของวิธี):** เขียนไว้ต้น Data Package ถัดจาก Lane Classification
- จัดด้วย GICS ก่อน → ใช้เกณฑ์ตัวเลขเมื่อ GICS แยกไม่ออก (SaaS: recurring ≥60% + growth >15% · Cyclical: EBIT peak→trough ≥30% หรือ CV margin ≥0.3 · Biotech: rNPV pipeline >50% EV · Holding: ≥3 segment ≥15% · Utility: regulated ≥50%) — ทุกตัวเลขมี URL
- ระบุ: ประเภทหลัก · ประเภทรอง (ถ้ามี) · วิธีหลัก + ตัวตรวจ ตามตาราง "วิธีคำนวณตามประเภทหุ้น"
- จัดจาก business/financial data เท่านั้น ก่อน Emma เริ่ม — ล็อกตลอด pipeline (หลักเดียวกับ Lane Classification)
- ข้อมูลไม่พอจัด → `PENDING` + ระบุว่าขาดอะไร (ห้ามเดา)

**VS2 Pre-registration (บังคับ `TRIAL` — ดู CLAUDE.md ข้อ 1.5):** block `🔒 Pre-registered Judgment Calls` ใน Data Package — ล็อกก่อนส่งให้ Emma/Quinn/Bear:

| Judgment call | ค่าที่ล็อก | เหตุผล/source |
|---|---|---|
| แหล่ง WACC ภายนอกที่นับ (รายชื่อ) | | |
| เกณฑ์ stale-rate (bps) | | |
| วิธีเลือกเมื่อ beta 2 วิธีห่าง >150bps | | |
| Peer list (เลือกก่อนดู multiple ตาม B-V1 guideline) | | |
| ประเภทธุรกิจ | | |
| ความยาว explicit forecast + มี fade หรือไม่ | | |

- Atlas ห้ามคำนวณ/ดู FV ใดๆ ก่อนกรอก block นี้เสร็จ
- **Raw-data completeness (สำหรับ 1.7):** Section A–D + F ต้องมีตัวเลขดิบครบพอให้คนอื่นคำนวณ WACC + DCF ใหม่เองได้โดยไม่ต้องเห็น Locked WACC/peer list (Rf, ERP + URL, raw beta, D/E, งบ 3 ส่วน, shares, net debt, lease)
```

### A2 — `emma.md`: ตาราง 1.6 + ตัวตรวจเป็นตัวเลข + ใช้ค่า pre-registered

**ตำแหน่ง:** หลังบรรทัด `**VS2:** ใช้ Locked WACC/bridge/net debt/shares จาก Atlas เท่านั้น ...` (บรรทัด ~40) ก่อน `**Relative Valuation:**`

**ข้อความ:**
```markdown
**VS2 Validation (`TRIAL` — ดู CLAUDE.md ข้อ 1.5–1.6):**
- ใช้ค่าใน `🔒 Pre-registered Judgment Calls` ของ Atlas · ถ้าจำเป็นต้องเปลี่ยน → บันทึก: เปลี่ยนอะไร · ก่อน/หลังเห็นผล · FV ก่อน/หลัง (ห้ามเปลี่ยนเงียบ)
- ทำตาราง **Judgment-Call Sensitivity** ทุกรายงาน: เปลี่ยนทีละจุด (ทุกจุดที่ pre-register + จุดอื่นที่กระทบ) → FV ถ้าเลือกอีกทาง + Δ% ของ Blended FV · จุดใด >15% → ค่าที่ใช้ต้องมี source ≥2
- **ตัวตรวจ (cross-check) ตามประเภทธุรกิจต้องรายงานเป็นตัวเลข** ไม่ใช่แค่ชื่อวิธี · วิธีหลัก vs ตัวตรวจห่าง ≥25% → reconciliation table ทดสอบทั้งสองทิศก่อนสรุป
- ยืนยันว่าหุ้นเข้าเกณฑ์ประเภทที่ Atlas จัดจริง (ตัวเลข + URL) — ไม่ต้องอธิบายเหตุผลระดับประเภทซ้ำ · ไม่เห็นด้วย → flag ใน notes ให้ Morgan (ห้ามเปลี่ยนเอง)
```

### A3 — `emma.md`: Blind Re-derivation Mode (ใหม่)

**ตำแหน่ง:** ก่อน `## Data Package (บังคับ — อ่านก่อนวิเคราะห์ทุกครั้ง)` (บรรทัด ~95)

**ข้อความ:**
```markdown
## 🙈 Blind Re-derivation Mode (`TRIAL` — ดู CLAUDE.md ข้อ 1.7 · ใช้เมื่อ prompt จาก Charlie ขึ้นต้นด้วย `BLIND RE-DERIVATION`)

โหมดนี้ **override** กฎ Data Package ด้านล่าง:
- อ่าน **เฉพาะ** ไฟล์ blind input ที่ Charlie ระบุ (`agent_notes/charlie/YYYY-MM-DD_TICKER_blind_input.md`)
- **ห้ามอ่าน:** `reports/`, `agent_notes/*/` ไฟล์อื่นของ ticker นี้, Data Package ของ Atlas, `portfolio/`, `dashboard/`, `learning-log.md`
- **ห้าม WebSearch:** analyst price target, consensus FV, บทความ valuation, รายงานของทีม — WebSearch ได้เฉพาะข้อมูลดิบที่ input ขาด (เช่น Damodaran unlevered beta ของอุตสาหกรรม) พร้อม URL
- คำนวณ WACC เอง (Blume + bottom-up beta ตาม VS2 1.1) · เลือก peer เอง · ทำ DCF ตาม VS2 1.3 (+ ชั้น 2 ถ้า PV(TV)/EV > 70%)
- Output: `agent_notes/emma/YYYY-MM-DD_TICKER_blind.md` — WACC, FV ต่อหุ้น, ทุก judgment call ที่เลือก + เหตุผล · ปิดท้าย `*Emma (Blind) — YYYY-MM-DD | TICKER*`
- ไม่ให้ conviction, ไม่ให้ recommendation
```

### A4 — `charlie.md`: ขั้น 1.7 ใน pipeline + วิธี dispatch

**ตำแหน่ง 1:** ใน code block `## Pipeline ที่ต้องทำตาม` — แทรกบรรทัดระหว่าง `→ Charlie สรุป + เขียน Research Report` กับ `→ Morgan ตรวจ QA`:
```
  → [ถ้า recommendation = BUY] Blind Re-derivation (VS2 1.7) → Charlie เทียบผล
```

**ตำแหน่ง 2:** ต่อท้าย bullet list ใน `## วิธี Delegate` (หลังบรรทัด `- **Max**: แจ้งหลัง Leo เสร็จ ...`)

**ข้อความ:**
```markdown
- **Blind Re-derivation (VS2 1.7 `TRIAL`)** — trigger: (ก) report recommendation = BUY (ก่อนส่ง Morgan) (ข) Max แจ้งว่าหุ้นที่ถือ re-verify แล้ว MOS พลิกเครื่องหมาย (ค) CIO สั่ง · ไม่ทำกับ learning-queue/SKIP
  1. สร้าง `agent_notes/charlie/YYYY-MM-DD_TICKER_blind_input.md` — คัดเฉพาะ **ตัวเลขดิบ** จาก Data Package Section A–D + F (ราคา, งบ 3 ส่วน, shares, net debt, lease, Rf, ERP, raw beta, D/E) พร้อม URL · **ห้ามใส่:** Locked WACC, external WACC list, peer list, pre-registered block, ประเภทธุรกิจ, Street PT, FV ใดๆ, ตัวเลขที่ทีม/CIO เคยพูด
  2. Spawn `emma` — prompt ขึ้นต้น `BLIND RE-DERIVATION` + path ของ blind input เท่านั้น (ห้ามสรุปบริบทของ analysis เดิมใน prompt)
  3. เทียบ Blind FV กับ Emma FV เดิม: ≤10% = ผ่าน · >10% = หา root cause ทีละ judgment call เทียบตาราง 1.6 → แก้ report หรืออธิบาย ก่อนส่ง Morgan
  4. บันทึกผลใน report ส่วน ⚙️ Behind the Scenes: Blind FV · Emma FV · Δ% · root cause (ถ้า >10%)
```

### A5 — `qa.md` (Morgan): checklist ใหม่

**ตำแหน่ง:** หลังบรรทัด `- [ ] **VS2 ชั้น 2** (\`TRIAL\`): ...` (บรรทัด ~173) ก่อนบรรทัดว่าง + `**2.6C — Atlas Macro Integration:**`

**ข้อความ:**
```markdown
- [ ] **VS2 ประเภทธุรกิจ** (`TRIAL`): Atlas จัดประเภทด้วย GICS + เกณฑ์ตัวเลข (มี URL) ก่อน Emma เริ่ม · วิธีหลักตรงประเภท · ตัวตรวจรายงานเป็นตัวเลข · วิธีหลัก vs ตัวตรวจห่าง ≥25% มี reconcile สองทิศ — ไม่ครบ = `RULE_VIOLATION`
- [ ] **VS2 ข้อ 1.5 Pre-registration** (`TRIAL`): Data Package มี block `🔒 Pre-registered Judgment Calls` · ค่าที่ใช้จริงตรงกับที่ล็อก หรือมีบันทึกการเปลี่ยน (อะไร / ก่อน-หลังเห็นผล / FV ก่อน-หลัง) — ไม่ครบ = `RULE_VIOLATION`
- [ ] **VS2 ข้อ 1.6 Judgment-Call Sensitivity** (`TRIAL`): Emma มีตาราง · ครอบคลุมทุกจุดที่ pre-register · จุดที่กระทบ >15% มี source ≥2 — ไม่ครบ = `RULE_VIOLATION`
- [ ] **VS2 ข้อ 1.7 Blind Re-derivation** (`TRIAL` — เฉพาะ report ที่ recommendation = BUY): มีไฟล์ `agent_notes/emma/*_TICKER_blind.md` ที่ปิดท้ายครบ · blind input ไม่มี Locked WACC/peer/FV/Street PT ปน · Δ ≤10% หรือมี root cause ใน ⚙️ Behind the Scenes — ไม่มี = `RULE_VIOLATION` · blind input ปนข้อมูลต้องห้าม = `RULE_VIOLATION` (ต้องรันใหม่)
```

### A6 — `max.md`: Execute gate + MOS-flip trigger

**ตำแหน่ง 1:** Mode 2 `**Step 2 — ตรวจ Portfolio Rules**` — ใน code block เพิ่มบรรทัดแรกก่อน `1. Conviction ≥ 6.0?`:
```
0. VS2 1.7 Blind Re-derivation มีผลใน report (Δ ≤10% หรือมี root cause)?  → ถ้าไม่มี: NO BUY — แจ้ง Charlie
```

**ตำแหน่ง 2:** หลังบรรทัด `**VS2 (ตั้งแต่ 2026-10-08):** ...` ใน `### Re-Analysis Trigger Check` (บรรทัด ~268)

**ข้อความ:**
```markdown
**VS2 1.7 (`TRIAL`):** re-verify แล้ว MOS **พลิกเครื่องหมาย** (บวก↔ลบ) → แจ้ง Charlie dispatch Blind Re-derivation **ก่อน**เสนอ sell/trim/add ใดๆ — ระบุสถานะใน 🔍 Re-Analysis Trigger Check block (`1.7 pending` / `1.7 done Δ X%`)
```

### A7 — `vera.md`: Method-Level Calibration ใน Quarterly

**ตำแหน่ง:** ใน Quarterly Review Format — หลัง section `## 🏭 Model Accuracy` (บรรทัด `**Quant Risk (Quinn):** ...`) ก่อน `---` / `## 📚 Lessons for Next Quarter`

**ข้อความ:**
```markdown

---

## 🧪 Method-Level Calibration (`TRIAL` — log-only, ดู CLAUDE.md Quarterly Output ข้อ 7)
| กลุ่มวิธี | # Analyses | FV drift (FV re-verify ถัดไป vs FV เดิม) | % FV ตกนอก Street PT range (ทิศ) | Realized vs FV (6mo / 12mo) |
|---|---|---|---|---|
| DCF ล้วน | | | | |
| DCF + multiples (VS2 ชั้น 2) | | | | |
| วิธีอื่น (P/B, rNPV, DDM, SOTP, AFFO) | | | | |
- จัดกลุ่มจาก report: ชั้น 2 trigger ไหม + ประเภทธุรกิจที่ Atlas จัด · FV drift ดึงจาก Re-Analysis Log ใน `portfolio/decisions.md`
- **ห้ามสรุปว่าวิธีไหนดี/แย่** จนกว่าแต่ละกลุ่ม n ≥ 10 ที่ผ่าน 12 เดือน — ก่อนนั้นเขียน "n = X — ยังไม่มีนัยสำคัญ"
- Blind Re-derivation log: # ครั้ง · Δ% แต่ละครั้ง · กี่ครั้ง >10% + root cause
```

### A8 — `quinn.md` + `bear.md`: ใช้ค่า pre-registered

**ตำแหน่ง:** ต่อท้ายบรรทัด `**VS2:** ใช้ Locked WACC/bridge/net debt/shares จาก Atlas · ...` ในทั้งสองไฟล์ (quinn.md ~190, bear.md ~40) — เติมท้ายบรรทัดเดิม:
```
 · ใช้ peer/forecast length ตาม `🔒 Pre-registered Judgment Calls` (VS2 1.5) — เปลี่ยนต้องบันทึก อะไร / ก่อน-หลังเห็นผล / FV ก่อน-หลัง
```

### A9 — `CLAUDE.md` § Morgan QA Protocol → Rule Compliance (เพิ่ม 1 บรรทัด)

**ตำแหน่ง:** ต่อท้าย list `### Rule Compliance (ต้อง PASS ทุกข้อ)` หลัง `- [ ] Position size ≤ 10%, ≥ 3% (ถ้า deploy)`

**ข้อความ:**
```markdown
- [ ] VS2 validation (`TRIAL`): ประเภทธุรกิจ + pre-registration (1.5) + judgment-call sensitivity (1.6) + blind re-derivation (1.7, เฉพาะ BUY) — รายละเอียดใน `.claude/agents/qa.md` Step 2.6
```

---

## หลังแก้เสร็จ

1. `git diff --stat` — คาดว่าแตะ 8 ไฟล์: atlas, emma, charlie, qa, max, vera, quinn, bear (.md ใน `.claude/agents/`) + CLAUDE.md (1 บรรทัด)
2. ตรวจว่าไม่มีบรรทัดเดิมถูกลบ ยกเว้น A8 (เติมท้ายบรรทัดเดิม = 1 แก้/ไฟล์)
3. Commit: `agents: wire validation framework TRIAL (VS2 1.5-1.7, classification, method calibration) into agent files` อ้าง `e4bc4db` + brief นี้ → push

## งานถัดไป (ไม่อยู่ใน commit นี้)

- **Vera calibration เกณฑ์จัดประเภท** (one-off, ก่อนใช้กับหุ้นจริง): รันเกณฑ์ GICS + ตัวเลขย้อนกับหุ้นที่วิเคราะห์เต็มแล้ว → ดูว่าไม่มีหุ้นเข้า 0 หรือ ≥3 ประเภทผิดปกติ · ผลไม่นับเป็น trial data · ถ้าเกณฑ์ตัวไหนหลวม/ตึงเกิน → ส่งกลับ Opus review ก่อนแก้ CLAUDE.md

*Opus 5.5 — 2026-10-13 | Brief สำหรับ Hermes · Opus ไม่แก้ agent files / CLAUDE.md*
