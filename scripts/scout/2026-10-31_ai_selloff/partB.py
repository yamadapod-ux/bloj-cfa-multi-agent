from hist import *
import json,sys
L=sys.argv[1:]
EBITDA_DA=DA
for t in L:
    try:
        y=ych(t,'1y','1d'); ts=[time_.strftime('%Y-%m-%d',time_.gmtime(z)) for z in y['timestamp']]; q=y['indicators']['quote'][0]
        cl=q['close']; hi=max(x for x in q['high'] if x); hid=ts[[i for i,x in enumerate(q['high']) if x==hi][0]]
        def at(d):
            i=bisect.bisect_right(ts,d)-1
            while cl[i] is None:i-=1
            return cl[i]
        p=y['meta']['regularMarketPrice']; p21=at('2026-10-21'); p1=at('2026-09-30')
        f=facts(t); rs=[x for x in series(f,REV) if x.get('start')]; e=max(x['end'] for x in rs)
        r=ttm_at(f,REV,e); cfo=ttm_at(f,CFO,e); cx=ttm_at(f,CAPEX,e) or 0; oi=ttm_at(f,OPI,e); da=ttm_at(f,DA,e) or 0
        eq=inst1(f,EQ,e); d=debt(f,e); c=mkt(f,e)
        try: sh,_=shares_cover(f)
        except Exception: sh=shares(f,e,[])
        mc=p*sh; ev=mc+d-c; ebitda=(oi or 0)+da; ic=(eq or 0)+d-c
        fcf=(cfo or 0)-cx
        # 5y FCF avg
        fys=sorted({x['end'] for x in rs if 350<=dur(x)<=380})[-5:]
        fl=[]
        for fe in fys:
            C=ttm_at(f,CFO,fe); X=ttm_at(f,CAPEX,fe) or 0
            if C is not None: fl.append(C-X)
        print(f"{t:5} end {e} px {p:8.2f} hi {hi:8.2f}@{hid} off {100*(p/hi-1):6.1f}% | 9/30→10/21 {100*(p21/p1-1):+6.1f}% 10/21→10/30 {100*(p/p21-1):+6.1f}% | mcap {mc/1e9:6.1f}B rev {r/1e9 if r else 0:6.1f} EBIT {(oi or 0)/1e9:6.2f} EBITDA {ebitda/1e9:6.2f} FCF {fcf/1e9:6.2f} FCFy {100*fcf/mc:5.1f}% 5yavgFCF {(sum(fl)/len(fl))/1e9 if fl else 0:6.2f} EV/EBITDA {ev/ebitda if ebitda>0 else 0:5.1f} ND/EBITDA {(d-c)/ebitda if ebitda>0 else 0:4.1f} Eq {(eq or 0)/1e9:6.1f} ROICpre {100*(oi or 0)*0.79/ic if ic>0 else 0:5.1f}%")
    except Exception as ex: print(t,'ERR',repr(ex)[:150])
