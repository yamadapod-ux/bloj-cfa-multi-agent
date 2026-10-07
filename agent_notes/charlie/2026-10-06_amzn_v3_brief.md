# AMZN v3 — Business-Type-Correct Re-run (Learning run, CIO approved 2026-10-06)

> ร่างโดย Opus 2026-10-06 — Sonnet อ่านจากไฟล์นี้โดยตรง ห้าม copy จากแชท
> **ไม่ใช่ trial data ของ LANE-AI-INFRA** (CLAUDE.md § Lane ข้อ 5 — ห้ามนับ AMZN) · เป็นงานเรียนรู้: "ถ้าใช้เครื่องมือที่ถูกกับธุรกิจประเภทนี้ ผลต่างจาก v1/v2 แค่ไหน และเพราะอะไร"
> Re-analysis file rule (กฎเหล็ก 11): append Update Log ใน `reports/AMZN_2026-10-06_v2_rerun.md` หรือสร้างไฟล์ v3 ตาม precedent v2 — เลือกแบบเดียวกับ v2 เพื่อให้เทียบกันได้ · dashboard/data.js แทนที่ object เดิม ห้ามซ้อน

## ทำไมต้องรันใหม่ (จุดอ่อนของ v1/v2)
1. TGR exception ใน v2 ทดสอบด้วย **trailing company-level ROIC vs WACC** — v2 รัน 14:04 ก่อนกฎ in-service/incremental ROIC (`e167bfb` 15:22) → ใช้เกณฑ์ที่เรายอมรับแล้วว่าผิดสำหรับ build-out
2. Bear ข้อหลัก "ROIC ครึ่งหนึ่งของ GOOGL/MSFT ทั้งที่ capex 2x" = วงกลม: capex หนัก → CIP อยู่ในตัวหาร → ROIC ต่ำ → ถูกลงโทษซ้ำ
3. ROIC/margin รวมบริษัทเอา AWS (op margin ~39%) ปนกับ retail (margin บาง) → ควรแยกประเมิน
4. WACC 11.2% (β 1.44) อยู่นอกกรอบ mega-cap 7–9% ใน CLAUDE.md — ไม่เคยถูก challenge

## ⚠️ Anti-goal-seeking (บังคับ — อ่านก่อนเริ่ม)
- **ล็อกวิธีการทั้งหมดในไฟล์นี้ก่อนดูผล** — ห้ามเปลี่ยนวิธี/peer/ตัวเลขหลังเห็น FV
- CIO มีความเห็นว่า AMZN ระยะยาวไม่น่าอยู่แค่ $200 — **นั่นคือ hypothesis ที่ v3 ทดสอบ ไม่ใช่คำตอบที่ต้องได้** ถ้า v3 ยังได้ FV ใกล้ $200 → รายงานตามจริงพร้อมเหตุผล
- Peer/segment multiple ต้องเลือกก่อนคำนวณ (ตาม peer-selection guideline B-V1) และบันทึกเหตุผล
- Return-side locked rules ไม่เปลี่ยน (40/30/30, MOS threshold, conviction gate)

## Pipeline: Atlas → Emma ∥ Quinn → Bear → Charlie → Morgan (ตามปกติ, ราคาสด ≥2 sources)

### Atlas — Data Package เพิ่มเติม
- Segment reporting จาก 10-K/10-Q ล่าสุด: revenue, operating income, **capex และ assets ต่อ segment** (AWS / North America / International; ads ถ้าแยกเปิดเผยได้ — ถ้าไม่มีให้ระบุว่าเป็น estimate พร้อมที่มา)
- PP&E แยก **construction in progress (CIP)** vs in-service (10-K PP&E note)
- Beta จาก ≥3 แหล่ง (เช่น stockanalysis, Yahoo, Morningstar/GuruFocus) + 10Y Treasury + ERP source
- Classification เข้า LANE-AI-INFRA หรือไม่ (รายงาน PASS/FAIL/DATA_INSUFFICIENT ตาม patch3) — ใช้เพื่อเลือกเครื่องมือเท่านั้น ไม่นับ trial

### Emma — วัดด้วยเครื่องมือของ build-out
1. **ROIC บน in-service capital** (หัก CIP ออกจาก invested capital) — company-level และ AWS-level
2. **Incremental ROIC 3 ปี และ 5 ปี** (ΔNOPAT ÷ Δinvested capital) แสดงทั้งคู่
3. **Sum-of-the-parts:** AWS (DCF แยก หรือ EV/EBIT จาก peer cloud ที่เลือกก่อน) + Retail NA/Intl (EV/Sales หรือ EV/EBIT จาก peer retail) + Ads (ถ้าแยกได้) − net debt
4. Consolidated DCF แสดง **ROIC recovery path รายปี** + capex/revenue path ที่ normalize ลงเมื่อ build-out จบ
5. **WACC reconciliation:** แสดง WACC จาก β ทั้ง 3 แหล่ง + bottom-up β (peer unlevered) → เลือก 1 ค่าพร้อมเหตุผล; ถ้ายังอยู่นอก 7–9% ต้องอธิบายว่าทำไม
6. TGR: ทดสอบ capex-cycle exception ใหม่ด้วยเกณฑ์ `e167bfb` (in-service + incremental ROIC)

### Quinn
- Sensitivity 5×5: **WACC × AWS growth** (แทน Yr1 growth × WACC เดิม)
- **Reverse DCF:** ที่ราคาปัจจุบัน ตลาด price-in growth/margin/WACC เท่าไหร่
- **Forward value path:** FV ณ ปี 2027 / 2029 / 2031 (ใน base case) — ตอบคำถาม "ระยะยาวมูลค่าไปถึงไหน" แยกจาก "วันนี้ควรจ่ายเท่าไหร่"
- P-W EV 3 scenario; Bear scenario ≥25% และรวมกรณี capex ไม่ได้ผลตอบแทน

### Bear
- แยก Temporary/reinvestment vs Structural ทุกข้อ (กฎ Bear Discount Classification)
- ห้ามใช้ trailing ROIC รวมบริษัทเป็นหลักฐาน impairment — ถ้าจะแย้งเรื่องผลตอบแทน capex ต้องใช้ incremental/in-service ROIC
- Thesis Invalidation ผูก milestone + วันที่ (เช่น AWS growth / AWS margin / backlog ในไตรมาสที่ระบุ)
- Bear ยังต้องแย้งจริง — เช่น AWS share loss, antitrust, capex overbuild ทั้งอุตสาหกรรม

### Charlie — ส่วนบังคับใน report
**ตารางเทียบ v1 / v2 / v3:**

| | v1 (เช้า) | v2 (14:04) | v3 | Δ v3 vs v2 | สาเหตุ |
|---|---|---|---|---|---|
| Emma FV | $230.63 | $230.63 | | | |
| Quinn P-W EV | $203.50 | $203.50 | | | |
| Bear FV | $159.72 | $156.27 | | | |
| Blended FV | $201.22 | $200.18 | | | |
| MOS | -20.3% | -21.4% | | | |
| WACC | 11.2% | 11.2% | | | |
| TGR | 3.0% | 3.0% | | | |
| Conviction avg | 5.33 | 5.40 | | | |
| Verdict | NO BUY | NO BUY | | | |

**Attribution:** แยกว่า Δ มาจากแต่ละการเปลี่ยนแปลงเท่าไหร่ (in-service ROIC/TGR · SOTP · WACC · Bear reclassification) — ทำทีละตัวแบบ step-by-step

**"มูลค่าวันนี้ vs ราคาระยะยาว":** อธิบายภาษาง่ายว่า Blended FV = ราคาที่ควรจ่ายวันนี้เพื่อได้ผลตอบแทน = WACC ไม่ใช่ราคาเป้าระยะยาว + แสดง forward value path ของ Quinn

### Morgan
- ตรวจ anti-goal-seeking: วิธี/peer ตรงกับไฟล์นี้, ไม่มีการเปลี่ยนหลังเห็นผล
- ตรวจ segment numbers + CIP กับ 10-K
- ตรวจ WACC reconciliation

## ผลลัพธ์
- ถ้า v3 ผ่าน gate → ไม่ deploy อัตโนมัติ — Max ต้องปฏิบัติตาม Regime Gate + Max Consultation Rule ปกติ และ flag ให้ CIO เห็นก่อน (เพราะเป็น learning run บน CIO-override ticker)
- ไม่ว่าผลเป็นอย่างไร → Leo บันทึก lesson สั้นๆ ใน learning-log.md: "เครื่องมือแบบไหนเปลี่ยนผลแค่ไหน"
- Commit + push · รายงานกลับ: ตาราง v1/v2/v3 + attribution + verdict

*Opus — 2026-10-06 | AMZN v3 brief, CIO approved item 1*

---

## Addendum (Opus — 2026-10-06, หลัง Sonnet review)

**1. Segment capex — ลองแหล่งนี้ก่อนจะใช้ DATA_INSUFFICIENT:**
- 10-K ของ AMZN ใน segment note (Note "Segment Information") เคยเปิดเผย **"Property and equipment, net by segment"** และ **"Total net additions to property and equipment by segment"** (North America / International / AWS) — ตรวจ 10-K ล่าสุดก่อน (เป็นตัวเลขรายปี; 10-Q อาจไม่มี)
- CIP: 10-K Note "Property and Equipment" มีบรรทัด **"Construction in progress"**
- ถ้า 10-K ล่าสุดไม่มีจริง → รายงาน `DATA_INSUFFICIENT` ตรงๆ ห้ามประมาณจาก capacity/data-center commitment โดยไม่มี source; ถ้าจำเป็นต้องใช้ estimate ให้ label `ESTIMATE` + วิธีคิด + URL และ Emma ต้องแสดง SOTP ทั้งแบบมีและไม่มีตัวเลขนั้น
- Ads ไม่ใช่ segment ที่รายงาน operating income → ใช้ได้แค่ revenue; ถ้าจะแยก Ads ใน SOTP ต้อง label `ESTIMATE` ชัดเจน หรือรวมไว้ใน Retail

**2. Web-search budget:** ตั้ง 40–50 calls ทั้ง pipeline (Atlas ~15–20, Emma ~10, Quinn ~5, Bear ~8–10, Morgan ~5) · ถ้าใกล้หมด → หยุดและรายงานว่าขาดอะไร ห้ามเติมด้วย training knowledge

*Opus — 2026-10-06 | Addendum to AMZN v3 brief*

---

## v3.1 — Correction Run (Opus review of `ccf547e`, CIO approved 2026-10-07)

> Sonnet อ่านจากไฟล์นี้โดยตรง · **แก้เฉพาะจุดที่ผิดกฎ/brief** — ทุกข้อด้านล่างอ้างกฎที่เขียนไว้แล้ว ไม่ได้แก้เพราะไม่ชอบผล
> **Anti-goal-seeking ยังบังคับ:** ถ้า v3.1 ยังได้ FV ต่ำกว่าราคา → รายงานตามจริง · ห้ามแก้อะไรนอกรายการนี้
> Re-analysis file rule: append Update Log ใน `reports/AMZN_2026-10-07_v3.md` + append agent_notes เดิม (ห้ามสร้างไฟล์ v3.1 ใหม่) · data.js แทนที่ object เดิม

### สิ่งที่ v3 ทำถูก — คงไว้ ห้ามแตะ
Segment net sales / op income (ตรง 10-K, 2 sources) · CIP by segment = DATA_INSUFFICIENT · in-service ROIC AWS 25.7% / consolidated 21.76% · incremental ROIC 3yr 31.4% · Beta 3 แหล่ง · WACC arithmetic

### ข้อผิดพลาดที่ต้องแก้

**E1. Attribution ผิด (Charlie)** — v3 อ้างว่า Δ ~80% มาจาก "smoothed-FCF → explicit capex-path" แต่ v2 Emma ก็เป็น explicit path อยู่แล้ว (10yr, revenue 16%→5%, FCF margin 0%→15%). สิ่งที่เปลี่ยนจริงคือ horizon 10→5 ปี และ Yr1 growth 16%→11%. **แก้:** ทำ attribution ใหม่ทีละตัวแปรจากตัวเลขจริง

**E2. Horizon ผิดกฎ (Emma)** — CLAUDE.md (แก้ 2026-10-06): Emma ใช้ explicit 7–10yr+ เป็นค่าเริ่มต้นเมื่อ business case รองรับ. v3 ใช้ 5 ปี แล้วตัดจาก growth 7% (2030) ลง TGR 3% ทันที. **แก้:** explicit **10 ปี (2026–2035)** ให้ growth / capex-to-revenue / margin ค่อยๆ เข้าสู่ steady state ก่อน terminal year (terminal year: growth ใกล้ TGR, reinvestment rate = g ÷ RONIC)

**E3. Yr1 growth ไม่มีที่มา (Emma)** — 11% ไม่มี source. **แก้:** ใช้ consensus revenue growth FY2026/FY2027 (≥2 sources + URL) หรือ build-up จาก segment (AWS / NA / Intl แยก growth) — แสดงที่มา

**E4. DCF ขัดกับ incremental ROIC ของตัวเอง (Emma)** — net investment 2026–29 ≈ $260B สร้าง NOPAT เพิ่มแค่ ≈ $44B (implied ~17%) ขณะที่วัดได้ 31.4%. **แก้:** แสดงบรรทัด **implied RONIC รายปี** ในตาราง DCF (ΔNOPAT(t+1) ÷ net investment(t)) และ reconcile กับ incremental ROIC ที่วัดได้ — ถ้าตั้งใจให้ต่ำกว่า ต้องให้เหตุผลพร้อมหลักฐาน (เช่น AI capex return ต่ำกว่าอดีต — อ้าง source) ไม่ใช่ปล่อยเป็นผลข้างเคียงของ margin path ที่ตั้งเอง. Terminal: reinvestment rate ต้องสอดคล้องกับ g และ RONIC ที่ระบุ

**E5. SOTP multiples ไม่มี source (Emma) — ผิด Training Knowledge Ban + brief** — 15x (NA/Intl) และ 18x (Ads) "ไม่ verify". **แก้:**
- **เลือก peer ก่อนคำนวณ** ตาม B-V1 peer-selection guideline (เขียน list + เหตุผลก่อนดู multiple): retail/logistics peer 3–5 ตัว, cloud/infra peer 3–5 ตัว, digital-ads peer 3–5 ตัว
- EV/EBIT (หรือ EV/EBITDA) ของทุก peer พร้อม URL → ใช้ median; แสดงตารางทุกตัว
- AWS: ทำทั้ง standalone DCF (10yr) **และ** peer EV/EBIT cross-check — ถ้าต่างกัน ≥25% ต้องมี reconciliation table
- Ads: ถ้าหา revenue + URL ได้ → ใช้; margin ยังเป็น ESTIMATE ได้แต่ต้องมีที่มา

**E6. Budget ใช้ไม่ถึงครึ่ง แต่อ้าง DATA_INSUFFICIENT "เพราะเกิน budget" — ผิด patch3** — Emma/Quinn search 0 calls, ทั้ง pipeline 22/40–50. **แก้ (budget v3.1 = 30 calls เพิ่ม):**
- Incremental ROIC 5yr (2020→2025): ดึง op income + PP&E net FY2020 จาก 10-K (SEC / stockanalysis / macrotrends) — ห้าม DATA_INSUFFICIENT ถ้ายังไม่ลองแหล่งบังคับ
- Risk-free: 10Y Treasury ล่าสุด (same-week, ≥2 sources) · ERP: Damodaran ปัจจุบัน + URL
- PP&E / net additions by segment: cross-check source ที่ 2 (SEC filing ตรง)

**E7. ตัวเลข capex ไม่ตรงกันระหว่างรอบ (Atlas)** — v2 ใช้ ~$220B/ปี, v3 ใช้ ~$143B (2026). **แก้:** ยืนยัน (a) capex FY2025 actual จาก cash-flow statement (b) management capex guidance FY2026 — ≥2 sources + URL; ระบุว่า v2 หรือ v3 ผิด และ DCF ใช้ตัวที่ยืนยันแล้ว

**E8. Bear 20% haircut — classification ผิดนิยาม + double-count (Bear)**
- CLAUDE.md นิยาม Structural = "competitive erosion ... ที่**ไม่มี credible recovery path**". AWS share 30%→28% ขณะที่ AWS growth เร่งขึ้น (สูงสุดใน 18 ไตรมาส) + backlog $496B → Bear ต้องอธิบายด้วยหลักฐานว่าทำไมเข้านิยาม structural; ถ้าอธิบายไม่ได้ → จัดเป็น competitive risk (ไม่ใช่ impairment)
- Share-loss risk อยู่ใน Quinn Bear scenario แล้ว → **ห้าม haircut ซ้ำ** บน SOTP
- **Bear FV ต้องเป็น valuation ของ Bear เอง** (เช่น DCF ด้วย bear assumptions ที่ระบุ: AWS growth / margin / capex return ต่ำ) ไม่ใช่ % ลดจากตัวเลขของ Emma
- Bear ยังต้องแย้งจริง — ถ้ามีหลักฐาน structural ที่หนักแน่นก็ใช้ได้

**E9. Thesis Invalidation #3 ใช้ตัวเลขผิดระดับ (Bear)** — "consolidated capex/revenue < 60%" แต่ consolidated อยู่ ~18–20%; 75% คือ AWS. **แก้:** ระบุให้ถูกระดับ (AWS capex/revenue หรือ consolidated) พร้อม threshold ที่สอดคล้องกับ DCF path

**E10. Quinn** — sensitivity / P-W EV / forward value path ต้องรันใหม่บน DCF ที่แก้แล้ว · Bear scenario ≥25% และต้องเป็น DCF ที่มี assumption ชัด (ไม่ใช่ตัวเลขกลม) · Reverse DCF: แสดง implied (growth, margin, RONIC) ที่ราคาปัจจุบัน ไม่ใช่แค่ implied WACC

**E11. Morgan ควร FAIL ไม่ใช่ CONDITIONAL PASS** — multiples ไม่มี source = `SOURCE_MISSING`, horizon ผิดกฎ = `RULE_VIOLATION`, DATA_INSUFFICIENT โดยไม่ลองแหล่งบังคับ = `RULE_VIOLATION`. **แก้:** Morgan QA v3.1 ตรวจ E1–E10 ครบทุกข้อ (checklist ✅/❌ ต่อข้อ) + anti-goal-seeking (วิธี/peer ล็อกก่อนเห็นผล — peer list ต้องมี timestamp ก่อนตาราง multiple) · บันทึก self-correction ว่า v3 QA ควรเป็น FAIL พร้อม reject types

### Charlie — ตารางบังคับ v2 / v3 / v3.1
| | v2 | v3 | v3.1 | Δ v3.1 vs v3 | สาเหตุ (ข้อ E#) |
|---|---|---|---|---|---|
| Emma DCF FV | | | | | |
| Emma SOTP FV | — | | | | |
| Emma FV (final) | $230.63 | | | | |
| Quinn P-W EV | $203.50 | $100.00 | | | |
| Bear FV | $156.27 | $96.72 | | | |
| Blended FV | $200.18 | $101.71 | | | |
| MOS | -21.4% | -60.3% | | | |
| WACC | 11.2% | 11.07% | | | |
| Explicit horizon | 10yr | 5yr | 10yr | | E2 |
| Implied RONIC (avg forecast) | | ~17% | | | E4 |
| Capex FY2026 used | ~$220B? | ~$143B | | | E7 |
| Verdict | NO BUY | NO BUY | | | |

+ attribution ทีละ E# (เปลี่ยนทีละข้อ วัด Δ FV) · + forward value path 2027/2029/2031 ใหม่

### เมื่อเสร็จ
- Leo: แก้ lesson ใน learning-log.md ที่บันทึกจาก v3 ("เครื่องมือถูกต้อง → thesis อ่อนลง") ให้สะท้อนผล v3.1 จริง — เขียนสั้น (ตาม Learning Log Conciseness)
- Commit + push ข้อความอ้าง `AMZN v3.1` · รายงานกลับ: ตาราง v2/v3/v3.1 + attribution ต่อ E# + Morgan verdict + web-search ที่ใช้จริงต่อ agent

*Opus — 2026-10-07 | AMZN v3.1 correction brief, CIO approved*

---

## v3.2 — Segment-Consistency Fix (Opus review of `eb115ac`, CIO approved 2026-10-07) — รอบสุดท้าย

> Sonnet อ่านจากไฟล์นี้โดยตรง · แก้ **จุดเดียว** (internal consistency) + ผลที่ตามมา — ห้ามแตะอย่างอื่น
> คงไว้: segment data, in-service/incremental ROIC, WACC 10.95%, TGR 3%, capex FY2026 $220B, SOTP peer lists + multiples + URLs, AWS standalone DCF, Bear reclassification
> Anti-goal-seeking ยังบังคับ — ผลออกมาเท่าไหร่รายงานตามนั้น · append Update Log ใน `reports/AMZN_2026-10-07_v3.md` + agent_notes เดิม · data.js แทนที่ object เดิม
> **หลังรอบนี้ปิด AMZN learning run** — ไม่มี v3.3 เว้นแต่ CIO สั่ง

### ปัญหาที่พบใน v3.1
| | Consolidated DCF | AWS-only DCF |
|---|---|---|
| EV | $669.7B | $1,247.8B |
| NOPAT 2035 | $168.8B | $207.7B |

Consolidated < AWS ส่วนเดียว → implied retail+ads NOPAT 2035 ≈ **−$39B** (ปัจจุบัน NA+Intl EBIT +$34.4B) = เป็นไปไม่ได้. สาเหตุ: consolidated op margin ตั้งเอง 11.5%→15% ไม่สะท้อน mix shift ที่ AWS model ของ Emma เอง implies (AWS ~44% ของ revenue ที่ margin 42% ปี 2035 → consolidated margin ควรราว ~22%). ผลตาม: implied RONIC 6.5% ต่ำเทียม · Bear DCF ($47.81) สร้างบน framework เดียวกัน (และต่ำกว่า no-growth value ≈ $54) · Emma เฉลี่ย DCF $68 กับ SOTP $191 (ห่าง ~2.8x) โดยไม่ reconcile · Quinn P-W EV = re-weight ตัวเลข Emma/Bear (ไม่ independent, นับซ้ำใน Blended)

### F1. Emma — Consolidated DCF แบบ bottom-up (แทน consolidated top-down ของ v3.1)
- Consolidated FCFF(t) = **AWS FCFF(t)** (ใช้ AWS standalone path v3.1 ตามเดิม) **+ Retail FCFF(t)** (NA+Intl) **+ Ads** (ถ้าแยก — ถ้าไม่แยก รวมใน Retail) − corporate/unallocated (ถ้ามีใน 10-K)
- Retail model ใหม่ (10yr): revenue growth จาก consensus/segment trend (มี source), EBIT margin จาก NA/Intl ปัจจุบัน (6.95% / 2.93%, 10-K) → path ที่มีเหตุผล + source, capex = consolidated capex $220B − AWS capex $154.1B ใน 2026 แล้ว normalize
- **ตรวจบังคับ:** Σ segment revenue = consolidated revenue · Σ segment capex = consolidated capex ($220B ปี 2026) · consolidated margin ที่ได้ = ผลรวม ไม่ใช่ input
- แสดง implied RONIC รายปีใหม่ (บน consolidated bottom-up)
- **Emma FV:** ถ้า DCF bottom-up กับ SOTP ห่าง < 25% → ใช้ค่าเฉลี่ยได้ · ถ้า ≥ 25% → reconciliation table (สาเหตุของ gap ทีละรายการ) ก่อน แล้วเลือกตัวที่ reconcile แล้วพร้อมเหตุผล — **ห้ามเฉลี่ยก่อน reconcile**

### F2. Bear — Bear DCF บน framework bottom-up
- ใช้โครงเดียวกับ F1 แต่ assumption ของ Bear ระบุรายตัว (AWS growth / AWS margin / AWS capex normalization / retail margin) ให้ชัดว่าต่างจาก Emma ตรงไหน
- **Sanity:** ถ้า Bear FV < no-growth value (NOPAT FY2025 ÷ WACC ÷ shares ≈ $54) → ต้องอธิบายว่า assumption ไหนทำให้ capex ใหม่ได้ RONIC < WACC และสอดคล้องกับการที่ Bear จัด capex เป็น Temporary หรือไม่ — ถ้าขัดกัน แก้อย่างใดอย่างหนึ่ง

### F3. Quinn — scenario ของตัวเอง (independent)
- Bull / Base / Bear = Quinn รัน bottom-up DCF เองด้วย assumption ของ Quinn ที่ระบุชัด (เช่น Bull: AWS growth ตาม backlog conversion + margin 42%+; Bear: AWS growth ตกเร็ว + capex ไม่ลด) — **ห้ามใช้ FV สุดท้ายของ Emma หรือ Bear เป็น scenario โดยตรง** (กันนับซ้ำใน Blended)
- Bear scenario ≥ 25% · Sensitivity 5×5 WACC × AWS growth บน bottom-up framework · Reverse DCF: implied AWS growth + margin ที่ราคาปัจจุบัน · forward value path 2027/2029/2031
- ใช้ web-search ได้ ≤ 5 calls ถ้าต้องการ consensus สำหรับ scenario

### F4. Morgan — ตรวจ consistency (ใหม่)
- ✅/❌ Σ segment = consolidated (revenue, capex, EBIT) ในทุกปี forecast ของ Emma และ Bear
- ✅/❌ Consolidated EV ≥ ผลรวมที่สมเหตุสมผลของ segment (ไม่มี segment ใดได้ NOPAT ติดลบโดยไม่มีเหตุผล)
- ✅/❌ ไม่มีการเฉลี่ยวิธีที่ห่าง ≥25% โดยไม่ reconcile
- ✅/❌ Quinn scenario ไม่ใช่ FV สุดท้ายของ Emma/Bear
- บันทึก self-correction: v3.1 QA PASS ควรเป็น FAIL (`SANITY_FAIL`: consolidated < segment)

### Charlie — ตาราง v2 / v3 / v3.1 / v3.2 + attribution ของ F1–F3
และ **สรุป learning run ทั้งหมด 1 ย่อหน้า:** เครื่องมือ build-out บอกอะไรเกี่ยวกับ AMZN (capex quality vs ราคา) และอะไรที่ผิดซ้ำๆ ใน 4 รอบ

### เมื่อเสร็จ
- Leo แก้ lesson ใน learning-log.md ให้ตรงผล v3.2 (สั้น)
- Commit + push อ้าง `AMZN v3.2` · รายงานกลับ: ตาราง + attribution + Morgan verdict

*Opus — 2026-10-07 | AMZN v3.2 brief, CIO approved*
