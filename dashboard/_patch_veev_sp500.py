"""
dashboard/_patch_veev_sp500.py
Targeted patch: update sp500Reference + sp500ReferenceNote fields inside the
VEEV (v2, date 2026-08-20) entry in dashboard/data.js.

WHY THIS SCRIPT EXISTS (instead of a direct Write to data.js):
- dashboard/data.js is far too large (~11,442 lines) to safely rewrite in
  full via the Write tool.
- Per house rule "Dashboard Write Safety": NEVER use a full-file Write on
  data.js — always use a targeted Python script.

HOW TO RUN:
    cd "C:\\Users\\user\\Desktop\\บลจ\\บลจ CFA"
    python dashboard/_patch_veev_sp500.py
"""

import sys

DATA_JS_PATH = "dashboard/data.js"

OLD_BLOCK = (
    '    sp500Reference: null,\n'
    '    sp500ReferenceNote: "TBD — CIO data package ไม่มีตัวเลข index level '
    'ตรงๆ วันนี้ (มีแต่ P/E/earnings-yield context) — Vera ต้อง verify '
    'ย้อนหลังก่อนใช้ alpha calculation",\n'
)

NEW_BLOCK = (
    '    sp500Reference: 7707.98,\n'
    '    sp500ReferenceNote: "7,707.98 (Aug 19, 2026 close — Yahoo Finance + '
    'StockAnalysis.com SPY $769.06 cross-check, verified โดย Vera 2026-08-20 '
    'session, resumed 2026-08-21)",\n'
)


def main():
    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    count = content.count(OLD_BLOCK)
    if count == 0:
        print("ERROR: OLD_BLOCK not found verbatim in data.js. Aborting — no changes written.")
        sys.exit(1)
    if count > 1:
        print(f"ERROR: OLD_BLOCK found {count} times (expected exactly 1). Aborting to avoid ambiguous replace.")
        sys.exit(1)

    # Sanity check: this block must sit inside the VEEV v2 entry (date 2026-08-20)
    idx = content.find(OLD_BLOCK)
    window = content[max(0, idx - 2000):idx]
    if 'ticker: "VEEV"' not in window or 'date: "2026-08-20"' not in window:
        print("ERROR: sanity check failed — OLD_BLOCK does not appear to be inside VEEV 2026-08-20 entry. Aborting.")
        sys.exit(1)

    new_content = content.replace(OLD_BLOCK, NEW_BLOCK, 1)

    # Basic structural sanity checks
    if new_content.count("{") != content.count("{") + 0 or new_content.count("}") != content.count("}") + 0:
        # replace shouldn't change brace counts at all since we didn't touch braces
        pass

    veev_count = new_content.count('    ticker: "VEEV",')
    if veev_count != 1:
        print(f"ERROR: expected exactly 1 VEEV ticker entry after patch, found {veev_count}. Aborting write.")
        sys.exit(1)

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("VEEV sp500Reference fields patched successfully: 7707.98 + verified note.")


if __name__ == "__main__":
    main()
