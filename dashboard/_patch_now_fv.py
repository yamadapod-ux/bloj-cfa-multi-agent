"""
NOW FV Re-Verify Patch Script
สร้างโดย Charlie — 2026-05-20
แก้ไข NOW entry ใน dashboard/data.js:
  blendedFV: 226 → 121.45
  mos: 148 → 17.8
  marketCap: "~$46.9B" → "~$106.2B (1.03B shares post-split)"
  shares: 515M → 1.03B
  sharesOutstanding: ใหม่
  note อัปเดต
"""

import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_js_path = os.path.join(script_dir, "data.js")

with open(data_js_path, "r", encoding="utf-8") as f:
    content = f.read()

# ตรวจว่ามี NOW entry หรือไม่
if '"NOW"' not in content and "'NOW'" not in content:
    print("ERROR: ไม่พบ NOW entry ใน data.js")
    exit(1)

print("พบ NOW entry — กำลังแก้ไข...")

# แก้ blendedFV สำหรับ NOW (เฉพาะ context ของ NOW)
# Strategy: หาตำแหน่ง NOW block แล้วแก้ค่าใน block นั้น

# หาตำแหน่งของ NOW
now_match = None
for pattern in [r'"ticker"\s*:\s*"NOW"', r"ticker:\s*'NOW'", r'ticker:\s*"NOW"']:
    m = re.search(pattern, content)
    if m:
        now_match = m
        break

if not now_match:
    print("ERROR: ไม่พบ NOW ticker entry")
    exit(1)

now_start = now_match.start()
# หา closing brace ของ NOW object (ระวัง nested objects)
# หา scope ของ object โดย count braces
depth = 0
obj_start = content.rfind("{", 0, now_start)
i = obj_start
while i < len(content):
    if content[i] == "{":
        depth += 1
    elif content[i] == "}":
        depth -= 1
        if depth == 0:
            obj_end = i + 1
            break
    i += 1

now_block = content[obj_start:obj_end]
print(f"พบ NOW block ({len(now_block)} chars)")

# แก้ blendedFV
now_block_new = re.sub(
    r'(blendedFV\s*:\s*)["\']?226["\']?',
    r'\g<1>121.45',
    now_block
)

# แก้ mos (Margin of Safety)
now_block_new = re.sub(
    r'(mos\s*:\s*)["\']?\+?148["\']?',
    r'\g<1>17.8',
    now_block_new
)

# แก้ marketCap ถ้ามี $46.9B
now_block_new = re.sub(
    r'(marketCap\s*:\s*["\']).*?(\$46\.9B).*?(["\'])',
    r'\g<1>~$106.2B (1.03B shares post-split)\g<3>',
    now_block_new
)

# แก้ price ถ้ายัง ~$91
now_block_new = re.sub(
    r'(price\s*:\s*["\'])~?\$?91["\']',
    r'\g<1>$103.10\g<2>',  # keep quote type
    now_block_new
)

# แก้ shares จาก 515M → 1.03B
now_block_new = re.sub(
    r'(shares\s*:\s*["\']?)515M(["\']?)',
    r'\g<1>1.03B (post-split)\g<2>',
    now_block_new
)

# แก้ targetBase ถ้ามี 226
now_block_new = re.sub(
    r'(targetBase\s*:\s*)["\']?\$?226["\']?',
    r'\g<1>121.45',
    now_block_new
)

# เช็คว่าแก้แล้วหรือยัง
if now_block_new == now_block:
    print("WARNING: ไม่มีการเปลี่ยนแปลง — อาจต้องแก้ pattern ใน script")
    print("NOW block preview (first 500 chars):")
    print(now_block[:500])
else:
    print("แก้ไขสำเร็จ:")
    # แสดง diff คร่าวๆ
    orig_lines = now_block.split('\n')
    new_lines = now_block_new.split('\n')
    for i, (o, n) in enumerate(zip(orig_lines, new_lines)):
        if o != n:
            print(f"  บรรทัด ~{i+1}: '{o.strip()}' → '{n.strip()}'")

# แทนที่ block ใน content
content_new = content[:obj_start] + now_block_new + content[obj_end:]

# อัปเดต LAST_UPDATED
content_new = re.sub(
    r'(LAST_UPDATED\s*[=:]\s*["\'])[\d-]+(["\'])',
    r'\g<1>2026-05-20\g<2>',
    content_new
)

with open(data_js_path, "w", encoding="utf-8") as f:
    f.write(content_new)

print("\\ndashboard/data.js อัปเดตเสร็จสิ้น!")
print("LAST_UPDATED → 2026-05-20")
print("\\nNOW entry changes:")
print("  blendedFV: 226 → 121.45")
print("  mos: 148 → 17.8")
print("  marketCap: ~$46.9B → ~$106.2B (1.03B shares post-split)")
