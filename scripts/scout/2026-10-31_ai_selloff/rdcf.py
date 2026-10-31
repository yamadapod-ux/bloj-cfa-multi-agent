from hist import *
import json
A=json.load(open('partA.json')); Rf=float(open('rf.txt').read()); ERP=0.042; TGR=0.03
CONS={'NVDA':[0.906,0.682],'META':[0.216],'GOOGL':[0.271],'MSFT':[0.193,0.199],'AMZN':[0.147]}
def path(c):
    g=list(c); last=g[-1]; n=10-len(g)
    for i in range(1,n+1): g.append(last+(TGR-last)*i/n)
    return g
def val(t,k,o,ronic_term=0.20,margin=None,wacc=None):
    g=[k*x for x in path(CONS[t])]
    R=o['rev']; m=margin if margin is not None else o['m']; W=wacc or o['wacc']; tax=o['tax']
    r1=min(o['roic'],1.0); pv=0
    for i,gi in enumerate(g):
        R*=1+gi; nop=R*m*(1-tax); ron=r1+(ronic_term-r1)*i/9
        fcff=nop*(1-max(gi,0)/ron); pv+=fcff/(1+W)**(i+1)
    nopT=R*(1+TGR)*m*(1-tax); tv=nopT*(1-TGR/ronic_term)/(W-TGR)
    pv+=tv/(1+W)**10
    return (pv-o['nd'])/o['sh'], tv/(1+W)**10/pv
def solve(t,o,**kw):
    lo,hi=0.0,5.0
    for _ in range(80):
        mid=(lo+hi)/2
        if val(t,mid,o,**kw)[0]<o['price']: lo=mid
        else: hi=mid
    return mid
res={}
for t,o in A.items():
    f=facts(t); e=o['end']
    oi=ttm_at(f,OPI,e); tx=ttm_at(f,TAX,e); pti=ttm_at(f,PTI,e) or ttm_at(f,['IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic'],e)
    eq=inst1(f,EQ,e); o['m']=oi/o['rev']; o['tax']=min(max(tx/pti,0.15),0.25) if pti else 0.18
    ic=eq+o['debt']-o['cash']; o['roic']=oi*(1-o['tax'])/ic; o['eq']=eq
    E=o['price']*o['sh']; D_=o['debt']; ke=Rf+o['beta_blume']*ERP; kd=(Rf+0.008)*(1-0.21)
    o['ke']=ke; o['wacc']=(E*ke+D_*kd)/(E+D_)
    k=solve(t,o); trig,tvsh=val(t,1.2,o)
    # sensitivities on trigger
    s={'ronT15':val(t,1.2,o,ronic_term=0.15)[0],'ronT30':val(t,1.2,o,ronic_term=0.30)[0],'w-1':val(t,1.2,o,wacc=o['wacc']-0.01)[0],'w+1':val(t,1.2,o,wacc=o['wacc']+0.01)[0],'m-3':val(t,1.2,o,margin=o['m']-0.03)[0],'m+3':val(t,1.2,o,margin=o['m']+0.03)[0]}
    o.update(k=k,trig_rdcf=trig,tv_share=tvsh,sens=s,fv_k1=val(t,1.0,o)[0])
    res[t]=o
    print(f"{t}: EBIT m {o['m']*100:.1f}% tax {o['tax']*100:.1f}% ROIC {o['roic']*100:.0f}% (IC {ic/1e9:.0f}B eq {eq/1e9:.0f}B) Ke {ke*100:.2f}% WACC {o['wacc']*100:.2f}% | implied k={k:.2f}x consensus | trig(1.2x) ${trig:.2f} ({(trig/o['price']-1)*100:+.1f}%) TV% {tvsh*100:.0f} | FV@1.0x ${o['fv_k1']:.0f}")
    print('    sens', {a:round(b,0) for a,b in s.items()})
json.dump(res,open('partA2.json','w'),default=str)
