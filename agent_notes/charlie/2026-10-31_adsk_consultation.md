# ADSK — Max × Charlie Consultation (2026-10-31)

**ที่มา:** MOS ≤ 0% (STRONG SELL ตาม Exit Rules, max.md) ค้างมา 20 รอบ Review Mode (10-07 → 10-31) โดยไม่เคยทำ consultation จริง — CIO สั่งปิดเรื่องนี้วันนี้ (CIO authorize Max autonomy, CIO observing)

## 1. ข้อเท็จจริง (verified 2026-10-31)

| รายการ | ค่า | Source |
|---|---|---|
| ราคา Oct 30 2026 close | **$249.61** | [stockanalysis.com history](https://stockanalysis.com/stocks/adsk/history/) + [financialcontent.com](https://www.financialcontent.com/quote/NQ:ADSK/historical) — exact match |
| Blended FV (v1, ก่อน VS2) | $221.79 (fvVerifiedDate 2026-09-12, 49 วัน) | reports/ADSK_2026-06-09.md |
| MOS | (221.79 − 249.61) / 221.79 = **−12.54%** | คำนวณ |
| Street PT | median **$302.50** / avg $307.54 / low $215 / high $375 (36 analysts, updated Oct 23 2026) | [stockanalysis.com forecast](https://stockanalysis.com/stocks/adsk/forecast/) |
| Street PT (2nd) | avg ~$316.84 (32 analysts) | MarketBeat ผ่าน [WebSearch aggregate](https://www.marketbeat.com/stocks/nasdaq/adsk/price-target) |
| Analyst action ล่าสุด | BofA Buy $300 (10-23), Citi Hold $276 (10-06), Piper $338→$300 (9-28) | stockanalysis.com (TipRanks feed) |
| Q3 FY27 earnings | ~Nov 24–26 2026 (ยังไม่ confirm) | [earningswhispers](https://earningswhispers.com/stocks/ADSK), [marketscreener calendar](https://www.marketscreener.com/quote/stock/AUTODESK-INC-40246776/calendar/) |
| Weight / stopDist | ~5.8% / 36.4% | portfolio.js |

## 2. Bear Flip Triggers (5) — สถานะ 2026-10-31

| # | Trigger | สถานะ | เหตุผล |
|---|---|---|---|
| 1 | Current RPO < 8% YoY ใน Q3 FY27 | ไม่ยิง (ยังไม่มีข้อมูล) | print ~Nov 24–26 |
| 2 | Revenue growth < 12% 2 ไตรมาสติด | ไม่ยิง | Q2 FY27 beat, Q3 guide $2.125–2.140B |
| 3 | Institutional holder ลดผิดปกติ | ไม่ยิง | ไม่พบข้อมูลใหม่ |
| 4 | AI BIM/CAD ฟรี adopt >15% share | ไม่ยิง | ไม่พบ |
| 5 | NRR < 100% | ไม่ยิง (data gap) | ไม่เปิดเผย |

## 3. Thesis Invalidation (5) — สถานะ

| # | Criterion | สถานะ |
|---|---|---|
| 1 | Churn spike > 5% | ไม่ยิง |
| 2 | EU Open BIM mandate > 30% revenue | ไม่ยิง |
| 3 | AI tool ถูก adopt เป็น primary workflow | ไม่ยิง |
| 4 | Scandal / accounting / hostile M&A | ไม่ยิง |
| 5 | Current RPO ติดลบ 2 ไตรมาส | ไม่ยิง |

**รวม: Bear Flip 0/5 · Thesis Invalidation 0/5** (ตรงกับที่เช็คไว้ 10-23)

## 4. ข้อค้นพบใหม่ที่ 20 รอบก่อนพลาด — Re-Analysis Trigger #5 ยิงอยู่แล้ว

Street PT median $302.50 สูงกว่า Blended FV $221.79 **+36.4%** (เกณฑ์ ≥25%) — แม้แต่ Street PT ต่ำสุด ($215) ยังใกล้ FV ของเรา. รูปแบบเดียวกับ AMZN v3.2 (FV ต่ำกว่า Street low) ที่เป็นต้นเหตุของ VS2. FV $221.79 เป็น v1 (ก่อน VS2: ไม่มี WACC 2-method / external cross-check / fade) — ตาม CLAUDE.md "ถ้า position เข้าเงื่อนไข trigger ข้อใด → flag ก่อนเสนอ sell/trim ใดๆ บน FV ที่อาจ stale"

Process gap: Review Mode 20 รอบรายงาน "0/5 formal triggers" ทั้งที่ #5 ยิง — Max ไม่ได้ดึง Street PT มาเทียบ. บันทึกเป็น lesson.

## 5. ทางเลือก

**(A) HOLD-WATCH จนถึง Q3 FY27 + pre-commit กฎตัดสิน**
- ข้อดี: ไม่ขายบน FV ที่ trigger #5 บอกว่าอาจ stale; print cRPO (ตัวชี้ขาดตาม Bull #1 / Bear #1) อีก ~3.5 สัปดาห์; earnings จะยิง Trigger #1 บังคับ re-verify อยู่แล้ว — re-verify ตอนนี้ไม่มีข้อมูลธุรกิจใหม่ ได้แค่ methodology update; ต้นทุนรอ: weight 5.8%, stopDist 36%
- ข้อเสีย: ถ้า FV v1 ถูก การถือ 3.5 สัปดาห์ที่ MOS −12.5% มี expected return ต่ำกว่า cash (3.8%/ปี ≈ +0.25% ในช่วงนี้) — ต้นทุนเล็ก

**(B) TRIM 30% ตอนนี้ (~0.72sh ≈ $180)**
- ข้อดี: สอดคล้องกับ precedent REGN 2026-08-23 (MOS −5.31% deepening → trim 30%)
- ข้อเสีย: precedent นั้นเองพิสูจน์ว่า trim บน stale FV เสียของ — REGN FV re-verify ขึ้น $792→$889 และราคาตอนนี้ $927.89 (+11% เหนือราคาที่ trim $834.04). ADSK อยู่ในสภาพเดียวกัน (trigger #5 ยิง + FV v1)

## 6. ความเห็น Charlie

เห็นด้วยกับ (A) แต่ **ต้องไม่ให้เป็นการเลื่อนครั้งที่ 21** — ต้องมีวันตัดสินที่ล็อกไว้และกฎที่ไม่มีข้อยกเว้น. MOS −12.5% ที่ลึกขึ้นเป็นสัญญาณจริงที่ไม่ควรเพิกเฉย แต่สัญญาณนั้นวัดจาก FV ที่มีเหตุผลเชื่อได้ว่าต่ำเกิน — การขายบนตัวเลขนั้นคือการทำซ้ำความผิดพลาด REGN ส.ค.

## 7. การตัดสินใจของ Max (final) — **(A) HOLD-WATCH, time-boxed, pre-committed**

ไม่มี trade วันนี้. กฎล็อกล่วงหน้า (เขียนก่อนรู้ผล):
1. Q3 FY27 print (~Nov 24–26) → Emma re-verify FV แบบ **VS2** ภายใน Review รอบถัดไปหลัง print (Trigger #1)
2. ถ้า current RPO < 8% YoY (Bear Flip #1) → **SELL เต็ม** (Bear Flip = downgrade to SELL)
3. ถ้า current RPO ติดลบ YoY → Thesis Invalidation path (Risk Rule 3)
4. ถ้า VS2 FV ใหม่ยังให้ MOS ≤ 0% → **TRIM 50% ทันทีในรอบนั้น** — ไม่ได้รับข้อยกเว้นซ้ำ ไม่ re-analyze วนอีก
5. ถ้า VS2 MOS > 0% และ cRPO ≥ 10% → HOLD ต่อ, ปิด STRONG SELL item
6. Hard deadline: ถ้า **2026-12-05** ยังไม่มี VS2 re-verify (เช่น print เลื่อน) → ใช้ข้อ 4 บน FV ที่มีอยู่
7. ระหว่างรอ: Review Mode รายงานสถานะ "HOLD-WATCH (consulted 10-31, decision gate Q3 FY27)" — ไม่นับเป็น unresolved consultation อีก

*Charlie × Max — 2026-10-31 | ADSK Consultation*
