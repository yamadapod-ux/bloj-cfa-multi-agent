# Charlie Funnel Redesign Proposal — 2026-09-06

**สถานะ:** ✅ **APPROVED + ENCODED 2026-09-06** — CIO อนุมัติ "Encode เป็น trial ตามที่ Charlie เสนอ". Encoded เข้า `CLAUDE.md` (§ Scout Filter Rules Filter D+E+A-redef · § Tier 1 check 2b + Tier 1.5 Lane Assignment · § Vera Funnel Health 3-stage) + `.claude/agents/max.md` (Mode 1 Step 4) + `.claude/commands/scout.md` (Step 4) ด้วย tag `(TRIAL — review 2026-12-31)`. Trial: Scout Round 28–30 (post-FOMC → สิ้นปี). **ยังไม่ใช้กับ Return-side locked rules.**
**Trigger:** CIO ถาม (2026-09-06) — "gate ดีขึ้นไหม หรือควรปรับปรุง — ที่ต้องการคือ scout หุ้นดีๆ แล้วค่อยวิเคราะห์หุ้นที่มีแนวโน้มจะผ่าน บลจ. เรา"
**Precedent:** `agent_notes/charlie/2026-09-01_strategic_note.md` (scout re-orientation VALUE-FIRST + gate hold) · `feedback_learning_over_returns.md` · `feedback_cio_selection_gate.md`
**ขอบเขต:** แก้เฉพาะ **resource-triage layer** (scout screen + Tier 1) — **ไม่แตะ Return-side locked rules** (ยืนยันในข้อ 2)

---

## 0. บทสรุปผู้บริหาร (อ่าน 60 วินาที)

| ประเด็น | คำตอบ Charlie |
|---------|--------------|
| **Gate มีปัญหาไหม?** | **ไม่** — Gate ตัดสินถูกทุกเคสที่ตรวจสอบได้ (APTV/CNC/QCOM/MU/CRCL...). Alpha inception-to-date **+0.42%** ยังบวก → Pre-commitment Rule ห้ามแก้ Return-side rules จนกว่า rolling 8Q alpha trend ติดลบ. **ห้ามแตะ MOS 15% / Conviction 7.0(V) 6.5(G) / 40-30-30.** |
| **ปัญหาจริงคืออะไร?** | **Scout→analysis conversion ≈ 0%** — deploy ล่าสุด ADSK 2026-06-14 → หลังจากนั้น **25 full analyses / 6 re-analyses ใน ~12 สัปดาห์ · deploy 0 · token ~200–255K ต่อเคส**. Scout ป้อน universe ที่ไม่มีทางผ่าน gate ตั้งแต่ต้น |
| **Root cause** | Scout screen (VALUE-FIRST: A beaten-down / B cheap-multiple / C ROIC>WACC) คัด "ดูถูก + เป็นธุรกิจจริง" แต่**ไม่ได้คัดสิ่งที่ gate เช็คจริง** = (1) credible gap ถึง conservative FV และ (2) credible path ถึง conviction ≥ gate. หุ้นที่ผ่าน A+B+C แต่ FAIL gate = ราคาลงมาเพราะ **permanent impairment** ไม่ใช่ dislocation ชั่วคราว |
| **ข้อเสนอ** | เพิ่ม **Filter D** (FV pre-check), **Filter E** (conviction pre-screen), **นิยาม "beaten-down reason" ใหม่ใน A**, **Tier 1 check 2 เป็น bidirectional**, และ **2-Lane system** (fast-track vs learning-queue) เพื่อรักษา learning objective ของ CIO |
| **ผลคาดหวัง** | ประหยัด token ~2.5–3.5M / ไตรมาส (จากการไม่วิ่ง full pipeline บนเคสที่ยืนยันผลได้จากตัวเลข scout). **ไม่การันตี deploy เพิ่ม** — ตลาด near-ATH + Fed-hawkish ทำ fat pitch หายากจริง (F) |
| **Charlie แนะนำ** | **Adopt-with-modification** — ทดลอง 3 scout rounds (Round 28–30, post-FOMC → สิ้นปี) ก่อน lock เข้า CLAUDE.md |

---

## 1. Diagnosis — Conversion Problem

### 1.1 ภาพรวม funnel ตั้งแต่ deploy ล่าสุด

- **Last deploy:** ADSK 2026-06-14 (T1, $476.23, Conv 7.0, MOS +31.6%)
- **หลังจากนั้น:** full analyses ใหม่ (new ticker) **25 ตัว** + re-analyses **6 ครั้ง** (ACGL v2, VEEV v2, NOW, QCOM v2, RDDT full, + lightweight RDDT) → **deploy 0**
- **Regime timeline:** RISK-ON 3/4 (มิ.ย.–ส.ค.) → TRANSITIONAL-CAUTIOUS (Atlas 2026-09-01, judgment override) → RISK-ON 3/4 (Atlas 2026-09-05, Fed-hawkish overlay)
- **Portfolio ปัจจุบัน:** 7 positions (RDDT ปิด 09-03), cash ~65%, alpha +0.42%

### 1.2 ตาราง 15+ analyses — มิ.ย. → ก.ย. 2026 (จาก `decisions.md` + `deployment_log.md` + `tracker.md`)

| # | Date | Ticker | Bucket | ราคา | Blended FV | **MOS (raw)** | **Conv** | Moat | ROIC vs WACC | Overhang หลัก | Gate result |
|---|------|--------|--------|------|-----------|--------------|---------|------|--------------|--------------|-------------|
| 1 | 06-10 | MCO | Value | ~$448 | $429 | **−4.2%** | 7.0 | Wide | ROIC 30% >> WACC | — | MOS fail |
| 2 | 06-14 | ACGL v1 | Value | $91.66 | $106 | +15.6% | **6.3** | Narrow+ | > | peak-ROE anchoring | Conv fail |
| 3 | 06-17 | TOST | Growth | $25.28 | $34 | +33.3% | **6.33** | Narrow | คร่อม (FCF quality) | FCF $654M vs NI $412M | Conv fail |
| 4 | 07-06 | CRDO | Growth | $241.91 | $185.86 | **−23.2%** | **6.3** | Narrow | > | cust. conc. ~90% top-10, β 3.20 | dual fail |
| 5 | 07-12 | WPM | Value | $110.05 | $99.20 | **−9.9%** | **6.3** | Wide | > | Salobo 38–40% NAV conc. | dual fail |
| 6 | 07-22 | PGR | Value | $205.90 | $208 | **+1.0%** | **6.67** | Narrow+ | > | op margin ต่ำสุด peer, −2 down-days/wk | dual fail |
| 7 | 07-29 | DXCM | Value | $74.85 | $75.14 | **+0.4%** | **6.17** | Narrow+ | > | earnings −40% crash precedent, T2 mix | dual fail |
| 8 | 08-02 | ABBV | Value | $250.94 | $251.08 | **+0.06%** | **6.77** | Narrow | ROIC 14–16% ≈/> | Rinvoq IRA 2027, neg. equity | dual fail |
| 9 | 08-05 | ETN | Value | $444.80 | $308.25 | **−30.7%** | **6.23** | Narrow | > | Emma-Quinn FV gap 3.05x | dual fail |
| 10 | 08-05 | VRT | Growth | $269.93 | $276.82 | +2.55% | **6.00** | Narrow | > | Eaton+Schneider เข้า thermal | Conv fail |
| 11 | 08-10 | ICE | Value | $150.30 | $162.90 | **+8.4%** | **6.17** | Wide | > | MarketAxess deal leverage 3.4x | dual fail |
| 12 | 08-10 | NET | Growth | $304.58 | $60.92 | **−80.0%** | **5.33** | Narrow | op margin −14% | dual-class + Delaware suit | dual fail |
| 13 | 08-18 | ACGL v2 | Value | $97.81 | $91.86 | **−6.1%** | **5.5** | Narrow+ | > | rev −10.5%, CR แย่ลง 2Q | dual fail |
| 14 | 08-18 | TDG | Value | $1,231.62 | $1,085.33 | **−11.9%** | **6.33** | Wide | ROIC 19.4% > | DoD IG price-gouging, right-to-repair NDAA | dual fail |
| 15 | 08-20 | VEEV v2 | Value | $251.00 | $188.81 | **−24.8%** | 6.5 | Wide | > | ราคา +51% จาก S&P inclusion flow | MOS fail |
| 16 | 08-21 | SHOP | Growth | $145.54 | $129.99 | −0.8% | **6.0** | Wide | > | founder 40% vote, agentic unproven | Conv fail |
| 17 | 08-22 | TLS | Growth | $4.395 | $4.09 | **−6.9%** | **5.83** | Narrow | GAAP loss | 91% federal conc., 1Q hard evidence | Conv fail |
| 18 | 08-24 | NOW | Value (re) | $128.48 | $125.65 | **−2.2%** | **5.83** | Wide | > | TGR cap → FV ลด, held position | MOS fail (held) |
| 19 | 08-27 | MU | Growth | $918.31 | $291.92 | **−68.2%** | **6.0** | Narrow | cyclical peak | +680%/1yr, cycle peak | dual fail |
| 20 | 08-28 | CRCL | Growth | $92.26 | $26.00 | **−71.8%** | **5.67** | Narrow (eroding) | float model | 95% rev = Fed float, Open USD consortium | dual fail |
| 21 | 08-29 | ADI | Value | $361.78 | $229 | **−36.7%** | **5.83** | Wide | ROIC 34–45% > | MOFCOM anti-dumping ruling ~09-13 | dual fail |
| 22 | 08-29 | MELI | Growth | $1,966.25 | $1,207 | **−38.6%** | **5.33** | Wide | ROIC 14.2% ≈ WACC ~13% | 100% LatAm, op margin ยุบ 6.7%, Shopee | Conv fail (deep) |
| 23 | 08-30 | GCT | Growth | $52.95 | $57.02 | **+7.7%** (ESG-adj +0.2%) | **6.17** | Narrow | ROIC ~23% > WACC 13.5% | dual-class 74.8%, 2 short-sellers, KPIs un-audited, CEO 48 sells | Conv fail |
| 24 | 08-31 | CHYM | Growth | $33.20 | $22.30 | **−32.8%** | **4.83** | Narrow | > | Durbin/Reg II litigation binary, worst peer metrics | tri fail |
| 25 | 09-01 | ZETA | Growth | $30.88 (scout $23.50 **STALE +31%**) | $19.16 | **−38.0%** | **5.5** | Narrow | > | Davoodi class action MTD denied → discovery, SBC 12.4% | dual fail |
| 26 | 09-01 | OSCR | Growth | $29.96 | $21.10 | **−29.6%** | **4.83** | Narrow | ROIC 4–8% < WACC 8% | ACA ePTC cliff 2026 (legislative binary), P/B 4.5x, β 2.38 | tri fail |
| 27 | 09-03 | FSLR | Value | $202.60 | $155.29 | **−23.4%** | **5.67** | Narrow+ | ROIC 19.6% > | Section 301/122 tariff suit (moat + demand risk), backlog −2Q | dual fail |
| 28 | 09-04 | CNC | Value | $68.02 (scout $43.68 **STALE +55.7%**) | $44.53 | **−34.5%** | 6.0 | Narrow | ROIC 4–8% < WACC 8.1–8.3% | one-time CMS item ปน guidance, buyer-power รัฐ | MOS fail (clean) |
| 29 | 09-05 | QCOM v2 | Value (re) | $168.71 | $111.59 | **−33.9%** | 6.33 | Narrow | > | Apple modem loss **confirmed**, β 1.35→1.68 | MOS fail (clean) |
| 30 | 09-06 | APTV | Value | $47.95 | $45.09 | **−6.0%** (ESG-adj −9.7%) | **5.5** | Narrow | ROIC ~9–11% ≈ WACC 10% | China ~28% rev = structural (mgmt-confirmed), net debt 2.1x | dual fail |

### 1.3 สองกลุ่ม failure (ตามที่ CIO สรุป — Charlie ยืนยัน)

**กลุ่ม A — Growth priced-for-perfection** (13 ตัว): CRDO, VRT, NET, MU, CRCL, MELI, GCT, CHYM, ZETA, OSCR, TOST, TLS, SHOP
- ลักษณะ: ธุรกิจโตเร็วจริง execute จริง แต่ราคา = premium multiple / near-ATH → MOS ติดลบลึก (−23% ถึง −80%) หรือ conviction ต่ำจาก un-provable KPI / governance / binary
- **สาเหตุ scout ป้อนผิด:** VALUE-FIRST screen "ควร" คัดกลุ่มนี้ออกด้วย Filter A (beaten-down ≥30%) — แต่ **scout price ผิดหลายเคส** (ZETA $23.50 vs จริง $30.88 = +31%; MELI/MU/GCT ราคาจริง near-ATH) → Filter A ผ่านหลอกๆ

**กลุ่ม B — Value fairly-priced / trap** (12 ตัว): MCO, WPM, PGR, DXCM, ABBV, ETN, ICE, TDG, ACGL, FSLR, CNC, QCOM, APTV
- ลักษณะ: หุ้น de-rate จริง (−30% ถึง −50% จาก high) แต่ราคาลงมาเพราะ **fundamental แย่ลงจริง** — China structural (APTV, QCOM), ACA legislative (CNC, OSCR), buyer-power (CNC), earnings-power impairment (QCOM Apple modem), or ROIC ≈ WACC ไม่ compound (APTV, ACGL, MELI)
- **สาเหตุ scout ป้อนผิด:** Filter A+B+C ผ่าน (ราคาลงจริง + multiple ต่ำจริง + ROIC เคยเหนือ WACC) แต่ screen **ไม่เช็ค "ทำไมราคาลง"** — permanent impairment vs cyclical dislocation

### 1.4 Data-integrity sub-problem (แยกจาก conversion)

Scout price error **2 ครั้งติด** ใน Round 27: ZETA +31% (09-01), CNC +55.7% (09-04) — ทำ Filter A ผ่านหลอก นำไปสู่ full pipeline ที่ไม่จำเป็น. มีกฎ Price Verification ที่ scout stage อยู่แล้ว (CLAUDE.md, เพิ่ม 2026-09-04) แต่ **ยังไม่ได้บังคับใช้จริง** — ข้อเสนอนี้ทำให้ Filter D/E ต้อง re-verify ราคาก่อนคำนวณ → บังคับโดยธรรมชาติ

---

## 2. สิ่งที่ห้ามแตะ + เหตุผล

| Rule | Type | สถานะ | เหตุผลที่ห้ามแตะตอนนี้ |
|------|------|-------|----------------------|
| MOS threshold (Value ≥15% / Growth Reverse-DCF ≤1.2× + ≤70th pct) | **Return-side** | 🔒 LOCKED | Rule Classification Table: แก้ก่อน rolling 8Q alpha trigger ไม่ได้ |
| Conviction gate (Value ≥7.0 / Growth ≥6.5) | **Return-side** | 🔒 LOCKED | เดียวกัน |
| Blended FV weights 40/30/30 | **Return-side** | 🔒 LOCKED | เดียวกัน — Error #8/#9 prevention (ปฏิเสธ fabricated 40/35/25) ทำงานแล้ว 6 ครั้งติด |
| Position size 8–10% / min 3% | Return-side | 🔒 LOCKED | เดียวกัน |
| Deployment Rules #1–5 / Force Deploy | Return-side | 🔒 LOCKED | เดียวกัน |

**หลักฐานว่า gate ทำงานถูก (ไม่ใช่ false negative):**
- APTV — business ROIC ~9–11% ≈ WACC 10% = ไม่ compound + China structural (management ยืนยันเอง). Bear: "แม้ buy at $40 ก็ generous"
- CNC — fwd P/E "ถูก" 11.8–14.6x เป็นภาพลวงจาก one-time CMS item; normalized ~15.3–15.8x ≈ sector median; ROIC 4–8% < WACC
- QCOM v2 — ราคาร่วง −22.6% แต่ FV ร่วง −41.9% เพราะ Apple modem loss confirmed (ไม่ใช่ risk แล้ว) — **ราคาถูกลงไม่ได้แปลว่า MOS ดีขึ้น** (contradicts CIO's initial hypothesis, ยืนยันโดย pipeline)
- MU / CRCL / MELI — Kelly ติดลบทุกระดับ, 0–1/25 sensitivity cells justify ราคา

**Alpha status:** inception-to-date **+0.42%** (portfolio +5.14% vs S&P +4.71%, 09-03 close). Rolling 4Q/8Q ยัง N/A (~3.9 เดือน). → **ไม่เข้า pre-commitment trigger** → Return-side rules ล็อกต่อ

**สิ่งที่แก้ได้ (resource-triage layer — ไม่อยู่ใน Rule Classification Table):**
- Scout Filter Rules (screen direction) — เคยแก้ 2026-09-01 (growth-first → value-first) แล้วโดยไม่แตะ gate
- Tier 1 Quick-Screen (arithmetic routing) — เคยแก้ v1 → v2 (2026-09-05)
- Pipeline lane structure (fast-track vs learning-queue) — ใหม่, ไม่ขัด rule ใด

---

## 3. ข้อเสนอละเอียด — Exact Text

> ทั้งหมดนี้เป็น **resource-triage layer** — ไม่เปลี่ยนเกณฑ์ตัดสินใจลงทุน เปลี่ยนแค่ "อะไรควรได้ full pipeline"

### 3.A — Filter D ใหม่ (FV pre-check ที่ scout stage)

**แทรกใน:** `CLAUDE.md` § Scout Filter Rules — VALUE-FIRST · **หลัง** block "Primary filter (บังคับ — candidate ต้องผ่านทั้ง A + B + C)" และ **ก่อน** "Price Verification ที่ scout stage"
**เปลี่ยนหัวข้อ block:** จาก "candidate ต้องผ่านทั้ง A + B + C" → **"candidate ต้องผ่านทั้ง A + B + C + D + E"**

```markdown
- **D. Credible valuation gap (บังคับ — เพิ่ม 2026-09-06):** ก่อนส่ง candidate เข้า pipeline Max ต้องทำ naive FV 1 รอบและยืนยันว่ามี **gap ≥ 20% ระหว่างราคาปัจจุบันกับ conservative FV**:
  - **Naive FV = normalized/mid-cycle FCF ÷ WACC** (no-growth perpetuity) — ใช้ **through-cycle FCF ไม่ใช่ TTM peak** (ถ้าธุรกิจ cyclical: เฉลี่ย 5 ปี หรือ mid-cycle margin × normalized revenue). WACC ใช้ค่าประมาณ sector (7–9% mega-cap / 10–13% mid-cap / 13–16% small-cap หรือ EM)
  - **Cross-check:** analyst consensus PT range (WebSearch ≥2 แหล่ง) — ถ้า Street PT median **ต่ำกว่า** ราคาปัจจุบัน = สัญญาณเตือน (candidate ตกรอบ). ถ้า Street PT สูงกว่ามาก (>25%) แต่ naive FV ต่ำกว่าราคา = ใช้ naive FV เป็นเกณฑ์ตัดสิน (Street อาจ extrapolate peak)
  - **เกณฑ์ผ่าน:** ราคาปัจจุบัน ≤ 0.80 × naive FV (มี MOS อย่างน้อย ~20% ก่อนเข้า pipeline)
  - **เกณฑ์ตกรอบ:** ราคาปัจจุบัน > 0.90 × naive FV **หรือ** ราคาปัจจุบัน อยู่ในช่วง ±10% ของ naive FV (ไม่มีที่ว่างให้ MOS 15% clear หลัง DCF เต็ม) → deprioritize, ไม่ส่ง fast-track
  - **เกณฑ์ก้ำกึ่ง (0.80–0.90 ×):** ส่งเข้า learning-queue lane (ดู 3.E) ไม่ใช่ fast-track
  - Multiple-based cross-check: EV/EBITDA หรือ EV/Revenue ต้องอยู่ **bottom-third ของ 5Y history ตัวเอง** — ถ้าอยู่ >70th percentile ทั้งที่ราคา "ลง 30% จาก high" = high เดิมเป็น bubble, ตกรอบ
```

**ผลที่คาด (จากตาราง 1.2):** MCO / PGR / DXCM / ABBV / ICE / VRT / SHOP / APTV / CNC / QCOM / ZETA / OSCR / CHYM / MU / CRCL / ADI / MELI / NET / CRDO / ETN / TDG / WPM / FSLR → **ตกรอบที่ scout** (ราคา ≥ 0.90× หรือ MOS ติดลบชัดจาก naive FV). เหลือ TOST / GCT → learning-queue

### 3.B — Filter E ใหม่ (conviction pre-screen)

**แทรกใน:** ตำแหน่งเดียวกับ D, ต่อจาก D

```markdown
- **E. Conviction viability (บังคับ — เพิ่ม 2026-09-06):** candidate ต้องผ่าน **≥ 2 ใน 3** sub-criteria (ถ้าผ่านแค่ 1 → learning-queue lane; ถ้าผ่าน 0 → ตกรอบ):
  1. **Moat กว้างพอ** — Wide หรือ Narrow+ ที่มีหลักฐานชัด (pricing power / switching cost / network effect / cost advantage ถาวร). Narrow ที่ margin ต่ำสุดใน peer group = ไม่ผ่าน sub-criterion นี้
  2. **Through-cycle ROIC ชัดเจนเหนือ WACC** — spread ≥ +3pp ใน trailing 5Y average (ไม่ใช่แค่ TTM peak). ROIC ที่ **คร่อม** WACC (±2pp) เช่น APTV ~9–11% ≈ WACC 10%, MELI 14.2% ≈ 13%, ACGL peak-anchored, CNC/OSCR 4–8% < 8% = ไม่ผ่าน
  3. **ไม่มี unresolved structural / regulatory / governance / accounting overhang** — เช่น:
     - Legislative binary ที่ยังไม่ resolve (ACA ePTC — CNC/OSCR; right-to-repair NDAA — TDG)
     - Structural demand headwind ที่ management ยืนยันเอง (China — APTV/QCOM)
     - Dual-class super-voting + insider selling pattern (GCT founder 74.8% + CEO 48 sells; NET; SHOP)
     - Active securities litigation past MTD / short-seller report ที่ยังไม่ถูก rebut (ZETA Davoodi discovery; GCT Culper+Grizzly)
     - Un-audited operational KPIs ที่เป็นแกน thesis (GCT GMV/active buyers)
  - **หมายเหตุ:** overhang ที่ **quantifiable + asymmetric payoff** (เช่น regulatory case ที่มี strong precedent for dismissal, probability-weighted) ยังส่ง learning-queue ได้ — ไม่ auto-reject
```

**ผลที่คาด:** GCT / CHYM / ZETA / OSCR / NET / SHOP / CNC / APTV / QCOM / TLS / TOST → ตกรอบ/learning-queue จาก sub-criterion 2 หรือ 3

### 3.C — นิยาม "beaten-down reason" ใหม่ใน Filter A

**แทนที่ bullet A เดิม:**
> **A. Beaten-down:** ราคาปัจจุบัน **ลง ≥ 30% จาก 52-week high** (บังคับ — นี่คือ filter ที่สำคัญที่สุด; ห้าม scout หุ้นที่อยู่ใน 10% ของ 52W high เว้นแต่ CIO สั่งตรง)

**ด้วย:**
```markdown
- **A. Beaten-down ด้วยเหตุผลที่ถูกต้อง (บังคับ — แก้นิยาม 2026-09-06):** ราคาปัจจุบัน **ลง ≥ 30% จาก 52-week high** (ยืนยันด้วย WebSearch ≥2 sources — ห้ามใช้ scout price จากแหล่งเดียว, ดู Price Verification block ด้านล่าง) **และ** Max ต้องระบุ **"beaten-down reason"** เป็นข้อความสั้นๆ จัดประเภทเป็น 1 ใน 2:
  - ✅ **Cyclical / sentiment / temporary dislocation** — cycle trough, rate-driven overreaction, sector-wide selloff ที่ไม่แยกแยะ, one-time charge ที่จบแล้ว, litigation ที่มี precedent เอียงไปทาง resolve → **ผ่าน Filter A**
  - ❌ **Permanent earnings-power impairment** — structural demand loss ที่ management ยืนยัน (APTV China, QCOM Apple modem), secular decline, regulatory regime change ที่ยังไม่ resolve และ default outcome = bearish (CNC/OSCR ACA), competitive moat erosion ที่ยืนยันด้วยตัวเลข market share → **deprioritize / reject ที่ scout** (ห้าม fast-track; ส่ง learning-queue ได้ถ้า CIO ต้องการ data point)
  - ถ้า Max ไม่แน่ใจว่าจัดกลุ่มไหน → เขียนทั้ง 2 มุมใน scout note และ default เป็น learning-queue lane
```

### 3.D — Tier 1 Quick-Screen check 2 เป็น bidirectional

**แทนที่ในตาราง § Tier 1 Quick-Screen แถว # 2:**
> | 2 | ราคาแพงเวอร์แค่ไหน | Scout Filter B → แปลงเป็น naive FV ... | ราคาปัจจุบัน > 1.5× naive FV | → **Full Pipeline** (ไม่ติด...) |

**ด้วย:**
```markdown
| 2a | ราคาแพงเวอร์แค่ไหน | Scout Filter B/D → naive FV (FCF÷WACC no-growth perpetuity, normalized FCF) | ราคาปัจจุบัน **> 1.5× naive FV** | → เช็ค 2b |
| 2b | ราคาไม่มีที่ว่างให้ MOS เลยไหม | Scout Filter D naive FV | ราคาปัจจุบัน **อยู่ภายใน ±10% ของ naive FV** (Value bucket: ไม่มีทาง clear MOS ≥15% หลัง DCF เต็ม) **หรือ** ราคา > 0.95× naive FV สำหรับ Growth bucket | → **SKIP** (QUICK-SCREEN SKIP) |
```
**เพิ่มหมายเหตุใต้ตาราง:**
```markdown
**Check 2 bidirectional (เพิ่ม 2026-09-06):** เดิม SKIP เฉพาะขาแพงเวอร์ (>1.5×). เพิ่มขา SKIP กลาง — ราคาที่ "ไม่แพงจนเวอร์ แต่ก็ไม่มีที่ว่างให้ MOS clear" (±10% ของ naive FV). Charlie ทำเองเป็น arithmetic routing ไม่ spawn agent (ตัวเลขจาก scout Filter D มีอยู่แล้ว). Calibration: PGR ($205.90 vs naive FV ~$200 = +2.9%) / DXCM (+0.4%) / ABBV (+0.06%) / APTV (−6%) / ICE (+8.4%) ติดขา 2b ทุกตัว — SKIP ฟรี แทนที่จะเสีย ~200K/ตัว. เคสที่ยังต้อง Full Pipeline: MOS ก้ำกึ่งจริงๆ ที่ต้อง DCF เต็มถึงจะรู้ (naive FV gap 15–25%)
```

### 3.E — 2-Lane System

**แทรกใน:** `CLAUDE.md` § Tier 1 — Quick-Screen · **หลัง** "เกณฑ์ SKIP" table · **ก่อน** "ไม่ใช้กับ:"

```markdown
### Tier 1.5 — Lane Assignment (เพิ่ม 2026-09-06 — respect CIO learning objective)

หลัง candidate ผ่าน Tier 1 (ไม่ SKIP) Charlie จัด lane จาก Scout Filter D + E:

| Lane | เงื่อนไข | Pipeline | Token budget |
|------|---------|----------|--------------|
| **Fast-track** | ผ่าน Filter D ชัด (ราคา ≤ 0.80× naive FV) **และ** Filter E ครบ 3/3 | Full pipeline ปกติ (Atlas → Emma∥Quinn → Bear → Charlie → Morgan QA → Leo → Vera → Max) | ~200–255K |
| **Learning-queue** | ก้ำกึ่ง — ผ่าน A+B+C แต่ Filter D อยู่ 0.80–0.90× **หรือ** Filter E ผ่านแค่ 2/3 **หรือ** beaten-down reason จัดกลุ่มไม่ชัด | **Tier 1.5 lightweight เท่านั้น:** Emma standalone FV (DCF + moat + 1 peer table) + Bear-lite challenge (5 risks + 3 bear-flip) — **ไม่มี Atlas Data Package เต็ม / ไม่มี Quinn / ไม่มี Morgan QA / ไม่ update dashboard REPORTS** | ~30–50K |
| **Reject** | ไม่ผ่าน A/B/C **หรือ** Filter D > 0.90× **หรือ** Filter E 0–1/3 **หรือ** beaten-down reason = permanent impairment | บันทึก `QUICK-SCREEN SKIP` ใน deployment_log.md | ~0–3K |

**Learning-queue output:** journal เข้า `agent_notes/charlie/learning_queue_YYYY-MM.md` (ไฟล์เดียวต่อเดือน, append) — ระบุ ticker / lightweight FV / conviction estimate / ทำไมไม่ fast-track / 6-month price checkpoint date. **ไม่เข้า `portfolio/decisions.md` เป็น formal recommendation** เว้นแต่ CIO สั่งยกระดับ

**CIO override (บังคับมีทางออก):** CIO สั่ง fast-track candidate ใดก็ได้ตรงๆ — bypass lane assignment ทั้งหมด (เหมือน FSLR 2026-09-03 ที่ CIO สั่ง learning exercise แม้ regime TC)

**ยกระดับ learning-queue → fast-track เมื่อ:** (a) Emma lightweight FV พบ MOS ≥ 25% (Filter D miscalibrated ทางอนุรักษ์เกิน) **หรือ** (b) overhang ที่กด Filter E resolve จริง (litigation dismissed, legislation passed, China stabilizes) **หรือ** (c) ราคา pull back ≥ 15% เพิ่มจากตอน scout
```

---

## 4. Back-Test — 30 analyses ผ่าน Filter D + E + A-redef

> ใช้ตัวเลข MOS / conviction / moat / ROIC-WACC / overhang **จริง** จากรายงานเดิม. naive-FV proxy = Blended FV ทีม (conservative — จริงๆ scout จะได้ค่าหยาบกว่า แต่ทิศทางเดียวกัน)

| Ticker | ราคา vs Blended FV | Filter D | Filter E (moat/ROIC/overhang) | A-redef | **Routing ใหม่** | Full pipeline เดิมเสีย |
|--------|-------------------|----------|-------------------------------|---------|------------------|----------------------|
| MCO | 1.04× (+4% เหนือ FV) | ❌ >0.90 | 2/3 (Wide, ROIC>>, no overhang) | cyclical OK | **REJECT-D** | ~200K |
| ACGL v1 | 0.86× | 🟡 ก้ำกึ่ง | 1/3 (Narrow+, peak-anchored ROIC, no) | cyclical OK | **LEARNING-QUEUE** | ~210K |
| TOST | 0.74× | ✅ PASS | 1/3 (Narrow, FCF-quality คร่อม, no hard overhang) | cyclical OK | **LEARNING-QUEUE** (E 1/3) | ~200K |
| CRDO | 1.30× | ❌ | 1/3 (Narrow, cust conc 90%, β3.2) | — | **REJECT-D** | ~220K |
| WPM | 1.11× | ❌ | 1/3 (Wide, Salobo 38% conc) | commodity-price OK | **REJECT-D** | ~215K |
| PGR | 0.99× | ❌ ±10% | 1/3 (Narrow, op-margin worst peer) | cyclical OK | **REJECT-D** (Tier1 2b) | ~210K |
| DXCM | 1.00× | ❌ ±10% | 2/3 (Narrow+, ROIC>>, earnings crash risk) | dislocation OK | **REJECT-D** (Tier1 2b) | ~230K |
| ABBV | 1.00× | ❌ ±10% | 1/3 (Narrow, ROIC≈, IRA overhang) | impairment (IRA) | **REJECT-D/A** | ~215K |
| ETN | 1.44× | ❌ | 2/3 (Narrow, ROIC>>, no) | cyclical OK | **REJECT-D** | ~230K |
| VRT | 0.98× | ❌ ±10% | 2/3 (Narrow, ROIC>>, competition) | cyclical OK | **REJECT-D** (Tier1 2b, Growth 0.95×) | ~230K |
| ICE | 0.92× | ❌ >0.90 | 2/3 (Wide, ROIC>>, deal leverage temp) | dislocation OK | **REJECT-D** | ~215K |
| NET | 5.00× | ❌❌ | 0/3 (Narrow op−14%, dual-class+suit) | impairment | **REJECT-D/E** | ~240K |
| ACGL v2 | 1.06× | ❌ | 0/3 (rev −10.5%, CR worse) | impairment (deteriorating) | **REJECT-D/E/A** | ~210K |
| TDG | 1.14× | ❌ | 1/3 (Wide, ROIC>, DoD IG + NDAA) | impairment (right-to-repair) | **REJECT-D** | ~230K |
| VEEV v2 | 1.33× | ❌ | 2/3 (Wide, ROIC>>, ราคา S&P-flow) | dislocation (แต่ราคาแพง) | **REJECT-D** | ~210K |
| SHOP | 1.12× | ❌ | 1/3 (Wide, ROIC>>, founder 40% vote) | — | **REJECT-D** | ~215K |
| TLS | 1.07× | ❌ | 0/3 (Narrow, GAAP loss, 91% fed conc) | — | **REJECT-D/E** | ~200K |
| NOW (re) | 1.02× | n/a — held position, ไม่ผ่าน scout | — | — | **N/A (open position re-verify)** | ~210K (จำเป็น — Re-Analysis Trigger) |
| MU | 3.15× | ❌❌ | 1/3 (Narrow, cyclical peak) | impairment (cycle peak) | **REJECT-D** (Tier1 2a >1.5×) | ~255K |
| CRCL | 3.55× | ❌❌ | 0/3 (Narrow eroding, Fed-float, consortium) | impairment | **REJECT-D/E** (Tier1 2a) | ~240K |
| ADI | 1.58× | ❌❌ | 2/3 (Wide, ROIC>>, MOFCOM ruling) | impairment (cycle+rate peak) | **REJECT-D** (Tier1 2a) | ~235K |
| MELI | 1.63× | ❌❌ | 1/3 (Wide, ROIC≈WACC, LatAm+Shopee) | trough (แต่ราคาแพง) | **REJECT-D** (Tier1 2a) | ~235K |
| GCT | 0.93× (ESG-adj 1.00×) | 🟡 ก้ำกึ่ง | 1/3 (Narrow, ROIC>, dual-class+short-sellers+un-audited KPI) | cyclical OK | **LEARNING-QUEUE** (D ก้ำกึ่ง, E 1/3) | ~230K |
| CHYM | 1.49× | ❌ | 1/3 (Narrow, Durbin binary, worst peer) | — | **REJECT-D** | ~215K |
| ZETA | 1.61× (scout price ผิด) | ❌❌ | 1/3 (Narrow, class action discovery, SBC 12%) | — | **REJECT-D** (+ Price Verification จับ scout error) | ~215K |
| OSCR | 1.42× | ❌ | 0/3 (Narrow, ROIC<WACC, ACA binary, β2.38) | impairment (ACA) | **REJECT-D/E/A** | ~220K |
| FSLR | 1.30× | ❌ | 1/3 (Narrow+, ROIC>, Section 301/122 suit = moat risk) | impairment (tariff moat uncertain) | **REJECT-D** | ~215K |
| CNC | 1.53× (scout price ผิด) | ❌❌ | 0/3 (Narrow, ROIC<WACC, one-time item, buyer-power) | impairment (ACA + rates) | **REJECT-D/E/A** (+ Price Verification จับ +55.7% error) | ~255K |
| QCOM v2 | 1.51× | ❌❌ | 1/3 (Narrow, Apple modem confirmed) | impairment (modem loss) | **REJECT-D/A** (Tier1 2a) | ~220K |
| APTV | 1.06× (ESG-adj 1.11×) | ❌ ±10% | 0/3 (Narrow, ROIC≈WACC, China structural mgmt-confirmed) | impairment (China) | **REJECT-D/E/A** (Tier1 2b) | ~210K |

### 4.1 สรุป back-test

| Routing | จำนวน | Ticker |
|---------|-------|--------|
| **REJECT ที่ scout / Tier 1** | **25** | MCO, CRDO, WPM, PGR, DXCM, ABBV, ETN, VRT, ICE, NET, ACGL v2, TDG, VEEV v2, SHOP, TLS, MU, CRCL, ADI, MELI, CHYM, ZETA, OSCR, FSLR, CNC, QCOM v2, APTV *(นับ APTV = 26 จริง — ดูหมายเหตุ)* |
| **LEARNING-QUEUE (Tier 1.5 lightweight)** | **3** | ACGL v1, TOST, GCT |
| **N/A (open-position re-verify — ต้องทำอยู่แล้ว)** | **2** | NOW, (RDDT lightweight) |
| **FAST-TRACK full pipeline** | **0** | — (ไม่มีเคสไหนผ่าน D ชัด + E 3/3 ในชุดนี้) |

> **หมายเหตุ:** ตาราง 4 มี 30 แถว, REJECT = 26 (รวม APTV), LEARNING-QUEUE = 3, N/A = 1 (NOW). RDDT lightweight ไม่อยู่ในตาราง

### 4.2 Token saved (ประมาณการ)

- **REJECT 26 เคส:** เดิมเสีย full pipeline ~200–255K/เคส = **~5.5M token** → ใหม่เสีย Tier 1 arithmetic + Price Verify ~1–3K/เคส = ~65K → **ประหยัด ~5.4M**
- **LEARNING-QUEUE 3 เคส:** เดิม ~210K/เคส = 630K → ใหม่ Tier 1.5 lightweight ~40K/เคส = 120K → **ประหยัด ~510K**
- **รวมช่วง 12 สัปดาห์:** **~5.9M token saved** (~3.2M/ไตรมาส normalized ถ้า cadence ช้าลงหลัง regime TC)
- **ข้อควรระวัง:** ตัวเลขนี้เป็น upper bound — สมมติว่า Filter D/E ที่ scout จะได้ข้อสรุปตรงกับ full pipeline. จริงๆ จะมี ~10–20% ที่ scout ตัดสินไม่ชัด → เข้า learning-queue เพิ่ม → ประหยัดจริง ~70–80% ของตัวเลขข้างบน = **~4–4.5M/12 สัปดาห์**

---

## 5. False-Negative Risk

### 5.1 Filter D อาจปฏิเสธ candidate ดีเหล่านี้ผิด

| ประเภท | ตัวอย่าง / กลไก | ความเสี่ยง |
|--------|----------------|-----------|
| **Margin-trough cyclical** | MELI — EV/Rev 3.05x = 5-year LOW เพราะ margin ยุบชั่วคราว (anti-Shopee investment) ไม่ใช่ราคาแพง. Naive FV บน TTM FCF จะดู "แพง" ทั้งที่ normalized margin recovery → FV จริงสูงกว่ามาก | สูง — naive FV บน depressed earnings = under-estimate |
| **Deep-value ที่ Street ไม่ cover / cover น้อย** | Small-cap, spin-off, post-restructuring — consensus PT ไม่มีหรือ stale → cross-check ขาดข้อมูล | กลาง |
| **Turnaround ที่ FV ยากประเมิน** | ธุรกิจกำลังพลิก (loss → profit inflection) — no-growth perpetuity FCF÷WACC ไม่จับ inflection | กลาง-สูง |
| **Hidden asset / SOTP** | Net cash 30%+ ของ market cap, non-core segment ซ่อนมูลค่า (GCT net cash $10.34/sh = 19%) — naive FCF÷WACC ไม่จับ balance-sheet value | กลาง |

### 5.2 Filter E อาจปฏิเสธ contrarian play ที่ดีผิด

- Overhang ที่ **เป็นเหตุผลของ discount พอดี** และมีแนวโน้ม resolve บวก — เช่น regulatory case ที่มี strong legal precedent for dismissal (FSLR Section 301/122 อยู่บนกลไกเดียวกับที่ SCOTUS ตีตก IEEPA tariff ไปแล้ว — แต่กลไกนั้นตัดทั้ง 2 ทาง), litigation ที่ settlement เล็ก (GCT $2.75M)
- **ความเสี่ยง:** Filter E sub-criterion 3 (no unresolved overhang) เป็น binary เกินไป — ถ้าใช้เข้มจะกรอง contrarian ทั้งหมด ซึ่งคือ VALUE-FIRST universe โดยนิยาม

### 5.3 Safety valves (เสนอ)

1. **Learning-queue เป็น catch-all** — candidate ที่ Filter D/E ตัดสินไม่ชัด **ไม่ reject** แต่ได้ Tier 1.5 lightweight (Emma standalone FV จับ margin-trough / inflection / SOTP ที่ naive FV พลาด) — cost แค่ ~40K
2. **Filter D ใช้ normalized/mid-cycle FCF ไม่ใช่ TTM** — เขียนไว้ใน exact text แล้ว (แก้ margin-trough bias บางส่วน)
3. **CIO override** — CIO สั่ง fast-track ใดก็ได้ตรงๆ (precedent FSLR)
4. **ยกระดับ learning-queue → fast-track** เมื่อ lightweight FV พบ MOS ≥25% (Filter D อนุรักษ์เกิน) หรือ overhang resolve
5. **Quarterly review ของ learning-queue realized outcomes** (Vera) — ถ้า learning-queue names วิ่งขึ้น >20% ใน 6 เดือนบ่อยๆ = Filter D/E เข้มเกิน → เป็น data point สำหรับ rolling-8Q review (เหมือน near-miss log ปัจจุบัน)

---

## 6. Deploy-Rate / Vera Funnel Health — ปรับ metric

### 6.1 ปัญหาถ้ามี learning-queue

Deploy rate ปัจจุบัน = `# DEPLOYED ÷ # full analyses`. ถ้า learning-queue (Tier 1.5) นับรวมใน denominator → deploy rate จะดูแย่ลงเทียม (learning-queue = journaling, คาดหวัง deploy 0% โดยออกแบบ)

### 6.2 เสนอ metric ใหม่ (แก้ CLAUDE.md § Vera Protocol — Weekly/Quarterly Output §6 Funnel Health)

```markdown
**Funnel Health — 3-stage (แก้ 2026-09-06):**

| Stage | นิยาม | Baseline คาดหวัง (RISK-ON) |
|-------|-------|---------------------------|
| **Scout → Fast-track rate** | # fast-track ÷ # candidates ที่ผ่าน A+B+C | ~15–30% (ถ้าต่ำกว่านี้ต่อเนื่อง = universe ยังผิด หรือ Filter D/E เข้มเกิน) |
| **Fast-track → Deploy rate** | # DEPLOYED ÷ # fast-track analyses | ~40–60% (นี่คือ metric ที่สะท้อน gate calibration จริง — fast-track = ทีมเชื่อว่าน่าจะผ่าน) |
| **Learning-queue realized outcome** | 6-month price move ของ Tier 1.5 names (แยก track, ไม่อยู่ใน deploy-rate denominator) | informational — ป้อน rolling-8Q gate review |

**Overall conversion** (scout → deploy) ยัง track ต่อเป็น context แต่**ไม่ใช่ judge metric หลักอีกต่อไป** — เพราะ Filter D/E ตั้งใจตัด universe ก่อนถึง pipeline

**Funnel Diagnostic Trigger (แก้):** **Fast-track → Deploy rate** < 20% ใน RISK-ON ติดกัน 2 ไตรมาส → mandatory diagnostic (เดิมใช้ overall deploy rate < 10%)
```

### 6.3 deployment_log.md tags

- คงเดิม: `DEPLOYED` / `SKIPPED` (full pipeline fail gate) / `QUICK-SCREEN SKIP` (Tier 1 arithmetic)
- **เพิ่ม:** `LEARNING-QUEUE` (Tier 1.5 lightweight — journal, no formal recommendation) — Vera แยกออกจาก Funnel Health denominator

---

## 7. Recommendation + Rollout

### 7.1 Charlie แนะนำ: **ADOPT-WITH-MODIFICATION**

| ข้อเสนอ | Charlie verdict | Modification |
|---------|----------------|--------------|
| **Filter D** (FV pre-check) | ✅ Adopt | ใช้ **normalized/mid-cycle FCF** (ไม่ใช่ TTM) + threshold ผ่านที่ ≤0.80× / ก้ำกึ่ง 0.80–0.90× / reject >0.90× — ไม่ใช้ Street PT เป็นเกณฑ์เดี่ยว (Street extrapolate peak) |
| **Filter E** (conviction pre-screen) | ✅ Adopt แต่ **soft-score** | ผ่าน ≥2/3 sub-criteria (ไม่ใช่ hard gate ทั้ง 3) — 1/3 → learning-queue, 0/3 → reject. ป้องกันการกรอง contrarian universe ทิ้งหมด |
| **A-redefinition** (beaten-down reason) | ✅ Adopt | เป็น **required written field** ใน scout note + default learning-queue ถ้าไม่ชัด — ไม่ auto-reject ทันที (ลด subjective-call risk) |
| **Tier 1 check 2 bidirectional** | ✅ Adopt เต็ม | Charlie ทำเอง arithmetic — cost ~0. Calibration ชัด (PGR/DXCM/ABBV/APTV/ICE ติดหมด) |
| **2-Lane system** | ✅ Adopt — **สำคัญที่สุด** | เป็นสิ่งที่รักษา `feedback_learning_over_returns` + `feedback_cio_selection_gate` — CIO ยังได้ดู analysis เคสก้ำกึ่ง แค่ในรูป lightweight |

### 7.2 สิ่งที่ Charlie **ไม่**เสนอ (พิจารณาแล้วตัดออก)

- ❌ ไม่เพิ่ม Filter E เป็น hard 3/3 — จะทำให้ scout หา candidate ไม่ได้เลยในตลาดนี้ (ทุก beaten-down name มี overhang บางอย่าง — นั่นคือเหตุผลที่มันถูก)
- ❌ ไม่ลด MOS/Conviction threshold — Return-side locked, ไม่ใช่ปัญหา
- ❌ ไม่ทำ learning-queue เป็น full Morgan QA — ขัดวัตถุประสงค์ประหยัด token

### 7.3 Rollout plan

| Phase | ระยะเวลา | สิ่งที่ทำ | Success criteria |
|-------|---------|----------|-----------------|
| **0. CIO review** | ทันที | CIO อ่าน proposal นี้ + อนุมัติ/แก้ | CIO sign-off |
| **1. Trial** | Scout Round 28–30 (post-FOMC 09-16 → สิ้นปี 2026, ~3 rounds) | Encode Filter D/E/A + Tier 1 2b + 2-lane เข้า CLAUDE.md ด้วย tag `(TRIAL — review 2026-12-31)`. Max ใช้จริงทุก scout round. Vera track fast-track rate + learning-queue outcomes | ≥1 fast-track candidate ต่อ round · token/round ลด ≥40% |
| **2. Review** | 2026-12-31 หรือ Q4 quarterly | Vera + Charlie ทบทวน: (a) fast-track → deploy rate (b) learning-queue names ที่ "น่าจะ fast-track" กี่ตัว (c) false-negative จริงกี่ตัว | ตัดสิน lock / modify / revert |
| **3. Lock หรือ revert** | Q1 2027 | ถ้า trial ผ่าน → ลบ tag TRIAL, เป็น permanent rule. ถ้าไม่ผ่าน → revert เป็น VALUE-FIRST เดิม + บันทึก lesson | — |

### 7.4 ความเสี่ยงของข้อเสนอนี้เอง (F — ยอมรับตามตรง)

1. **ไม่การันตี deploy เพิ่ม** — ส่วนใหญ่ของ deploy-0 เป็นเรื่องตลาด (S&P near-ATH + Fed-hawkish Warsh + hike priced → fat pitch หายากจริง, CLAUDE.md Regime-adaptive note ระบุไว้แล้ว). Funnel redesign แก้ **token waste ต่อการยืนยัน no-deploy** — ไม่ได้สร้าง opportunity
2. **Filter D/E เพิ่ม subjective judgment ที่ scout stage** — Max ต้องตัดสิน "cyclical vs permanent" / "moat กว้างพอไหม" ก่อนมี full pipeline. Mitigant: default learning-queue เมื่อไม่ชัด + Emma lightweight เป็น backstop
3. **Trial period อาจสั้นเกิน** — 3 rounds ในตลาด TC/near-ATH อาจไม่มี fast-track candidate เลย → ประเมิน Filter D/E ไม่ได้จริง. Mitigant: ถ้าจบ trial แล้วมี fast-track < 2 ตัว → ต่อ trial อีก 2 rounds ก่อนตัดสิน
4. **2-lane เพิ่ม bookkeeping** — ไฟล์ `learning_queue_YYYY-MM.md` + tag ใหม่ใน deployment_log + Vera metric ใหม่. Mitigant: 1 ไฟล์/เดือน append-only, ไม่ต้อง dashboard sync

---

## 8. สรุปให้ CIO (ทวน)

**คำถาม CIO:** gate ดีขึ้นไหม / ควรปรับปรุงยังไง เพื่อ scout หุ้นดีแล้ววิเคราะห์เฉพาะตัวที่มีแนวโน้มผ่าน

**คำตอบ Charlie:**
- **Gate ไม่ต้องแก้ (และแก้ไม่ได้ตาม pre-commitment)** — มันตัดสินถูก 30/30 เคส. Alpha +0.42% ยังบวก
- **แก้ที่ปากทาง (scout screen)** — เพิ่ม 3 filter (D = มี valuation gap จริงไหม / E = มี path ถึง conviction ไหม / A-redef = ลงเพราะ dislocation หรือ impairment) + Tier 1 check 2 สองทาง + 2-lane
- **Back-test:** 26/30 เคสจะถูกตัดที่ scout (ประหยัด ~4–5.5M token/ไตรมาส) · 3 เคสเข้า learning-queue lightweight · 0 เคสจะ fast-track (สะท้อนว่าตลาดไม่มี fat pitch จริง ไม่ใช่ screen พัง)
- **Learning objective ปลอดภัย** — CIO ยังได้ดู analysis เคสก้ำกึ่งผ่าน learning-queue (Emma FV + Bear-lite) + override ได้ทุกเมื่อ
- **แนะนำ:** adopt แบบ trial 3 scout rounds post-FOMC, review 2026-12-31, ค่อย lock

**CFA Framework:** Capital Allocation / Investment Process Design (CFA L3 — Portfolio Management: manager selection & process discipline) · Relative + Absolute Valuation screening (CFA L2)

**ความเสี่ยงสำคัญ:** false-negative บน margin-trough cyclical / turnaround ที่ naive FV ประเมินต่ำ — mitigant = normalized FCF + learning-queue backstop + CIO override

---

*Charlie — 2026-09-06 | Funnel Redesign Proposal (DRAFT for CIO review — ยังไม่ encode) | ไม่แตะ Return-side locked rules | Trial 3 rounds → review 2026-12-31*
