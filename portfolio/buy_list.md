# 🎯 Buy List — Pre-Analyzed Entry Zones

*สร้าง 2026-09-01 (Charlie Strategic Note response) | ดูแลโดย Charlie + Max*

**จุดประสงค์:** ชื่อที่**วิเคราะห์เต็ม pipeline แล้ว** + มี Blended FV + entry zone ที่คำนวณไว้ — พอตลาดย่อ / regime flip / catalyst ยิง เรา deploy ได้ใน **1 สัปดาห์** ไม่ต้องวิเคราะห์จากศูนย์

**กฎ:**
1. เข้า list นี้ได้เฉพาะ ticker ที่ผ่าน full pipeline (มี `reports/TICKER_*.md`) — ไม่ใช่ scout candidate ดิบ
2. ทุก entry ต้องมี: Blended FV (+ วันที่ verify), entry zone (price range), stop, ≥2 Bull Flip Triggers ที่วัดได้, re-check date
3. **ราคาปัจจุบัน + gap-to-entry** = Max อัปเดตทุก Portfolio Review (Mode 3) — ห้าม stale เกิน 2 สัปดาห์
4. เมื่อราคาแตะ entry zone **และ** Bull Flip Trigger ≥1 ยิง **และ** Regime อนุญาต (RISK-ON, หรือ TC + risk-side ok) → Max ping Charlie → fast-track (Emma lightweight FV re-verify → Max×Charlie consult → deploy)
5. FV เก่าเกิน 90 วัน หรือ ผ่าน earnings ใหม่ → ต้อง Emma re-verify ก่อน deploy (Re-Analysis Trigger Rule)
6. ออกจาก list: กลายเป็น position / thesis dead (MOS < −30% ที่ FV ใหม่) / Bear Flip ยิง → ย้ายไป watchlist Archive

---

## Active — รอ pullback / catalyst

| Ticker | Bucket | Last Analysis | Blended FV (raw / ESG-adj) | Entry Zone (mid) | Stop | Price (asof) | Gap to entry | Bull Flip Triggers (ย่อ) | Re-check |
|--------|--------|---------------|---------------------------|------------------|------|--------------|--------------|--------------------------|----------|
| **ADI** | Value | 2026-08-29 | $229 / $218 | **$185–205** ($195) | $156 | $361.78 (8/28) | **−46%** (ต้องย่อลึก) | China MOFCOM ruling ~13 ก.ย. ไม่มี duty / Fed จบ hiking + 10Y <4.0% / 2Q distributor POS growth ≥ shipment / ราคา ≤$210 | MOFCOM 13 ก.ย. + Sept FOMC + Q4 FY26 (~พ.ย.) |
| **GCT** | Growth | 2026-08-30 | $57.02 / $53.03 | **$44–48** ($46) | $37 | $52.95 (8/28) | **−13%** | ราคา ≤$46 + thesis intact / Q3 2026 OCF-NI conversion ฟื้น + AR คงที่ / conviction lift ≥6.5 / ไม่มี short report #3 / KPI third-party audit | Q3 2026 earnings (~ต้น พ.ย.) |
| **MELI** | Growth | 2026-08-29 | $1,207 / $1,085 | **$1,050–1,300** ($1,175) | $940 | $1,966.25 (8/28) | **−40%** (ต้องย่อลึก) | ราคา ≤$1,450 / 2Q op-margin recovery + Brazil credit NPL คงที่ / ads revenue disclosure เริ่ม break out | Q2 CY2026 earnings + ads disclosure |
| **ZETA** | Growth | 2026-09-01 | $19.16 / $17.53 | **$17–20** ($18.50) | $14.80 | $30.88 (8/31) | **−40%** (ต้องย่อลึก) | Davoodi settle ≤$75M + no knowing-misrep docs / GAAP op margin >10% 2Q + organic ≥25% / SBC <9% rev + share count flat / gross margin ≥62% + Regime RISK-ON | Sept FOMC + Q3 2026 earnings + Davoodi discovery Q4 |
| **CHYM** | Growth | 2026-08-31 | $22.30 / $21.07 | **$18–21** ($19.50) | $15.60 | $33.20 (8/28) | **−41%** (ต้องย่อลึก) | ราคา ≤$21 / 8th Circuit Reg II resolution ไม่กระทบ Durbin exemption / GAAP op margin ≥20% sustained 2Q / ARPAM growth re-accel ≥+12% YoY | 8th Circuit Reg II ruling + Q3 2026 earnings + Sept FOMC |
| **OSCR** | Growth | 2026-09-01 | $21.10 / $19.20 | **$16–19** ($17.50) | $14.00 | $29.96 (8/31) | **−42%** (ต้องย่อลึก) | multi-yr (≥3yr) clean ePTC extension signed / 2027 membership decline ≤5% YoY / ราคา ≤$18–20 / Sept 16 Investor Day op margin ≥5.0% + H2 MLR ≤82% | Oscar Investor Day 16 ก.ย. + Sept FOMC + ACA legislation ก่อน Nov 1 |

> **หมายเหตุ:** 4/6 (ADI/MELI/ZETA/CHYM/OSCR) ต้องย่อ −40%+ ถึงเข้า entry — realistic เฉพาะใน bear market. **GCT (−13%) + potentially ADI on China ruling** = ใกล้ที่สุด. ถ้าตลาด correction −15–20% (มา ~1 ครั้ง/4–6 ปี) → ZETA/CHYM/OSCR เข้า range พร้อมกัน

---

## Pending — ยังไม่ full pipeline (จาก watchlist, รอ post-FOMC scout Round 27)

*(ว่าง — จะเติมหลัง Scout Round 27 mandate ใหม่: de-rated sectors managed care / beaten healthcare / energy / rate-sensitive, filter ≥−30% จาก 52W high)*

Candidate ที่น่าสนใจจาก analyses ที่ผ่านมา (peers ที่โดนทุบพร้อมกัน — ยังไม่วิเคราะห์เต็ม):
- **CNC** (Centene) — #1 ACA via Ambetter, ~$160B revenue, TTM net loss −2.83% (MLR blowout), P/B <1.0x, historically P/E 10–12x — diversified + ถูกกว่า OSCR
- **MOH** (Molina) — government-focused, long profit track record, net margin ~breakeven, ~$40B revenue
- **CNX** (CNX Resources) — nat gas Appalachia, 25 straight FCF+ quarters, ROIC 16.5%, P/E ~5–6x, AI-data-center power demand — reject Round 26 เพราะ growth อ่อน แต่ value ชัด

---

## Removed / Graduated

| Ticker | Date | เหตุผล |
|--------|------|--------|
| *(none yet)* | | |

---

*Charlie + Max | Last updated: 2026-09-01 (initial build — 6 Active from Aug–Sep 2026 analyses)*
