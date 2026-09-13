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

| Ticker | Bucket | Last Analysis | Blended FV (raw / ESG-adj) | Entry Zone (mid) | Stop | Price (asof 2026-09-11 close) | Gap to entry | Bull Flip Triggers (ย่อ) | Re-check |
|--------|--------|---------------|---------------------------|------------------|------|--------------|--------------|--------------------------|----------|
| **GCT** | Growth | 2026-08-30 | $57.02 / $53.03 | **$44–48** ($46) | $37 | $51.87 (Sept 11 close) | **−11%** (ห่างขึ้นจาก −7% — ราคาขึ้นต่อ) | ราคา ≤$46 + thesis intact / Q3 2026 OCF-NI conversion ฟื้น + AR คงที่ / conviction lift ≥6.5 / ไม่มี short report #3 / KPI third-party audit | Q3 2026 earnings (~ต้น พ.ย.) |
| **ADI** | Value | 2026-08-29 | $229 / $218 | **$185–205** ($195) | $156 | $378.78 (Sept 11 close, +4.85% day) | **−49%** (ห่างขึ้นจาก −46% — rally วันนี้, MOFCOM ruling ~13 ก.ย. ยังไม่ออกผล) | China MOFCOM ruling ~13 ก.ย. ไม่มี duty / Fed จบ hiking + 10Y <4.0% / 2Q distributor POS growth ≥ shipment / ราคา ≤$210 | MOFCOM ~13 ก.ย. + Sept FOMC + Q4 FY26 (~พ.ย.) |
| **FSLR** | Value | 2026-09-03 | $155.29 / n/a | **$125–135** ($130) | $104 | $209.03 (Sept 11 close) | **−38%** (แคบลงเล็กน้อยจาก −39%) | Book-to-bill ≥1.0x 2Q ติด / Section 301/122 litigation ชนะหรือ codify / ราคา ≤$135 (MOS≥15%) / gross margin ≥50% sustained 2Q / FY2027 growth guide ≥5% | Q3 2026 earnings (~ต.ค./พ.ย.) + CIT litigation ruling |
| **ZETA** | Growth | 2026-09-01 | $19.16 / $17.53 | **$17–20** ($18.50) | $14.80 | $30.18 (Sept 11 close) | **−39%** (แคบลงเล็กน้อยจาก −41%) | Davoodi settle ≤$75M + no knowing-misrep docs / GAAP op margin >10% 2Q + organic ≥25% / SBC <9% rev + share count flat / gross margin ≥62% + Regime RISK-ON | Sept FOMC + Q3 2026 earnings + Davoodi discovery Q4 |
| **MELI** | Growth | 2026-08-29 | $1,207 / $1,085 | **$1,050–1,300** ($1,175) | $940 | $1,897.37 (Sept 11 close) | **−38%** (แคบลงเล็กน้อยจาก −41%) | ราคา ≤$1,450 / 2Q op-margin recovery + Brazil credit NPL คงที่ / ads revenue disclosure เริ่ม break out | Q2 CY2026 earnings + ads disclosure |
| **CHYM** | Growth | 2026-08-31 | $22.30 / $21.07 | **$18–21** ($19.50) | $15.60 | $33.00 (Sept 11 close) | **−41%** (แคบลงจาก −45%) | ราคา ≤$21 / 8th Circuit Reg II resolution ไม่กระทบ Durbin exemption / GAAP op margin ≥20% sustained 2Q / ARPAM growth re-accel ≥+12% YoY | 8th Circuit Reg II ruling + Q3 2026 earnings + Sept FOMC |
| **OSCR** | Growth | 2026-09-01 | $21.10 / $19.20 | **$16–19** ($17.50) | $14.00 | $32.77 (Sept 11 close) | **−47%** (flat) | multi-yr (≥3yr) clean ePTC extension signed / 2027 membership decline ≤5% YoY / ราคา ≤$18–20 / Sept 16 Investor Day op margin ≥5.0% + H2 MLR ≤82% | Oscar Investor Day 16 ก.ย. + Sept FOMC + ACA legislation ก่อน Nov 1 |
| **QCOM** | Value | 2026-09-05 | $111.59 / $106.01 | **$85–97** ($91) | $73 | $181.97 (Sept 11 close, +2.88% day) | **−50%** (gap ใหญ่สุด, ห่างขึ้นจาก −47%) | Beta mean-revert ≤1.50 2Q ติด / BMW-VW LOI→signed contract ≥$2B/yr / Sept 2026 US-China summit truce ต่ออายุ 12mo+ / QCT Handset decline ชะลอเหลือ single-digit YoY 2Q / ราคา ≤$85–97 | Sept 2026 US-China summit + Q4 FY2026 earnings (~พ.ย. 2026) |
| **ACN** | Value | 2026-09-11 (Full Exit — ex-position) | $199.51 / $185.50 | **$150–170** ($160) | n/a (former position stop $148) | $183.90 (Sept 11 close, +3.37% day) | **−8% to −18%** (ห่างขึ้นจาก −4%/−16% — post-exit rally) | Q4 FY26 (10/1) organic rev ≥+4% LC 2Q ติด / bookings YoY ≥flat + book-to-bill >1.05 2Q ติด / GenAI bookings run-rate ≥$10B/yr / FY27 guide ≥+6% LC + FCF ≥$12B / EBIT margin ≥17% ต่อเนื่อง 2Q พร้อม revenue reaccel | Q4 FY26 earnings (~ปลาย ก.ย./ต.ค. 2026) — decision point เดิม |

> **หมายเหตุ (2026-09-13 refresh, Portfolio Review Mode 3):** ตลาด rally แรงวันที่ 11 ก.ย. (ADI +4.85%, QCOM +2.88%, ACN +3.37%) ทำให้ gap ของ ADI/QCOM/ACN **ห่างขึ้น** ขณะที่ FSLR/ZETA/MELI/CHYM **แคบลงเล็กน้อย** และ GCT ยังคงห่างขึ้นต่อเนื่อง (−7%→−11%) เพราะราคาวิ่งขึ้นไม่หยุด GCT ยังเป็นตัวใกล้ entry ที่สุดในกลุ่ม (−11%) — GCT range $25.15–$56.27, ราคา $51.87. ถ้าย่อถึง ~$46 + Q3 2026 (~ต้น พ.ย.) ยืนยัน OCF-NI conversion ฟื้น + conviction lift ≥6.5 → deploy candidate ตัวแรก. **8/9 ตัวที่เหลือ (ADI/FSLR/ZETA/MELI/CHYM/OSCR/QCOM/ACN) ต้องย่อ −38% ถึง −50%** — realistic เฉพาะใน correction −15–20% (มา ~1 ครั้ง/4–6 ปี) หรือ thesis-specific catalyst (ACN Q4 FY26 earnings). **Regime TRANSITIONAL-CAUTIOUS → Force Deploy SUSPENDED** — แม้ราคาแตะ entry zone ก็ยัง**ห้าม deploy ใหม่**จนกว่า Atlas re-call RISK-ON (post-FOMC 2026-09-16) รายการนี้เป็นแค่ fast-track prep เท่านั้น. **FV ages (asof 2026-09-13):** ADI/MELI/ZETA/CHYM/OSCR/GCT = 14–15 วัน · FSLR = 10 วัน · QCOM = 8 วัน · ACN = 2 วัน — ยังไม่มีตัวไหนเกิน 90 วัน (ไม่ต้อง forced re-verify) แต่ GCT ใกล้ entry → Emma lightweight FV re-verify จะ trigger ก่อน deploy ถ้าราคาแตะ $46.

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

*Charlie + Max | Last updated: 2026-09-13 (Portfolio Review Mode 3 — ราคาทุกตัวรีเฟรชจาก Sept 11 2026 close. GCT ยังคงใกล้ entry ที่สุดในกลุ่ม (−11%, ห่างขึ้นจาก −7% เพราะราคายังวิ่งขึ้น) ตามด้วย ACN (−8% to −18%, ห่างขึ้นจาก −4%/−16% หลัง post-exit rally +3.37%) — ACN เป็น re-entry ที่ต้อง thesis rebuild (conviction เพิ่งร่วง 7.17→5.17) ไม่ใช่แค่ price-only. Regime TC → Force Deploy SUSPENDED, ทุกตัวยังรอ regime กลับ RISK-ON ก่อน deploy ได้จริง.) — 9 Active*

**Note (2026-09-09):** APTV (2026-09-06, dual-gate FAIL) และ LKQ (2026-09-08, single-gate FAIL conviction) — full analysis เสร็จแล้วทั้งคู่ แต่ **ไม่เพิ่มเข้า buy_list** (APTV: forward return ~5.9% CAGR ที่ entry zone ต่ำเกิน; LKQ: Bear objection — entry zone แคบ = false green-light) → track เป็น WATCH item ใน decisions.md + Bull Flip Triggers แทน. CNC (2026-09-04, AVOID) ก็ไม่เข้า (forward return ต่ำ).
