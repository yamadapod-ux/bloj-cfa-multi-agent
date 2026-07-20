---
description: Push ผลการวิเคราะห์ล่าสุดขึ้น Dashboard (data.js) + Life OS Inbox แล้ว git push. เรียกเปล่า = auto-detect entry ล่าสุด หรือระบุ "/sync TICKER DATE" เพื่อ specific entry
---

## งาน: Sync Dashboard + Life OS

**Arguments:** $ARGUMENTS

---

### Step 1 — หา Target Entry

**ถ้า `$ARGUMENTS` มีค่า** (เช่น "NVDA 2026-05-14"):
- แยก TICKER = คำแรก, DATE = คำที่สอง

**ถ้าไม่มี arguments** → auto-detect:
- Read `portfolio/decisions.md`
- หา row ล่าสุดในตาราง (วันที่ใหม่สุด / บรรทัดล่างสุด)

ดึงข้อมูลที่ต้องใช้:
```
TICKER        = ___
DATE          = ___
RECOMMENDATION = BUY / HOLD / AVOID / WAIT
CONVICTION    = ตัวเลข (เช่น 7.5)
KEY_THESIS    = สรุป thesis 1 ประโยค
```

---

### Step 2 — ตรวจและอัปเดต Dashboard

Read `dashboard/data.js`

ตรวจว่ามี object ที่มี `ticker: "TICKER"` และ `date: "DATE"` อยู่แล้วหรือไม่

**กรณี: ยังไม่มี entry นี้ใน dashboard:**
1. Read `reports/TICKER_DATE.md` (full report content)
2. เพิ่ม object ใหม่เข้าไปใน `REPORTS` array ด้านในตาม format:
   ```javascript
   {
     ticker: "TICKER",
     company: "Company Name",
     date: "DATE",
     sector: "...",
     price: 0.00,
     recommendation: "...",
     blendedFV: 0.00,
     targetBull: 0.00,
     targetBase: 0.00,
     stopLoss: 0.00,
     convictionEmma: 0,
     convictionQuinn: 0,
     convictionBear: 0,
     convictionAvg: 0.0,
     pwEV: 0.00,
     beta: 0.00,
     sharpe1Y: 0.00,
     maxDrawdown: 0.00,
     moat: "...",
     esgRating: "...",
     esgScore: 0.0,
     keyThesis: "...",
     topRisk: "...",
     entryZone: "...",
     positionSize: "...",
     bullFlipTriggers: ["...", "...", "..."],
     bearFlipTriggers: ["...", "...", "..."],
     thesisInvalidation: "...",
     reportFile: "../reports/TICKER_DATE.md",
     fullContent: `[full markdown จาก report file — escape backticks เป็น \` และ ${ เป็น \${]`
   }
   ```
3. อัปเดต `LAST_UPDATED` ที่ด้านบนไฟล์เป็น TODAY
4. Write กลับลง `dashboard/data.js`

**กรณี: มีแล้ว:**
- ข้ามขั้นนี้ ✅ dashboard up-to-date แล้ว

---

### Step 3 — Push to Life OS Inbox

รัน push script:
```bash
python "C:/Users/user/Desktop/life-os/push_to_inbox.py" TICKER DATE RECOMMENDATION CONVICTION "KEY_THESIS"
```

รอ output ยืนยัน `✅ Added TICKER_DATE to inbox.json`

---

### Step 4 — Git Push

```bash
git -C "C:/Users/user/Desktop/life-os" add inbox.json && git -C "C:/Users/user/Desktop/life-os" commit -m "inbox: TICKER report พร้อมแล้ว DATE" && git -C "C:/Users/user/Desktop/life-os" push origin main
```

---

### Step 5 — รายงาน CIO

```
✅ Sync เสร็จแล้ว — [TICKER] [DATE]

📊 Dashboard : [updated ใหม่ / already up-to-date]
📥 Life OS   : ✅ pushed to inbox.json
🐙 GitHub    : ✅ synced to main

[RECOMMENDATION] · Conviction [CONVICTION]/10
[KEY_THESIS สั้นๆ]
```
