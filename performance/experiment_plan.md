# Experiment Plan — AI แทนคนได้ในจุดไหน (WP-E)

*เขียนก่อนเริ่มเก็บข้อมูลตาม E0 · Owner: Vera (scorecard) / Hermes (infra) · ทบทวนครั้งแรก 2026-12-31 จากนั้นทุกไตรมาส*

กองทุนนี้เป็นพอร์ตจำลอง $10K (ไม่มีเงินจริง) เริ่ม 2026-05-09 เพื่อทดลองว่า AI (ทีม 9 agent) แทนคนได้ในจุดไหนของกระบวนการลงทุน — แบ่งเป็น 6 ขั้น: scout · วิเคราะห์ · QA · ตัดสินใจ · ลงมือและคุมความเสี่ยง · เรียนรู้

## E0 — สมมติฐานและเกณฑ์ผ่าน

| # | สมมติฐาน | ขั้นตอนที่เกี่ยวข้อง | เกณฑ์ผ่าน |
|---|---|---|---|
| H1 | FV ของทีมคลาดจากราคาจริงที่ 12 เดือน **น้อยกว่า** Street consensus PT ณ วันเดียวกัน | วิเคราะห์ | \|Team FV − realized price\| < \|Street PT median − realized price\| เฉลี่ยทุกตัวที่ครบ 12 เดือน |
| H2 | กลุ่ม conviction สูง ได้ผลตอบแทนจริงดีกว่ากลุ่ม conviction ต่ำ | ตัดสินใจ | Win rate + avg return ของ conviction ≥7.0 (Value) / ≥6.5 (Growth) สูงกว่ากลุ่มต่ำกว่า gate อย่างมีนัยสำคัญ (ดู Conviction Calibration Table ใน quarterly report) |
| H3 | หลัง WP3 (ledger ต่อเข้า cron) trigger ความเสี่ยงอย่างน้อย 90% ถูกปิดภายใน SLA โดยไม่มีคนสั่ง | ลงมือ/คุมความเสี่ยง | % ของ ledger item ประเภท stop_loss/consultation/regime_recall/qa_reanalysis ที่ปิดภายใน SLA ของตัวเอง (ดู `portfolio/actions.json sla_days`) โดยไม่มี CIO สั่งเอง ≥90% |
| H4 | หุ้นที่ pipeline เต็มอนุมัติ ชนะตะกร้า screen-only (E5) | วิเคราะห์ + QA | ผลตอบแทนถ่วงน้ำหนักเท่ากันของตะกร้า pipeline-approved > ตะกร้า screen-only (A–C ผ่านแต่ไม่ fast-track) ที่ 6/12 เดือน |
| H5 | ผลตอบแทนพอร์ตชนะกองทุน active ที่คนบริหาร (E3) | ทั้งระบบ | Alpha ของพอร์ตจำลอง vs กองทุนที่เลือกใน E3 เป็นบวก ที่ rolling 4Q/8Q เดียวกับ Pre-commitment Rule |

ทบทวนครั้งแรก **2026-12-31** จากนั้นทุกไตรมาสคู่กับ Vera Quarterly Output

## E1 — บันทึกทุกครั้งที่คนเข้ามาช่วย

**กระบวนการ (มีผลตั้งแต่วันนี้เป็นต้นไป ไม่ backfill ประวัติเก่า):**
- ทุกคำสั่ง/การตัดสิน/การแก้กฎ/การแก้ข้อมูล/การ override จาก CIO → บันทึกด้วย:
  `node scripts/actions.js add --type intervention --title "<สั้นๆ>" --owner CIO --evidence "<อ้างอิง>"` แล้ว `close --id <ID> --note "<รายละเอียด model ที่ตัดสิน>"` ทันทีถ้าจบในรอบเดียว (ไม่ใช่งานค้าง)
- เพิ่ม `type: 'intervention'` ใน `VALID_TYPES` ของ `scripts/actions.js` แล้ว (ทดสอบ `--dry-run` ผ่าน — ดู improvement_log)
- ทุก decision record ที่เกิดจาก intervention ต้องระบุว่า **model ไหนเป็นคนตัดสิน** (Hermes / Claude Code agent ตัวไหน / CIO เอง) — ตามที่แผนกำหนด

## E2 — เวอร์ชันกฎ (RULESET)

- ตั้งใจใส่ `> **RULESET 2026-11-24**` ไว้บรรทัดบนสุดของ `CLAUDE.md` ต่อจาก H1 title — **บล็อกจาก cron session:** `CLAUDE.md` เป็น protected agent-instruction file ต้องมี interactive user/gateway approve การเขียน ซึ่ง cron run นี้ไม่มี (ลองแก้แล้วได้ error `BLOCKED: ... requires approval but no interactive user or gateway is present`)
- **Action ค้าง:** รอ CIO หรือ Opus ทำการแก้ 1 บรรทัดนี้เองในเซสชันที่มี interactive approval (ไม่ใช่ cron) — เนื้อหาบรรทัดที่ต้องเพิ่มอยู่ด้านบนนี้แล้ว พร้อม copy-paste ได้เลย
- เหตุผลที่ reference วันที่ 2026-11-24: เป็นวันที่ D1–D4 + Tiered Sizing (Option B) ถูกอนุมัติล่าสุด ถือเป็นจุดเริ่ม ruleset version ปัจจุบัน
- ตั้งแต่มีบรรทัดนี้แล้ว: ทุก decision record (`portfolio/decisions.md`) และทุกแถวใน `portfolio/deployment_log.md` ต้องระบุเลขเวอร์ชันนี้ไปด้วย — เปลี่ยนกฎได้เฉพาะวันทบทวน (ทุกไตรมาส) ยกเว้นแก้กฎที่ขัดกันเองหรือเขียนผิด

## E3 — Benchmark 3 ชั้น (เทียบกับมืออาชีพ ไม่ใช้ CIO เป็นตัวเทียบ)

| ชั้น | Benchmark | แทนอะไร | สถานะ |
|---|---|---|---|
| 1 | S&P 500 | การลงทุนแบบไม่ต้องวิเคราะห์ | มีอยู่แล้ว (`performance/tracker.md`, `dashboard/portfolio.js`) |
| 2 | Street consensus PT + rating (Buy/Hold/Sell) ณ วันวิเคราะห์ | นักวิเคราะห์มืออาชีพระดับหุ้นรายตัว | ทีมเก็บ PT อยู่แล้วในหลายรายงาน — **เพิ่มใหม่ตั้งแต่วันนี้:** ทุกรายงาน/re-analysis ต้องบันทึก consensus **rating** (Buy/Hold/Sell, ≥2 sources) คู่กับ PT ที่มีอยู่แล้ว ใส่ใน Research Report Format (📌 ข้อมูลหลัก หรือ ⚙️ Behind the Scenes) — มีผลตั้งแต่รายงานถัดไป ไม่ backfill 58 รายงานเก่า |
| 3 | **Fidelity Contrafund (FCNTX)** | ผู้จัดการกองทุนมืออาชีพระดับพอร์ต (คนบริหาร, หุ้นสหรัฐสาย growth, มี NAV รายวัน) | **ล็อกแล้ว** — เหตุผลเลือก ดูด้านล่าง |

### เหตุผลเลือก FCNTX (ล็อกก่อนเริ่มเทียบ ตามที่แผนกำหนด)
- Morningstar Category: **Large Growth** — ตรงกับ mandate "US stocks growth-tilted" ของกองทุนจำลอง
- คนบริหารจริง (co-portfolio managers: William Danoff since 1990, Asher Anolic + Jason Weiner since 2025) — ไม่ใช่ index fund, ไม่ใช่ quant/systematic fund — ตรงเกณฑ์ "มีคนบริหาร"
- Daily NAV, no transaction fee, เปิดซื้อขายทุกวันที่ NYSE เปิด — เทียบ alpha รายวัน/รายสัปดาห์ได้เหมือน S&P 500
- Benchmark ภายในของตัวเองคือ S&P 500 — เทียบ 3 ทาง (เรา vs FCNTX vs S&P 500) ได้โดยไม่ซ้อนทับ
- Source: fundresearch.fidelity.com/mutual-funds/summary/316071109 (ตรวจ 2026-11-26), institutional.fidelity.com fact sheet Sep 30 2026
- **ข้อควรระวัง:** William Danoff (manager หลักตั้งแต่ 1990) ประกาศเกษียณมีผล ~31 ธ.ค. 2026 — ถ้าการเปลี่ยนผู้จัดการกระทบ style/performance อย่างมีนัยสำคัญ ให้ Vera ตั้ง flag ใน quarterly report ไม่ต้องเปลี่ยน benchmark (เป็น real-world event ที่ fund จริงต้องเจอเหมือนกัน)
- **เริ่มเทียบจาก 2026-05-09** (วันเริ่มกองทุนจำลอง) — NAV ของ FCNTX วันที่ใกล้เคียงที่สุด (เช่น นัดซื้อขายวันที่ NYSE เปิดใกล้ 5/9 ที่สุด) ให้ Vera ดึงตอนทำ E7 scorecard ฉบับแรก (ยังไม่ดึงในรอบนี้ เพื่อประหยัด token — ล็อกแค่ตัวกองทุนก่อน)

## หมายเหตุ

- E4–E7 ยังไม่เริ่ม (อยู่หลัง Checkpoint A/B/D ตามลำดับใหม่ใน `คุยกับ hermes - แผนปรับปรุง.md`)
- เอกสารนี้คือ E0 + E3 ที่ล็อกค่าไว้ก่อนเริ่มเก็บข้อมูล ตามกติกา "ล็อกก่อนเห็นผล" เดียวกับ VS2 §1.5
