# Brief สำหรับ Hermes (Sonnet): แก้ CLAUDE.md ตาม Validation Framework Review

*Opus 5.5 → Hermes (Sonnet) · 2026-10-13*
*ที่มา: `2026-10-08_valuation_validation_framework_proposal.md` (Hermes draft) → `2026-10-12_opus_response_validation_framework.md` (Opus review, commit `4fba12c`) → Hermes ตรวจแล้วแนะนำอนุมัติทั้งหมด*
*Opus ไม่แก้ CLAUDE.md เอง — Hermes เป็นผู้แก้ เมื่อ CIO สั่ง*

---

## ⚠️ Erratum ของ Opus review (แก้ความเข้าใจก่อนลงมือ)

Opus review §1 แถว C3 เขียนว่า Multi-Segment ข้อ 5 "ใช้กับ Bear เท่านั้น" — **ผิด**. เนื้อกฎเขียนว่า "ถ้า **FV ใด**ต่ำกว่า no-growth value" อยู่แล้ว (Hermes จับได้). ที่ไม่ตรงคือ **ชื่อหัวข้อ** "Bear floor sanity" เท่านั้น → แก้ #6 ข้างล่างจึงเป็นการเปลี่ยนชื่อหัวข้ออย่างเดียว ไม่แตะเนื้อกฎ

---

## หลักการแก้ (ทุกจุด)

- ใช้ **targeted Edit** เท่านั้น ห้าม Write ทับ CLAUDE.md ทั้งไฟล์
- ของใหม่ทุกข้อติด `TRIAL — review 2026-12-31` (รอบเดียวกับ VS2 ชั้น 2)
- **ห้ามแตะ:** 40/30/30, MOS threshold, conviction gate, TGR ceiling, Rule Classification Table — ทุกข้อเป็น QA/methodology ไม่ใช่ Return-side
- แก้เสร็จ: `git diff CLAUDE.md` ตรวจว่ามีแค่ 7 จุดนี้ แล้ว commit + push

---

## การแก้ 7 จุด

### #1 — VS2 ข้อ 1.5 Pre-registration (ใหม่)

**ตำแหน่ง:** ต่อท้ายข้อ 1.4 (หลังบรรทัด `- แสดงใน Score Dashboard + buy_list · **เป็นข้อมูลประกอบ ไม่ใช่ gate** ...`) ก่อน `#### ชั้น 2`

**ข้อความ:**
```markdown
**1.5 ล็อกจุดดุลยพินิจล่วงหน้า (Pre-registration) (`TRIAL` — review 2026-12-31)**
- Atlas ล็อกค่าของจุดดุลยพินิจต่อไปนี้ใน Data Package **ก่อน** Emma/Quinn/Bear เห็นตัวเลข valuation ใดๆ:
  - WACC: รายชื่อแหล่งภายนอกที่จะนับ · เกณฑ์ `stale-rate` · วิธีเลือกเมื่อ beta 2 วิธีห่าง >150bps
  - Peer list (ตามเกณฑ์ B-V1 peer-selection guideline)
  - ประเภทธุรกิจ (ตามตาราง "วิธีคำนวณตามประเภทหุ้น")
  - ความยาว explicit forecast + มี fade หรือไม่
- เปลี่ยนค่าที่ล็อกได้ **แต่** report ต้องบันทึก: เปลี่ยนอะไร · เปลี่ยนก่อนหรือหลังเห็นผล · FV ก่อน/หลังเปลี่ยน
- เหตุผล: AMZN v3.4 — judgment call (เช่น stale-rate 75bps, ตัดแหล่ง WACC ภายนอก 4/6) ถูกเลือกหลังรู้ทิศทางผล · การล็อกล่วงหน้าแก้ที่ต้นเหตุ แทนการ flag หลังผลออก
- **Morgan:** จุดดุลยพินิจที่ไม่ได้ล็อกล่วงหน้า และไม่ได้บันทึกการเปลี่ยน = `RULE_VIOLATION`
```

### #2 — VS2 ข้อ 1.6 ตาราง Judgment-Call Sensitivity (ใหม่)

**ตำแหน่ง:** ต่อจาก #1

**ข้อความ:**
```markdown
**1.6 ตาราง Judgment-Call Sensitivity (`TRIAL` — review 2026-12-31)**
Emma ทำทุกรายงาน — เปลี่ยนทีละจุด (ตัวอื่นคงเดิม):

| # | Judgment call | ค่าที่ใช้ | ทางเลือกที่สมเหตุสมผลอีกทาง | FV ถ้าเลือกทางนั้น | Δ% ของ Blended FV | Source รองรับค่าที่ใช้ |
|---|---|---|---|---|---|---|

- ขั้นต่ำ: ทุกจุดที่ล็อกไว้ใน 1.5 + จุดอื่นที่ Emma เห็นว่ากระทบ
- จุดใดกระทบ **>15% ของ Blended FV** → ค่าที่ใช้ต้องมี source ≥2 รองรับ + ระบุใน ⚙️ Behind the Scenes
- ต่างจาก Market-Implied Sanity Check: อันนั้นถาม "ต้องขยับแค่ไหนถึงปิด gap กับราคาตลาด" · อันนี้ถาม "ทางเลือกที่สมเหตุสมผลเท่ากันทำให้ FV แกว่งแค่ไหน" — ใช้คู่กัน
- **ไม่ใช่ gate** — ไม่เปลี่ยน recommendation อัตโนมัติ
- **Morgan:** ไม่มีตาราง / จุดกระทบ >15% มี source <2 = `RULE_VIOLATION`
```

### #3 — VS2 ข้อ 1.7 Blind Re-derivation (ใหม่)

**ตำแหน่ง:** ต่อจาก #2

**ข้อความ:**
```markdown
**1.7 Blind Re-derivation (`TRIAL` — review 2026-12-31)**
- **Trigger (เฉพาะ):** (ก) ก่อน Max execute BUY จริง (ข) หุ้นที่ถืออยู่ซึ่ง re-verify แล้ว MOS พลิกเครื่องหมาย (ค) CIO สั่ง — **ไม่ทำ** กับ learning-queue / SKIP
- Charlie dispatch Emma instance ใหม่ที่ได้ **raw data เท่านั้น** (งบการเงิน, Rf, ERP, raw beta, ราคา, shares) — **ห้าม**ส่ง WACC/peer list ที่ Atlas ตัดสินแล้ว, report เดิม, brief, Street PT หรือตัวเลขที่ทีม/CIO เคยพูด
- Instance ใหม่คำนวณ WACC + FV เองทั้งหมด (เหตุผล: bias อาจฝังอยู่ใน Data Package ตั้งแต่ขั้น Atlas — blind ที่ใช้ Data Package เดิมจึงไม่ช่วย)
- ผล: ห่างจาก Emma FV เดิม ≤10% = ผ่าน · >10% = หา root cause ทีละจุดโดยเทียบกับตาราง 1.6 ก่อน Max execute
- ต้นทุน ~1 Emma run (~30–50K token) ต่อเคส
- **Max:** trigger (ก) เข้าแต่ยังไม่มีผล 1.7 → ห้าม execute
```

### #4 — เกณฑ์จัดประเภท + เหตุผลระดับประเภท (ใหม่)

**ตำแหน่ง:** ใต้ตาราง "วิธีคำนวณตามประเภทหุ้น" — **ไม่แก้ตารางเดิม** เพิ่มตารางใหม่ต่อจาก bullet `- **Morgan:** ไม่มีการจัดประเภท / ...` ของตารางนั้น

**ข้อความ:**
```markdown
**เกณฑ์จัดประเภท + เหตุผลของวิธี (`TRIAL` — review 2026-12-31)**
Atlas จัดประเภทด้วย GICS ก่อน แล้วใช้เกณฑ์ตัวเลขเมื่อ GICS แยกไม่ออก — บันทึกตัวเลข + URL ใน Data Package

| ประเภท | ตัวกรองแรก | เกณฑ์ตัวเลข | ทำไมวิธีหลักเหมาะ |
|---|---|---|---|
| ธนาคาร / ประกัน | GICS Banks, Insurance | — | หนี้คือวัตถุดิบของธุรกิจ ไม่ใช่ financing → FCFF/WACC ไม่มีความหมาย · book value ผูกกับ regulatory capital |
| REIT | GICS REITs | — | ต้องจ่าย ≥90% ของกำไร · ค่าเสื่อมทางบัญชีไม่สะท้อนมูลค่าอสังหา → AFFO/NAV ตรงกว่า |
| Utility (regulated) | GICS Utilities | ≥50% revenue จาก rate-regulated operations | ผลตอบแทนถูกกำหนดโดย regulator (allowed ROE × rate base) → การเติบโตคาดได้จาก rate base |
| หุ้นลงทุนหนัก | — | PV(TV)/EV > 70% (มีอยู่แล้ว) | มูลค่าส่วนใหญ่อยู่ใน terminal → DCF เปราะต่อ TGR/margin → ต้องมี multiples ถ่วง |
| Software / SaaS โตเร็ว | GICS Software | recurring/subscription ≥60% revenue **และ** growth >15% YoY | SBC + deferred revenue บิด FCF → ต้องคุม cash-flow definition (DCF Cash Flow Consistency Rule) |
| Cyclical | GICS Semis, Materials, Industrials, Energy, Autos | EBIT peak→trough ร่วง ≥30% ในวัฏจักรล่าสุด (≤10 ปี) **หรือ** CV ของ EBIT margin 10 ปี ≥0.3 | ปีเดียวไม่แทน earnings power → ต้องใช้ mid-cycle |
| Biotech / pharma | GICS Biotech, Pharma | rNPV pipeline (ยังไม่อนุมัติ) >50% ของ EV → rNPV เป็นหลัก · <50% → DCF ส่วนที่มีกำไรเป็นหลัก | กระแสเงินขึ้นกับผลทดลองแบบ binary → ต้องคูณด้วยโอกาสผ่านแต่ละ phase |
| Holding / conglomerate | — | ≥3 segment ไม่เกี่ยวข้องกัน แต่ละ ≥15% ของ revenue หรือ EV | แต่ละธุรกิจมี risk/growth ต่างกัน → WACC/multiple เดียวบิดมูลค่า |
| AI / Infra build-out | — | เกณฑ์ lane เดิม 3 ข้อ | (ตาม lane) |
| ธุรกิจทั่วไป | — | ไม่เข้าประเภทใดข้างบน (default) | FCF สม่ำเสมอ → DCF ตรงที่สุด |

- **ตัวเลขเกณฑ์เป็นค่าตั้งต้น ยังไม่ calibrate** — ก่อนใช้จริง Vera รันย้อนกับหุ้นที่วิเคราะห์เต็มแล้ว (แบบ lane AI/Infra calibration `faa04d2`) ดูว่าไม่มีหุ้นเข้า 0 ประเภทหรือ ≥3 ประเภทผิดปกติ · ผล calibration ไม่นับเป็น trial data
- แต่ละรายงานไม่ต้องเขียนเหตุผลระดับประเภทซ้ำ — ตอบแค่ "หุ้นนี้เข้าเกณฑ์ประเภทนั้นจริงไหม" (ตัวเลข + URL)
- **Morgan:** จัดประเภทโดยไม่มีตัวเลขตามเกณฑ์ = `RULE_VIOLATION`
```

### #5 — Vera Quarterly Output ข้อ 7: Method-Level Calibration (ใหม่)

**ตำแหน่ง:** ใน `### Quarterly Output` ต่อท้ายข้อ 6 (Funnel Health) — หลัง bullet `- **Trial review 2026-12-31:** Vera + Charlie ทบทวน ...` ก่อน `### Pre-Commitment Trigger Check`

**ข้อความ:**
```markdown
7. **Method-Level Calibration (`TRIAL` — review 2026-12-31, log-only):**

   | กลุ่มวิธี | # Analyses | FV drift (FV re-verify ถัดไป vs FV เดิม) | % ที่ FV ตกนอก Street PT range (ทิศไหน) | Realized price vs FV (6mo / 12mo) |
   |---|---|---|---|---|
   | DCF ล้วน | | | | |
   | DCF + multiples (VS2 ชั้น 2) | | | | |
   | วิธีอื่น (P/B, rNPV, DDM, SOTP, AFFO) | | | | |

   - รวม 3 กลุ่ม (ไม่แยก 10 ประเภท — sample ปัจจุบัน ~30 analyses แบ่ง 10 ประเภทเหลือ 2–3/กลุ่ม ใช้สรุปไม่ได้)
   - **ห้ามใช้ตัดสินเปลี่ยนวิธี** จนกว่าแต่ละกลุ่มมี **n ≥ 10 ที่ผ่าน 12 เดือนแล้ว**
   - หลัง n ≥ 10: กลุ่มใด error สูงกว่าค่าเฉลี่ยติดกัน 4 ไตรมาส → review วิธีของกลุ่มนั้น (ไม่ต้องรอ 8Q เพราะเป็น methodology ไม่ใช่ gate)
   - Realized price เป็นสัญญาณประกอบเท่านั้น — ตลาดตั้งราคาผิดได้นานเกิน 12 เดือน · FV drift + Street-range เป็นตัวชี้วัดที่ไม่ขึ้นกับตลาด
```

### #6 — เปลี่ยนชื่อหัวข้อ Multi-Segment ข้อ 5

**ตำแหน่ง:** `### Multi-Segment / SOTP Consistency Rule` ข้อ 5

**แก้:** `5. **Bear floor sanity:** ถ้า FV ใดต่ำกว่า ...` → `5. **No-growth floor sanity (FV ของทุกคน):** ถ้า FV ใดต่ำกว่า ...`

เนื้อกฎที่เหลือ **ไม่แตะ**

### #7 — ตาราง VS2: วิธีหลัก vs ตัวตรวจต้อง reconcile

**ตำแหน่ง:** ใต้ตาราง "วิธีคำนวณตามประเภทหุ้น" — เพิ่ม bullet ใหม่ต่อจาก `- หุ้นเข้าได้หลายประเภท → ...`

**ข้อความ:**
```markdown
- วิธีหลักกับตัวตรวจ (cross-check) ห่าง ≥25% → reconciliation table ทดสอบทั้งสองทิศ **ก่อน**สรุปผล (หลักเดียวกับ Multi-Segment ข้อ 3) — ตัวตรวจต้องรายงานเป็นตัวเลขทุกรายงาน ไม่ใช่แค่ระบุชื่อวิธี
```

---

## หลังแก้เสร็จ

1. `git diff CLAUDE.md` — ตรวจว่ามีเฉพาะ 7 จุดนี้
2. Commit message แนะนำ: `rules: validation framework TRIAL (pre-registration, judgment-call sensitivity, blind re-derivation, classification criteria, method calibration)` อ้าง `4fba12c` + brief นี้
3. Push
4. ถ้า Vera agent file (`.claude/agents/vera.md`), Atlas, Emma, Morgan มี checklist ที่ควรสะท้อน #1–#5 → แจ้ง CIO ว่ายังไม่ได้แก้ agent files (แยกเป็นงานถัดไป ไม่รวมใน commit นี้)

*Opus 5.5 — 2026-10-13 | Brief สำหรับ Hermes · Opus ไม่แก้ CLAUDE.md*
