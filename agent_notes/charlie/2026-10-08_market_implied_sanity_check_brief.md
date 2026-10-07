# Brief for Sonnet — Market-Implied Sanity Check (new rule, `TRIAL`)

*Opus — 2026-10-08 · CIO approved · งานแก้ไฟล์กฎเท่านั้น — ไม่รัน pipeline ไม่แตะ ticker ใดๆ ไม่ย้อนแก้ AMZN*

## ที่มา (สั้น)
CIO เสนอ "Implied Price Move Sanity Check" หลัง AMZN v3.2 (MOS −51%) — ขนาด gap ที่ใหญ่ผิดปกติควรเป็นสัญญาณให้ตรวจโมเดล ไม่ใช่รายงาน MOS เฉยๆ. Opus ปรับ mechanism 3 จุดก่อนลงกฎ:
1. **ไม่ใช้ historical drawdown เป็นเกณฑ์** — MOS ไม่ใช่การพยากรณ์ว่าราคาต้องร่วง (gap ปิดได้ด้วย FV โตขึ้นตามเวลา) และการตัดช่วง 2008/2022 ออกเป็นการเลือกข้อมูล (AMZN เองร่วง 56% ปี 2022). ใช้ **gap-closing assumption test** แทน — ใช้โมเดลเดิม ไม่ต้อง WebSearch เพิ่ม และชี้ตรงไปที่ assumption ที่ "เงียบ" (TGR, terminal margin)
2. **ใช้ทั้งสองทิศ** (|MOS| ≥ 35%) — MOS บวกสูงผิดปกติอันตรายกว่า เพราะนำไปสู่ BUY จริง
3. Threshold 35% เป็น `TRIAL` review 2026-12-31 พร้อม trial อื่น

## งานที่ต้องทำ (targeted Edit เท่านั้น — ห้าม Write ทับทั้งไฟล์)

### 1. `CLAUDE.md` — เพิ่ม section ใหม่ **ระหว่าง** § Multi-Segment / SOTP Consistency Rule กับ § MOS Threshold แยกตาม Bucket (วางก่อนบรรทัด `### MOS Threshold แยกตาม Bucket`) ข้อความตามนี้:

```markdown
### Market-Implied Sanity Check (`TRIAL` — เพิ่ม 2026-10-08, review 2026-12-31, ไม่ใช่ Return-side rule)

**ที่มา:** AMZN v3.2 — Blended FV $125.66 vs ราคา ~$256 (MOS −51%) — CIO ตั้งคำถามว่า gap ขนาดนี้คือ "ตลาดแพงจริง" หรือ "โมเดล conservative เกินจริง" และไม่มีกฎใดบังคับให้แยกสองกรณี · ไม่แตะ MOS threshold / conviction gate / 40-30-30 — เป็นขั้น "ต้องอธิบายให้ผ่าน" ก่อน Morgan QA PASS เท่านั้น (โครงเดียวกับ Multi-Segment ข้อ 5)

**Trigger:** |MOS| ≥ 35% เทียบ Blended FV (ทั้งทิศบวกและลบ) **และ** ไม่มี fraud / going-concern / regulatory-shutdown risk ที่ระบุชัดใน report

**Emma ต้องแสดงตาราง "Gap-Closing Assumption"** — แก้ทีละตัวแปร (ตัวอื่นคงเดิม) แล้วรายงานค่าที่ทำให้ Emma DCF FV = ราคาตลาด:

| ตัวแปร | ค่าที่ใช้ | ค่าที่ปิด gap | ช่วงที่เป็นไปได้ (history / peer / consensus + source) | อยู่ในช่วง? |
|--------|----------|--------------|------------------------------------------------------|-----------|
| TGR | | | | |
| Terminal EBIT/FCF margin | | | | |
| WACC | | | | |
| Revenue CAGR (explicit period) | | | | |

**ตีความ:**
- มีตัวแปรใดปิด gap ได้ **ภายในช่วงที่เป็นไปได้** → โมเดลเปราะต่อตัวแปรนั้น — report ต้องอธิบายว่าทำไมค่าที่ใช้น่าเชื่อกว่าค่าที่ปิด gap (ห้ามอธิบายด้านเดียว — หลักเดียวกับ Multi-Segment ข้อ 3)
- ทุกตัวแปรต้องขยับ **เกินช่วงที่เป็นไปได้** → ยืนยันว่าตลาด mispriced จริง (ทิศลบ = ตลาดแพง · ทิศบวก = ต้องระบุว่าทำไมตลาดถึงพลาด)
- **ไม่เปลี่ยน recommendation อัตโนมัติ** · historical drawdown ใส่เป็น context ได้ แต่ไม่ใช่เกณฑ์ตัดสิน

**Morgan:** เข้า trigger แต่ไม่มีตาราง / ช่วงที่เป็นไปได้ไม่มี source / ตีความขัดกับตาราง = `RULE_VIOLATION`

**Vera (trial review 2026-12-31):** นับจำนวนครั้งที่ trigger, กี่ครั้งที่ "โมเดลเปราะ" vs "ตลาด mispriced", และมีกรณีใดที่ตารางนำไปสู่การแก้ assumption จริง
```

### 2. `.claude/agents/qa.md` — เพิ่ม checklist item ใน § 2.6B Cross-agent Consistency **ต่อจากบล็อก Multi-Segment / SOTP Consistency** (ก่อนบรรทัด `**2.6C — Atlas Macro Integration:**`):

```markdown
- [ ] **Market-Implied Sanity Check** (`TRIAL`, ดู CLAUDE.md § Market-Implied Sanity Check): ถ้า |MOS| ≥ 35% และไม่มี fraud/going-concern/regulatory-shutdown risk → มีตาราง Gap-Closing Assumption (TGR / terminal margin / WACC / revenue CAGR) พร้อมช่วงที่เป็นไปได้ที่มี source และการตีความสอดคล้องกับตาราง — ไม่ครบ = `RULE_VIOLATION`
```

### 3. `.claude/agents/emma.md` — เพิ่มย่อหน้าสั้น **ต่อจากบล็อก Multi-Segment / SOTP Consistency** (บรรทัด ~33 และรายการข้อย่อยที่ตามมา):

```markdown
**Market-Implied Sanity Check (`TRIAL` — เพิ่ม 2026-10-08, ดู CLAUDE.md):** ถ้า |MOS| ≥ 35% (ทิศใดก็ได้) → แสดงตาราง Gap-Closing Assumption: แก้ทีละตัวแปร (TGR, terminal margin, WACC, revenue CAGR) หาค่าที่ทำให้ DCF FV = ราคาตลาด เทียบกับช่วงที่เป็นไปได้ (มี source) — ถ้าตัวแปรใดปิด gap ได้ในช่วงที่เป็นไปได้ ต้องอธิบายว่าทำไมค่าที่ใช้น่าเชื่อกว่า
```

## ห้ามทำ
- ห้ามแก้ MOS threshold, conviction gate, 40/30/30 หรือ Rule Classification Table
- ห้ามย้อนรันกฎนี้กับ AMZN หรือ ticker ที่วิเคราะห์ไปแล้ว (AMZN learning run ปิดที่ v3.2)
- ห้ามแตะ `dashboard/data.js`

## เมื่อเสร็จ
- ตรวจด้วย `grep -n "Market-Implied Sanity Check" CLAUDE.md .claude/agents/qa.md .claude/agents/emma.md` → ต้องเจอทั้ง 3 ไฟล์
- Commit + push อ้าง `market-implied sanity check rule (TRIAL)` · รายงานกลับ: file:line ที่เพิ่ม

*Opus — 2026-10-08 | Market-Implied Sanity Check brief, CIO approved*
