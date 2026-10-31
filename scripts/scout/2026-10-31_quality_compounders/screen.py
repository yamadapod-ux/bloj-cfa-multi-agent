# Quality Compounder screen 2026-10-31 (brief 2026-10-28). SEC companyfacts + Yahoo + Nasdaq + stockanalysis consensus.
from hist import *
import json, re, math, sys, statistics as st
Rf=0.04929; ERP=0.042; TGR=0.03; RONT=0.20
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120'}
def sa(t):
    fn=f'sa_{t}.html'
    if not os.path.exists(fn):
        open(fn,'w',encoding='utf8').write(u.urlopen(u.Request(f'https://stockanalysis.com/stocks/{t.lower()}/forecast/',headers=UA),timeout=30).read().decode('utf8','ignore'))
    h=open(fn,encoding='utf8').read()
    g1=re.search(r'revenueThis:\{last:[0-9.e]+,this:[0-9.e]+,growth:(-?[0-9.]+)',h); g2=re.search(r'revenueNext:\{last:[0-9.e]+,this:[0-9.e]+,growth:(-?[0-9.]+)',h)
    tg=re.search(r'targets:\{low:([0-9.]+),high:([0-9.]+),count:(\d+),median:([0-9.]+),average:([0-9.]+),updated:"([0-9-]+)"',h)
    return dict(g=[float(x.group(1))/100 for x in (g1,g2) if x], pt=tg.groups() if tg else None)
def nasdaq(t):
    r=u.Request(f'https://api.nasdaq.com/api/quote/{t}/info?assetclass=stocks',headers={'User-Agent':'Mozilla/5.0','Accept':'application/json'})
    d=json.loads(u.urlopen(r,timeout=20).read())['data']
    return float(d['primaryData']['lastSalePrice'].strip('$').replace(',','')), d['primaryData']['lastTradeTimestamp'], d['keyStats']['fiftyTwoWeekHighLow']['value']
def beta(t):
    a=ych(t,'5y','1mo'); b=ych('^GSPC','5y','1mo')
    A=dict(zip(a['timestamp'],a['indicators']['adjclose'][0]['adjclose'])); B=dict(zip(b['timestamp'],b['indicators']['adjclose'][0]['adjclose']))
    k=[x for x in sorted(A) if x in B and A[x] and B[x]]
    ra=[A[k[i]]/A[k[i-1]]-1 for i in range(1,len(k))]; rb=[B[k[i]]/B[k[i-1]]-1 for i in range(1,len(k))]
    ma,mb=st.mean(ra),st.mean(rb); cov=sum((x-ma)*(y-mb) for x,y in zip(ra,rb))/(len(ra)-1)
    return cov/st.variance(rb)
SBC=['ShareBasedCompensation','AllocatedShareBasedCompensationExpense']
def ttm2(f,c,e):
    v=ttm_at(f,c,e)
    if v is not None: return v
    s=[x for x in series(f,c) if x.get('start') and 350<=dur(x)<=380 and x['end']<=e]
    return max(s,key=lambda x:x['end'])['val'] if s else None
def roic_at(f,e):
    oi=ttm2(f,OPI,e); tx=ttm2(f,TAX,e); pti=ttm2(f,PTI,e)
    if oi is None: return None,None
    tax=min(max(tx/pti,0.15),0.27) if (pti and tx is not None) else 0.21
    eq=inst1(f,EQ,e) or 0; ic=eq+debt(f,e)-mkt(f,e)
    return (oi*(1-tax)/ic if ic>0 else float('nan')), tax
def path(c):
    g=list(c)[:2] or [0.05]; last=g[-1]; n=10-len(g)
    return g+[last+(TGR-last)*i/n for i in range(1,n+1)]
def dcf(o,k=1.0,W=None,ront=RONT,m=None):
    W=W or o['wacc']; m=o['m'] if m is None else m; R=o['rev']; r1=min(o['roic'],1.0); pv=0
    for i,gi in enumerate([k*x for x in path(o['cg'])]):
        R*=1+gi; nop=R*m*(1-o['tax']); ron=r1+(ront-r1)*i/9
        pv+=nop*(1-max(gi,0)/ron)/(1+W)**(i+1)
    tv=R*(1+TGR)*m*(1-o['tax'])*(1-TGR/ront)/(W-TGR); pvtv=tv/(1+W)**10
    return (pv+pvtv-o['nd'])/o['sh'], pvtv/(pv+pvtv)
def solvek(o):
    lo,hi=-1.0,6.0
    for _ in range(80):
        mid=(lo+hi)/2
        if dcf(o,mid)[0]<o['price']: lo=mid
        else: hi=mid
    return mid
out={}
for t in (sys.argv[1:] if __name__=="__main__" else []):
  try:
    f=facts(t); rows,sp=run(t); e=rows[-1][0]
    y=ych(t,'1y','1d'); price=y['meta']['regularMarketPrice']
    np_,nd_date,rng=nasdaq(t); s=sa(t)
    sh=shares(f,e,sp); nd=debt(f,e)-mkt(f,e); r=ttm_at(f,REV,e)
    rpy=ttm_at(f,REV,rows[-5][0]) if len(rows)>=5 else None
    oi=ttm2(f,OPI,e); ro,tax=roic_at(f,e)
    cfo=ttm2(f,CFO,e); cx=ttm2(f,CAPEX,e) or 0; sbc=ttm2(f,SBC,e) or 0; da=ttm2(f,DA,e) or 0
    fys=sorted({x['end'] for x in series(f,REV) if x.get('start') and 350<=dur(x)<=380})[-5:]
    rh=[roic_at(f,d)[0] for d in fys]
    b=beta(t); bb=0.67*b+0.33; E_=price*sh; D_=debt(f,e); ke=Rf+bb*ERP; kd=(Rf+0.008)*0.79
    wacc=(E_*ke+D_*kd)/(E_+D_)
    hist5=sorted(m for (d,p,s_,rv,n,m) in rows if d>='2021-10-01'); evr=(price*sh+nd)/r
    pct=sum(1 for m_ in hist5 if m_<=evr)/len(hist5)*100
    o=dict(t=t,end=e,price=price,np=np_,ndate=nd_date,rng52=rng,sh=sh,nd=nd,rev=r,yoy=(r/rpy-1) if rpy else None,m=oi/r,tax=tax,roic=ro,roic_hist=list(zip(fys,rh)),
           cfo=cfo,capex=cx,sbc=sbc,da=da,beta=b,bb=bb,ke=ke,wacc=wacc,cg=s['g'],pt=s['pt'],evrev=evr,evrev_pct=pct,evrev_med=hist5[len(hist5)//2],n5=len(hist5))
    o['fv'],o['tvshare']=dcf(o); o['fv_wm']=dcf(o,W=wacc-0.01)[0]; o['fv_wp']=dcf(o,W=wacc+0.01)[0]; o['fv_r30']=dcf(o,ront=0.30)[0]
    o['naive']=(oi*(1-tax)/wacc-nd)/sh; o['k']=solvek(o)
    o['pfv']=price/o['fv']; o['trig']=0.85*o['fv']; o['ownfcf']=cfo-cx-sbc
    out[t]=o
    print(f"{t:5} {e} px {price:8.2f} (nasdaq {np_:8.2f}) rev {r/1e9:6.2f}B yoy {100*(o['yoy'] or 0):5.1f}% cons {[round(100*x,1) for x in s['g']]} EBITm {100*o['m']:4.1f}% ROIC {100*ro:5.1f}% hist {[round(100*x) if x==x and x is not None else None for x in rh]} beta {b:.2f}->{bb:.2f} WACC {100*wacc:.2f}%")
    print(f"      FV {o['fv']:8.2f} (W-1 {o['fv_wm']:.0f} W+1 {o['fv_wp']:.0f} RONt30 {o['fv_r30']:.0f}) naive {o['naive']:.0f} P/FV {o['pfv']:.2f} trig {o['trig']:.2f} ({100*(o['trig']/price-1):+.1f}%) impl k {o['k']:.2f} TV% {100*o['tvshare']:.0f} EV/Rev {evr:.2f} pct {pct:.0f} | ownerFCF {o['ownfcf']/1e9:.2f}B yld {100*o['ownfcf']/E_:.1f}% ND {nd/1e9:.1f}B PT {s['pt']}")
  except Exception as ex:
    import traceback; print(t,'ERR',repr(ex)); traceback.print_exc(limit=1)
if __name__=="__main__": json.dump(out,open("screen_"+sys.argv[1]+".json","w"),default=str)
