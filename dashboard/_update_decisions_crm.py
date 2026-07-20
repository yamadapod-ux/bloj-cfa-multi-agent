filepath = "C:/Users/user/Desktop/บลจ/บลจ CFA/portfolio/decisions.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

print(f"decisions.md loaded: {len(content)} chars")

# ---- อัปเดต Re-Analysis Log: CRM v1 -> v2 ----
# แทนที่ row เก่าของ CRM ใน Re-Analysis Log
# หาตำแหน่ง Re-Analysis Log section
re_analysis_old_row = "| **2026-05-29** | **CRM** | **v1->v2 (QA Fix)** | **BUY -- ข้อมูล corrected; Rating ยังคงเป็น BUY แต่ FV เปลี่ยน** | **Morgan QA FAIL (5 HIGH issues): Revenue $37.9B->$41.5B (official FY2026); FCF $13.1B->$14.4B; Q1 FY27 data added (Revenue $11.1B +13%, Agentforce +205%); FY2027 guide $45.8-46.2B; Weights 40/35/25->40/30/30 (CLAUDE.md fix); Shares 967M->937M. Emma FV $311->$351; Quinn P-W EV $244->$260; Bear P-W EV $192->$202. Blended FV $258->$279. MOS +42.5%->+54.1%. Rating UNCHANGED: BUY (stronger thesis post-fix).** |"

# row นี้มีอยู่แล้ว ไม่ต้องเพิ่มอีก
if re_analysis_old_row in content:
    print("CRM Re-Analysis row already exists in decisions.md -- no change needed")
else:
    print("CRM Re-Analysis row not found -- checking content...")
    # ตรวจว่า CRM มีอยู่ใน re-analysis log ไหม
    if "CRM" in content and "v1->v2" in content:
        print("CRM v1->v2 exists but format slightly different -- OK")
    else:
        print("CRM not found in re-analysis log")

# ---- อัปเดต S&P 500 ref ใน CRM row ----
# แก้ S&P 500 ref จาก est. เป็น 7,520.36 verified
old_sp = "**S&P 500 ref ~5,700-5,750 (est. -- URL pending)**"
new_sp = "**S&P 500 ref 7,520.36** (May 27 close — positions.md source)"
if old_sp in content:
    content = content.replace(old_sp, new_sp, 1)
    print("S&P 500 ref updated from est. to verified 7,520.36")
else:
    # try alternative format
    old_sp2 = "**S&P 500 ref ~5,700-5,750 (est. — URL pending)**"
    if old_sp2 in content:
        content = content.replace(old_sp2, new_sp, 1)
        print("S&P 500 ref updated (alternative format)")
    else:
        print("S&P 500 ref marker not found -- may already be updated or format differs")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"decisions.md saved: {len(content)} chars")
