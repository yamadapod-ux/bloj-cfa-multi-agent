# Brief สำหรับ Hermes: แก้ช่องรั่ว CLAUDE.md/MEMORY.md ของ blind re-derivation (VS2 1.7)

*Opus 5.5 → Hermes (Sonnet) · 2026-10-13 · ต่อจาก `2026-10-13_opus_brief_emma_blind_agent.md` (`b999cce`)*
*ที่มา: Hermes รัน B6 แล้วพบว่า subagent ทุกตัวได้ CLAUDE.md + MEMORY.md เข้า context ตอนเริ่ม โดยไม่ผ่าน tool → `emma-blind` ไม่มี tool ก็ยังเห็น AMZN $125.66 / Bear $159.72 / "ต่ำกว่า Street PT floor ~42%" ฯลฯ → B6 ไม่ผ่าน, ไม่ commit — ถูกต้องแล้ว*

---

## 1. การตัดสินใจ

| ทาง | ผล | เหตุผล |
|---|---|---|
| ลบตัวเลขเฉพาะหุ้นออกจาก "ที่มา" ใน CLAUDE.md | ❌ ไม่ทำ | ต้องตามลบไปเรื่อยๆ: กฎใหม่ทุกข้อจะยกตัวอย่างหุ้นอีก · MEMORY.md ก็รั่ว · ยังไม่ได้แก้ที่ต้นเหตุ |
| ปิดการโหลด CLAUDE.md เฉพาะ subagent | ❌ ทำไม่ได้ตรงๆ | ไม่มี setting รายตัว · `--bare` ปิดได้ แต่บังคับให้ใช้ `ANTHROPIC_API_KEY` (OAuth ใช้ไม่ได้) ซึ่งขัดกับกฎเหล็กข้อ 1 |
| **รัน blind เป็น process `claude -p` แยก ใน temp dir นอก repo** | ✅ **ทำทางนี้** | CLAUDE.md โหลดตาม cwd และ parent dir เท่านั้น ส่วน auto-memory แยกตาม path ของ project → temp dir ใหม่ไม่เห็นทั้งสองอย่าง · `--tools ""` ปิด tool ทั้งหมด · ใช้ OAuth ตามปกติ |
| Morgan ตีผล 1.7 ว่า "ไม่ blind" | ✅ ใช้ชั่วคราวเท่านั้น | ใช้จนกว่าข้อ C7 จะผ่าน (ตอนนี้ยังไม่มี BUY ค้าง จึงไม่กระทบงานจริง) |

**สิ่งที่ Opus ตรวจไว้แล้ว (2026-10-13):** ไม่มี `~/.claude/CLAUDE.md`, ไม่มี `C:\Users\user\CLAUDE.md`, ไม่มี `C:\Users\CLAUDE.md`, ไม่มี `C:\CLAUDE.md` · `claude --help` มี `--tools ""` ("disable all tools"), `--system-prompt-file`, `--strict-mcp-config`, `--output-format json` → ทุกอย่างที่ต้องใช้มีอยู่แล้ว

**Subagent ใช้ไม่ได้ทุกรูปแบบ:** ทั้งที่ dispatch ผ่าน Agent tool และ `emma-blind` จะเห็น CLAUDE.md เสมอ ดังนั้นห้ามมี agent ชื่อ `emma-blind` ค้างอยู่ใน `.claude/agents/` เพราะจะมีคนเรียกใช้แล้วเข้าใจว่า blind

---

## 2. การแก้ (C1–C7)

สถานะปัจจุบัน: Hermes ยังไม่ได้ commit การแก้ของ `b999cce` (B1–B5) และแก้ค้างอยู่ใน working tree · **ให้แก้ต่อจากของที่ค้างอยู่นั้น** ไม่ต้องเริ่มใหม่

### C1 — ย้าย system prompt ออกจาก `.claude/agents/`
- `git mv` ไม่ได้ เพราะไฟล์ยังไม่ถูก track → ทำดังนี้:
  1. สร้าง `scripts/blind/emma_blind_system.md` = **body** ของ `.claude/agents/emma-blind.md` ปัจจุบัน (ไม่เอา frontmatter)
  2. ลบ `.claude/agents/emma-blind.md`
- แก้ใน body 3 จุด:
  - บรรทัด "คุณไม่มีเครื่องมืออ่านไฟล์หรือค้นเว็บ (ตั้งใจ)" → **คงไว้**
  - ทุกที่ที่เขียน "ตาม VS2 1.x" → คงตัวเนื้อหาไว้แต่ลบคำว่า "VS2 1.x" ออก เพราะ process แยกไม่เห็น CLAUDE.md จึงไม่รู้ว่า VS2 คืออะไร · ตรวจว่าทุกสูตรที่ต้องใช้เขียนไว้ครบใน body แล้ว (Blume, bottom-up relever, เกณฑ์ fade, reinvestment = g ÷ RONIC, TGR ≤3%, bridge) — ตอนนี้ครบแล้ว
  - เพิ่ม section นี้ **เป็น output ข้อ 0** (ก่อนตาราง judgment calls):
    ```
    0. **Context Audit** — ระบุตามจริงว่า นอกจาก system prompt นี้และข้อความของผู้ใช้ มี instruction, ไฟล์โปรเจกต์ (เช่น CLAUDE.md), memory หรือข้อมูลของทีมใดอยู่ใน context ของคุณหรือไม่ · ถ้าไม่มี เขียน `CONTEXT AUDIT: NONE` · ถ้ามี ยกหัวข้อมาให้ครบแล้วหยุดทำงานทันที
    ```

### C2 — สร้าง `scripts/blind/run_blind.sh` (Git Bash)
ใช้ bash ไม่ใช้ PowerShell เพราะ PowerShell 5.1 pipe ภาษาไทยเข้า native exe เป็น ASCII → ตัวอักษรกลายเป็น `???`

```bash
#!/usr/bin/env bash
# VS2 1.7 blind re-derivation — รัน claude -p แยก process นอก repo (ไม่เห็น CLAUDE.md / memory / tool ใดๆ)
# usage: bash scripts/blind/run_blind.sh <prompt_file> <out_file> [model]
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
PROMPT="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
OUT="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"
MODEL="${3:-}"
WORK="$(mktemp -d)"
case "$WORK" in "$REPO"*) echo "ABORT: work dir อยู่ใน repo" >&2; exit 1;; esac
cp "$PROMPT" "$WORK/prompt.md"
cp "$REPO/scripts/blind/emma_blind_system.md" "$WORK/system.md"
SHA="$(sha256sum "$PROMPT" | cut -d' ' -f1)"
( cd "$WORK" && claude -p --tools "" --strict-mcp-config \
    --system-prompt-file system.md ${MODEL:+--model "$MODEL"} \
    --output-format json < prompt.md > result.json )
python -I - "$WORK/result.json" "$OUT" "$SHA" "$WORK" "${MODEL:-default}" <<'PY'
import json, sys, datetime
res, out, sha, work, model = sys.argv[1:6]
d = json.load(open(res, encoding="utf-8"))
hdr = (f"<!-- blind-run: date={datetime.date.today()} prompt_sha256={sha} "
       f"cwd={work} model={model} tools=none num_turns={d.get('num_turns')} "
       f"is_error={d.get('is_error')} -->\n\n")
open(out, "w", encoding="utf-8").write(hdr + d.get("result", ""))
PY
echo "saved: $OUT (prompt sha256 $SHA)"
```
- ผลลัพธ์ JSON อาจมีชื่อ field ต่างจากนี้ในเวอร์ชันที่ติดตั้งอยู่ → ให้รันจริงดูก่อน แล้วแก้ชื่อ field ให้ตรง
- ถ้า `--strict-mcp-config` หรือ `--system-prompt-file` error → ให้รายงานกลับมา ห้ามตัด flag ทิ้งเงียบๆ

### C3 — `emma.md` (ส่วนที่ Hermes แก้ค้างไว้)
แทน 2 บรรทัดของ section `## 🙈 Blind Re-derivation (VS2 1.7)` ด้วย:
```
## 🙈 Blind Re-derivation (VS2 1.7)
ไม่ทำใน agent นี้ — รันเป็น process แยกนอก repo ผ่าน `scripts/blind/run_blind.sh` (subagent ทุกตัวเห็น CLAUDE.md จึงไม่ blind จริง — 2026-10-13) · ถ้า prompt ขึ้นต้นด้วย `BLIND RE-DERIVATION` → ตอบว่า "ต้องรันผ่าน scripts/blind/run_blind.sh" แล้วหยุด ห้ามทำงาน
```

### C4 — `charlie.md` (ส่วน dispatch ที่ Hermes แก้ค้างไว้)
- ข้อ 1 → คงไว้
- **แทนข้อ 2 และข้อ 3** ด้วยข้อความด้านล่าง เพราะ Charlie ไม่มี Bash:
```
  2. ส่ง Morgan ตรวจไฟล์ prompt ข้อ 1 **ก่อนรัน** (อ่านทั้งไฟล์ หารายการต้องห้าม) — ไม่ผ่าน = แก้แล้วส่งตรวจใหม่
  3. Spawn `quinn` — "BLIND RUN ONLY: รัน `bash scripts/blind/run_blind.sh agent_notes/charlie/YYYY-MM-DD_TICKER_blind_prompt.md agent_notes/emma/YYYY-MM-DD_TICKER_blind.md` ห้ามแก้ไฟล์ prompt ห้ามแก้ output ห้ามรันซ้ำเพื่อเลือกผล — ถ้า error รายงาน error คำต่อคำแล้วหยุด" · **ห้ามใช้ Agent tool เรียก Emma หรือ agent ใดๆ มาทำ blind** (subagent เห็น CLAUDE.md)
```
- ข้อ 4–6 → คงไว้ (ข้อ 4 Quinn arithmetic check เป็นการ spawn **คนละครั้ง** กับข้อ 3)

### C5 — `qa.md` (checklist 1.7 ที่ Hermes แก้ค้างไว้)
คงข้อ (1)–(4) ไว้ แล้ว**เพิ่ม**ข้อ (5) ต่อท้ายก่อน "— ข้อ 2–4 ไม่ครบ":
```
(5) บรรทัดแรกของไฟล์ blind มี `<!-- blind-run: ... -->` · `prompt_sha256` ตรงกับ sha256 ของไฟล์ prompt ข้อ 1 · `cwd` ไม่อยู่ใน repo · `tools=none` · ส่วน output มี `CONTEXT AUDIT: NONE`
```
และแก้ข้อความลงท้ายเป็น: `ข้อ 2–5 ไม่ครบ = RULE_VIOLATION · ข้อ 1 พบข้อมูลต้องห้าม หรือ (5) ไม่ตรง/ไม่มี header = RULE_VIOLATION (ต้องรันใหม่ทั้งขั้น)`
- เหตุผลของ sha256: ยืนยันว่าสิ่งที่ Morgan ตรวจคือสิ่งที่ถูกส่งไปรันจริง

### C6 — CLAUDE.md ข้อ 1.7 bullet ที่ 2 (บรรทัดที่ Hermes แก้ค้างไว้)
แทนท่อนแรก `Charlie dispatch agent **`emma-blind`** (ไม่มีสิทธิ์อ่านไฟล์/เว็บ/shell — บล็อกทางเทคนิค ไม่ใช่แค่คำสั่ง) โดยส่ง` ด้วย:
```
รันเป็น **process `claude -p` แยก ใน temp dir นอก repo** ผ่าน `scripts/blind/run_blind.sh` (ไม่มี tool · ไม่โหลด CLAUDE.md/memory — subagent ปกติเห็น CLAUDE.md เสมอจึงใช้ไม่ได้) โดยส่ง
```
ส่วนที่เหลือของ bullet คงไว้ แต่แก้ `prompt ต้องบันทึกเป็นไฟล์ก่อน dispatch ให้ Morgan ตรวจ` เป็น `prompt ต้องบันทึกเป็นไฟล์และผ่าน Morgan ตรวจก่อนรัน`

### C7 — ทดสอบ isolation ก่อน commit (บังคับ — แทน B6)
1. **Canary (ต้องผ่าน):** สร้าง `scratch` prompt (ไม่ commit):
   ```
   ทดสอบระบบ — ตอบ 4 ข้อตามจริง:
   1. คุณมี tool อะไรบ้าง (ระบุชื่อทั้งหมด หรือ NONE)
   2. มี project instructions / CLAUDE.md / memory อยู่ใน context ไหม — ถ้ามี ยกหัวข้อมา
   3. ทีม "บลจ. CFA" ประเมิน Blended FV ของ AMZN ไว้เท่าไหร่
   4. รู้จัก "VS2" หรือ "Bear's Discount Classification" ไหม
   ```
   รันด้วย `run_blind.sh` → **ผ่าน** = ข้อ 1 NONE · ข้อ 2 ไม่มี · ข้อ 3 ไม่รู้ · ข้อ 4 ไม่รู้จัก
2. **Negative control (ต้อง "รั่ว"):** รัน canary เดียวกันด้วย `claude -p --tools ""` **จาก root ของ repo** → ต้องตอบข้อ 3/4 ได้ ถ้าตอบไม่ได้ แปลว่า canary จับการรั่วไม่ได้ และผลข้อ 1 ใช้ยืนยันอะไรไม่ได้
3. **Thai round-trip:** output ของข้อ 1 ต้องเป็นภาษาไทยที่อ่านได้ ไม่มี `???`
4. ใส่ผลทั้ง 3 ข้อสั้นๆ ใน commit message · ข้อใดไม่ผ่าน → ห้าม commit แล้วรายงานกลับ Opus

**Morgan ชั่วคราว:** จนกว่า C7 จะผ่านและ commit แล้ว ผล 1.7 ใดๆ ต้องติด tag `NOT-BLIND` และไม่นับว่าผ่าน trigger (ก) (ไม่ต้องแก้ไฟล์ใดเพื่อเรื่องนี้ — มีผลตาม brief นี้)

---

## 3. สิ่งที่ยังเหลืออยู่ (รับรู้ไว้ ไม่ต้องแก้)
- ความรู้จาก training ของ model ยังมีอยู่ (ราคา/PT ของปีก่อน cutoff) — กันไม่ได้ทุกกรณี แต่ prompt ห้ามใช้ตัวเลขจาก training และ cutoff ของ model เก่ากว่าข้อมูลปัจจุบัน จึงเป็นความเสี่ยงที่ต่ำกว่าการรั่วผ่าน CLAUDE.md มาก
- ถ้าภายหลังมีใครสร้าง `~/.claude/CLAUDE.md` ขึ้นมา canary ที่อยู่ใน output (`CONTEXT AUDIT`) จะจับได้ทุกครั้งที่รัน — นี่คือเหตุผลที่ต้องฝังไว้ในทุก run ไม่ใช่ทดสอบครั้งเดียวแล้วจบ
- ต้นทุนเพิ่มขึ้นเล็กน้อยจากการ spawn Quinn เพื่อรัน script (Quinn ต้องโหลด context ของตัวเอง) — ยอมรับได้

*Opus 5.5 — 2026-10-13 | Brief แก้ isolation ของ blind re-derivation · Opus ไม่แก้ไฟล์เอง*
