import sys;sys.argv=['x'];exec(open('evh.py').read().split('for t in sys.argv')[0])
L='VST CEG NRG TLN PWR MTZ MYRG PRIM IESC POWL HUBB NVT CMI GNRC BWXT ESAB DY AGX ACM EIX PCG'.split()
for t in L:
    f=facts(t); y=ych(t)
    ts=[time_.strftime('%Y-%m-%d',time_.gmtime(z)) for z in y['timestamp']]; cl=y['indicators']['quote'][0]['close']
    sp=[(time_.strftime('%Y-%m-%d',time_.gmtime(int(k))),v['numerator']/v['denominator']) for k,v in y.get('events',{}).get('splits',{}).items()]
    ends=sorted({x['end'] for x in series(f,REV) if x.get('start') and x['end']>='2021-09-01'})
    rows=[]
    for e in ends:
        eb=ebit(f,e); da=ttm2(f,DA,e) or 0; sh=shares(f,e,sp)
        if eb is None or not sh: continue
        i=bisect.bisect_right(ts,e)-1
        while cl[i] is None:i-=1
        E=eb+da
        if E>0: rows.append((cl[i]*sh+debt(f,e)-mkt(f,e))/E)
    e=ends[-1]; eb=ebit(f,e); da=ttm2(f,DA,e) or 0; sh=shares(f,e,sp)
    if sh<1e6 or not sh: pass
    p=y['meta']['regularMarketPrice']; nd=debt(f,e)-mkt(f,e); E=eb+da
    h=sorted(rows); q33=h[int(len(h)/3)]
    trigB=(q33*E-nd)/sh
    rs=[x for x in series(f,REV) if x.get('start')]
    fys=sorted({x['end'] for x in rs if 350<=dur(x)<=380})[-5:]
    fl=[ (ttm_at(f,CFO,fe) or 0)-(ttm_at(f,CAPEX,fe) or 0) for fe in fys]
    nf=sum(fl)/len(fl); mc=p*sh; W=0.095 if mc>20e9 else (0.105 if mc>5e9 else 0.115)
    eq=inst1(f,EQ,e) or 0; ic=eq+nd; roic=eb*0.77/ic if ic>0 else float('inf')
    naive=(nf/W-nd)/sh; ft=0.8*naive
    print(f"{t:5} px {p:8.2f} mcap {mc/1e9:5.1f}B WACC {W*100:.1f}% ROIC {roic*100:5.1f}% ({roic/W*100:4.0f}% of WACC) | B-trig(EV/EBITDA p33 {q33:.1f}x) ${trigB:8.2f} ({(trigB/p-1)*100:+.0f}%) | 5yFCF {nf/1e9:5.2f}B naiveFV ${naive:8.2f} px/naive {p/naive if naive>0 else float('nan'):5.2f}x D-fast ${ft:8.2f} ({(ft/p-1)*100:+.0f}%)")
