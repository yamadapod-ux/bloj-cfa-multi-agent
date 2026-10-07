# AMZN Valuation Methodology — สำหรับให้ผู้เชี่ยวชาญ/มืออาชีพตรวจสอบ

*สรุปโดย Charlie (orchestrator), 2026-10-08 — รวบรวมจาก agent_notes/emma, agent_notes/quinn, agent_notes/bear, reports/AMZN_2026-10-07_v3.md (commits ccf547e → eb115ac → 20c3a3f → e03073b)*

**ผลสุดท้าย: Blended Fair Value = $125.66/share | ราคาตลาด (2026-10-07) = $259.92 | MOS = −51.65% | Verdict = NO BUY**

---

## 1. โครงสร้างโดยรวม — Blended FV = 40% Emma + 30% Quinn + 30% Bear

นี่คือ fixed weighting rule ของกองทุน (ไม่เปลี่ยนตามเคส — "Return-side locked rule"):

```
Blended FV = 0.40 × Emma_FV + 0.30 × Quinn_PW-EV + 0.30 × Bear_FV
           = 0.40 × $148.53 + 0.30 × $131.69 + 0.30 × $89.13
           = $59.41 + $39.51 + $26.74
           = $125.66
```

สามมุมมองมาจาก **3 คนละโมเดล อิสระจากกัน** (ไม่ใช่คนเดียวคำนวณ 3 ครั้ง):
- **Emma** = equity analyst, central/base-case assumptions
- **Quinn** = quantitative, probability-weighted scenario (ไม่ยืมตัวเลขของ Emma/Bear)
- **Bear** = devil's advocate, harsher assumptions ของตัวเอง, ต้องหา reason ที่ล้มทุก thesis

---

## 2. Emma FV = $148.53 — Sum-of-the-Parts bottom-up DCF (segment-level)

### 2.1 โครงสร้าง: แยก AWS กับ Retail (NA+Intl) ก่อน แล้วรวมเป็น consolidated

**หลักการบังคับ (Multi-Segment Consistency Rule):** consolidated DCF **ต้องเป็นผลรวมของ segment จริง** (revenue, capex, EBIT ทุกปีรวมกันได้พอดีกับทั้งบริษัท) ห้ามตั้ง consolidated margin เป็น input แยกต่างหาก — นี่คือจุดที่ v3.1 (รอบก่อน) ทำผิดและถูกจับได้ (ดู §5)

### 2.2 AWS segment — standalone DCF
| Input | ค่า | ที่มา |
|---|---|---|
| Revenue growth | 33% (Yr1) → 8% (Yr10, terminal) | 10-K segment data + AWS backlog disclosure |
| Terminal EBIT margin | 42% | derived จาก AWS margin trend, cross-check กับ Azure/GCP margin |
| Capex/Revenue path | 90% → 15% (2035, normalize ตาม build-out cycle) | 10-K capex guidance $220B FY2026 |
| WACC | 10.95% | beta 1.45 (3 sources ตรงกัน) × ERP 4.14% (Damodaran Sep 2026) + RF 5.29% (3 sources) |
| TGR | 3.0% | standard terminal growth (nominal GDP-adjacent) |
| **AWS DCF EV** | **$1,248.0B** | — |

### 2.3 Retail (NA+Intl) segment — bottom-up DCF (ไม่ใช่ peer-multiple)
| Input | ค่า | ที่มา |
|---|---|---|
| Revenue growth | 11% (Yr1) → 4% (terminal) | NA 16% YoY / Intl 15% YoY ล่าสุด (Q2'26), taper ตามมาตรฐาน mega-cap decelerating growth |
| EBIT margin | 6.2% (Q2'26 actual blended) → 8.0% (terminal) | sourced จาก Q2'26 earnings + analyst consensus margin-expansion trend (fulfillment automation) |
| Capex Yr1 | $65.9B (= consolidated $220B − AWS $154.1B) | residual จาก consolidated guidance |
| D&A/revenue | 3.0% → 3.5% | mature retail infra depreciation |
| **Retail DCF EV** | **$380.3B** | — |

### 2.4 รวมเป็น Consolidated DCF (Σ segment, ไม่ใช่ top-down)
- Σ segment revenue 2026 = AWS $171.2B + Retail $652.9B = **$824.1B** ✅ ตรงกับ consolidated จริง
- Σ segment capex 2026 = AWS $154.1B + Retail $65.9B = **$220.0B** ✅ ตรงกับ guidance
- Consolidated terminal margin (2035) = **19.8%** — เป็น**ผลลัพธ์**จากการถ่วงน้ำหนัก AWS margin (42%, mix ~35%) + Retail margin (8%, mix ~65%) **ไม่ใช่ตั้งเอง**
- PV(FCFF 10yr) = $362.1B + PV(Terminal Value, g=3%) = $1,266.2B → **Consolidated EV = $1,628.2B**
- − Net debt $9.2B → Equity $1,619.0B ÷ 10.90B shares = **Emma FV = $148.53/share**

### 2.5 เช็คความสมเหตุผล (sanity check บังคับ)
- Consolidated EV ($1,628.2B) > AWS-only EV ($1,248.0B) ✅ — ทางคณิตศาสตร์ต้องเป็นแบบนี้ (ผลรวมต้องมากกว่าส่วนเดียว) — รอบก่อน (v3.1) ผิดกฎนี้ ตอนนี้แก้แล้ว
- Implied Retail+Ads NOPAT 2035 = +$74.3B (เป็นบวก สมเหตุสมผลเทียบ NA+Intl EBIT ปัจจุบัน ~$34B ที่มี margin runway)

### 2.6 เทียบกับ SOTP (peer-multiple) — เลือก DCF เพราะ peer ไม่ match
Emma คำนวณ SOTP คู่กันไว้เป็น cross-check:
- AWS: DCF $1,248.0B vs peer-multiple (MSFT/GOOGL/ORCL median 19.9x) $1,291.1B → gap 3.5% (เล็ก, ไม่ต้อง reconcile)
- Retail: DCF $380.3B vs peer-multiple (WMT 27.3x / COST 40.89x / TGT 9.2x, median 27.3x) $938.3B → **gap 146.7%** — สาเหตุชี้ชัด: WMT/COST มี terminal-growth profile สูงกว่า AMZN retail segment ในโมเดลนี้มาก (COST มี membership moat, WMT มี scale-efficiency moat) — เอา multiple ของบริษัทที่โตเร็วกว่าไปคูณกับ segment ที่โตช้ากว่า = ประเมินสูงเกินจริง
- **เลือก DCF bottom-up เป็นตัวหลัก** เพราะผ่าน "Σsegment=consolidated" test ที่ SOTP ไม่ผ่าน — SOTP เก็บไว้เป็น sensitivity เท่านั้น

---

## 3. Bear FV = $89.13 — independent DCF, harsher assumptions

Bear ใช้โครงเดียวกับ Emma (segment-level bottom-up) แต่ **ตั้ง assumption ของตัวเองทุกตัวให้เข้มกว่า**:

| Variable | Emma (base) | Bear (harsher) |
|---|---|---|
| AWS growth Yr1→Yr10 | 33%→8% | 28%→8% |
| AWS terminal margin | 42% | 38.6% (competitive pricing pressure จาก GCP AI-inference) |
| AWS capex/revenue path | 90%→15% | 88%→16% (ยัง normalize จริง แค่ช้ากว่า) |
| Retail growth/margin | 11%→4% / 6.2%→8.0% | 9%→3% / 5.8%→6.1% (margin ไม่ expand ต่อเนื่อง) |

- Bear DCF EV = $980.8B → **Bear FV = $89.13/share**
- **Sanity check บังคับ:** Bear FV ($89.13) ต้อง**สูงกว่า** no-growth value (NOPAT ÷ WACC = $53.87) เพราะ Bear เองจัด AWS capex cycle เป็น "Temporary" (ไม่ใช่ structural impairment) — ถ้า capex Temporary แปลว่าสุดท้าย RONIC ต้อง ≥ WACC โดยเฉลี่ย ผลที่ได้ ($89.13 > $53.87) ✅ สอดคล้อง
- Implied RONIC ปี 2027-2029 ต่ำกว่า WACC (8.3-9.7%) แล้วไต่ขึ้นแตะ/เกิน WACC ปี 2031+ (11.0%) — J-curve lag ปกติของ capex ที่ยังไม่ online เต็มที่

---

## 4. Quinn P-W EV = $131.69 — probability-weighted scenario (independent)

Quinn สร้าง 3 scenario จาก assumption ของตัวเอง **ไม่ยืม FV ของ Emma/Bear** (กันการนับซ้ำ):

| Probability | Scenario | FV/share |
|---|---|---|
| 25% | Bull | $244.06 |
| 50% | Base | $134.27 |
| 25% | Bear | $14.17 |

```
P-W EV = 0.25×$244.06 + 0.50×$134.27 + 0.25×$14.17
       = $61.02 + $67.14 + $3.54
       = $131.69/share
```

Reverse-DCF check: ราคาตลาดปัจจุบัน ($259.92, EV ~$2,803B) สูงกว่า**แม้ Bull scenario ของ Quinn เอง** (EV ~$2,669B) ~5% — ตลาดต้องการ AWS margin terminal >44% หรือ AWS growth เกิน 35% เริ่มต้นเพื่อ justify ราคาปัจจุบัน ซึ่งเกินกว่าทุก scenario ที่ Quinn สร้างแม้ scenario บวกที่สุด

---

## 5. WACC — beta ยืนยันจาก 3 แหล่งอิสระ

| Input | ค่า | แหล่ง |
|---|---|---|
| Beta | 1.43-1.45 | wallstreetnumbers.com (1.43, Sep 2026), 2 แหล่งอื่นตรงกัน — **ไม่ใช่ 1.0 เท่า S&P500** |
| Risk-free rate | 5.29% | 3 sources ตรงกัน (ต.ค. 2026) |
| ERP | 4.14% | Damodaran (Sep 1, 2026) |
| **WACC** | **10.95%** | CAPM |

หมายเหตุ: WACC นี้อยู่นอกกรอบ 7-9% ที่ปกติใช้กับ mega-cap beta<1.3 — ทีมอนุมัติให้ใช้เพราะมี justification ชัด (thin-margin retail + capex supercycle ดัน beta ขึ้นจริง ไม่ใช่ error)

---

## 6. Sanity-check เพิ่มเติม (Market-Implied Sanity Check, v3.3)

ทดสอบว่าต้องขยับตัวแปรไหนแค่ไหนถึงจะปิด gap ไปที่ราคาตลาด ($259.92) — **ทุกตัวแปรต้องขยับเกินช่วงที่มีหลักฐานรองรับ:**

| ตัวแปร | ค่าที่ใช้ | ค่าที่ต้องใช้เพื่อปิด gap | ปัญหา |
|---|---|---|---|
| TGR | 3.0% | 6.69% | เกิน nominal GDP long-run ceiling (~5.5%) |
| Terminal margin (ทั้ง 2 segment) | AWS 42% / Retail 8% | +9.58pp ทั้งคู่ | AWS จะเกิน Azure margin จริง (~43%); Retail จะเกิน WMT/COST/TGT จริง 2 เท่า |
| WACC | 10.95% | 8.39% | implied beta 0.80 — ขัดกับ beta จริงที่ยืนยัน 1.45 |
| Revenue CAGR | ตามตาราง | ×1.53 (AWS Yr1 →42.8%) | เกิน AWS all-time-high growth rate จริง (37.0%) |

แม้ Emma FV เดี่ยวปิด gap ได้สมบูรณ์ (= $259.92 เท่าราคาตลาด) **Blended FV จะได้แค่ $170.21** (เพราะ Quinn/Bear ไม่เปลี่ยน) — ต้องให้ Emma FV ถึง **$484.19** (เกินราคาตลาดเองอีก 86%) ถึงจะทำให้ Blended = ราคาตลาด ซึ่งเป็นไปไม่ได้ในทางปฏิบัติ

---

## 7. จุดที่ยังเป็น Open Item (ยังไม่ปิดสนิท — บอกตรงๆ ไม่ซ่อน)

1. **Retail DCF vs SOTP gap 146.7% ที่เลือก DCF เป็นหลัก** — อธิบายด้านเดียวว่า SOTP overstate (peer multiple ไม่ตรง growth-profile) แต่ยังไม่ทดสอบว่า Retail DCF เองอาจ **understate** (เพราะ Ads ซึ่งโตเร็ว/margin สูงฝังอยู่ใน NA/Intl แต่โมเดลใช้ terminal growth 4% เหมาะรวมทั้งก้อน)
2. **คำอธิบายทางเลือกสำหรับ gap ที่เหลือ** — ราคาตลาดอาจสะท้อน optionality (Trainium custom-silicon, Anthropic partnership) ที่ DCF framework ของทีม (horizon 10 ปี) ไม่ capture — นี่เป็นสมมติฐาน ไม่ใช่สิ่งที่พิสูจน์ได้ด้วย DCF แบบดั้งเดิม

---

## 8. สิ่งที่อยากให้มืออาชีพช่วยตรวจเป็นพิเศษ

1. **Terminal margin AWS 42%** — สมเหตุผลไหมเทียบ hyperscaler margin จริงในอุตสาหกรรม (Azure/GCP) ระยะยาว
2. **Retail terminal growth 4%** — ควรแยก Ads ออกจาก NA/Intl หรือไม่ (Ads มี margin/growth สูงกว่ามาก แต่ 10-K ไม่แยก operating income ให้)
3. **TGR 3.0% แบบเดียวทั้ง 2 segment** — AWS (cloud, high-growth terminal) กับ Retail (mature, low-growth) ควรใช้ TGR ต่างกันไหม
4. **Peer selection สำหรับ SOTP** — WMT/COST/TGT เหมาะสมไหมในการเทียบ AMZN retail (ที่มี logistics/fulfillment network ต่างจาก pure retailer)
5. **โครง Blended 40/30/30** — น้ำหนักนี้เหมาะกับหุ้นที่มี segment valuation ซับซ้อนแบบ AMZN ไหม หรือควรปรับ weighting เมื่อมี SOTP เข้ามาเกี่ยวข้อง

---

*ไฟล์ต้นฉบับแบบเต็ม (รวม audit script, ตาราง DCF ปีต่อปีทั้ง 10 ปี): `agent_notes/emma/2026-10-07_AMZN_v3.md`, `agent_notes/bear/2026-10-07_AMZN_v3.md`, `agent_notes/quinn/2026-10-07_AMZN_v3.md`, `agent_notes/emma/2026-10-08_AMZN_v3.3.md`*
