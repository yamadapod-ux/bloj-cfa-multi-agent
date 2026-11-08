# Round 89 -- apply prune (archive 7, SLA fix 5), header line, prune block, report, deployment log.
import re
W='../../../portfolio/watchlist.md'; DL='../../../portfolio/deployment_log.md'
s=open(W,encoding='utf-8').read(); L=s.split('\n')
# 1) header
i=next(k for k,x in enumerate(L) if x.startswith('*ล่าสุด (2026-11-07)'))
L[i]=L[i].replace('*ล่าสุด (2026-11-07)','*ก่อนหน้า (2026-11-07)',1)
L.insert(i,"*ล่าสุด (2026-11-08): **Scout Round 89 — Office REITs** (ครั้งแรก; BXP/VNO/SLG/KRC/HPP ตามคำสั่ง + DEI/CUZ/HIW/BDN/PDM/JBGS/ARE/ESRT/CDP/OPI, Yahoo/Nasdaq close 11-06; PGRE ถูก Rithm ซื้อแล้ว, EQC ไม่มีข้อมูล). Filter A 6/15 (OPI/HPP/JBGS/ESRT/ARE/DEI) → reason 5 → B+C 4 → D/E 0. **0 fast-track · 0 learning-queue · 15 reject (4 QUICK-SCREEN SKIP: HPP/ESRT/ARE/DEI)**. P/FFO ~7× ดูถูกแต่ FFO ไม่หัก TI/capex/capitalized interest; ใกล้สุด ARE (0.85× หลังหัก cap. interest, E 1/3) รอ Investor Day 12-02. Prune: **archive 7** (IBKR/URI/EME/INDI/ANIP/BKSY/VMD), SLA fixed 5 → 11-14.*")
# 2) archive rows
ARC={'IBKR':'$75.82 (11-06, Yahoo = Nasdaq) · −23.2% จาก high $98.75','URI':'$1,055.57 (11-06) · −12.2% จาก high $1,202.12 (ไม่ผ่าน A)','EME':'$608.45 (11-06) · −36.1% จาก high $951.96',
     'INDI':'$1.81 (11-06; +33.6% วันเดียว 11-06 ยังไม่ได้เช็คข่าว) · −67.0% จาก high $5.49','ANIP':'$67.41 (11-06) · −29.4% จาก high $95.45','BKSY':'$21.33 (11-06) · −59.7% จาก high $52.88','VMD':'$9.13 (11-06) · −27.6% จาก high $12.61'}
moved={}
for t in ARC:
    k=next(k for k,x in enumerate(L) if x.startswith(f'| {t} |'))
    cells=[c.strip() for c in L[k].strip('|').split('|')]
    moved[t]=(cells[1],cells[3]); del L[k]
a=next(k for k,x in enumerate(L) if x.startswith('|--------|---------|---------------------|'))
rows=[f"| {t} | {moved[t][0]} | {moved[t][1]} | 2026-11-08 | Stale timeout (Rule #1) — Round 89 prune: >60 วันไม่มี update จาก CIO/Charlie, target 2026-11-07 ผ่านไปแล้วโดยไม่มี Tier 1 re-run (เตือนไว้ใน prune R86-88). ไม่ได้ประเมินคุณภาพใหม่ — re-list ได้ถ้า CIO/Charlie ต้องการ | {ARC[t]} |" for t in ARC]
L[a+1:a+1]=rows
# 3) SLA fix 5
for t in ['WYNN','VICI','ALLY','NBIX','BYD']:
    k=next(k for k,x in enumerate(L) if x.startswith(f'| {t} |'))
    L[k]=L[k].rstrip().rstrip('|').rstrip()+' **SLA re-fix 2026-11-08 (Round 89 prune): Target 2026-11-14** — target 11-07 ผ่านไปแล้วโดยไม่ได้รัน Tier 1 |'
# 4) prune block before R88 prune
k=next(k for k,x in enumerate(L) if x.startswith('**Prune Pass 2026-11-07 (Mode 1 Step 0 — Round 88)'))
L[k:k]=open('prune.md',encoding='utf-8').read().rstrip('\n').split('\n')+['']
s='\n'.join(L).rstrip('\n')+'\n'+open('r89.md',encoding='utf-8').read()
open(W,'w',encoding='utf-8').write(s)
d=open(DL,encoding='utf-8').read().rstrip('\n')+'\n'+open('dep.md',encoding='utf-8').read()
open(DL,'w',encoding='utf-8').write(d)
print('ok',list(moved))
