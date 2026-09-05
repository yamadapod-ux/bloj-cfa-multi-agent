# Monthly Lessons — กันยายน 2026

> Leo ดูแล | Pattern extraction จาก sessions ของเดือนนี้ | สร้าง/อัปเดตต้นเดือนถัดไป หรือเมื่อ CIO เรียก
> ครอบคลุม: 2026-09-01 ถึง 2026-09-05 (5 sessions แรกของเดือน)

---

## 1. Pattern Recognition — เรื่องที่เกิดซ้ำเดือนนี้

### 1.1 Scout price data integrity — ผิดพลาด 2 ครั้งติดกันใน 1 สัปดาห์ (ZETA → CNC)
| Ticker | Date | Scout อ้างราคา | ราคาจริง (verified) | Error |
|--------|------|----------------|----------------------|-------|
| **ZETA** | 2026-09-01 | $23.50 ("2.8x P/S discount") | $30.88 (near-ATH, YTD +52%) | +31% |
| **CNC** | 2026-09-04 | $43.68 ("beaten-down 33.8% จาก 52W high") | $68.02 (ห่างจาก 52W high แค่ -1.9%) | +55.7% (รุนแรงกว่า ZETA) |

**Pattern:** ทั้งคู่มาจาก Scout Round 27 (VALUE-FIRST screen ที่เพิ่งเปลี่ยนวันที่ 1 ก.ย.) — thesis เดิม ("cheap/beaten-down") พังทันทีที่ Atlas verify ราคาสด 2 sources ใน Phase 1 ของทุกครั้ง /analyze workflow ทำงานถูกต้อง — จับได้ก่อนที่จะ deploy ผิดพลาด แต่ทีมเลือกเดินหน้า full pipeline ต่อด้วยราคาที่ verify แล้วแทนที่จะหยุดกลางคัน (ตาม ZETA precedent) ทั้งสองครั้ง — ผล AVOID ยืนยันด้วยเหตุผล valuation ล้วนๆ ไม่กระทบ decision แต่ทำให้ token เสียไปกับ candidate ที่ premise ผิดตั้งแต่ scout stage และ n=2 นี้ยังไม่ใช่ valid test case ของ VALUE-FIRST screen ใหม่เพราะ premise ผิดตั้งแต่ต้นทั้งคู่ — escalate เป็นเรื่องจริงจังให้ Max ทบทวน scout scanning process แยกต่างหาก (ไม่ใช่แค่ ZETA one-off อย่างที่คิดตอนแรก)

### 1.2 "Priced-for-perfection" NO-DEPLOY streak ยืดยาวต่อเนื่องข้ามเดือน (สิ้นสุดที่ 8 ครั้งติด ก่อนพัก scout)
MU(8/27)→CRCL(8/28)→ADI(8/29)→MELI(8/29)→GCT(8/30)→CHYM(8/31)→**ZETA(9/1)→OSCR(9/1)** = 8 candidates ติดกัน จบด้วย 0 deploy จาก ~20 analyses ใน 2.5 เดือน — เป็นตัวกระตุ้นให้ CIO สั่ง "จัดการสิ่งที่ควรทำ" (1 ก.ย.) นำไปสู่ 3 การเปลี่ยนแปลง process ใหญ่ (ดู 3.1)

### 1.3 Process/rule change ต้อง iterate ถึง 2-3 รอบเพราะ premise ผิดตั้งแต่ออกแบบ (Tier 1 Quick-Screen)
| เวอร์ชัน | Design | ผลจริงเมื่อ live-test | สาเหตุที่ผิด |
|---------|--------|------------------------|--------------|
| v1 (4 ก.ย.) | Check 3 spawn Bear-lite subagent, ประเมิน ~10-15K tokens | QCOM live test (5 ก.ย.) = **~43K tokens** จริง | ประเมิน token cost จาก raw WebSearch count เฉยๆ ไม่ได้คิด agent-framework overhead |
| v2 (5 ก.ย.) | Charlie ทำ WebSearch เอง (ไม่ spawn subagent) check 3 กลายเป็น flag ไม่ใช่ gate | GEV live test = ต้อง spawn sub-subagent อยู่ดี เพราะ charlie.md **ไม่เคยมี WebSearch tool grant** → ใช้ไป **~83K tokens** (แพงกว่า v1 เกือบเท่าตัว) | ออกแบบ v2 บนสมมติฐานว่า Charlie ทำ WebSearch ได้เอง โดยไม่เช็ค tool grant จริงก่อน |
| v2-fixed (5 ก.ย.) | เพิ่ม WebSearch ให้ charlie.md tool grant | ยังไม่ re-verify live | — |

**บทเรียนที่ต้องจำ:** เมื่อออกแบบ process ใหม่ที่พึ่งพา capability ของ agent ตัวใดตัวหนึ่ง (เช่น "Charlie ทำ X เอง") **ต้องเช็ค tool grant จริงในไฟล์ agent ก่อนเขียนกฎ** ไม่ใช่สมมติจาก role description — นี่คือ error class เดียวกับที่เคยเจอใน Vera (feedback_vera_tracker_data_loss — grant ไม่ตรงกับ instruction)

### 1.4 Parallel agent execution ทำให้เกิด data conflict ได้ (S&P 500 case, 4 ก.ย.)
Max's Portfolio Review และ Vera's Weekly Report รันคู่ขนานกันใน session เดียวกัน ต่างคน WebSearch ราคา S&P 500 close 2026-09-03 เอง — ได้ 3 ค่าต่างกัน: Max $7,699.64 (บทความ stale/mismatched), Vera $7,747.71 (verified ผ่าน day-chain + cross-source), CIO ad-hoc WebSearch ได้ค่าที่ 3 อีกอัน (ทั้งหมด root cause เดียวกัน: รันพร้อมกันจึงไม่มีโอกาส cross-check กันก่อน Single Source of Truth Rule's "flag if inconsistent" step จะทำงาน) → แก้ด้วย repeat targeted WebSearch สร้าง day-by-day chain (Sept1 $7,631.47 → Sept2 $7,666.60 → Sept3 $7,747.71, %-change สอดคล้องกันภายในทุกวัน) cross-verify CNBC+Yahoo Markets ยืนยัน $7,747.71 ถูกต้อง → **alpha ที่เคยรายงานไว้ +1.56%/+1.07% ถูกแก้เป็น +0.42%** (portfolio.js + dataIntegrityLog)

### 1.5 Vera weekly cadence ขาดหายไปเกือบ 4 สัปดาห์ก่อนถูกจับได้
4 ก.ย. เป็นครั้งแรกที่ Vera ทำ Weekly Report catch-up หลังห่างหายไปพักใหญ่ — ระหว่าง catch-up พบว่า alpha ที่บันทึกไว้ตอน RDDT exit (+1.56%) เป็น partial/ผิดพลาด ตัวจริงคือ +0.42% (เกี่ยวเนื่องกับ 1.4 ด้วย) — **ระบบยังไม่มีกลไกเตือนอัตโนมัติเรื่อง cadence lapse** ต้องพึ่ง CIO/Vera สังเกตเอง

---

## 2. Calibration Update — agent ปรับตัวยังไง

- **Charlie:** เขียน Strategic Note ฉบับแรก (1 ก.ย.) เมื่อ CIO ถามภาพรวมตรงๆ — แยก 0/20 deploy ออกเป็น "gate ทำงานถูกต้อง" vs "scout ป้อน universe ผิด" อย่างชัดเจน แทนที่จะแก้ gate เมื่อรู้สึกหงุดหงิดกับ 0 deploy — ยึด Pre-commitment Rule ไว้แน่น (alpha −0.8% ยังไม่เข้า rolling-4Q trigger)
- **Atlas:** Regime override เป็น judgment-based มากขึ้น — TC override จาก raw majority-vote RISK-ON 3/4 ต่อเนื่องหลายวัน (9/1 จาก Fed-hawkish+geopolitical shock, 9/3 จาก equity risk premium compressed) แสดงว่า Atlas ใช้ judgment มากกว่าทำ mechanical vote เฉยๆ
- **Emma/Quinn/Bear:** DCF Cash Flow Consistency Rule ทำงานเสถียรต่อเนื่อง (RDDT reconciliation gap 12.5-14.3% << 25% threshold, FSLR/CNC ไม่ trigger เพราะ SBC ต่ำ) — internalize สำเร็จตั้งแต่เดือนที่แล้ว ไม่มี error ใหม่ในหมวดนี้เดือนนี้
- **Max:** เริ่มแยก "QUICK-SCREEN SKIP" (Tier 1) ออกจาก "SKIPPED" (full pipeline) ใน deployment_log.md อย่างชัดเจน — ป้องกันความสับสนว่า candidate ไหนผ่าน full research แล้วบ้าง

---

## 3. Rule Pressure Points

### 3.1 Scout Filter Rules (CLAUDE.md) — แก้ไขจริงเดือนนี้ (1 ก.ย.)
เปลี่ยนจาก growth-momentum เป็น **VALUE-FIRST** (ราคาลง ≥30% จาก 52W high บังคับ + FCF yield/EV-EBITDA cheap + ROIC>WACC) — ไม่แตะ MOS threshold/conviction gate (Return-side locked). เพิ่ม Vera Funnel Health/Deploy-Rate trigger + `portfolio/buy_list.md` ใหม่ (pre-analyzed names รอ pullback). **ยังไม่มี valid test case จริง** — 2 candidates แรกที่ทดสอบ (ZETA, CNC) ทั้งคู่ scout price ผิดตั้งแต่ต้น (ดู 1.1) จึงยังตอบไม่ได้ว่า screen ใหม่คัดถูกต้องจริงหรือไม่

### 3.2 Max Consultation Rule — ทดสอบ edge case ใหม่ (RDDT full exit, 3 ก.ย.)
Full pipeline recommendation (SELL) นับเป็น "consulted by pipeline design" ตาม CLAUDE.md อยู่แล้ว — Charlie review แล้ว concur กับ full exit (ไม่ใช่ partial trim) แม้ Strategic Note เดิม (1 ก.ย.) เคย lean ไปทาง "HOLD-core + tighten stop" — เป็นตัวอย่างที่ escalation จาก lightweight → full pipeline เปลี่ยนข้อสรุปของ Charlie เองได้เมื่อข้อมูลใหม่ชัดเจนขึ้น (Quinn/Bear stale correction)

### 3.3 Re-Analysis Trigger Rule — ยิงถูกต้องบน QCOM (5 ก.ย.)
Trigger #2 (FV อายุเกิน 90 วัน + price divergence -22.6%) ทำงานตามออกแบบ — ผลลัพธ์หักล้าง assumption ของ CIO เอง (ราคาร่วง ≠ MOS ดีขึ้นเสมอ) เป็นหลักฐานว่า trigger นี้ยังจำเป็นแม้ทีมจะ "รู้สึกว่า" ราคาถูกลงแล้วน่าจะปลอดภัยกว่า

### 3.4 WebSearch budget (200/200) หมดกลาง session — เจอครั้งแรกที่บันทึกชัดเจน (QCOM, 5 ก.ย.)
Bear และ Morgan ทั้งคู่ต้องสลับไปใช้ WebFetch แทน WebSearch กลาง session เพราะ quota เต็ม — Morgan ยอมรับว่า WebFetch เป็น "acceptable substitute" เพราะยัง independent-fetch ไม่ใช่เชื่อ citation ของรายงาน แต่ Bear ยอมรับตรงๆ ว่ามี data gap จริง (US-China summit catalyst ยัง verify ไม่ได้) — **นี่คือ operational constraint ใหม่ที่ยังไม่มีกฎรองรับ** ว่าจะทำอย่างไรเมื่อ budget หมดกลาง multi-agent pipeline (คล้ายกับ Session Interruption/Resume Protocol แต่คนละสาเหตุ — อันนี้คือ tool quota ไม่ใช่ session limit)

---

## 4. CIO Override Events

ไม่มีในเดือนนี้ (ณ วันที่บันทึก 2026-09-05) — CIO ยังให้ทีม autonomy เต็มตาม preference เดิม แต่มี **CIO-directed exception 2 ครั้ง** ที่ควรบันทึกแยกจาก override เพราะไม่ใช่การขัดแย้งกับทีม:
1. **FSLR (3 ก.ย.)** — CIO สั่งวิเคราะห์เต็มแม้ Regime = TRANSITIONAL-CAUTIOUS (ปกติ block) เพื่อเป็น "learning exercise" พิสูจน์ว่า valuation gate ทำงานอิสระจาก regime gate จริงไหม — ผลลัพธ์ยืนยัน double-blocked ถูกต้องตามที่ออกแบบไว้
2. **GEV (5 ก.ย.)** — CIO สั่งทดสอบ ticker ที่ de-list ไปแล้ว ("Thesis dead" 7/30) เป็น system-test ของ Tier 1 Quick-Screen v2 — เผยบั๊ก tool-grant (ดู 1.3)
3. **QCOM (5 ก.ย.)** — CIO ตั้งสมมติฐานเองว่าราคาร่วงน่าจะทำให้ MOS ดีขึ้น ทีม re-analyze แล้วพบผลตรงข้าม (ดู 3.3) — CIO ไม่ push back ต่อผลลัพธ์ที่ขัดกับสมมติฐานตัวเอง สอดคล้องกับ preference "learning over returns"

---

## 5. Open Questions

1. **Scout scanning process ต้องแก้ยังไง** ให้ราคาที่ scout อ้างแม่นยำขึ้น — ทั้ง ZETA และ CNC ผิดจาก single-source stale/mismatched data ตั้งแต่ scout stage (ไม่ใช่ตอน full pipeline verify) จะเพิ่ม mandatory 2-source check ที่ scout stage เองไหม (ก่อนถึง full pipeline)?
2. **VALUE-FIRST screen ยังไม่มี valid test case** — ต้องรอ candidate ตัวที่ 3 ที่ scout price ถูกต้องตั้งแต่ต้นก่อนถึงจะประเมินได้ว่า screen ใหม่ทำงานดีกว่าเดิมจริงไหม
3. **Tier 1 Quick-Screen v2-fixed (WebSearch grant แล้ว) ยังไม่ re-verify live** — token cost จะลดลงจริงตามที่คาดไหม (เทียบ v1 43K / v2-buggy 83K)?
4. **WebSearch quota 200/200 เป็น operational risk ต่อ multi-agent pipeline แค่ไหน** — ควรมีกฎ fallback (เช่น WebFetch เป็น substitute ที่ยอมรับได้) เขียนเป็นทางการใน CLAUDE.md ไหม หรือเป็น one-off ที่ไม่เกิดซ้ำบ่อย?
5. **Vera weekly cadence lapse (~4 สัปดาห์)** — ควรมี mechanism เตือนอัตโนมัติ (เช่น check วันที่ของ weekly report ล่าสุดทุกครั้งที่ Portfolio Review เกิดขึ้น) เพื่อไม่ให้เกิดซ้ำไหม?
6. **REGN Re-Analysis Trigger #2 กำลัง deepen** (MOS -6.50% จาก -0.89%, ราคาแตะ 52W high ใหม่) — Emma batch FV re-verify (commissioned 1 ก.ย., priority ACN→CRM→REGN→ADBE→GOOGL→ADSK) ยังไม่ execute ณ วันที่บันทึกนี้ — เป็น outstanding action item ที่ต้องติดตามต้นเดือนถัดไป

---
*Leo — 2026-09-05 | Monthly Lessons กันยายน 2026 (sessions เดือนนี้ ณ วันที่บันทึก: ZETA, OSCR, RDDT Lightweight+Full Re-Analysis, FSLR, CNC, QCOM Re-Analysis, GEV Tier1-test, Charlie Strategic Note, Max Portfolio Review 9/1+9/4, Vera Weekly catch-up)*
