# Memory selloff scout: Filter A/B/D + Tier 1 math. Close 2026-11-05 (Yahoo = Nasdaq). SEC companyfacts for WDC/STX/SNDK; SKHY from 6-K (partial).
Rf,ERP=4.84,4.41
N={'WDC':dict(px=267.63,hi=799.87,lo=132.43,sh=374.3,cash=1314,debt=789,oth=0,b=1.92,rev=14482,ocf=4861,cap=572,op=5707,da=391,qf=1604-227,pt=622.5,ptd='10-27',fy=[1880-1122,-408-821,-294-487,1691-412,3929-418]),
'STX':dict(px=466.53,hi=1145,lo=228.61,sh=230,cash=1258,debt=2383,oth=0,b=1.85,rev=13799,ocf=4832,cap=675,op=5464,da=280,qf=1690-211,pt=1045,ptd='10-29',fy=[1657-381,942-316,918-254,1083-265,3674-569]),
'SNDK':dict(px=806.43,hi=2354.39,lo=183,sh=142.3,cash=5136+70,debt=0,oth=2289,b=1.99,rev=28971,ocf=17546,cap=181,op=20993,da=112,qf=6363-54,pt=2000,ptd='11-03',fy=[-713-219,-309-166,84-204,11671-177])}
EV={}
for t,x in N.items():
    w=(Rf+x['b']*ERP)/100; mc=x['px']*x['sh']; net=x['cash']+x['oth']-x['debt']; ev=mc-net; fcf=x['ocf']-x['cap']; avg=sum(x['fy'])/len(x['fy'])
    nf=lambda f:(f/w+net)/x['sh']; EV[t]=ev/x['rev']
    print(f"{t} off-high {100*(x['px']/x['hi']-1):.1f}% above-low +{100*(x['px']/x['lo']-1):.0f}% mcap {mc/1e3:.1f}B net {net/1e3:.2f}B EV {ev/1e3:.1f}B WACC {100*w:.2f}%")
    print(f"  FCF TTM {fcf} yield {100*fcf/mc:.1f}% | Q annualized {4*x['qf']} yield {400*x['qf']/mc:.1f}% | EV/Rev {ev/x['rev']:.2f} | EV/EBITDA {ev/(x['op']+x['da']):.1f} | opm {100*x['op']/x['rev']:.1f}%")
    print(f"  naive FV: avg-{len(x['fy'])}y FCF {avg:.0f} -> ${nf(avg):.0f} (P/FV {x['px']/nf(avg):.2f}) | TTM -> ${nf(fcf):.0f} ({x['px']/nf(fcf):.2f}) | Qx4 -> ${nf(4*x['qf']):.0f} ({x['px']/nf(4*x['qf']):.2f})")
    print(f"  price@FCFy6%(TTM) ${fcf/.06/x['sh']:.0f} | 1.5x naive(TTM) ${1.5*nf(fcf):.0f} | FCF needed for price=1.5x naive ${(x['px']/1.5*x['sh']-net)*w:.0f}M | PT med {x['pt']} ({x['ptd']}) gap +{100*(x['pt']/x['px']-1):.0f}%")
NP={'NTAP':4.36,'P':7.12}
for t,peers in {'WDC':['STX','SNDK','NTAP','P'],'STX':['WDC','SNDK','NTAP','P'],'SNDK':['WDC','STX','NTAP','P']}.items():
    v=sorted(EV.get(p,NP.get(p)) for p in peers); med=(v[1]+v[2])/2
    print(t,'peer EV/Rev',[round(a,2) for a in v],'median',round(med,2),'subject',round(EV[t],2),'ratio',round(EV[t]/med,2))
sh=14103466480000/20000; ad=123.90*10; kr1=1264000/1340.07; kr2=1132000/1362.41
print('SKHY shares(ex-treasury) M',round(sh/1e6,1),'ADS-implied common $',ad,'mcap $B',round(ad*sh/1e9,1),'| KRX 11-05 $',round(kr1,0),'premium',round(100*(ad/kr1-1),1),'| KRX 11-06 $',round(kr2,0),'premium',round(100*(ad/kr2-1),1))
print('SKHY off-high',round(100*(123.90/199.87-1),1),'KRX off-high',round(100*(1132000/2987000-1),1),'H1 capex/rev %',round(100*17595/131895,1),'Q3 op margin %',round(100*83333.818/104615.483,1))
