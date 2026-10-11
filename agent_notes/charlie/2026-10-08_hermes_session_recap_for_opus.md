# Recap สำหรับ Opus — เส้นทางก่อน VS2 + ผล AMZN v3.4 (เขียนโดย Hermes/Bubu)

*บันทึกนี้เขียนเพราะ chat ของ CIO กับ Opus หลุด/หมด token บ่อย — ให้ Opus อ่านไฟล์นี้แทนการเล่าปากเปล่าซ้ำ*

## บริบท: ทำไมเรื่องนี้เริ่มต้น

AMZN ถูกวิเคราะห์มา 5 รอบ (v1 → v2 → v3 → v3.1 → v3.2) ด้วย pure FCFF-DCF bottom-up
ผล Blended FV วนอยู่ใน **$100-230** ทุกรอบ ขณะที่:
- Sell-side consensus (58-60 นักวิเคราะห์): เฉลี่ย **$328**, ต่ำสุด **$230**, สูงสุด **$405**
- ไม่มี sell-side รายใดต่ำกว่า $230
- v3.2 (ก่อน VS2) ได้ **$125.66** — ต่ำกว่า Street floor ~45%

CIO ถามตรงว่า "ทำไมไม่มีที่ไหนให้ต่ำกว่า $200 เลยสักที่" → นำไปสู่การขุดหา root cause จริง

## สิ่งที่ Hermes (ผม) ลองทำ — และพลาดตรงไหน (สำคัญ ให้ Opus รู้ไว้เตือน pattern นี้)

1. **รอบแรก: หาแหล่งเทียบ** — เจอ wallstsmart/vcpscanner ที่ FV ใกล้เคียงทีม ($97-174) → CIO จับได้ว่าเป็น **confirmation bias** (เลือก query ที่เข้าทาง, แหล่งไม่น่าเชื่อถือ) ยอมรับผิดแล้ว
2. **รอบสอง: เดา AWS taper rate** — สมมติว่าปัญหาคือ AWS growth taper เร็วเกินไป (33%→8% ใน 10 ปี) เทียบ backlog $496B จริง แล้ว**เดา FV เองว่าควรได้ $145-160** โดยไม่รันโมเดลจริง — CIO ชี้ว่าตัวเลขนี้ยัง conservative เกินไปและเป็นการเดาในมืด ไม่น่าเชื่อถือ
3. **จุดบอดที่ใหญ่ที่สุด:** ไม่เคยนับ **non-operating assets** (Anthropic stake ~$190B) เข้า equity bridge เลยตลอด 2 รอบที่เสนอ — นี่คือ ~$17.56/หุ้น หลังภาษีที่หายไปจากทุกเวอร์ชันก่อน VS2
4. **ไม่ได้คำนวณ FV ปีที่ 5** แม้ CIO เตือนเรื่อง horizon 5+ ปีไปแล้วรอบหนึ่ง — ยังคงปรับแค่ FV วันนี้
5. **ไม่เคย verify WACC กับภายนอก** — raw beta 1.45 ไม่ปรับ Blume ไม่เทียบ 3 แหล่ง

**สรุป pattern ที่ Opus ควรระแวงจาก Hermes:** มีแนวโน้มแก้ปัญหาด้วยการ "จูนตัวแปรเดียวที่เห็นชัดสุด" (taper, weight) แล้วเดาตัวเลขผลลัพธ์ก่อนรันจริง แทนที่จะหา structural bug ที่กระทบทุกหุ้น — Opus's VS2 approach (fix methodology ทั้งระบบ, ไม่ตั้งเป้า FV, บังคับแก้ทั้งสองทิศ) ถูกต้องกว่ามาก

## VS2 Brief (Opus, 2026-10-08) — ทำไมดีกว่า

ไฟล์: `agent_notes/charlie/2026-10-08_vs2_amzn_v3.4_brief.md`

**Root causes ที่ Opus เจอ (กระทบทุกหุ้น ไม่ใช่แค่ AMZN):**
- WACC ไม่เคยเทียบภายนอก (raw beta ไม่ปรับ)
- ไม่นับ non-operating assets (Anthropic ~$190B)
- DCF ปีสุดท้ายกระโดด 8%→3% ไม่มี fade
- net debt ไม่ตรงกันข้ามรอบ ($50.7B vs $9.24B), share count ไม่ตรง (10.79 vs 10.90)
- Ads revenue เป็น ESTIMATE ไม่มี source
- ไม่มีวิธีรับมือ DCF เปราะเมื่อ FCF ช่วงแรกติดลบ (capex supercycle)

**กลไกป้องกัน bias ที่ Opus ใส่ไว้:**
- Anti-anchoring: "ตั้งใจไม่ใส่ตัวเลขประมาณใน brief ห้ามตั้งเป้า FV"
- ทุกการแก้ต้องทำทั้งสองทิศ (ห้ามเลือกแก้แต่จุดที่ดัน FV ขึ้น)
- Atlas จัดประเภทหุ้นก่อน Emma เห็นข้อมูล (กัน cherry-pick วิธี)
- Peer selection ต้องเลือกก่อนเห็นผลลัพธ์

**3 ชั้นกฎ VS2:**
- ชั้น 1 (ทุกหุ้น): WACC ร่วม + non-op bridge + DCF standard (fade, terminal RONIC, lease, net debt/shares ชุดเดียว) + FV ปีที่ 5 คู่กับ FV วันนี้
- ชั้น 2 (TRIAL, หุ้นที่ PV(TV)/EV > 70%): ผสม DCF กับ forward EV/EBIT + core P/E ถ่วงน้ำหนักตาม TV%
- ชั้น 3: กฎ lane เดิม (AI/Infra) ไม่เปลี่ยน

**Business-type valuation map (addendum):** จัดประเภทหุ้น 10 แบบ → วิธีหลักต่างกัน (DCF ล้วน / DCF+multiples / P/B+DDM /SOTP ฯลฯ) Atlas เลือกก่อนเห็นข้อมูล

## ผลรัน AMZN v3.4 (VS2) — จริง ไม่ใช่เดา

รันผ่าน Claude Code CLI (`claude -p --dangerously-skip-permissions`), เสร็จ 3 Phase, commits:
- Phase 1 (กฎ VS2 ลง CLAUDE.md/qa.md/agent files): `be1c4ac`
- Phase 1E (dashboard How We Work): `9d544f8`
- Phase 2+3 (AMZN v3.4 + max.md): `0db36b3`

**ตัวเลข:**
| | v3.2 (เดิม) | v3.4 (VS2) |
|---|---|---|
| Blended FV วันนี้ | $125.66 | **$201.47** |
| MOS (ราคา $259.92) | -51.6% | **-22.5%** |
| Verdict | NO BUY | **NO BUY** (ยืนยัน แต่ gap แคบลงมาก) |
| FV ปีที่ 5 | ไม่มี | **$292.84** |
| ผลตอบแทนคาด/ปี (5Y) | ไม่มี | **+2.4%/ปี** (แพ้ S&P คาด 9.5%/ปี ชัดเจน) |

- Locked WACC = 9.72% (Blume 10.46% / bottom-up 8.98%, ห่าง 148bps ผ่านเกณฑ์ 150bps)
- Non-op bridge = $17.56/หุ้น หลังภาษี (Anthropic $190.4B + OpenAI $28.7B + อื่นๆ)
- Net debt $31.04B, diluted shares 10.903B
- Morgan verdict: CONDITIONAL PASS (1 SOURCE_MISSING)
- buy_list entry zone $161-171 (mid $166) — ยังไม่ผ่าน conviction gate, ไม่มี trade

**Open items ที่ subagent flag ไว้ ยังไม่ตัดสิน (รอ Opus/CIO):**
1. ชั้น 2 (multiples) ไม่ trigger เพราะ PV(TV)/EV = 61.1% (เกณฑ์ >70%) — แต่ถ้านับรวมช่วง fade อาจ trigger ได้ ต้องตัดสินว่าจะนับ fade period รวมด้วยไหม
2. capex FY2027 ใช้ consensus (ไม่มี guidance ตรง) — สมมติฐานที่ subagent เลือกเอง
3. cost of debt ปรับเอง — ไม่มี source ตรงจาก filing
4. ไม่มีไฟล์เก็บ FCF รายปีของ v3.2 เดิม ต้องสร้างโมเดลใหม่จากศูนย์แทนการ diff กับของเดิม

## สรุปสำหรับ Opus

ตัวเลขที่ CIO ควรเชื่อถือได้ตอนนี้คือ **$201.47 (วันนี้) / $292.84 (ปีที่ 5)** จาก VS2 ไม่ใช่ $125.66 เดิม — แต่ verdict ยังเป็น **NO BUY** ทั้งสองกรอบเวลา เพราะ MOS ยังติดลบและ expected return ปีที่ 5 แพ้ S&P ชัดเจน ประเด็นที่เหลือคือ open items ข้างบน (ชั้น 2 trigger หรือไม่, capex/cost-of-debt assumption) ที่ Opus ควรรีวิวต่อ ไม่ใช่การกลับไปเดา taper/weight แบบที่ Hermes เคยเสนอผิดมา

---

## Addendum 2 (เขียนทับเพิ่มหลัง v3.4 เสร็จ) — CIO ตั้งคำถามเรื่อง motivated reasoning + ข้อเสนอ validation framework ใหม่

### สิ่งที่เกิดต่อจากนี้ (หลังรายงานผล v3.4 ให้ CIO)

1. **CIO ถามตรง:** "แปลกไหมที่พยายามทำให้ออกมาแถวๆ 200 ทั้งที่ส่วนตัวอยากได้ราคานั้นโดยหาเหตุผลรองรับ" → เป็นคำถามเรื่อง motivated reasoning / reverse-engineering the valuation ที่ตรงประเด็นมาก

2. **Hermes ไปขุด attribution table 7 ขั้น จากไฟล์จริง** (`reports/AMZN_2026-10-07_v3.md` § Attribution 7 ขั้น) พบว่า:
   - ขั้น 1 WACC (+$40.57), ขั้น 2 Non-op bridge (+$17.57), ขั้น 5 แยก Ads (+$36.03) → **ดันขึ้น**
   - ขั้น 3 Net debt/lease (-$2.05), ขั้น 4 Fade+terminal+capex (-$17.77, Bear โดนหนักสุด -$37) → **ดันลงจริง**
   - สรุป: **ไม่ใช่การเลือกแก้แต่ทิศทางเดียว** มีทั้งขึ้นและลงจริงตามที่ VS2 บังคับไว้
   - **แต่** ตัวผลักขึ้นใหญ่สุด 2 ตัว (WACC +$40.57, Ads split +$36.03 = รวม $76.6) **มากกว่าผลสุทธิทั้งหมด** (+$74.91 จาก 126.56→201.47) — แปลว่าผลลัพธ์พึ่งพา 2 judgment call นี้มาก และทั้งคู่มีจุดที่ "เลือกเอง" อยู่:
     - WACC: external median ไม่ stale มาจาก **n=2 เท่านั้น** (ทิ้ง 4/6 แหล่งเป็น "stale") และ median ภายนอกจริงๆ คือ 13.2% ห่างจาก base 9.72% ถึง ~350bps
     - Ads: เลือก peer META/GOOGL (premium multiple) สำหรับ segment ที่ไม่ได้ยืนธุรกิจอิสระจริง

3. **CIO ยืนยันเจตนาที่ถูกต้อง:** ที่อยากแก้ไม่ใช่เพราะ "อยากได้ $200" แต่เพราะ "$125.66 ต่ำกว่าทุกแหล่งภายนอกจนแทบเป็นไปไม่ได้จริง" — Hermes ยืนยันว่านี่คือ sanity-check ที่ถูกทิศทาง (หาบั๊ก) ไม่ใช่ตั้งเป้าผลลัพธ์ (หาเหตุผลรองรับเลขที่อยากได้) ต่างจาก motivated reasoning ตรงที่ไม่ได้บอกทีมว่า "ทำให้ได้ $200" แต่บอกว่า "ไปหาว่าทำไมมันผิด"

4. **CIO สรุปว่าโมเดลเดิม "ทั้งผิดและใช้ไม่ได้กับปัจจุบัน"** — Hermes เห็นด้วย แยก 2 เรื่อง:
   - **ผิด (error เชิงข้อเท็จจริง ไม่เกี่ยวยุคสมัย):** ไม่นับ Anthropic stake, net debt ไม่ตรงกันข้ามรอบ, WACC ไม่เคย cross-check
   - **ใช้ไม่ได้กับปัจจุบัน (สมมติฐานเหมาะกับธุรกิจ FCF นิ่ง ไม่เหมาะ AMZN ช่วง capex supercycle):** pure DCF ไม่มี cross-check, ไม่มี fade ก่อน terminal

5. **CIO ถามว่า VS2 ใช้แค่ AMZN หรือหุ้นอื่นด้วย** → ยืนยันว่า VS2 เป็นกฎกลางเข้า CLAUDE.md แล้ว ใช้กับทุกหุ้น แต่**หุ้นที่ถืออยู่แล้วในพอร์ตยังไม่ถูกรันซ้ำ** — รอรอบ re-verify ตามปกติ (ยังไม่ force รันทั้งพอร์ตตอนนี้ เว้นแต่ CIO จะสั่ง override)

6. **CIO ถามว่าจะรู้ได้ยังไงว่า business-type map (10 ประเภท) คำนวณถูกจริง ไม่ใช่แค่ลองแล้วดูผล** → Hermes เขียนเอกสารข้อเสนอใหม่

### เอกสารใหม่ที่ Opus ต้องรีวิว: Validation Framework Proposal

ไฟล์: `agent_notes/charlie/2026-10-08_valuation_validation_framework_proposal.md` (commit `08e2a46`, push แล้ว)

เสนอ 4 ชั้นตรวจสอบ (A ก่อนคำนวณ / B ระหว่างคำนวณ / C internal consistency / D backtest ระยะยาว) — **ส่วนที่ใหม่และยังไม่มีในระบบ:**
- **B1 Anchor-Proximity Flag:** ถ้าผลลัพธ์ท้ายสุดอยู่ใกล้ (±5%) ตัวเลขที่เคยมีคนพูดไว้ก่อนเริ่มคำนวณ → auto-flag ให้ Morgan ตรวจ judgment call ทุกจุดเพิ่มเติม (**เคส AMZN v3.4 เข้าเกณฑ์นี้พอดี** — $201.47 ใกล้ตัวเลข "$200" ที่ CIO เคยพูดไว้ก่อน)
- **B2 Degrees-of-Freedom Audit:** ให้ Morgan นับทุก judgment call (ไม่ใช่แค่ error) + sensitivity table ว่าแต่ละจุดกระทบ FV เท่าไหร่ถ้าเลือกทางตรงข้าม
- **B3 Blind Re-derivation Test:** เมื่อ B1 trigger ให้ subagent คนที่สองที่ไม่รู้ตัวเลขเป้าหมายคำนวณใหม่จาก data package เดียวกัน มาเทียบ
- **D2 Method-Level Calibration Table:** แยก scorecard ตาม business-type ไม่รวมเป็นก้อนเดียว เพื่อรู้ว่าวิธีไหนแม่นกว่าจริงเมื่อเทียบราคาจริง

**4 Open Items ที่ Hermes ตอบเองไม่ได้ ต้องให้ Opus ตัดสิน:**
1. ประเภทหุ้นอื่น (SaaS, Cyclical, Biotech ฯลฯ) ยังไม่มีเกณฑ์ตัวเลขจัดประเภทแบบ "ลงทุนหนัก" (PV(TV)/EV>70%) — ควรมีไหม ควรเป็นเกณฑ์อะไร
2. Anchor-proximity threshold ±5% เหมาะสมไหม
3. Blind re-derivation (B3) ควรทำทุกเคสที่ trigger หรือจำกัดแค่หุ้นที่จะ deploy จริง (เพราะ cost/เวลาสูง)
4. Method-level calibration (D2) ต้องรอข้อมูลสะสมนานแค่ไหนถึงมีความหมายทางสถิติ (sample size ต่อ business-type ตอนนี้ยังน้อย)

## งานที่ยังค้างอยู่ตอนนี้ (ยังไม่เสร็จ — สรุปรวมทั้งหมด)

- [ ] **Validation Framework Proposal ยังไม่ผ่าน CIO/Opus approve** — เขียนไว้เป็น draft เท่านั้น ยังไม่ commit เข้า CLAUDE.md
- [ ] **Open Items 4 ข้อข้างบน** ยังไม่มีคำตอบ
- [ ] **AMZN v3.4 open items เดิม 4 ข้อ** (ชั้น 2 trigger หรือไม่ถ้านับ fade รวม, capex FY2027 consensus, cost of debt ไม่มี source ตรง, ไม่มีไฟล์ FCF รายปีของ v3.2 เดิมให้ diff) — ยังไม่ตัดสิน
- [ ] **WACC external median n=2** — ควรหาแหล่งเพิ่มให้ sample แน่นกว่านี้ก่อนเชื่อ 9.72% เต็มที่ไหม
- [ ] **Ads peer selection (META/GOOGL)** — ยังไม่มีใครตรวจสอบอย่างเป็นอิสระว่าเหมาะสมหรือเลือกเพราะดันผลลัพธ์ขึ้น
- [ ] **หุ้นอื่นในพอร์ตที่ถืออยู่ ยังไม่ผ่าน VS2** — รอรอบ re-verify ปกติ (CIO ยังไม่สั่ง override ให้เร่งทำทั้งพอร์ตตอนนี้)
- [ ] **business-type map ประเภทอื่น (นอกจาก "ลงทุนหนัก")** ยังไม่มีเกณฑ์ตัวเลขชัดเจนสำหรับ auto-classify

*Hermes (Bubu) — 2026-10-08, เขียนต่อจาก Addendum 1 เดิม*
