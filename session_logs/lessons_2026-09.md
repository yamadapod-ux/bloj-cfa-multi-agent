# Monthly Lessons — กันยายน 2026

> Leo ดูแล | Pattern extraction จาก sessions ของเดือนนี้ | สร้าง/อัปเดตต้นเดือนถัดไป หรือเมื่อ CIO เรียก
> ครอบคลุม: 2026-09-01 ถึง 2026-09-23 (อัปเดตล่าสุดหลัง overnight autonomous run — Scout Round 31/32 + Tier 1.5 NVR/BSX)

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

### 1.6 Filter B (multiple percentile cross-check) จับ "AI-capex bubble peak" ได้ถูกต้อง 3 ตัวรวด (Scout Round 32, 23 ก.ย.)
CAT (-24.8% จาก 52W high), VRT (-34.2%), GNRC (-31.7%) ทั้ง 3 ตัวผ่าน Filter A (ลงเกิน 20% จาก high) แต่ **REJECT ที่ Filter B ทั้งหมด** เพราะ EV/EBITDA ยังอยู่ 93.9th/34.36x-vs-5Y-avg-21.85x/95.4th percentile ของ 5Y history ตัวเอง — สรุปคือ 52W high เดิมของทั้ง 3 ตัวเป็น **AI-infra-capex bubble peak** ไม่ใช่ fair-value anchor ปกติ นี่คือตัวอย่างที่ชัดที่สุดเท่าที่เคยมีมาของ Filter B ทำงานตามที่ CLAUDE.md ออกแบบไว้ ("ถ้าอยู่ >70th percentile ทั้งที่ราคาลงจาก high = high เดิมเป็น bubble, ตกรอบ") — สัญญาณว่า screen มีความสามารถแยก "ราคาตก" ออกจาก "ราคาตกจนถูกจริง" ได้ดีในหมวด AI-infra-adjacent industrials โดยเฉพาะ

### 1.7 Tier 1.5 learning-queue token cost เกิน estimate ~3× ยืนยันเป็นครั้งที่ 3 ติดต่อกัน (LKQ → NVR → BSX)
| Ticker | Date | Emma | Bear-lite | รวม |
|--------|------|------|-----------|-----|
| LKQ | 2026-09-07/08 | 84K | 58K | 142K |
| NVR | 2026-09-23 | 92K | 68K | 160K |
| BSX | 2026-09-23 | 99K | ~66K | ~165K |

Proposal เดิม (Scout Funnel Redesign, 2026-09-06) ประเมิน lightweight tier ไว้ที่ ~30-50K — ของจริงสูงกว่านั้นราว **3×** ทุกครั้งไม่มีข้อยกเว้น (n=3 แล้ว) นี่ไม่ใช่ one-off variance อีกต่อไปแต่เป็น **systematic underestimate ของ agent-framework overhead** (ตรงกับ error class เดียวกับ Tier 1 Quick-Screen v1 ใน 1.3) — สำคัญสำหรับ Vera trial review 2026-12-31: ถ้า escalate rate ของ learning-queue ยังสูง (LKQ escalate แล้ว, NVR/BSX ยัง park/watch) การมี lightweight tier ต้นทุนจริงอาจใกล้เคียงหรือแพงกว่าการส่งตรงเข้า fast-track ในบางเคส ต้องคำนวณ breakeven ใหม่ด้วยตัวเลขจริงไม่ใช่ estimate เดิม

### 1.8 FDX corporate-action data integrity — ต้องเช็คก่อนใช้ 52W-high comparison เป็น Filter A input (Scout Round 32, 23 ก.ย.)
FedEx spin-off segment ออกเป็น FDXF (มิ.ย. 2026) ทำให้ราคา FDX ร่วง -17.79% ในวันเดียวจาก corporate action ไม่ใช่ organic decline — 52W high $392.86 ที่ตั้งไว้ก่อนวันนั้นทำให้ % from high comparison ไม่ valid ตรงๆ Max flag ได้ถูกต้องและอ้างอิง precedent เดียวกัน (BDX/Waters spin, Round 29) — เป็นสัญญาณว่า scout scanning ควรมี "corporate action check" (spin-off/merger/special-dividend) เป็น step มาตรฐานก่อนคำนวณ Filter A ให้กับทุก candidate ที่มี high volatility 1-day move ผิดปกติ ไม่ใช่รอให้เจอทีละตัว

---

## 2. Calibration Update — agent ปรับตัวยังไง

- **Charlie:** เขียน Strategic Note ฉบับแรก (1 ก.ย.) เมื่อ CIO ถามภาพรวมตรงๆ — แยก 0/20 deploy ออกเป็น "gate ทำงานถูกต้อง" vs "scout ป้อน universe ผิด" อย่างชัดเจน แทนที่จะแก้ gate เมื่อรู้สึกหงุดหงิดกับ 0 deploy — ยึด Pre-commitment Rule ไว้แน่น (alpha −0.8% ยังไม่เข้า rolling-4Q trigger)
- **Atlas:** Regime override เป็น judgment-based มากขึ้น — TC override จาก raw majority-vote RISK-ON 3/4 ต่อเนื่องหลายวัน (9/1 จาก Fed-hawkish+geopolitical shock, 9/3 จาก equity risk premium compressed) แสดงว่า Atlas ใช้ judgment มากกว่าทำ mechanical vote เฉยๆ
- **Emma/Quinn/Bear:** DCF Cash Flow Consistency Rule ทำงานเสถียรต่อเนื่อง (RDDT reconciliation gap 12.5-14.3% << 25% threshold, FSLR/CNC ไม่ trigger เพราะ SBC ต่ำ) — internalize สำเร็จตั้งแต่เดือนที่แล้ว ไม่มี error ใหม่ในหมวดนี้เดือนนี้
- **Max:** เริ่มแยก "QUICK-SCREEN SKIP" (Tier 1) ออกจาก "SKIPPED" (full pipeline) ใน deployment_log.md อย่างชัดเจน — ป้องกันความสับสนว่า candidate ไหนผ่าน full research แล้วบ้าง
- **Bear (Tier 1.5, 23 ก.ย.):** เริ่มใช้ "reverse-DCF-consistency check" เป็นเครื่องมือ cross-check เชิงระบบใน lightweight assessment (NVR case) — จับได้ว่า scenario ของ Emma เอง (แม้ label ว่า "conservative") ยัง optimistic กว่า market-implied growth จริง เป็น technique ใหม่ที่ไม่เคยเห็นชัดเจนขนาดนี้มาก่อนใน Tier 1.5 — ควรเป็น standard step ต่อไป

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

### 3.5 Filter D ยังกัน MOS-less deploy ได้แม้กับ business คุณภาพสูงสุดที่เคย scout มา (NVR, 23 ก.ย.)
NVR มี ROIC 41.88% — สูงสุดเท่าที่เคย scout มาในทุก round — ผ่าน Filter A+B+C ชัดเจนทั้งหมด แต่ Filter D REJECT เพราะไม่มี credible valuation gap และแม้ Max พยายามหาเหตุผล (capital-light land-option model อาจถูก naive perpetuity underestimate) ให้ Emma ทำ lightweight ทดสอบสมมติฐานนั้นโดยตรง ผลคือ Bear's reverse-DCF ยืนยันว่าตลาด price-in growth (2.7%) สูงกว่าที่แม้แต่ Emma's "conservative" scenario ประเมินไว้ — **Filter D ทำงานถูกต้องแม้กับ business model ที่ผิดปกติ** (land option vs land bank) ยืนยันว่ากฎนี้ไม่ได้ตัดสิน "ธุรกิจดีไหม" แต่ตัดสิน "มี margin of safety จริงไหม" สองเรื่องนี้แยกกันเด็ดขาดตามที่ระบบออกแบบไว้ — เป็นหลักฐานเพิ่มเติมสนับสนุน Pre-commitment Rule ที่ห้ามแก้ Return-side rules ด้วยอารมณ์ (แม้ตอนนี้จะยังเป็น trial period ของ Filter D/E ที่ยังไม่ lock)

---

## 4. CIO Override Events

ไม่มีในเดือนนี้ที่เป็น override จริง (CIO ยังให้ทีม autonomy เต็มตาม preference เดิม) แต่มี **CIO-directed exception เพิ่มขึ้นเป็น 4 ครั้ง** ที่ควรบันทึกแยกจาก override เพราะไม่ใช่การขัดแย้งกับทีม:
1. **FSLR (3 ก.ย.)** — CIO สั่งวิเคราะห์เต็มแม้ Regime = TRANSITIONAL-CAUTIOUS (ปกติ block) เพื่อเป็น "learning exercise" พิสูจน์ว่า valuation gate ทำงานอิสระจาก regime gate จริงไหม — ผลลัพธ์ยืนยัน double-blocked ถูกต้องตามที่ออกแบบไว้
2. **GEV (5 ก.ย.)** — CIO สั่งทดสอบ ticker ที่ de-list ไปแล้ว ("Thesis dead" 7/30) เป็น system-test ของ Tier 1 Quick-Screen v2 — เผยบั๊ก tool-grant (ดู 1.3)
3. **QCOM (5 ก.ย.)** — CIO ตั้งสมมติฐานเองว่าราคาร่วงน่าจะทำให้ MOS ดีขึ้น ทีม re-analyze แล้วพบผลตรงข้าม (ดู 3.3) — CIO ไม่ push back ต่อผลลัพธ์ที่ขัดกับสมมติฐานตัวเอง สอดคล้องกับ preference "learning over returns"
4. **Overnight autonomous run (23 ก.ย., ก่อนนอน)** — CIO อนุมัติให้ทีมทำงานต่อเนื่องไม่มี review ระหว่างทาง ("scout เสร็จ วิเคราะห์ต่อเลย ไม่ต้องเอาเบา") พร้อมกำหนดขอบเขตชัดเจนล่วงหน้า (ห้ามแตะ dashboard/git/decisions.md) — เป็นสัญญาณความไว้วางใจในกลไก scope-limiting ของทีมเอง แต่ก็สร้าง open question ใหม่เรื่อง unattended-run governance (ดู Open Questions ข้อ 7)

---

## 5. Open Questions

1. **Scout scanning process ต้องแก้ยังไง** ให้ราคาที่ scout อ้างแม่นยำขึ้น — ทั้ง ZETA และ CNC ผิดจาก single-source stale/mismatched data ตั้งแต่ scout stage (ไม่ใช่ตอน full pipeline verify) จะเพิ่ม mandatory 2-source check ที่ scout stage เองไหม (ก่อนถึง full pipeline)? — *อัปเดต 23 ก.ย.: ดูเหมือนแก้ไปแล้วบางส่วน (Scout Round 31/32 ระบุ 2-source cross-check สำหรับ BSX แล้ว) ควรยืนยันว่าเป็น standard practice แล้วจริงหรือยัง*
2. **VALUE-FIRST screen ยังไม่มี valid test case ที่ deploy จริง** — APTV/LKQ/LVS ผ่าน scout ไปถึง full pipeline แล้วแต่ทั้งหมดจบที่ NO-DEPLOY (fragile MOS หรือ conviction fail หรือ regime block) — ยังไม่มี BUY แม้แต่ตัวเดียวตั้งแต่ pivot เมื่อ 1 ก.ย. ยังต้องรอ candidate ที่ผ่านครบทุกเงื่อนไขพร้อมกัน
3. **Tier 1 Quick-Screen v2-fixed (WebSearch grant แล้ว) ยังไม่ re-verify live** — token cost จะลดลงจริงตามที่คาดไหม (เทียบ v1 43K / v2-buggy 83K)?
4. **WebSearch quota 200/200 เป็น operational risk ต่อ multi-agent pipeline แค่ไหน** — ควรมีกฎ fallback (เช่น WebFetch เป็น substitute ที่ยอมรับได้) เขียนเป็นทางการใน CLAUDE.md ไหม หรือเป็น one-off ที่ไม่เกิดซ้ำบ่อย?
5. **Vera weekly cadence lapse (~4 สัปดาห์)** — ควรมี mechanism เตือนอัตโนมัติ (เช่น check วันที่ของ weekly report ล่าสุดทุกครั้งที่ Portfolio Review เกิดขึ้น) เพื่อไม่ให้เกิดซ้ำไหม?
6. **REGN Re-Analysis Trigger #2** — resolved แล้ว 11 ก.ย. (stale-FV artifact, ไม่ใช่ overvaluation จริง — ดู batch closure 13 ก.ย.) — ปิด item นี้แล้ว
7. **Energy sector hunting-ground assumption ใน CLAUDE.md อาจล้าสมัย (ใหม่ — 23 ก.ย.)** — Scout Round 32 พบว่า WebSearch ยืนยัน XLE +47.7% YTD และ Morningstar US Energy Index +43.19% YTD = **best-performing S&P sector ปี 2026** (จาก Iran-war oil-price spike + Strait of Hormuz closure) — ตรงข้ามกับสมมติฐาน "energy E&P + midstream เป็น de-rated pocket" ที่ CLAUDE.md ใช้เป็น hunting-ground อ้างอิงเดิม Max ตัดออกจาก mandate ก่อน scan ได้ถูกต้องในคืนนี้ (ไม่เสีย token ไปกับ sector ที่ผิดสมมติฐาน) **แต่ CLAUDE.md เองยังไม่ได้ refresh assumption นี้** — Leo ไม่มีสิทธิ์แก้ CLAUDE.md เอง ต้องให้ CIO ตัดสินใจว่าจะปรับ hunting-ground list ทั้งก้อนหรือปล่อยให้แต่ละ scout round ตรวจสอบสดเองแบบที่เพิ่งทำไปคืนนี้
8. **Unattended overnight run governance (ใหม่ — 23 ก.ย.)** — คืนนี้เป็นครั้งแรกที่ทีมรัน 3 agent-runs ต่อเนื่องโดยไม่มี CIO review ระหว่างทางเลย (ต่างจาก Session Interruption/Resume Protocol ที่เป็นเรื่อง technical limit ไม่ใช่ deliberate unattended operation) — ทำงานได้ราบรื่นด้วย scope ที่กำหนดไว้ล่วงหน้าชัดเจน (ห้ามแตะ dashboard/git/decisions.md) ควรพิจารณาว่านี่ควรเป็น pattern ที่เป็นทางการ (เช่น "overnight scope contract" มาตรฐาน) สำหรับครั้งต่อไปที่ CIO อนุมัติแบบนี้ไหม หรือควรอยู่แค่ ad-hoc ตามที่ CIO สั่งตรงแต่ละครั้ง?

---
*Leo — 2026-09-23 (21:39, overnight autonomous run) | Monthly Lessons กันยายน 2026 อัปเดต — เพิ่ม section 1.6-1.8 (Filter B bubble-peak catch ×3, Tier 1.5 token cost 3× pattern ×3rd confirm, FDX corporate-action flag), 2 (Bear reverse-DCF technique), 3.5 (Filter D holds on best-ROIC-ever candidate), 4 (overnight-run exception #4), 5 (Q7-8 ใหม่: Energy hunting-ground staleness + unattended-run governance). Sessions ที่เพิ่มเข้ามาตั้งแต่บันทึกครั้งก่อน (5 ก.ย.): RDDT full exit, ACN/REGN/CRM/ADBE/GOOGL/ADSK Re-Analysis batch closure (13 ก.ย.), LVS full analysis (20 ก.ย.), Scout Round 30/31/32 + Tier 1.5 NVR/BSX (overnight 23 ก.ย.)*
