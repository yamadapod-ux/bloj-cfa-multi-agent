"""
One-shot backfill: embed fullContent (full markdown) ของแต่ละ report ลง data.js
Run: python dashboard/_backfill.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(ROOT, "reports")
DATA_JS = os.path.join(ROOT, "dashboard", "data.js")

def read_md(ticker, date):
    path = os.path.join(REPORTS_DIR, f"{ticker}_{date}.md")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def js_template_escape(s):
    """Escape สำหรับ JS template literal: backticks + ${"""
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

# อ่าน data.js ปัจจุบัน
with open(DATA_JS, "r", encoding="utf-8") as f:
    js = f.read()

# pattern: หาแต่ละ REPORTS entry (object)
# ใช้ regex แบบง่าย — จับช่วง { ... } ที่มี ticker: "X"
def patch_entry(js_text, ticker, date):
    md = read_md(ticker, date)
    if md is None:
        print(f"  [skip]skip {ticker} — file not found")
        return js_text

    escaped = js_template_escape(md)
    full_content_field = f',\n    fullContent: `{escaped}`'

    # หา block ของ ticker นี้ (จาก ticker: "X" ไปจนถึง } ตัวถัดไป)
    pattern = re.compile(
        r'(\{\s*\n?\s*ticker:\s*"' + re.escape(ticker) + r'"[\s\S]*?reportFile:\s*"[^"]+")(\s*\n?\s*\})',
        re.MULTILINE
    )

    def replacer(m):
        body = m.group(1)
        # update reportFile path: reports/X.md → ../reports/X.md
        body = re.sub(
            r'reportFile:\s*"reports/',
            'reportFile: "../reports/',
            body
        )
        # ถ้า fullContent อยู่แล้ว — replace
        if 'fullContent:' in body:
            # ลบ fullContent เก่า
            body = re.sub(
                r',\s*\n?\s*fullContent:\s*`[\s\S]*?`',
                '',
                body
            )
        return body + full_content_field + m.group(2)

    new_js, n = pattern.subn(replacer, js_text)
    if n == 0:
        print(f"  [skip]{ticker}: pattern not matched")
    else:
        print(f"  [ok]{ticker}: embedded {len(md):,} chars")
    return new_js

# ทุกตัวที่ต้อง backfill
TARGETS = [
    ("NVDA", "2026-04-24"),
    ("CCJ", "2026-04-24"),
    ("HIMS", "2026-04-24"),
    ("TMDX", "2026-04-24"),
]

for ticker, date in TARGETS:
    js = patch_entry(js, ticker, date)

# update LAST_UPDATED
js = re.sub(
    r'const LAST_UPDATED\s*=\s*"[^"]*";',
    'const LAST_UPDATED = "2026-04-25";',
    js
)

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(js)

print(f"\n[done] data.js updated ({len(js):,} chars)")
