**Prune Pass 2026-11-06 (Mode 1 Step 0 — Round 87):** ตรวจ live Pending ทั้ง 16 แถวตาม De-list Rules #1-3 พร้อมราคาสด 2 แหล่ง (Yahoo = Nasdaq historical ตรงกันทุกตัว, close 11-05). **De-listed 0 · SLA fixed 0** · live 16.
- **Rule #1:** ยังไม่มี target ผ่านกำหนด: **CRI 11-06 (วันนี้)** · IBKR/URI/EME/INDI/ANIP/BKSY/VMD/WYNN/VICI/ALLY/BYD/NBIX 11-07 · CMRE 11-17 · MMS 11-20 · WGO 12-19. คำเตือนเดิมยังอยู่: IBKR/URI/EME (scout 08-29, 69 วัน) ต้อง archive ใน prune แรกหลัง 11-07 ถ้ายังไม่รัน Tier 1.
- **Rule #2:** ไม่มีตัวไหนราคา >2× ขอบบน entry zone (สูงสุด NBIX $159.76 = 1.18× ของ $135 · WGO $33.17 = 1.14× · MMS $69.22 = 1.13× · BYD $77.07 = 1.10×) และไม่มี formal FV/MOS ให้วัด MOS < −30%. IBKR/URI/EME/INDI/ANIP/BKSY/VMD ไม่พบ zone ใน row จึงวัดข้อนี้ไม่ได้.
- **Rule #3:** `decisions.md` = 0 hits ทุก live ticker · grep `deployment_log.md` ไม่พบแถว SKIPPED/AVOID/DEPLOYED ของ live ticker · OPEN ยังเป็น ADBE/NOW/CRM/REGN/ADSK.
- **ธงรอบ 11-07 (ยังไม่ archive):** ไม่ผ่าน Filter A = **URI −13.2%** · **NBIX −14.2%** · **BYD −15.7%** · **ALLY −17.9%** · **VICI −18.2%**. **VMD กลับเข้า A แล้ว (−28.5%)**. **เข้า A แล้ว ควรรัน Tier 1 ก่อนตัดสิน archive = EME −37.5% · IBKR −26.3%.**
- **ราคาแตะ entry zone (ต้องแจ้ง Charlie ตาม Scout → Analysis SLA; regime TC ยังห้าม open ใหม่):** CMRE $12.79 (zone $12.00–13.50) · WYNN $79.32 ($77–85) · VICI $25.21 ($22–26, แต่ไม่ผ่าน A).

