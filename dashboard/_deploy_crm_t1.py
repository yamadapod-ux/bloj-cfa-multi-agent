"""
Max T1 Deploy — CRM 2026-05-29
- Ticker: CRM
- Action: DEPLOYED T1
- Entry: ~$181 (in zone $175-190)
- Shares: 2 shares = $362 = 3.6% of portfolio ($10,000)
- Conservative T1: 3.6% vs IPS target 4% — 2 full shares at $181
- Stop Loss: $146 (-20%)
- Portfolio cash after: $8,360.07 - $362.00 = $7,998.07
"""

# ---- 1. Update deployment_log.md ----
deployment_log_path = "C:/Users/user/Desktop/บลจ/บลจ CFA/portfolio/deployment_log.md"

with open(deployment_log_path, "r", encoding="utf-8") as f:
    content = f.read()

print(f"deployment_log.md loaded: {len(content)} chars")

# New deployment row
crm_deploy_row = "| **2026-05-29** | **CRM** | **DEPLOYED T1** | **Conv 7.0 >= 7.0 Value PASS; MOS +54.1% >= 15% PASS; Regime RISK-ON 4/4 PASS; Entry $181 in zone $175-190 PASS** | **$362.00 (3.62%)** | **T1** | **Value Bucket gate: Conviction 7.0/10 exactly at Value threshold + MOS +54.1% well above 15% minimum + RISK-ON + entry zone active ($181 in T1 $175-190). 2 shares at $181 = $362. Conservative size 3.62% (vs IPS target 4% = ~2.2 shares). Whole shares only. Agentforce +205% Q1 FY27 + RPO $72.4B = conviction justified. Morgan CONDITIONAL PASS (3 minor annotations non-blocking). Stop $146 set immediately.** | **-- (just deployed -- track 30d)** |"

# หาตำแหน่งก่อน CLFD row แทรก
old_last_row = "| **2026-05-22** | **CLFD** | **NO DEPLOY**"
if old_last_row in content:
    content = content.replace(old_last_row, crm_deploy_row + "\n" + old_last_row, 1)
    print("Step 1a: CRM deploy row added to deployment log table")
else:
    # append at end of table
    content = content + "\n" + crm_deploy_row + "\n"
    print("Step 1a: CRM deploy row appended to deployment log")

# Update Watchlist Status -- add CRM to watchlist table
old_watchlist_header = "## Watchlist Status — 2026-05-22 (Updated)"
new_watchlist_header = "## Watchlist Status — 2026-05-29 (Updated)"
content = content.replace(old_watchlist_header, new_watchlist_header, 1)

# Add CRM T2 to watchlist
old_googl_t2_line = "| **GOOGL T2** | **$388.91 (entry)** | **$360-375** | **T1 executed** | **HOLD T1 -- T2 รอ trigger** |"
crm_watchlist = "| **CRM T2** | **$181 (T1 entry)** | **$155-175 (T2)** | **T1 executed** | **HOLD T1 -- T2 รอ pullback $155-175** |"
if old_googl_t2_line in content:
    content = content.replace(old_googl_t2_line, old_googl_t2_line + "\n" + crm_watchlist, 1)
    print("Step 1b: CRM T2 added to watchlist")
else:
    print("WARNING: GOOGL T2 watchlist line not found")

# Add CRM Gate Analysis section
crm_analysis_section = """
---

## CRM T1 Deployment Analysis — 2026-05-29

**CRM: DEPLOYED T1 — RISK-ON Regime, Value Bucket**

| รายการ | ค่า |
|--------|-----|
| ราคา entry | $181.00 (verified: Salesforce Q1 FY27 Press Release + ValueTheMarkets) |
| Blended FV | $279 (Emma $351x40% + Quinn $260x30% + Bear $202x30%) |
| MOS | +54.1% |
| ESG-adj FV | ~$272 |
| Conviction | 7.0/10 -- Value gate 7.0 PASSED exactly |
| Regime | RISK-ON 4/4 -- Position multiplier 1.0x; Force Deploy Active |
| Deploy Status | DEPLOYED T1 -- 2 shares @ $181 = $362.00 (3.62% portfolio) |

**Gate-by-Gate Summary:**
| Gate | Status | Detail |
|------|--------|--------|
| Conviction >= 7.0 (Value) | PASS | 7.0 >= 7.0 |
| MOS >= 15% (Value) | PASS | +54.1% >= 15% |
| Revenue Growth N/A (Value bucket) | N/A | Value bucket uses MOS + Conviction gates only |
| Entry zone (<=5% above upper) | PASS | $181 in zone $175-190 -- at zone midpoint |
| Cash >= 10% floor | PASS | $7,998.07 (79.98%) post-deploy >> 10% floor |
| Sector allocation | PASS | Enterprise Software -- new sector, no concentration issue |
| Morgan QA | CONDITIONAL PASS | 5 HIGH issues resolved; 3 minor pending (non-blocking) |
| Regime | PASS | RISK-ON 4/4 |

**Sizing Decision:**
- Full IPS target (4%): $400 = 2.2 shares -> rounded to 2 whole shares
- Actual deploy: 2 shares x $181 = $362 (3.62%)
- Rationale: 2 whole shares conservative; leaves T2 capacity $155-175 (2.5%) + T3 $140-155 (1.5%)
- Max total capacity: 8% Value bucket = ~$800 remaining T2+T3

**T2 Triggers (Max monitoring):**
1. ราคาย่อ $155-175 -> T2 entry (เพิ่ม ~3 shares at ~$165 = ~$495 = 4.95%)
2. Q2 FY27 Agentforce ARR > $2B (confirms acceleration) -> T2 ณ ราคา <=190
3. Microsoft M365 threat clarity (no bundle announcement) -> thesis confirmation
4. RPO growth > 15% consecutive 2 quarters -> add confidence

**Counter-factual tracking:**
- Max จะ track ราคา CRM ทุก 30 วัน
- Stop Loss $146 = -19.3% from $181 entry

"""

# append analysis section before last watchlist section
old_watchlist_new = "## Watchlist Status — 2026-05-29 (Updated)"
content = content.replace(old_watchlist_new, crm_analysis_section + "\n" + old_watchlist_new, 1)
print("Step 1c: CRM deployment analysis section added")

with open(deployment_log_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"deployment_log.md saved: {len(content)} chars")

# ---- 2. Update positions.md ----
positions_path = "C:/Users/user/Desktop/บลจ/บลจ CFA/portfolio/positions.md"

with open(positions_path, "r", encoding="utf-8") as f:
    pos_content = f.read()

print(f"positions.md loaded: {len(pos_content)} chars")

# Update header date
old_header = "*Managed by Max | Updated: 2026-05-28 (Portfolio Review -- Price Refresh)*"
new_header = "*Managed by Max | Updated: 2026-05-29 (CRM T1 Deploy)*"
pos_content = pos_content.replace(old_header, new_header, 1)

# Update Portfolio Summary
old_cash = "| **Current Cash** | $8,360.07 |"
new_cash = "| **Current Cash** | $7,998.07 |"
pos_content = pos_content.replace(old_cash, new_cash, 1)

old_invested = "| **Market Value (Invested)** | $1,546.70 |"
new_invested = "| **Market Value (Invested)** | $1,908.70 |"  # old $1,546.70 + CRM $362.00
pos_content = pos_content.replace(old_invested, new_invested, 1)

old_total = "| **Total Portfolio Value** | $9,906.77 |"
new_total = "| **Total Portfolio Value** | $9,906.77 |"  # still same total (cash transferred to position)
pos_content = pos_content.replace(old_total, new_total, 1)

old_positions = "| **# Positions** | 3 (ADBE + NOW + GOOGL) |"
new_positions = "| **# Positions** | 4 (ADBE + NOW + GOOGL + CRM) |"
pos_content = pos_content.replace(old_positions, new_positions, 1)

old_cash_pct = "| **Cash %** | 84.39% |"
new_cash_pct = "| **Cash %** | 80.75% |"  # 7,998.07 / 9,906.77 = ~80.74%
pos_content = pos_content.replace(old_cash_pct, new_cash_pct, 1)

old_last_updated = "| **Last Updated** | 2026-05-28 |"
new_last_updated = "| **Last Updated** | 2026-05-29 |"
pos_content = pos_content.replace(old_last_updated, new_last_updated, 1)

# Update Current Positions table -- add CRM row after GOOGL
old_googl_pos = "| GOOGL | 2026-05-21 (T1) | $388.91 | 1 | $388.91 | **$389.50** | $389.50 | **+0.15%** | 3.93% | $310.00 | OPEN -- T1 |"
crm_pos_row = "| CRM | 2026-05-29 (T1) | $181.00 | 2 | $362.00 | **$181.00** | $362.00 | **0.00%** | 3.65% | $146.00 | OPEN -- T1 |"
if old_googl_pos in content:
    pos_content = pos_content.replace(old_googl_pos, old_googl_pos + "\n" + crm_pos_row, 1)
    print("Step 2a: CRM position row added")
else:
    # try without **$389.50**
    old_googl_simple = "| GOOGL | 2026-05-21 (T1) |"
    if old_googl_simple in pos_content:
        # find and replace the GOOGL line
        lines = pos_content.split("\n")
        for i, line in enumerate(lines):
            if "| GOOGL | 2026-05-21 (T1) |" in line:
                lines.insert(i+1, crm_pos_row)
                print(f"Step 2a: CRM position inserted after GOOGL at line {i}")
                break
        pos_content = "\n".join(lines)
    else:
        print("WARNING: GOOGL position line not found")

# Update Sector Allocation -- add Enterprise Software row
old_sector_table_end = "| Cash | $8,360.07 | 84.39% | -- |"
new_sector_end = "| Enterprise Software / AI (ADBE + NOW + CRM) | $1,518.70 | 15.33% | 25% |\n| Comm. Services / AI Platform (GOOGL) | $389.50 | 3.93% | 25% |\n| Cash | $7,998.07 | 80.74% | -- |"
if old_sector_table_end in pos_content:
    pos_content = pos_content.replace(old_sector_table_end, new_sector_end, 1)
    print("Step 2b: Sector allocation updated")
else:
    print("WARNING: Sector allocation line not found")

# Update Cash section
old_cash_section = "| Available Cash | $8,360.07 |"
new_cash_section = "| Available Cash | $7,998.07 |"
pos_content = pos_content.replace(old_cash_section, new_cash_section, 1)

old_cash_pct2 = "| Cash % | 84.39% |"
new_cash_pct2 = "| Cash % | 80.74% |"
pos_content = pos_content.replace(old_cash_pct2, new_cash_pct2, 1)

old_cash_note = "| Note | Cash 84% -- RISK-ON Force Deploy active | มี capacity deploy ได้อีก |"
new_cash_note = "| Note | Cash 80.74% -- RISK-ON Force Deploy active | CRM T1 deployed; T2/T3 + more candidates needed |"
pos_content = pos_content.replace(old_cash_note, new_cash_note, 1)

# Add CRM to Action Items
old_action_items = "## Action Items — 2026-05-28"
new_action_header = "## Action Items — 2026-05-29 (Post CRM T1 Deploy)"
pos_content = pos_content.replace(old_action_items, new_action_header, 1)

# Add CRM to INTU Stop Loss Check
old_stop_check_date = "## Stop Loss Check — 2026-05-28"
new_stop_check_date = "## Stop Loss Check — 2026-05-29"
pos_content = pos_content.replace(old_stop_check_date, new_stop_check_date, 1)

# Add CRM to stop loss table
old_googl_stop = "| GOOGL | $389.50 | $310.00 | $79.50 | +20.4% above stop | OK |"
crm_stop_row = "| CRM | $181.00 | $146.00 | $35.00 | +19.3% above stop | OK (just deployed) |"
if old_googl_stop in pos_content:
    pos_content = pos_content.replace(old_googl_stop, old_googl_stop + "\n" + crm_stop_row, 1)
    print("Step 2c: CRM added to stop loss check")
else:
    print("WARNING: GOOGL stop line not found")

# Update Watchlist -- add CRM T2
old_intu_sold = "| INTU | **SOLD** | -- | -- | -- | **AUTO-SELL 2026-05-21 @ $321.50** | -- | -- |"
crm_watchlist_entry = "| CRM T2 | HOLD T1 / rอ T2 | $155-175 | $146 | $181 (T1 entry) | T1 executed -- T2 รอ pullback | $279 | +54.1% |"
if old_intu_sold in pos_content:
    pos_content = pos_content.replace(old_intu_sold, old_intu_sold + "\n" + crm_watchlist_entry, 1)
    print("Step 2d: CRM T2 added to watchlist")

with open(positions_path, "w", encoding="utf-8") as f:
    f.write(pos_content)
print(f"positions.md saved: {len(pos_content)} chars")

print("\nAll deployment files updated successfully.")
print("Summary:")
print("  - deployment_log.md: CRM T1 DEPLOYED row + analysis section")
print("  - positions.md: CRM added to positions, cash updated $8,360.07 -> $7,998.07")
