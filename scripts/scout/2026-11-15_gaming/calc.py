# All inputs from sec_out*.txt / sec_wynn.txt (SEC XBRL), BRSL/SRAD 6-K press releases, prices_out.txt (close 2026-11-13)
def p(*a): print(*a)
# ---------- INSE (10-Q 2026-09-30) ----------
px=4.40; sh=26.366684
oi=30.5-19.2+29.4; da=52.4-39.1+41.5; ocf=52.0-50.8+45.7; capex=35.7-24.6+6.2; sbc=6.7-4.6+4.3
debt=322.9+2.5; cash=36.5; nd=debt-cash; eq=-13.0; mc=px*sh
p('INSE mc',round(mc,1),'OI',oi,'DA',round(da,1),'EBITDA',round(oi+da,1),'ND',round(nd,1),'ND/EBITDA',round(nd/(oi+da),2),'ND/adjEBITDA(110.5)',round(nd/110.5,2))
fcf=ocf-capex; p(' OCF',round(ocf,1),'capex',round(capex,1),'FCF',round(fcf,1),'yield',round(fcf/mc*100,1),'FCF-SBC',round(fcf-sbc,1),round((fcf-sbc)/mc*100,1))
capn=(32.0+17.0+35.7)/3; fn=ocf-capn-sbc; p(' norm capex FY23-25',round(capn,1),'norm FCF-SBC',round(fn,1),'yield',round(fn/mc*100,1))
for t in (0.21,0.25):
  n=oi*(1-t); p(' ROIC tax',t,'incl cash',round(n/(eq+debt)*100,1),'ex cash',round(n/(eq+debt-cash)*100,1))
q1_25=19.2-7.9-9.7; t1=30.5-q1_25+9.2; t2=t1-7.9+9.9; t3=t2-9.7+10.3; p(' TTM OI trend Q1/Q2/Q3 26',round(t1,1),round(t2,1),round(t3,1),'FY25',30.5)
for w in (0.13,0.15,0.16):
  for f,lab in ((fcf,'TTM raw'),(fn,'norm')): p(f'  naive FV {lab} @{w}',round(f/w/sh,2),'P/FV',round(px/(f/w/sh),2))
# ---------- BRSL (6-K Q3'26) ----------
px=9.81; sh=185; mc=px*sh; nd=3842; nci=1133; ev=mc+nd+nci
p('BRSL mc',round(mc),'EV(incl NCI book)',round(ev),'EV/adjEBITDA guide 1150',round(ev/1150,2),'EV/(adjEBITDA-amort~385)',round(ev/(1150-385),2),'ND/adjEBITDA 3.30 (co.)','ND/(EBITDA after amort)',round(nd/(1150-385),2))
raw=750-450; lic=(579+1675)/9; p(' FCF ex-license guide',raw,'yield',round(raw/mc*100,1),'license/yr',round(lic),'norm',round(raw-lic),'yield',round((raw-lic)/mc*100,1))
ebit=391*4/3
for t in (0.21,0.25):
  n=ebit*(1-t); p(' ROIC tax',t,'incl cash',round(n/(1942+4385)*100,1),'ex cash',round(n/(1942+4385-538)*100,1))
p(' adjEBIT Q3 130 vs 185',round(130/185-1,3),'9M 391 vs 500',round(391/500-1,3))
for f in (raw,raw-lic):
  for w in (0.10,0.12): p(f'  naive FV FCF {round(f)} @{w}',round(f/w/sh,2),'P/FV',round(px/(f/w/sh),2))
p(' PT Nasdaq 14.50 ->',round(px/14.5,3),'MarketBeat 15.10 ->',round(px/15.10,3))
# ---------- SRAD (6-K Q3'26, EUR) ----------
fx=1.1028; px=12.81; shd=217.737+783.671/10; shb=202.681+78.3671
mc_usd=px*shd; mc=mc_usd/fx; nc=190.143-59.199; ev=mc-nc
rev=1290.0-921.075+1086.848; fcf=167.0-149.477+176.630; sbc=54.9-42.785+44.175
p('SRAD econ shs dil',round(shd,1),'basic',round(shb,1),'mc $',round(mc_usd),'EURm',round(mc),'EV',round(ev),'rev TTM',round(rev,1),'EV/Rev',round(ev/rev,2),'fwd',round(ev/1525.5,2),'9M growth',round(1086.848/921.075-1,3))
p(' FCF TTM',round(fcf,1),'yield',round(fcf/mc*100,1),'SBC',round(sbc,1),'SBC/rev',round(sbc/rev*100,1),'FCF-SBC yield',round((fcf-sbc)/mc*100,1))
eb={'FY21':23.8+32.5-5.3,'FY22':17.8+41.4-5.2,'FY23':47.2+33.7-12.8,'FY24':22.6+78.9-11.0,'FY25':118.8+86.5-10.5}
ic={'FY21':735.6+435.4,'FY22':757.4+22.8,'FY23':872.8+50.1,'FY24':929.8+46.7,'FY25':978.3+62.9}
r=[eb[k]*0.79/ic[k]*100 for k in eb]; p(' EBIT',{k:round(v,1) for k,v in eb.items()},'ROIC',[round(x,1) for x in r],'avg',round(sum(r)/5,1))
n=eb['FY25']*0.79; p(' ROIC FY25-NOPAT on Q3 IC incl cash',round(n/(690.039+59.199)*100,1),'ex cash',round(n/(690.039+59.199-190.143)*100,1),'asset-side intang+GW 1904',round(n/1904.455*100,1))
for w in (0.10,0.13):
  fv=(fcf/w+nc)/shd*fx; p(f'  D-Legacy naive FV @{w} ${round(fv,2)} P/FV',round(px/fv,2))
p(' PT Nasdaq 17.19 ->',round(px/17.19,3),'MarketBeat 19.19 ->',round(px/19.19,3))
# ---------- GENI ----------
p('GENI FY25 OI -151.3, Q3-26 OI +10.4 (first positive), 9M26 net loss -147.9')
# ---------- WYNN Tier 1 (10-Q 2026-09-30) ----------
px=85.06; sh=102.551611; mc=px*sh
ocf=1352.7-874.6+742.2; capex=660.4-489.2+533.7; oi=1118.4-843.7+758.4; da=620.6-461.2+492.7; sbc=91.9-70.9+62.8
debt=10734.2+1159.7; cash=1642.2; nd=debt-cash; eq=-217.5
fcf=ocf-capex; capn=(442.8+419.9)/2; fn=ocf-capn
p('WYNN mc',round(mc),'OCF',round(ocf,1),'capex',round(capex,1),'FCF',round(fcf,1),'yield',round(fcf/mc*100,1),'norm FCF',round(fn,1),'yield',round(fn/mc*100,1),'SBC',round(sbc,1))
p(' EBITDA',round(oi+da,1),'ND',round(nd,1),'ND/EBITDA',round(nd/(oi+da),2))
nn=oi*0.79; p(' ROIC incl',round(nn/(eq+debt)*100,1),'ex',round(nn/(eq+debt-cash)*100,1),'vs 0.5xWACC 5.0%')
f3=(805.1+1006.3+692.3)/3
for f,lab in ((fcf,'TTM'),(fn,'norm maint capex'),(f3,'FY23-25 avg')):
  fv=f/0.103/sh; p(f'  naive FV {lab} {round(f)} @CoE10.3%',round(fv,2),'P/FV',round(px/fv,2))
