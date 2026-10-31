from hist import *
import json
px=json.load(open('px_NVDA.json'))
def beta(t):
    a=ych(t,'5y','1mo'); b=ych('^GSPC','5y','1mo')
    A=dict(zip(a['timestamp'],a['indicators']['adjclose'][0]['adjclose'])); B=dict(zip(b['timestamp'],b['indicators']['adjclose'][0]['adjclose']))
    k=[x for x in sorted(A) if x in B and A[x] and B[x]]
    ra=[A[k[i]]/A[k[i-1]]-1 for i in range(1,len(k))]; rb=[B[k[i]]/B[k[i-1]]-1 for i in range(1,len(k))]
    ma,mb=st.mean(ra),st.mean(rb); cov=sum((x-ma)*(y-mb) for x,y in zip(ra,rb))/(len(ra)-1)
    return cov/st.variance(rb), len(ra)
SBC=['ShareBasedCompensation','AllocatedShareBasedCompensationExpense']
out={}
for t in ['NVDA','META','GOOGL','MSFT','AMZN']:
    f=facts(t); rows,sp=run(t); e=rows[-1][0]
    price=px[t][0]; sh=shares(f,e,sp)
    nd=debt(f,e)-mkt(f,e); r=ttm_at(f,REV,e)
    ev=price*sh+nd; cur=ev/r
    hist5=[m for (d,p,s_,rv,n,m) in rows if d>='2021-10-01']
    pct=sum(1 for m in hist5 if m<=cur)/len(hist5)*100
    srt=sorted(hist5); import math
    def q(p_):
        k=(len(srt)-1)*p_; lo=math.floor(k); hi=math.ceil(k); return srt[lo]+(srt[hi]-srt[lo])*(k-lo)
    p70=q(0.70); trig_m=(p70*r-nd)/sh
    cfo=ttm_at(f,CFO,e); cx=ttm_at(f,CAPEX,e); sbc=ttm_at(f,SBC,e) or 0
    b,n=beta(t); bb=0.67*b+0.33
    # FY history FCF margin (last 5 FY)
    fys=sorted({x['end'] for x in series(f,REV) if x.get('start') and 350<=dur(x)<=380})[-5:]
    fy=[]
    for d in fys:
        R=ttm_at(f,REV,d); C=ttm_at(f,CFO,d); X=ttm_at(f,CAPEX,d); S=ttm_at(f,SBC,d) or 0
        fy.append((d,R,C,X,S,(C-X-S)/R))
    out[t]=dict(end=e,price=price,sh=sh,nd=nd,cash=mkt(f,e),debt=debt(f,e),rev=r,ev=ev,evrev=cur,pct=pct,p70=p70,min=srt[0],max=srt[-1],med=q(.5),n=len(hist5),trig_mult=trig_m,
        cfo=cfo,capex=cx,sbc=sbc,beta_raw=b,beta_blume=bb,nobs=n,fy=fy,revpy=ttm_at(f,REV,rows[-5][0]))
    o=out[t]
    print(f"{t} end {e} px {price} sh {sh/1e9:.3f}B mcap {price*sh/1e9:,.0f}B netdebt {nd/1e9:.1f} EV/Rev {cur:.2f} pctile {pct:.0f} (n={len(hist5)}, min {srt[0]:.2f} med {o['med']:.2f} p70 {p70:.2f} max {srt[-1]:.2f}) trig_mult ${trig_m:.2f} ({(trig_m/price-1)*100:.1f}%)")
    print(f"   revTTM {r/1e9:.1f} yoy {(r/o['revpy']-1)*100:.1f}% CFO {cfo/1e9:.1f} capex {cx/1e9:.1f} SBC {sbc/1e9:.1f} FCF-SBC {(cfo-cx-sbc)/1e9:.1f} margin {(cfo-cx-sbc)/r*100:.1f}% capex/rev {cx/r*100:.1f}% beta raw {b:.2f} blume {bb:.2f} n={n}")
    for d,R,C,X,S,m in fy: print(f"     FY{d} rev {R/1e9:.1f} cfo {C/1e9:.1f} capex {X/1e9:.1f} sbc {S/1e9:.1f} (FCF-SBC)/rev {m*100:.1f}%")
json.dump(out,open('partA.json','w'),default=str)
