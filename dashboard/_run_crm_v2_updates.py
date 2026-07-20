#!/usr/bin/env python3
"""
CRM v2 QA Fix — Master Update Runner
Runs both update scripts and verifies results.
Run from any directory: python dashboard/_run_crm_v2_updates.py
"""

import subprocess
import sys
import os

base = r"C:\Users\user\Desktop\บลจ\บลจ CFA"

scripts = [
    (os.path.join(base, "dashboard", "_update_crm_v2.py"), "dashboard/data.js"),
    (os.path.join(base, "dashboard", "_update_tracker_crm_v2.py"), "performance/tracker.md"),
]

all_pass = True
for script_path, target_file in scripts:
    print(f"\n{'='*60}")
    print(f"Running: {os.path.basename(script_path)}")
    print(f"Target: {target_file}")
    print('='*60)
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.returncode != 0:
        print(f"ERROR: {result.stderr}")
        all_pass = False
    else:
        print(f"OK: {target_file} updated successfully")

# Verify data.js syntax
print(f"\n{'='*60}")
print("Verifying dashboard/data.js syntax (node)...")
data_js_path = os.path.join(base, "dashboard", "data.js")
verify_script = f"const d = require('{data_js_path.replace(chr(92), '/')}'); console.log('REPORTS count:', typeof REPORTS !== 'undefined' ? REPORTS.length : 'N/A');"

# Simple check: count CRM entries and check for double entries
with open(data_js_path, "rb") as f:
    content = f.read().decode("utf-8")

crm_count = content.count('"CRM"')
blended_279 = "blendedFV: 279.00" in content
blended_258_old = "blendedFV: 258.00" in content
mos_54 = "mosPct: 54.1" in content
mos_42_old = "mosPct: 42.5," in content

print(f"  CRM ticker occurrences: {crm_count} (expected: varies, check for duplicates)")
print(f"  blendedFV: 279.00 present: {blended_279} (expected: True)")
print(f"  blendedFV: 258.00 still present: {blended_258_old} (expected: False)")
print(f"  mosPct: 54.1 present: {mos_54} (expected: True)")
print(f"  mosPct: 42.5 still present: {mos_42_old} (expected: False)")

if blended_279 and not blended_258_old and mos_54 and not mos_42_old:
    print("\ndata.js VERIFICATION: PASS")
else:
    print("\ndata.js VERIFICATION: FAIL — check script output above")
    all_pass = False

# Verify tracker.md
with open(os.path.join(base, "performance", "tracker.md"), "rb") as f:
    tracker = f.read().decode("utf-8")

tracker_279 = "Blended FV | **$279**" in tracker
tracker_541 = "+54.1%" in tracker
tracker_old_fv = "**$258**" in tracker
tracker_old_mos = "+42.5%" in tracker

print(f"\n{'='*60}")
print("Verifying performance/tracker.md...")
print(f"  Blended FV $279 present: {tracker_279} (expected: True)")
print(f"  MOS +54.1% present: {tracker_541} (expected: True)")
print(f"  Old $258 still present: {tracker_old_fv} (expected: False)")
print(f"  Old +42.5% still present: {tracker_old_mos} (expected: False)")

if tracker_279 and tracker_541 and not tracker_old_fv and not tracker_old_mos:
    print("\ntracker.md VERIFICATION: PASS")
else:
    print("\ntracker.md VERIFICATION: FAIL — check script output above")
    all_pass = False

print(f"\n{'='*60}")
if all_pass:
    print("ALL UPDATES COMPLETE: CRM v2 QA Fix synced to data.js + tracker.md")
    print("Next steps:")
    print("  1. Open dashboard/index.html in browser — verify CRM shows BFV $279, MOS 54.1%")
    print("  2. Morgan QA round 2 — report v2 ready for re-submission")
    print("  3. Max execute: CRM BUY T1 4% at $175-190, Stop $146")
else:
    print("SOME UPDATES FAILED — review errors above")
