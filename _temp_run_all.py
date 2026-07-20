#!/usr/bin/env python3
"""Run all Leo/Max updates for RDDT session"""

import os
import sys
import subprocess

base = r"C:\Users\user\Desktop\บลจ\บลจ CFA"

scripts = [
    os.path.join(base, "_temp_update_decisions.py"),
    os.path.join(base, "_temp_update_dashboard.py"),
]

for script in scripts:
    print(f"\n{'='*60}")
    print(f"Running: {script}")
    result = subprocess.run([sys.executable, script], capture_output=True, text=True, cwd=base)
    print("STDOUT:", result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    if result.returncode != 0:
        print(f"ERROR: {script} returned code {result.returncode}")
    else:
        print(f"SUCCESS: {script}")

print("\nAll scripts complete.")
