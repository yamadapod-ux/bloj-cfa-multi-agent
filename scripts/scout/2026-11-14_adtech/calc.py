# TTM = FY25 - 9M25 + 9M26 ($M); from SEC companyfacts (sec_out.txt)
def ttm(fy,a,b): return fy-a+b
D={}
D['TTD']=dict(px=15.68,sh=470.2,rev=ttm(2896.3,2049.5,2139.9),oi=ttm(589.3,332.4,260.8),ocf=ttm(992.7,681.1,803.7),
 capex=ttm(197.0,170.7,226.7)+ttm(12.8,9.1,11.6),sbc=ttm(490.6,378.5,313.7),da=ttm(115.8,83.8,94.5),eq=2702.5,debt=0,cash=1229.3+420.4,restr=44.3,tax=.21,wacc=(.10,.13),g9=2139.9/2049.5-1)
D['PINS']=dict(px=19.15,sh=582.7,rev=ttm(4221.8,2902.4,3361.1),oi=ttm(319.9,18.7,-105.2),ocf=ttm(1284.3,893.1,936.6),
 capex=ttm(32.4,21.5,54.8),sbc=ttm(880.5,649.8,847.7),da=ttm(25.2,19.1,28.6),eq=3104.3,debt=982.1,cash=654.3+815.7,restr=65.5,tax=.21,wacc=(.10,.13),g9=3361.1/2902.4-1)
D['SNAP']=dict(px=5.26,sh=1760.2,rev=ttm(5931.4,4215.0,4850.3),oi=ttm(-532.2,-581.9,-168.5),ocf=ttm(656.2,386.6,713.5),
 capex=ttm(219.0,155.0,142.5),sbc=ttm(1016.8,759.6,768.0),da=ttm(163.6,120.3,136.3),eq=2230.2,debt=3486.4,cash=1019.2+1751.4,restr=128.5,tax=.21,wacc=(.10,.13),g9=4850.3/4215.0-1)
D['CRTO']=dict(px=18.03,sh=49.214,rev=ttm(1944.9,1403.8,1269.1),oi=ttm(202.8,130.3,46.4),ocf=ttm(311.2,150.5,125.4),
 capex=ttm(102.7,75.3,126.9),sbc=ttm(57.8,52.0,39.1),da=None,eq=1144.1,debt=0,cash=274.8+28.0+22.7,restr=9.9,tax=.25,wacc=(.13,.16),g9=1269.1/1403.8-1)
for t,d in D.items():
    mc=d['px']*d['sh']; nc=d['cash']-d['debt']; ev=mc-nc
    fcf=d['ocf']-d['capex']; fs=fcf-d['sbc']
    nopat=d['oi']*(1-d['tax']); nopat_adj=(d['oi']+d['restr'])*(1-d['tax'])
    ic=d['eq']+d['debt']; icx=ic-d['cash']
    print(f"\n{t}: mcap {mc:,.0f} netcash {nc:,.0f} EV {ev:,.0f} rev {d['rev']:,.1f} 9Mgrowth {d['g9']*100:+.1f}% SBC/rev {d['sbc']/d['rev']*100:.1f}%")
    print(f"  OI {d['oi']:.1f} OCF {d['ocf']:.1f} capex {d['capex']:.1f} FCF {fcf:.1f} ({fcf/mc*100:.1f}%) FCF-SBC {fs:.1f} ({fs/mc*100:.1f}%) SBC {d['sbc']:.1f}")
    if d['da']: print(f"  EBITDA {d['oi']+d['da']:.1f} EV/EBITDA {ev/(d['oi']+d['da']):.1f}x  (adj restr {ev/(d['oi']+d['da']+d['restr']):.1f}x)")
    print(f"  ROIC GAAP: incl-cash {nopat/ic*100:.1f}% ex-cash {nopat/icx*100 if icx>0 else float('nan'):.1f}% | adj restr: {nopat_adj/ic*100:.1f}% / {nopat_adj/icx*100 if icx>0 else float('nan'):.1f}%  hurdle 0.8xWACC={0.8*d['wacc'][0]*100:.1f}%")
    for w in d['wacc']:
        for lbl,f in (('FCF',fcf),('FCF-SBC',fs)):
            fv=(f/w+nc)/d['sh']; print(f"  naiveFV {lbl}@{w:.0%}: ${fv:.2f} P/FV {d['px']/fv:.2f}x")
