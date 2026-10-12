# Opus Review: กรอบตรวจสอบว่าวิธีคำนวณมูลค่า "ผิด" หรือไม่

*ตอบ `agent_notes/charlie/2026-10-08_valuation_validation_framework_proposal.md` (Hermes draft) — Opus 5.5, 2026-10-12*
*สถานะ: ความเห็น/ข้อเสนอแก้ไข — **ยังไม่แก้ CLAUDE.md** จนกว่า CIO จะอนุมัติ*

---

## 1. สรุปคำตัดสินรายข้อ

| ข้อ | คำตัดสิน | เหตุผลสั้น |
|---|---|---|
| A1 Theoretical Fit | ✅ รับ — **ปรับรูปแบบ** | เขียนเหตุผลระดับประเภทครั้งเดียวในตาราง VS2; รายงานแต่ละตัวตอบแค่ "หุ้นนี้เข้าประเภทนั้นจริงไหม" (กันกลายเป็น boilerplate + เปลือง token) |
| A2 Classification Audit Trail | ✅ รับ | ดูข้อเสนอเกณฑ์ตัวเลขใน §3 Open Item 1 |
| A3 Multi-Method บังคับ | 🔁 มีอยู่แล้วบางส่วน | ตาราง VS2 มีคอลัมน์ "ตัวตรวจ" ทุกประเภทแล้ว — ที่ขาดคือ **ยังไม่บังคับ reconcile เมื่อวิธีหลัก vs ตัวตรวจห่าง ≥25%** → เติมประโยคเดียว |
| B1 Anchor-Proximity ±5% | 🔄 **เปลี่ยนกลไก** → Pre-registration | ดู §2.1 |
| B2 Degrees-of-Freedom Audit | ✅ รับ — **ข้อที่แข็งที่สุด** | ดู §2.2 |
| B3 Blind Re-derivation | ✅ รับ — **จำกัดขอบเขต** | ดู §2.3 |
| B4 Symmetric-Direction | 🔁 มีอยู่แล้ว | Multi-Segment ข้อ 3 (ทดสอบทั้งสองทิศ) |
| C1 Equity₅ Reconciliation | 🔁 มีอยู่แล้ว | VS2 ข้อ 1.4 |
| C2 Cross-Segment | 🔁 มีอยู่แล้ว | Multi-Segment Rule ใช้กับทุกหุ้นหลาย segment อยู่แล้ว ไม่ได้จำกัด AMZN |
| C3 No-Growth Floor | 🔁 มีอยู่แล้วบางส่วน | Multi-Segment ข้อ 5 ใช้กับ **Bear เท่านั้น** → แก้ถ้อยคำให้ครอบคลุม FV ของ Emma/Quinn ด้วย (แก้คำ ไม่ใช่กฎใหม่) |
| D1 Scorecard ตาม business-type | ✅ รับ — **รวมกลุ่มก่อน** | ดู §3 Open Item 4 |
| D2 Method-Level Calibration | ✅ รับ — **log เท่านั้น ห้ามใช้ตัดสินจนกว่า n พอ** | ดู §3 Open Item 4 |
| D3 TRIAL ทุก layer ใหม่ | ✅ รับ | สอดคล้องแนวทางที่ใช้อยู่ (Filter D/E, Lane AI/Infra, VS2 ชั้น 2) |

**ข้อสังเกตภาพรวม:** ข้อเสนอเดิมมี 13 ข้อ แต่ 5 ข้อ (A3, B4, C1, C2, C3) มีอยู่แล้วใน CLAUDE.md — ถ้าเขียนซ้ำเป็นกฎใหม่จะทำให้ CLAUDE.md ยาวขึ้นโดยไม่ได้อะไรเพิ่ม และเสี่ยงสองกฎขัดกันเองในอนาคต. ของใหม่จริงคือ **B1 (ในรูปใหม่), B2, B3, A1, A2, D1/D2**

---

## 2. ข้อที่ต้องปรับจากร่างเดิม

### 2.1 B1 → เปลี่ยนจาก "Anchor-Proximity Flag" เป็น "Judgment-Call Pre-registration"

**ปัญหาของร่างเดิม:**
1. เป็นการตรวจ **หลัง** ผลออกมาแล้ว — จับได้แค่กรณีบังเอิญตกในช่วง ±5% เท่านั้น ถ้า motivated reasoning ดันผลไปที่ +8% ก็หลุด
2. ตัวเลข anchor มักไม่ใช่ point target — เช่น CIO พูดว่า "ไม่มีที่ไหนต่ำกว่า $200" คือ **ขอบล่าง** ไม่ใช่เป้า; ±5% ของขอบล่างไม่มีความหมายทางสถิติ
3. ตัวเลขภายนอกที่ชอบธรรม (Street PT, consensus) ก็เป็น anchor ได้ — ห้ามดูไม่ได้ เพราะ VS2 1.1 บังคับ external cross-check อยู่แล้ว

**ต้นเหตุจริงที่ต้องแก้:** judgment call ถูกเลือก **หลังจาก**รู้ว่าแต่ละทางเลือกพาผลไปทางไหน (เช่น stale-rate threshold 75bps, การตัดแหล่ง WACC ภายนอก 4/6 แหล่งใน AMZN v3.4)

**ข้อเสนอแทน — Pre-registration (ใช้หลักเดียวกับ B-V1 peer-selection guideline ที่มีอยู่แล้ว):**
- Atlas ล็อกค่าของทุก judgment call ที่รู้ล่วงหน้าได้ **ใน Data Package ก่อน Emma/Quinn/Bear เห็นตัวเลขใดๆ:**
  - WACC: แหล่งภายนอกที่จะนับ + เกณฑ์ stale-rate + วิธีเลือกเมื่อ 2 วิธี beta ห่าง >150bps
  - Peer list (มีอยู่แล้วใน VS2 ชั้น 2 ข้อ 2)
  - ประเภทธุรกิจ (มีอยู่แล้ว — Atlas จัด ห้ามเปลี่ยนระหว่าง pipeline)
  - Explicit forecast length + มี fade หรือไม่
- เปลี่ยนค่าที่ล็อกไว้ภายหลังได้ **แต่** ต้องบันทึกใน report ว่าเปลี่ยนอะไร เปลี่ยนเมื่อไหร่ (ก่อน/หลังเห็นผล) และ FV ก่อน-หลังเปลี่ยน
- **Morgan:** judgment call ที่ไม่ได้ล็อกล่วงหน้าและไม่ได้บันทึกการเปลี่ยน = `RULE_VIOLATION`

**ผลข้างเคียงที่ดี:** Open Item 2 (threshold ±5% เหมาะไหม) หมดความจำเป็นไปเลย

### 2.2 B2 Degrees-of-Freedom Audit — รับ พร้อมกำหนดรูปแบบ

นี่คือ specification-curve analysis แบบย่อ — ต้นทุนต่ำ (คำนวณซ้ำทีละตัวแปรจากโมเดลเดิม) แต่ให้ข้อมูลมากที่สุดในทั้งเอกสาร

**รูปแบบที่เสนอ (Emma ทำ, Morgan ตรวจ):**

| # | Judgment call | ค่าที่ใช้ | ทางเลือกที่สมเหตุสมผลอีกทาง | FV ถ้าเลือกทางนั้น | Δ% ของ Blended FV | Source รองรับค่าที่ใช้ |
|---|---|---|---|---|---|---|

- **ขั้นต่ำ:** ทุก call ที่ pre-register ไว้ใน §2.1 + call อื่นที่ Emma เห็นว่ากระทบ
- **เกณฑ์:** call ใดกระทบ >15% ของ Blended FV → ต้องมี source ≥2 รองรับค่าที่ใช้ และระบุในส่วน ⚙️ Behind the Scenes
- **ต่างจาก Market-Implied Sanity Check อย่างไร:** Market-Implied ถามว่า "ตัวแปรไหนต้องขยับแค่ไหนถึงจะปิด gap กับราคาตลาด" (หันไปทางตลาด); B2 ถามว่า "ทางเลือกที่สมเหตุสมผลเท่ากันทำให้ FV แกว่งแค่ไหน" (หันเข้าหาตัวเอง) — ใช้ร่วมกันได้ ไม่ซ้ำ
- **ไม่ใช่ gate** — ไม่เปลี่ยน recommendation อัตโนมัติ (Return-side lock ไม่ถูกแตะ)

### 2.3 B3 Blind Re-derivation — รับ แต่จำกัดขอบเขต

**ประเด็นสำคัญที่ร่างเดิมมองข้าม:** subagent ใน pipeline นี้ได้แค่ Data Package อยู่แล้ว — แต่ bias อาจ **ฝังอยู่ใน Data Package เอง** (Atlas เป็นคนคำนวณ WACC และตัดแหล่งภายนอก). ดังนั้น blind re-derivation ต้อง:
- รับ **raw data** (งบการเงิน, Rf, ERP, beta raw, ราคา) — **ไม่ใช่** WACC/peer list ที่ Atlas ตัดสินไปแล้ว
- ไม่เห็น brief, report เดิม, ตัวเลขที่ CIO/ทีมเคยพูด, หรือ Street PT
- คำนวณ WACC + Emma-equivalent FV เองทั้งหมด

**ผล:** ห่าง ≤10% = เพิ่มความเชื่อมั่น · ห่าง >10% = หา root cause ทีละ judgment call (ใช้ตาราง B2 เป็นตัวเทียบ)

**Trigger (ตอบ Open Item 3):** ไม่ทำทุกเคส — ทำเฉพาะ
1. หุ้นที่จะ **deploy จริง** (ก่อน Max execute), และ
2. หุ้นที่ **ถืออยู่** ที่ re-verify แล้ว MOS **พลิกเครื่องหมาย**, และ
3. เคสที่ CIO สั่งตรง

ต้นทุนประมาณ 1 Emma run (~30-50K token) ต่อเคส — เทียบกับความเสียหายจาก deploy บน FV ที่ผิด ถือว่าคุ้ม; ส่วน learning-queue / SKIP ไม่คุ้ม

---

## 3. ตอบ Open Items

### Open Item 1 — เกณฑ์ตัวเลขของ classification ที่เหลือ

**หลักการ:** ใช้ **GICS เป็นตัวกรองแรก** (เป็นข้อเท็จจริงภายนอก ไม่ใช่ดุลยพินิจ) แล้วเพิ่มเกณฑ์ตัวเลขเฉพาะประเภทที่ GICS แยกไม่ออก

| ประเภท | ตัวกรองแรก | เกณฑ์ตัวเลข (ค่าตั้งต้นที่เสนอ — **ยังไม่ calibrate**) |
|---|---|---|
| ธนาคาร / ประกัน | GICS Financials (Banks, Insurance) | — (GICS พอ) |
| REIT | GICS Real Estate (REITs) | — |
| Utility (regulated) | GICS Utilities | ≥50% revenue มาจาก rate-regulated operations |
| หุ้นลงทุนหนัก | — | PV(TV)/EV > 70% (มีอยู่แล้ว) |
| Software / SaaS โตเร็ว | GICS Software | recurring/subscription revenue ≥60% **และ** revenue growth >15% YoY |
| Cyclical | GICS Semis, Materials, Industrials, Energy, Autos | EBIT ร่วงจาก peak ถึง trough ≥30% ในวัฏจักรล่าสุด (≤10 ปี) **หรือ** สัมประสิทธิ์ความแปรปรวนของ EBIT margin 10 ปี ≥0.3 |
| Biotech / pharma | GICS Biotech, Pharma | rNPV ของ pipeline (ยังไม่ได้รับอนุมัติ) >50% ของ EV → เน้น rNPV; ถ้า <50% → DCF ส่วนที่มีกำไรเป็นหลัก |
| Holding / conglomerate | — | ≥3 segment ที่ไม่เกี่ยวข้องกัน แต่ละ segment ≥15% ของ revenue หรือ EV |
| AI / Infra build-out | — | เกณฑ์ lane เดิม 3 ข้อ (มีอยู่แล้ว) |
| ธุรกิจทั่วไป | — | ไม่เข้าประเภทใดข้างบน (default) |

**ก่อนใช้จริง:** Vera ทดสอบย้อนกับหุ้นที่วิเคราะห์เต็มไปแล้ว (แบบเดียวกับ lane AI/Infra calibration `faa04d2`) — ดูว่าการจัดประเภทตรงกับสามัญสำนึกไหม และไม่มีหุ้นที่เข้า 0 ประเภทหรือ ≥3 ประเภทเยอะผิดปกติ. ผล calibration ไม่นับเป็น trial data

### Open Item 2 — Anchor-proximity threshold

ไม่จำเป็นแล้ว ถ้าเปลี่ยน B1 เป็น pre-registration (§2.1)

### Open Item 3 — ต้นทุน vs ประโยชน์ของ Blind Re-derivation

ดู §2.3 — จำกัดเฉพาะ deploy จริง / ถือครองที่ MOS พลิกเครื่องหมาย / CIO สั่ง

### Open Item 4 — D2 ต้องสะสมข้อมูลนานแค่ไหน

**ความจริงเรื่อง sample size:** ณ 2026-09-06 มี full analyses 25 ตัว (+ re-analyses) — ปัจจุบันน่าจะราว 30 ต้นๆ. ถ้าแบ่ง 10 ประเภท จะเหลือประเภทละ 2-3 ตัว — **ใช้สรุปอะไรไม่ได้ทางสถิติ**

**ข้อเสนอ:**
1. **รวมเหลือ 3 กลุ่ม** สำหรับ D2: (ก) DCF ล้วน (ข) DCF + multiples (VS2 ชั้น 2) (ค) วิธีอื่น (P/B, rNPV, DDM, SOTP)
2. **Log ทุกเคสตั้งแต่วันนี้ แต่ห้ามใช้ตัดสินเปลี่ยนวิธี** จนกว่าแต่ละกลุ่มมี **n ≥ 10 ที่ผ่าน 12 เดือนแล้ว** — ซึ่งคาดว่าอย่างเร็วคือปลายปี 2027
3. **ราคาจริงไม่ใช่ ground truth ของ FV** — ตลาดตั้งราคาผิดได้นานเกิน 6-12 เดือน (นั่นคือเหตุผลที่มี MOS ตั้งแต่แรก). ใช้ realized price เป็นสัญญาณประกอบ คู่กับตัวชี้วัดที่ไม่ขึ้นกับตลาด:
   - **FV drift:** FV จากรอบ re-verify ถัดไป (ข้อมูลใหม่) ต่างจาก FV เดิมเท่าไหร่ และ drift ไปทางเดียวกันต่อเนื่องไหม (bias เชิงระบบ)
   - **ระยะห่างจาก Street PT range:** FV ของเราตกนอก range ของ Street บ่อยแค่ไหน และทางไหน
4. ข้อยกเว้น "ไม่ต้องรอ 8Q เพราะเป็น methodology ไม่ใช่ gate" ในร่างเดิม — **เห็นด้วย** แต่เกณฑ์ "error สูงกว่าค่าเฉลี่ย 4 ไตรมาสติด" ควรใช้หลังข้อ 2 (n ≥10) เท่านั้น ไม่งั้นจะ trigger จาก noise ของ sample 2-3 ตัว

---

## 4. ลำดับการตรวจที่เสนอ (ฉบับแก้)

```
ก่อนคำนวณ:   A2 จัดประเภท (GICS + เกณฑ์ตัวเลข) → A1 หุ้นนี้เข้าประเภทจริงไหม
             → B1' Pre-register judgment calls ใน Data Package
ระหว่างคำนวณ: วิธีหลัก + ตัวตรวจ (มีอยู่แล้ว) → reconcile ถ้าห่าง ≥25% (A3 เติมประโยค)
             → B2 ตาราง judgment-call sensitivity
หลังคำนวณ:    C1–C3 + Market-Implied Sanity Check (มีอยู่แล้ว ใช้ต่อ)
             → B3 blind re-derivation (เฉพาะ deploy / MOS พลิก / CIO สั่ง)
ระยะยาว:      D1/D2 log 3 กลุ่ม → ตัดสินเมื่อ n ≥10/กลุ่ม · D3 ทุกกฎใหม่มี review date
```

---

## 5. ถ้า CIO อนุมัติ — ขอบเขตการแก้ CLAUDE.md (ประมาณการ)

**เพิ่มใหม่ (เป็น `TRIAL` — review 2026-12-31 พร้อม VS2 ชั้น 2):**
1. B1' Pre-registration → ต่อท้าย VS2 ชั้น 1 (ข้อ 1.5)
2. B2 Judgment-call sensitivity table → ต่อท้าย VS2 ชั้น 1 (ข้อ 1.6)
3. B3 Blind re-derivation → ใน Deployment Rules หรือ Max Consultation Rule (trigger ก่อน execute)
4. เกณฑ์ตัวเลขจัดประเภท → เพิ่มคอลัมน์ในตาราง "วิธีคำนวณตามประเภทหุ้น" + บรรทัดเหตุผลระดับประเภท (A1)
5. D2 → เพิ่มใน Vera Quarterly Output (log-only จนกว่า n ≥10)

**แก้ถ้อยคำกฎเดิม (ไม่ใช่กฎใหม่):**
6. Multi-Segment ข้อ 5 → ขยายจาก "Bear floor" เป็น FV ของทุกคน (C3)
7. ตาราง VS2 คอลัมน์ "ตัวตรวจ" → เติม "ห่าง ≥25% ต้อง reconcile" (A3)

**ไม่แตะ:** 40/30/30, MOS threshold, conviction gate, TGR ceiling — ทุกข้อข้างบนเป็น QA/methodology ไม่ใช่ Return-side

---

*Opus 5.5 — 2026-10-12 | Review ของ Hermes validation framework proposal · ยังไม่แก้ CLAUDE.md*
