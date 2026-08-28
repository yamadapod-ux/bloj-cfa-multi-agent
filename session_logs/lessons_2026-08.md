# Monthly Lessons — สิงหาคม 2026

> Leo ดูแล | Pattern extraction จาก sessions ของเดือนนี้ | สร้าง/อัปเดตต้นเดือนถัดไป หรือเมื่อ CIO เรียก

---

## 1. Pattern Recognition — เรื่องที่เกิดซ้ำเดือนนี้

### 1.1 "Priced for perfection at cycle peak" — AVOID pattern (2 ครั้งในเดือนเดียว)
| Ticker | Date | Rating | Cycle ที่ยอด | Blended FV vs Price | Conviction |
|--------|------|--------|--------------|---------------------|------------|
| **MU** | 2026-08-27 | AVOID | DRAM/NAND/HBM commodity memory cycle peak | $291.92 vs $918.31 (MOS −68.21%) | 6.0/10 (Emma 7/Quinn 4/Bear 7) |
| **CRCL** | 2026-08-28 | AVOID | Fed rate cycle peak (95% revenue = reserve float income) | $26.00 vs $92.26 (MOS −71.8%) | 5.67/10 (Emma 7/Quinn 4/Bear 6) |

**Pattern:** ในตลาด RISK-ON ที่ทำ new highs ต่อเนื่อง (S&P 500 7,730 ปลายส.ค.) ทีมเริ่มเจอ candidates ที่ตลาด value ด้วย **hyper-growth multiple ทับ earnings ที่กำลังอยู่ยอด cyclical/rate cycle** — TTM growth เป็น artifact ของ peak conditions ปีที่แล้ว (MU: +166.98% TTM แต่ consensus 5Y EPS หดตัว −10.4%; CRCL: +37.19% TTM แต่ Q2 +7% YoY). ทั้งสองเคส:
- Growth MOS Gate FAIL ทั้ง 2 วิธี (Reverse DCF implied growth สวนทาง consensus + multiple percentile สูง)
- Conviction structure เหมือนกัน: Emma 7 / **Quinn 4** (FV precision ต่ำ) / Bear 6–7 → gap 3.0 flag แต่ **directional unanimity**
- Bear เพิ่ม Extreme Bear tier + สรุปว่าทีม underestimate downside เสมอ
- Recommendation robust ต่อ WACC/TGR assumption — sensitivity test ยังให้ MOS ติดลบ 40%+ แม้ใช้ bull-friendly inputs

**Implication สำหรับทีม:** เมื่อ Atlas macro brief flag "cycle position = peak" หรือ "TTM growth = artifact ของ peak conditions" → ให้ weight bear/downside scenario บน revenue line มากขึ้นตั้งแต่ต้น + คาดว่า Growth MOS Gate จะ FAIL. Charlie ควร frame รายงานเป็น "great business? maybe. good entry? no" ตั้งแต่ TL;DR

### 1.2 Morgan QA Round 1 FAIL — Terminal Growth Rate เกินเพดาน (เกิดซ้ำหนักมาก)
DXCM → ICE → ACGL → TLS → NOW → **MU** = 5–6 instances ในไตรมาสนี้ ของ pattern เดียวกัน: DCF terminal growth rate g > 3% (เพดาน sanity check 1–3%). ทุกครั้ง correction cascade เต็มรูปแบบ (recompute FV → Blended FV → MOS → Stop Loss → dashboard). **CRCL ไม่ติด pattern นี้** (Emma TGR 2.5%, Quinn 3.0%, Bull cap 3.0% — compliant ตั้งแต่ Round 1) — เป็นสัญญาณว่า Emma/Quinn เริ่ม internalize เพดาน 3% หลัง MU

### 1.3 Structured-data ESG mismatch ที่ Leo ต้องแก้ก่อน embed (เกิดซ้ำ)
TLS 2026-08-22 (ESG 5.7 arithmetic → 6.0) + **CRCL 2026-08-28 (ESG 6.0 pre-Bear-challenge → 5.6 reconciled)**. Emma's structured-data block มักไม่ update ESG หลัง Bear challenge / reconciliation. **Leo checklist ถาวร:** ก่อน embed data.js ทุกครั้ง ให้ pull reconciled ESG จาก report §🌱 (ตาราง Emma/Bear/Reconciled) ไม่ใช่ copy จาก Emma's structured block

---

## 2. Calibration Update — agent ปรับตัวยังไง

- **Emma + Quinn:** เริ่ม default NOPAT-based FCFF + TGR ≤ 3.0% โดยไม่ต้องถูก Morgan เตือน (CRCL compliant Round 1) — DCF Cash Flow Consistency Rule (VEEV) + TGR cap (MU) internalized
- **Bear:** เพิ่ม Extreme Bear tier เป็น standard practice หลัง MU (CRCL ก็มี $8 tier 15%) — "ทีม underestimate downside เสมอ" กลายเป็น operating assumption
- **Quinn conviction calibration:** conviction 4/10 บน AVOID call ที่มั่นใจทิศทางสูง — เพราะแยก "มั่นใจทิศทาง" ออกจาก "มั่นใจ FV เป๊ะ" อย่างชัดเจน (methodology sensitivity, no beta, short history). Vera ควรจับใน quarterly calibration ว่า low-conviction directional-unanimous AVOID calls แม่นแค่ไหน

---

## 3. Rule Pressure Points

- **Conviction gate 6.5 (Growth) — ติดบ่อยมาก:** VRT, SHOP, TLS (5.83), MU (6.0), CRCL (5.67) — single-gate หรือ dual-gate failure ที่ conviction เป็นตัว fail. Growth-bucket candidates ส่วนใหญ่ในไตรมาสนี้ conviction 5.7–6.3 → log ไว้รอ 4Q review (ยังไม่ถึง trigger — ต้อง rolling 8Q alpha < 0)
- **Blended FV weight 40/30/30 — fabrication risk:** SHOP Error #8 (40/35/25 อ้าง IPS ที่ไม่มีจริง) → CRCL report ปฏิเสธ 40/35/25 อย่างชัดเจนใน Behind the Scenes + Morgan cross-check CLAUDE.md สด. Pattern prevention ทำงาน
- **"Max Consultation Rule" ที่อ้างในรายงานแต่ไม่มีใน CLAUDE.md** — NOW 2026-08-24 flag (Error #9) ยังเป็น open question สำหรับ CIO ว่าจะ formalize หรือไม่. CRCL ไม่มี position → ไม่เกี่ยว

---

## 4. CIO Override Events

ไม่มีในเดือนนี้ — CIO ให้ทีม autonomy เต็ม (นั่งดูวิเคราะห์). ทุก AVOID/HOLD call เป็น team decision

---

## 5. Open Questions

1. **rate-cycle / commodity-cycle peak plays จะมาบ่อยแค่ไหน** ถ้าตลาดยัง RISK-ON + new highs? ทีมควรมี checklist มาตรฐานสำหรับ "cyclical/rate-sensitive earnings ที่ยอด cycle" หรือไม่ (คล้าย ROIC Negative Equity Distortion checklist)?
2. **CRCL Arc Mainnet (16 ก.ย. 2026)** — non-reserve revenue traction จะพลิก thesis ได้จริงไหม? ต้องติดตาม Q4 2026 / Q1 2027 prints (Bull Flip #3: run-rate > $400M annualized ภายใน 12 เดือน)
3. **Quinn's low-conviction directional AVOID calls** — win rate เท่าไหร่? (MU/CRCL ยังต้องรอผลจริง) — Vera quarterly ควรแยก track
4. **Street PT vs internal Blended FV divergence สุดขั้ว** — CRCL Street ~$103–119 vs internal $26 (4–4.6×). Re-Analysis Trigger #5 (Street PT ห่าง ≥25%) จะยิงทันทีถ้า CRCL กลายเป็น position — แต่ตอนนี้เป็น watchlist only

---
*Leo — 2026-08-28 | Monthly Lessons สิงหาคม 2026 (สร้างพร้อม CRCL close-out; sessions เดือนนี้: TDG, VEEV v2, SHOP, TLS, NOW v2, MU, CRCL)*
