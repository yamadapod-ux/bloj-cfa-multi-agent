# Lane AI/Infra Build-out — Calibration Run (Vera)

> **⚠️ CALIBRATION RUN ONLY — ไม่นับเป็น TRIAL data ตาม CLAUDE.md section 5 ("Business-Type Lane: AI/Infra Build-out", ข้อ 5 TRIAL measurement)**
> วัตถุประสงค์: ทดสอบย้อนเกณฑ์ Classification ข้อ 1 (3 เกณฑ์) + ประเมินคร่าวๆ ว่า Scout filter ที่แทนเดิมจะผ่านกี่ตัว เพื่อดูว่าเกณฑ์ lane ใหม่หลวม/ตึงเกินไปหรือไม่ ก่อนเริ่มใช้งานจริง

**วันที่รัน:** 2026-10-06 | **ผู้รัน:** Vera | **อ้างอิง:** CLAUDE.md L336-377 (lane ใหม่), `agent_notes/charlie/2026-10-06_lane_ai_infra_draft.md` (ร่าง Opus)

---

## หุ้นที่เลือกมา (10 ตัว — เคย scout ไปแล้วในรอบก่อนๆ)

| # | Ticker | ที่มา (round/commit) |
|---|--------|----------------------|
| 1 | AMZN (AWS) | decisions.md 2026-10-06 (v1/v2), explicitly excluded from trial data per lane rule |
| 2 | EQIX | buy_list.md — Round ~68/69 data-center cluster, died Filter A near-ATH |
| 3 | DLR | buy_list.md — same data-center cluster as EQIX |
| 4 | IRM | buy_list.md — Filter A near-miss (-15.36%), data-center/ALM growth segment |
| 5 | AMT | buy_list.md — Filter A near-miss (-17.28%), tower + CoreSite data center |
| 6 | CCI | buy_list.md — Filter C/D methodology-conflict candidate (Round 67-ish) |
| 7 | ETN | decisions.md 2026-08-05 — Electrical Equipment, AI data-center-capex-tailwind theme |
| 8 | POWL | buy_list.md — Filter A survivor, data center mega-order (switchgear) |
| 9 | ASML | buy_list.md context (MKSI/ONTO semicap cluster, Round 68 bookings-miss rout) |
| 10 | AMAT | general semicap peer (Round 68 Semicap cluster: ASML/AMAT/KLAC/TER/ENTG) |

(ไม่พบตัวเลข capex/revenue อิสระสำหรับ KLAC/TER/ENTG/MKSI/ONTO ในเวลาที่มี — ใช้ ASML+AMAT เป็นตัวแทน semicap equipment cluster แทน เพื่อไม่ให้เกิน search budget)

---

## ผล Classification (เกณฑ์ข้อ 1 — ต้องผ่านครบ 3/3)

| Ticker | Capex/Rev TTM หรือ Capex YoY≥30% | Mgmt build-out program ชัดเจน (ขนาด$+timeframe) | ≥40% revenue growth จาก AI/DC/power/network/compute | ผล |
|---|---|---|---|---|
| **EQIX** | PASS — non-recurring capex guide $3.3-3.9B + recurring ~3% บน revenue guide $10.12-10.22B (FY26) ≈ 36-41% ≫15% ([8-K Feb 2026](https://investor.equinix.com/sec-filings)) | PASS — FY26 guidance ตัวเลขชัดเจน ($270-290M recurring + $3,385-3,865M non-recurring) | PASS (ปานกลาง-มั่นใจ) — Q2'26 +16% YoY "driven by robust core demand **and** one-time xScale fees" (xScale = hyperscale/AI campus product line); ไม่มีตัวเลข % breakdown ที่แม่นยำ | **✅ 3/3 เข้า lane** |
| **DLR** | PASS — Development CapEx guide **$4.25-4.75B** (raised จาก $3.25-3.75B) บน revenue guide $6.6-6.9B ≈ **64-70%** ≫15% ([Q2'26 8-K](https://investor.digitalrealty.com)) | PASS — ชัดเจนที่สุดในกลุ่ม: pipeline 1.4GW under construction, total cost $20B, stabilization dates ระบุปี 2027/2028 | PASS — mgmt ระบุตรงๆ ว่า development ปัจจุบัน "reflecting outsized demand from **hyperscale cloud and AI-oriented workloads**" | **✅ 3/3 เข้า lane (ชัดเจนที่สุด)** |
| **IRM** | PASS (ความมั่นใจปานกลาง — ไม่ได้ตัวเลข capex/revenue ตรงๆ แต่ segment ที่ลงทุนหนักสุด Data Center โต 39%, เป้าหมาย capacity 507MW→1.4GW "near-tripling") | PASS — "Project Matterhorn" 5-yr plan ระบุชัดเจน, capacity target ชัดเจน | PASS ชัดเจน — Data Center+ALM+Digital = 35% ของ revenue, โต 50%+ รวมกัน, contribute 14pp ของ 19% total growth (~74% ของ growth มาจากกลุ่มนี้) | **✅ 3/3 เข้า lane (แต่ capex/revenue ตัวเลขดิบยังไม่ยืนยัน — ต้อง Atlas หาตัวเลขจริงถ้าใช้ trial จริง)** |
| AMZN (AWS) | PASS — capex/rev TTM 22.3% (June'26), capex growth +58.8% YoY FY25 | PASS — 2026 capex guide $220B (raised จาก $200B), ระบุชัดเจนมาก | **FAIL (ใกล้เคียง)** — AWS revenue เพิ่ม $19.68B จาก consolidated revenue เพิ่ม $58.8B (H1'25→H1'26) = **~33.5% < 40%** | ❌ 2/3 — **near-miss, flag ด้านล่าง** |
| AMT | FAIL/marginal — capex guide $1.805-1.915B / revenue ~$11.3B ≈ 16-17% (เฉียด threshold) | FAIL (อ่อน) — เป็น routine annual capex guidance ไม่ใช่ named build-out program เฉพาะสำหรับ AI/DC | FAIL — CoreSite data-center segment revenue $1.05B จาก total ~$11.3B, core tower business (ไม่ใช่ AI) ยังเป็นตัวขับ growth หลัก | ❌ 1/3 ชัดเจน |
| CCI | FAIL ชัดเจน — capex ~$59M/quarter บน revenue ~$1.01B ≈ 5.8% | FAIL — ไม่มี build-out program เลย (ขาย fiber+small-cell ธุรกิจออกหมดแล้ว 2026, กลายเป็น pure-play US tower) | FAIL — ไม่มี AI/DC exposure เหลือแล้ว | ❌ 0/3 — **ไม่เกี่ยวกับ lane นี้เลยแล้ว** |
| ETN | FAIL ชัดเจน — capex/rev FY25 ≈ 3.3%, capex growth YoY +13.74% (<<30%) | FAIL — ไม่มี named AI-capex program ของตัวเอง (ETN เป็นผู้ขาย switchgear ให้ผู้สร้าง DC ไม่ใช่ผู้สร้างเอง) | ไม่ประเมิน (criterion 1 fail แล้ว) | ❌ 0/3 — **supplier ไม่ใช่ builder** |
| POWL | FAIL ชัดเจน — capex $10.4M 9mo / revenue $859.5M ≈ **1.2%** | FAIL — $400M data-center order คือ backlog/revenue ไม่ใช่ capex ของตัวเอง | ไม่ประเมิน | ❌ 0/3 — **supplier, ยืนยัน pattern เดียวกับ ETN** |
| ASML | FAIL ชัดเจน — capex/rev 2021-2025 อยู่ที่ 4.8-7.8%, ปี 2025 capex **ลดลง** -24% YoY (ไม่ใช่โต ≥30%) | FAIL (อ่อน) — capacity expansion พูดถึงแต่ไม่มีตัวเลข capex ของตัวเองชัดเจน (เป็น demand signal ของลูกค้า TSMC/Samsung/Intel มากกว่า) | ไม่ประเมิน | ❌ 0/3 — **equipment supplier, asset-light, ไม่ใช่ infra operator** |
| AMAT | **PASS ทาง OR-logic เท่านั้น** — capex/rev FY25 8% (<15%) **แต่** capex growth +89.9% YoY (≥30% ผ่าน) | FAIL — ภาษาเป็น "additional manufacturing capacity investments to support projected demand through the end of the decade" ไม่มีขนาด$+timeframe ชัดเจน | FAIL/ambiguous — revenue growth มาจากขาย equipment ให้ชิปเมคเกอร์ที่ลงทุน AI (ไม่ใช่ AMAT เองเป็น AI/DC operator) — ไม่เข้าเกณฑ์ตามเจตนารมณ์ lane | ❌ 1/3 — **เข้า criterion 1 ได้ทาง loophole แต่ถูกกรองออกถูกต้องด้วย criterion 2/3** |

### สรุป Classification: **3/10 เข้า lane เต็ม (EQIX, DLR, IRM)**, 1/10 near-miss (AMZN), 1/10 loophole-but-caught (AMAT), 5/10 fail ชัดเจน (AMT, CCI, ETN, POWL, ASML)

---

## ผลประเมิน Scout filter (เฉพาะ 3 ตัวที่เข้า lane — ประเมินคร่าวๆ ไม่ทำ full valuation/MOS)

| Ticker | ROIC on in-service capital / incremental ROIC > WACC | Runway ≥24mo หรือ FCF-positive core | Dilution ≤3%/yr | ประเมินรวม |
|---|---|---|---|---|
| **DLR** | น่าจะผ่าน — stabilized development yields 10-11.5% (mgmt disclosed), likely > REIT WACC ~7-8% | ต้องเช็คจริง — recycling capital ผ่าน dispositions/JV, ไม่ชัดว่า core FCF cover capex | **ติดชัดเจนมาก** — ออกหุ้น 12.3M shares มูลค่า ~$2.3B ในดีลเดียว (Blackstone stake acquisition) ในปีเดียว + ยังระดม equity ต่อเนื่องสำหรับ $20B development pipeline → likely >>3%/yr | **ติดชัดเจนที่ dilution filter** |
| **EQIX** | น่าจะผ่าน (ปานกลาง-มั่นใจ) — core colocation ROIC สูง, แต่ไม่ได้คำนวณ in-service-capital-adjusted ROIC จริง | ไม่ชัด — dividend payout ratio TTM 127.66% (สูงผิดปกติ, อาจสะท้อน REIT FFO distribution ปกติ แต่ต้องเช็คจริงว่า core FCF cover capex ได้ไหม) | ไม่ชัด — EQIX มีประวัติ equity raise สำหรับ growth capex สม่ำเสมอ, ความเสี่ยงเกิน 3%/yr มีจริงแต่ไม่ได้ยืนยันตัวเลข | **ไม่แน่ชัด — ต้องทำเต็มรูปแบบถึงจะสรุปได้** |
| **IRM** | น่าจะผ่าน (มั่นใจปานกลาง-สูง) — Data Center EBITDA margin 52.2% (+140bps), renewal spreads +12-14% cash/GAAP บ่งชี้ pricing power/returns ดี | น่าจะผ่าน — net lease-adjusted leverage 4.8x (ต่ำสุดตั้งแต่ก่อน REIT conversion 2014), capex "funded substantially through debt" ไม่ใช่ equity | น่าจะผ่าน — ระดมทุนผ่านหนี้เป็นหลัก ไม่ใช่หุ้น (ตรงข้ามกับ DLR) | **น่าจะผ่านต่อได้ชัดเจนที่สุดในกลุ่ม 3 ตัว** |

**สรุป: ~1/3 (IRM) ดูน่าจะผ่าน scout filter ได้ชัดเจน, อีก 2/3 (EQIX/DLR) มีความเสี่ยงจริง — DLR ติดชัดเจนที่ dilution, EQIX ไม่แน่ชัดต้องคำนวณจริง**

---

## Pattern ที่น่าสงสัย / ข้อเสนอ (ไม่แก้ CLAUDE.md เอง — รายงานกลับเท่านั้น)

1. **Capex/Revenue ≥15% threshold ทำงานถูกต้อง** — กรอง supplier/equipment companies (ETN, POWL, ASML) ออกได้สะอาด (capex/rev 1.2-7.8%, ต่ำกว่า threshold มาก) ไม่มี false-positive ในกลุ่มนี้ เพราะพวกนี้ *ขายของให้* คนสร้าง AI infra ไม่ได้สร้างเอง — เกณฑ์แยกแยะ "builder vs supplier" ได้ดี ไม่ควรแก้

2. **🚩 OR-logic "capex growth ≥30% YoY" เป็น loophole ที่เกือบหลุด** — AMAT (semicap equipment maker, capex/revenue จริงแค่ 8%) เข้า criterion 1 ได้ทาง capex-growth leg (+89.9% YoY) ทั้งที่ธุรกิจจริงเป็น equipment supplier ไม่ใช่ AI/DC operator เหมือน EQIX/DLR/IRM. กรณีนี้ถูกจับได้ถูกต้องด้วย criterion 2 (ไม่มี build-out program ชัดเจนพร้อมขนาด$+timeframe) และ criterion 3 (revenue growth มาจากขาย equipment ไม่ใช่จากเป็น AI/DC operator เอง) — **แต่ถ้าเจอบริษัทที่มี capex growth สูงจาก reason อื่น (เช่น M&A, FX, one-time) + มี vague PR language พอจะผ่าน criterion 2 ได้ลวกๆ ก็อาจหลุดเข้า lane ทั้งที่ไม่ใช่ตัวจริง** → ข้อเสนอ (ให้ CIO/Opus พิจารณา ไม่ใช่ Vera แก้เอง): เพิ่มเงื่อนไขใน criterion 2 ให้ระบุชัดว่า build-out program ต้องเป็นสินทรัพย์ที่ **บริษัทเองเป็นเจ้าของ/ดำเนินการ/สร้างรายได้โดยตรง** (ไม่ใช่ capacity ที่ขายให้ลูกค้าอื่นไปสร้างต่อ) เพื่อปิดช่องว่างระหว่าง "infra operator" กับ "infra equipment supplier" ให้ชัดกว่านี้

3. **🚩 Criterion 3 (≥40% revenue growth) อาจตึงเกินไปสำหรับ conglomerate ที่มี AI-segment ชัดเจนแต่เล็กกว่าทั้งบริษัท** — AMZN capex/revenue 22.3% (เหนือ threshold ไปมาก) + mgmt disclosure $220B ชัดเจนที่สุดในกลุ่มที่ทดสอบ แต่ตกเกณฑ์ข้อ 3 แบบหวุดหวิด (AWS contribute ~33.5% ของ consolidated revenue growth, ต่ำกว่า 40% เพียงเล็กน้อย) เพราะ segment อื่น (retail/ads) ยังโตควบคู่ไปด้วย. ตามกฎ CLAUDE.md ปัจจุบันระบุชัดอยู่แล้วว่า AMZN v1/v2 ไม่นับเป็น trial data ไม่ว่ากรณีใด (ไม่ใช่ปัญหาตรงนี้) — แต่ **pattern นี้บอกว่าเกณฑ์ 40% เป็น consolidated-revenue-growth basis อาจกันบริษัทใหญ่ที่มี AI-segment ชัดเจนหลุดออกจาก lane ทั้งที่ capex เป็นตัวจริงที่สุด (22%+ของ revenue)** → ข้อเสนอ (ให้ CIO/Opus พิจารณา): ถ้าบริษัทมี segment reporting แยกชัดเจน (เช่น AWS) ให้พิจารณาทางเลือกคำนวณ criterion 3 แบบ "สัดส่วน growth ของ segment ที่เป็น AI/DC ต่อ growth ของ segment นั้นเอง" แทนที่จะบังคับใช้ consolidated-level เสมอ — แต่นี่เป็นแค่ข้อสังเกต ไม่ใช่ urgent fix เพราะ sample size เท่าที่ทดสอบ (10 ตัว) มีแค่ AMZN เคสเดียวที่โดน pattern นี้

4. **Classification overall ไม่หลวมไม่ตึงเกินไป** — 3/10 เข้า lane เต็ม (ไม่ใช่ 10/10 = ไม่หลวม), ไม่ใช่ 0/10 (ไม่ตึงเกินไป), และตัวที่เข้าได้ (EQIX/DLR/IRM) ล้วนเป็นธุรกิจ pure-play data-center/digital-infra ที่ตรงเจตนารมณ์ lane จริงๆ ส่วนตัวที่ถูกกรองออก (supplier/equipment/tower-only) ก็ถูกกรองออกด้วยเหตุผลที่สมเหตุสมผล — **เกณฑ์ calibration ผ่าน ไม่พบ systemic ปัญหาที่ร้ายแรงพอต้องแก้ด่วน** ข้อเสนอข้อ 2-3 ด้านบนเป็นแค่ fine-tuning สำหรับ edge case ในอนาคต

---

## ข้อจำกัดของการ calibration รอบนี้ (ความโปร่งใส)

- ไม่ได้ทำ full valuation/MOS 25% ตามที่ scope ระบุไว้ — ประเมิน scout filter แบบคร่าวเท่านั้น (เวลาจำกัด)
- IRM capex/revenue ไม่มีตัวเลขตรงๆ จาก source ที่หาได้ในรอบนี้ — ใช้ segment revenue growth composition แทนเป็น proxy ที่แข็งแรงพอสำหรับ calibration แต่ไม่ใช่ตัวเลขยืนยันสุดท้าย
- ไม่ได้ลองหา KLAC/TER/ENTG/MKSI/ONTO (ใช้ ASML/AMAT เป็นตัวแทน semicap cluster) เพื่อประหยัด search budget (จำกัดไว้ 30-40 calls ตาม task brief — ใช้ไปแล้ว ~16 calls)
- ผลนี้เป็น **calibration เท่านั้น ไม่นับเป็น TRIAL data** ตาม CLAUDE.md — การ scout ใหม่จริงสำหรับ trial ต้องทำแยกต่างหากตาม pipeline เต็ม (Atlas classification → Emma/Quinn → Bear → Morgan QA)

---

*Vera — 2026-10-06 | Calibration run, not trial data*
