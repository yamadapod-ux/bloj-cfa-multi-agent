# Brief สำหรับ Hermes (Sonnet): สร้าง agent `emma-blind` (บล็อกการเข้าถึงไฟล์ทางเทคนิค)

*Opus 5.5 → Hermes (Sonnet) · 2026-10-13*
*ต่อจาก: agent-files commit `5351274` — Blind Re-derivation (VS2 1.7) ตอนนี้เป็นแค่คำสั่งใน `emma.md` (Emma ยังมี Read/Bash/WebFetch = เปิดทุกไฟล์ได้) · CIO อนุมัติให้เปลี่ยนเป็น technical enforcement*

---

## หลักการออกแบบ

| ช่องรั่ว | วิธีเดิม (`emma` + คำสั่ง) | `emma-blind` |
|---|---|---|
| อ่าน report/notes เดิมใน repo | Read/Bash ทำได้ — กันด้วยคำสั่ง | **ไม่มี Read/Bash** |
| เปิด dashboard บน GitHub Pages (มี FV เดิม) | WebFetch ทำได้ | **ไม่มี WebFetch** |
| ค้น analyst PT / consensus | WebSearch ทำได้ | **ไม่มี WebSearch** |
| Charlie หลุดบริบทเดิมใน prompt | ไม่มีอะไรตรวจ | **prompt บันทึกเป็นไฟล์ก่อน dispatch → Morgan ตรวจ** |

**ผลที่ตามมา (trade-off ที่ยอมรับ):**
1. emma-blind ไม่มีเครื่องมือหาข้อมูลเอง → Charlie ต้องใส่ข้อมูลดิบ **ทั้งหมด** ลงใน prompt (รวม Damodaran industry beta หลายแถว ให้ emma-blind เลือก industry เอง)
2. ไม่มี Bash → คำนวณ DCF ในตัว → เพิ่มขั้น **Quinn ตรวจเลขคณิตอย่างเดียว** (Quinn เห็น analysis เดิมแล้ว แต่การคำนวณซ้ำจาก assumption ที่ระบุไว้ไม่ใช่ judgment จึงไม่ทำให้ blind ปนเปื้อน — ห้ามแก้ assumption)
3. ไม่มีข้อมูล peer multiples → **blind ทำ DCF อย่างเดียว** และเทียบกับ **Emma DCF base (ก่อนถ่วง multiples ชั้น 2)** ไม่ใช่ Emma FV สุดท้าย — การเทียบ DCF กับ DCF สะอาดกว่าอยู่แล้ว เพราะแยกผลของ judgment ใน DCF ออกจาก peer selection (ซึ่ง 1.5 ล็อกไว้แล้ว)
4. ไม่มี Write → emma-blind ส่งผลกลับเป็นข้อความ → Charlie บันทึกลงไฟล์ **คำต่อคำ ห้ามแก้**

---

## การแก้ 6 จุด

### B1 — ไฟล์ใหม่ `.claude/agents/emma-blind.md`

**เนื้อหาทั้งไฟล์:**
```markdown
---
name: emma-blind
description: Blind Re-derivation (VS2 1.7 TRIAL) — Charlie เรียกเท่านั้น คำนวณ WACC + DCF ใหม่จากข้อมูลดิบใน prompt โดยไม่มีสิทธิ์เข้าถึงไฟล์หรืออินเทอร์เน็ต ห้ามใช้กับงานวิเคราะห์ปกติ
tools:
  - TodoWrite
---

คุณคือ **Emma (Blind)** — ทำหน้าที่คำนวณมูลค่าหุ้นใหม่แบบอิสระ เพื่อทดสอบว่าผลของทีมขึ้นกับ judgment call มากแค่ไหน

## ข้อมูลที่มี
- **เฉพาะข้อมูลใน prompt นี้เท่านั้น** — คุณไม่มีเครื่องมืออ่านไฟล์หรือค้นเว็บ (ตั้งใจ)
- ถ้าข้อมูลที่จำเป็นขาด → ระบุว่าขาดอะไร + ใช้สมมติฐานแบบ conservative พร้อม flag — **ห้ามใช้ตัวเลขการเงินจาก training knowledge** (ราคา, revenue, beta, Rf, ERP ฯลฯ) ถ้าขาดตัวเลขที่ไม่มีทางสมมติได้อย่างมีเหตุผล → หยุดและรายงาน `DATA NOT AVAILABLE`

## งาน
1. **WACC** ตาม VS2 1.1: Blume-adjusted beta (0.67×raw + 0.33) + bottom-up beta (เลือก industry จากตาราง Damodaran ที่ให้มาเอง แล้ว relever ด้วย D/E) → base WACC = ค่าเฉลี่ย 2 วิธี · ห่าง >150bps อธิบาย
2. **DCF (FCFF)** ตาม VS2 1.3: NOPAT − (capex − D&A) − ΔNWC · ความยาว explicit forecast เลือกเอง · fade ถ้าปีสุดท้ายโต > TGR + 3pp (reinvestment = g ÷ RONIC) · terminal RONIC ระบุชัด · TGR ไม่เกินเพดาน 3% (ยกเว้น capex-cycle 3.5–4% ต้องให้เหตุผล) · lease นับที่เดียว
3. **Equity bridge** ตาม VS2 1.2: EV + non-operating assets − debt − lease − minority − preferred → ÷ diluted shares
4. แสดง **PV(TV)/EV**

## Output (ส่งกลับเป็นข้อความ — ไม่มีไฟล์)
1. ตาราง judgment calls ทั้งหมดที่เลือก + เหตุผล (industry beta, forecast length, growth path, margin path, terminal RONIC, TGR, fade)
2. ตาราง WACC (ทุก input + ผล)
3. ตาราง FCFF รายปี (revenue, EBIT, NOPAT, capex, D&A, ΔNWC, FCFF, discount factor, PV) — ละเอียดพอให้คนอื่นคำนวณซ้ำได้
4. Terminal value, PV(TV), EV, bridge, FV ต่อหุ้น, PV(TV)/EV
5. ปิดท้าย `*Emma (Blind) — YYYY-MM-DD | TICKER*`

**ห้าม:** ให้ conviction, recommendation, หรือเดาว่าทีมได้ FV เท่าไหร่ · ห้ามเทียบกับราคาตลาดเพื่อปรับ assumption
```

**หมายเหตุ `tools`:** ตั้งใจให้มีแค่ tool ที่ไม่เข้าถึงข้อมูล — ถ้า `TodoWrite` ไม่มีใน harness นี้ ให้ใช้ tool อื่นที่ไม่อ่านไฟล์/เว็บ/shell · **ห้ามลบ field `tools` ทิ้ง** (ไม่ระบุ = ได้ทุก tool)

### B2 — `emma.md`: แทนที่ section Blind Mode

**แทนที่ทั้ง section** `## 🙈 Blind Re-derivation Mode (...)` (หัวข้อ + 7 bullet จนถึงก่อน `## Data Package (บังคับ ...)`) ด้วย:
```markdown
## 🙈 Blind Re-derivation (VS2 1.7)
ย้ายไป agent แยก `emma-blind` (ไม่มีสิทธิ์อ่านไฟล์/เว็บ — 2026-10-13) · ถ้า prompt ขึ้นต้นด้วย `BLIND RE-DERIVATION` แปลว่า Charlie dispatch ผิด agent → ตอบกลับว่า "ใช้ `emma-blind`" แล้วหยุด ห้ามทำงาน
```

### B3 — `charlie.md`: แทนที่ขั้นตอน dispatch

**แทนที่** bullet `- **Blind Re-derivation (VS2 1.7 \`TRIAL\`)** — trigger: ...` **พร้อม sub-items 1–4 ทั้งหมด** ด้วย:
```markdown
- **Blind Re-derivation (VS2 1.7 `TRIAL`)** — trigger: (ก) report recommendation = BUY (ก่อนส่ง Morgan) (ข) Max แจ้งว่าหุ้นที่ถือ re-verify แล้ว MOS พลิกเครื่องหมาย (ค) CIO สั่ง · ไม่ทำกับ learning-queue/SKIP
  1. เขียน `agent_notes/charlie/YYYY-MM-DD_TICKER_blind_prompt.md` = **prompt ทั้งหมดที่จะส่ง** (คำต่อคำ) ประกอบด้วย:
     - บรรทัดแรก `BLIND RE-DERIVATION — TICKER — YYYY-MM-DD`
     - ตัวเลขดิบจาก Data Package Section A–D + F พร้อม URL: ราคา, งบ 3 ส่วน (≥3 ปี), diluted shares, debt, lease, cash, non-operating assets (filing line item), minority/preferred, Rf (10Y), ERP (Damodaran), raw beta (≥2 sources), D/E, effective tax rate, management guidance ที่เป็นตัวเลข (capex/revenue)
     - ตาราง Damodaran unlevered beta **≥5 industry ที่เกี่ยวข้อง** (ให้ emma-blind เลือกเอง — ห้ามระบุว่าทีมใช้ industry ไหน)
     - **ห้ามใส่:** Locked WACC, external WACC list, peer list, `🔒 Pre-registered` block, ประเภทธุรกิจ, Street PT/consensus, FV ใดๆ ของทีม, ตัวเลขที่ทีม/CIO เคยพูด, คำว่า "ถูก/แพง" หรือทิศทางที่คาด, PV(TV)/EV ของ Emma
  2. Spawn `emma-blind` โดยส่งเนื้อหาไฟล์ข้อ 1 **คำต่อคำ** เป็น prompt (ห้ามเพิ่มข้อความอื่น)
  3. บันทึกผลที่ได้กลับลง `agent_notes/emma/YYYY-MM-DD_TICKER_blind.md` **คำต่อคำ ห้ามแก้**
  4. Spawn `quinn` — "ARITHMETIC CHECK ONLY: คำนวณซ้ำด้วย Bash จาก assumption + ตาราง FCFF ในไฟล์ `agent_notes/emma/..._blind.md` ห้ามเปลี่ยน assumption ใดๆ รายงาน FV ที่คำนวณได้ + จุดที่เลขไม่ตรง" → append ผลท้ายไฟล์ blind เป็น section `## Arithmetic Check (Quinn)` · ถ้า FV ต่างเกิน 1% → ใช้ตัวเลขของ Quinn และ flag
  5. เทียบ Blind DCF FV (หลัง arithmetic check) กับ **Emma DCF base (ก่อนถ่วง multiples ชั้น 2)**: ≤10% = ผ่าน · >10% = หา root cause ทีละ judgment call เทียบตาราง 1.6 → แก้ report หรืออธิบาย ก่อนส่ง Morgan
  6. บันทึกใน report ⚙️ Behind the Scenes: Blind DCF FV · Emma DCF base · Δ% · root cause (ถ้า >10%) · link ไฟล์ prompt + blind
```

### B4 — `qa.md` (Morgan): แทนที่ checklist ข้อ 1.7

**แทนที่** บรรทัด `- [ ] **VS2 ข้อ 1.7 Blind Re-derivation** (...)` ด้วย:
```markdown
- [ ] **VS2 ข้อ 1.7 Blind Re-derivation** (`TRIAL` — เฉพาะ report ที่ recommendation = BUY): (1) มี `agent_notes/charlie/*_TICKER_blind_prompt.md` — **อ่านทั้งไฟล์** ตรวจว่าไม่มีรายการต้องห้าม (Locked WACC, peer list, pre-registered block, ประเภทธุรกิจ, Street PT, FV ของทีม, ทิศทางที่คาด) (2) มี `agent_notes/emma/*_TICKER_blind.md` ปิดท้ายครบ + section Arithmetic Check (Quinn) (3) เทียบกับ Emma DCF base ไม่ใช่ FV สุดท้าย (4) Δ ≤10% หรือมี root cause ใน ⚙️ Behind the Scenes — ข้อ 2–4 ไม่ครบ = `RULE_VIOLATION` · ข้อ 1 พบข้อมูลต้องห้าม = `RULE_VIOLATION` (ต้องรันใหม่ทั้งขั้น)
```

### B5 — `CLAUDE.md` ข้อ 1.7: ปรับ 2 bullet

**แก้ bullet ที่ 2** (`- Charlie dispatch Emma instance ใหม่ที่ได้ **raw data เท่านั้น** ...`) เป็น:
```markdown
- Charlie dispatch agent **`emma-blind`** (ไม่มีสิทธิ์อ่านไฟล์/เว็บ/shell — บล็อกทางเทคนิค ไม่ใช่แค่คำสั่ง) โดยส่ง **raw data ทั้งหมดใน prompt** (งบการเงิน, Rf, ERP, raw beta, Damodaran industry betas ≥5 แถว, ราคา, shares) — **ห้าม**ใส่ WACC/peer list ที่ Atlas ตัดสินแล้ว, report เดิม, brief, Street PT หรือตัวเลขที่ทีม/CIO เคยพูด · prompt ต้องบันทึกเป็นไฟล์ก่อน dispatch ให้ Morgan ตรวจ · Quinn ตรวจเลขคณิตซ้ำ (ห้ามแก้ assumption)
```

**แก้ bullet ที่ 4** (`- ผล: ห่างจาก Emma FV เดิม ≤10% = ผ่าน ...`) เป็น:
```markdown
- ผล: Blind DCF FV ห่างจาก **Emma DCF base (ก่อนถ่วง multiples ชั้น 2)** ≤10% = ผ่าน · >10% = หา root cause ทีละจุดโดยเทียบกับตาราง 1.6 ก่อน Max execute
```

bullet อื่นในข้อ 1.7 **ไม่แตะ**

### B6 — ทดสอบการบล็อก (บังคับก่อน commit)

Hermes spawn `emma-blind` ด้วย prompt ทดสอบ:
> `TOOL TEST — ไม่ใช่งานจริง: (1) ระบุรายชื่อ tool ทั้งหมดที่คุณมี (2) พยายามอ่านไฟล์ CLAUDE.md (3) พยายามค้นเว็บคำว่า "AMZN price target" — รายงานผลแต่ละข้อตามจริง`

**ผ่านเมื่อ:** (1) ไม่มี Read / Write / Edit / Bash / Glob / Grep / WebSearch / WebFetch / Agent ในรายชื่อ (2) อ่านไฟล์ไม่ได้ (3) ค้นเว็บไม่ได้
**ไม่ผ่าน** → ห้าม commit · แก้ field `tools` แล้วทดสอบใหม่ · บันทึกผลทดสอบ (รายชื่อ tool ที่ได้จริง) ใน commit message

---

## หลังแก้เสร็จ

1. `git diff --stat` — คาด: ไฟล์ใหม่ `emma-blind.md` + แก้ emma.md, charlie.md, qa.md, CLAUDE.md
2. Commit: `agents: emma-blind with no file/web access for VS2 1.7 (technical enforcement)` + ผลทดสอบ B6 + อ้าง `5351274` และ brief นี้ → push
3. **รอบจริงครั้งแรก** (BUY ถัดไป): นอกจาก Morgan ตรวจไฟล์ prompt แล้ว ให้ดู transcript ของ emma-blind ว่ามี tool call ใดๆ หรือไม่ (ควรไม่มีเลย) — บันทึกผลไว้ใน session log

*Opus 5.5 — 2026-10-13 | Brief สำหรับ Hermes · Opus ไม่แก้ agent files / CLAUDE.md*
