# SLM 2026-10-16 valuation model (VS2 v2, CoE 8.60%) — Emma RI / Quinn 3-stage RI P-W / Bear P-W + FV5 + 1.6 sensitivities. Run: python 2026-10-16_SLM_model.py
import json, math
B0=2224.0; SH0=187.95; P0=22.33; r=0.0860; DIVSHARE=0.15  # dividends ~15% of NI (TTM 103/720=14%)

def ri_model(roe_path, payout, omega=None, g_term=None, roe_s=None, r=r, B0=B0):
    """Clean-surplus RI. roe_path = ROE for explicit years. Terminal: omega-decay (CFA CV) or growing perpetuity (roe_s,g_term) after explicit."""
    T=len(roe_path); B=[B0]; NI=[]; D=[]; RI=[]
    for t,roe in enumerate(roe_path):
        ni=roe*B[-1]; ri=(roe-r)*B[-1]; pay=payout[t] if isinstance(payout,list) else payout
        d=ni*pay; NI.append(ni); RI.append(ri); D.append(d); B.append(B[-1]+ni-d)
    # PV@T of RI beyond T
    if omega is not None:
        cvT = omega*RI[-1]/(1+r-omega)
    else:
        cvT = (roe_s-r)*B[-1]/(r-g_term)
    # values at each t (aggregate intrinsic, ex-distribution)
    def V_at(k):
        pv=sum(RI[t]/(1+r)**(t+1-k) for t in range(k,T))
        return B[k]+pv+cvT/(1+r)**(T-k)
    V=[V_at(k) for k in range(T+1)]
    # value-neutral buybacks -> share path
    sh=[SH0]
    for t in range(T):
        div=NI[t]*DIVSHARE; bb=max(D[t]-div,0); px=(V[t+1]+D[t])/sh[-1]
        sh.append(sh[-1]-bb/px)
    cons = V[0]*(1+r)**T - sum(D[t]*(1+r)**(T-1-t) for t in range(T))
    return dict(V0=V[0],FV0=V[0]/SH0,V5=V[T],FV5=V[T]/sh[T],sh5=sh[T],B=B,NI=NI,RI=RI,D=D,cvT=cvT,
                consistency_V5=cons,cons_gap=V[T]/cons-1,eps1=NI[0]/SH0,pv_cv_share=(cvT/(1+r)**T)/V[0])

out={}
# ---------- EMMA (primary RI, omega 0.80, 5y) ----------
E_path=[0.27,0.26,0.25,0.24,0.23]; E_pay=0.80
E=ri_model(E_path,E_pay,omega=0.80); out['emma']=E
# Emma 1.6 sensitivity (one at a time)
sens={}
sens['P1 CoE 10.5%']=ri_model(E_path,E_pay,omega=0.80,r=0.105)['FV0']
sens['P7a omega 0.62']=ri_model(E_path,E_pay,omega=0.62)['FV0']
sens['P7b omega 0.95']=ri_model(E_path,E_pay,omega=0.95)['FV0']
p10=[0.27,0.26,0.25,0.24,0.23,0.22,0.21,0.20,0.19,0.18]
sens['P7c explicit 10y (ROE fade 1pp/yr to 18%) + omega0.80']=ri_model(p10,E_pay,omega=0.80)['FV0']
sens['P10 Y1 ROE 25% (ex gain-on-sale), path -2pp']=ri_model([x-0.02 for x in E_path],E_pay,omega=0.80)['FV0']
sens['Payout 68% (FY23-25 actual) vs 80%']=ri_model(E_path,0.68,omega=0.80)['FV0']
sens['Rf +25bp (Fed hike) CoE 9.36%']=ri_model(E_path,E_pay,omega=0.80,r=0.0936)['FV0']
out['emma_sens']=sens
# Emma cross-checks
peers={'NAVI':(-1.98,0.37,9.64),'NNI':(8.08,1.22,15.07),'OMF':(23.28,1.93,6.70),'ALLY':(9.68,0.86,6.24),'SYF':(20.79,1.62,7.27)}
fpe=sorted(v[2] for v in peers.values()); med_fpe=fpe[2]
xs=[v[0] for v in peers.values()]; ys=[v[1] for v in peers.values()]
n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs); a=my-b*mx
ssr=sum((y-(a+b*x))**2 for x,y in zip(xs,ys)); sst=sum((y-my)**2 for y in ys); r2=1-ssr/sst
out['xcheck']=dict(med_fpe=med_fpe,pe_fv=med_fpe*3.38,reg_a=a,reg_b=b,r2=r2,
   pb_at_27=a+b*27, fv_pb27=(a+b*27)*11.83, pb_at_30=a+b*30.33, fv_pb30=(a+b*30.33)*11.83,
   justified_pb_E=(0.23-0.03)/(r-0.03))
out['nogrowth']=3.15/r
# ---------- QUINN (3-stage RI, growing perpetuity, P-W) ----------
Q_near=[0.27,0.26,0.25]
def quinn(roe_s,g=0.03,r=r):
    path=Q_near+[roe_s,roe_s]; pay=[0.80,0.80,0.80,1-g/roe_s,1-g/roe_s]
    return ri_model(path,pay,roe_s=roe_s,g_term=g,r=r)
Qs={'bull':(0.25,0.25),'base':(0.20,0.50),'bear':(0.13,0.25)}
q={k:quinn(v[0]) for k,v in Qs.items()}
Q_FV=sum(q[k]['FV0']*Qs[k][1] for k in Qs); Q_FV5=sum(q[k]['FV5']*Qs[k][1] for k in Qs)
out['quinn']={k:dict(FV0=q[k]['FV0'],FV5=q[k]['FV5'],cons=q[k]['cons_gap']) for k in q}; out['quinn_pw']=dict(FV0=Q_FV,FV5=Q_FV5)
# matrix CoE x ROE_s (Quinn base structure, deterministic)
coes=[0.081,0.086,0.0911,0.101,0.111]; roes=[0.13,0.16,0.20,0.23,0.25]
out['matrix']={f"{c:.4f}":[round(quinn(s,r=c)['FV0'],2) for s in roes] for c in coes}
# market-implied: ROE_s at 9.11 that gives P0 ; CoE that gives P0 at ROE_s 20%
def solve(f,lo,hi):
    for _ in range(100):
        m=(lo+hi)/2
        if f(lo)*f(m)<=0: hi=m
        else: lo=m
    return m
out['impl_roe_s']=solve(lambda s: quinn(s)['FV0']-P0,0.06,0.30)
out['impl_coe_base']=solve(lambda c: quinn(0.20,r=c)['FV0']-P0,0.05,0.30)
out['impl_omega_emma']=solve(lambda w: ri_model(E_path,E_pay,omega=w)['FV0']-P0,0.0,0.99)
# ---------- BEAR ----------
# logged change: omega 0.80 -> 0.62 (bear-base); also show FV with pre-registered 0.80
Bb_path=[0.24,0.21,0.18,0.16,0.15]; Bb_pay=0.75
bb=ri_model(Bb_path,Bb_pay,omega=0.62); bb_pre=ri_model(Bb_path,Bb_pay,omega=0.80)
bu=ri_model([0.27,0.26,0.25,0.24,0.22],0.80,omega=0.80)   # bear's own bull pair
ex=ri_model([0.10,0.08,0.12,0.14,0.15],0.60,omega=0.50)   # recession + policy reversal
W={'bear_base':0.55,'bull_pair':0.20,'extreme':0.25}
B_FV=bb['FV0']*0.55+bu['FV0']*0.20+ex['FV0']*0.25; B_FV5=bb['FV5']*0.55+bu['FV5']*0.20+ex['FV5']*0.25
B_FV_pre=bb_pre['FV0']*0.55+bu['FV0']*0.20+ex['FV0']*0.25
out['bear']=dict(base=bb['FV0'],base_pre_omega080=bb_pre['FV0'],bull=bu['FV0'],extreme=ex['FV0'],
  FV0=B_FV,FV5=B_FV5,FV0_if_omega080=B_FV_pre,cons=[bb['cons_gap'],bu['cons_gap'],ex['cons_gap']],
  base5=bb['FV5'],bull5=bu['FV5'],ext5=ex['FV5'])
# ---------- BLEND ----------
EF=E['FV0']; EF5=E['FV5']
blend=0.40*EF+0.30*Q_FV+0.30*B_FV; blend5=0.40*EF5+0.30*Q_FV5+0.30*B_FV5
out['blend']=dict(FV0=blend,FV5=blend5,MOS=(blend-P0)/P0,ret5=(blend5/P0)**0.2-1)
# 1.6 delta % of blended FV for each Emma sens
out['sens_delta_blended']={k:(0.40*(v-EF))/blend for k,v in sens.items()}
out['emma_summary']=dict(FV0=EF,FV5=EF5,cons_gap=E['cons_gap'],B=E['B'],NI=E['NI'],RI=E['RI'],D=E['D'],sh5=E['sh5'],pv_cv_share=E['pv_cv_share'],eps1=E['eps1'])
del out['emma']
print(json.dumps(out,indent=1,default=lambda x: round(x,4)))
e2=ri_model([0.21,0.26,0.25,0.24,0.23],E_pay,omega=0.80)['FV0']
e3=ri_model([0.21,0.20,0.19,0.18,0.17],E_pay,omega=0.80)['FV0']
print('EXTRA quinn base CoE+25', quinn(0.20,r=r+0.0025)['FV0'], 'emma CoE+25', ri_model(E_path,E_pay,omega=0.80,r=r+0.0025)['FV0'])
print('EXTRA blended if quinn probs 20/40/40', 0.4*EF+0.3*(0.2*q['bull']['FV0']+0.4*q['base']['FV0']+0.4*q['bear']['FV0'])+0.3*B_FV)
def team(rr):
    e=ri_model(E_path,E_pay,omega=0.80,r=rr)['FV0']
    qq=sum(quinn(v[0],r=rr)['FV0']*v[1] for v in Qs.values())
    b=ri_model(Bb_path,Bb_pay,omega=0.62,r=rr)['FV0']*0.55+ri_model([0.27,0.26,0.25,0.24,0.22],0.80,omega=0.80,r=rr)['FV0']*0.2+ri_model([0.10,0.08,0.12,0.14,0.15],0.60,omega=0.50,r=rr)['FV0']*0.25
    return 0.4*e+0.3*qq+0.3*b
for rr in [0.0796,0.0860,0.0911,0.0924,0.105]: print('EXTRA team CoE',rr, team(rr), (team(rr)-P0)/P0)
print('EXTRA team CoE for MOS15', solve(lambda c: team(c)/P0-1.15,0.06,0.12))
print('EXTRA price for MOS15', blend/1.15)
e2=ri_model([0.21,0.26,0.25,0.24,0.23],E_pay,omega=0.80)['FV0']; e3=ri_model([0.21,0.20,0.19,0.18,0.17],E_pay,omega=0.80)['FV0']
print('EXTRA emma Y1 roe21', e2, 0.4*(e2-EF), ' path-6pp', e3, 0.4*(e3-EF), 'blend', blend+0.4*(e3-EF))
# P4 alternatives: Blume only / bottom-up only (Emma)
print('EXTRA P4 blume-only 9.24', ri_model(E_path,E_pay,omega=0.80,r=0.0924)['FV0'], 'bottomup-only 7.96', ri_model(E_path,E_pay,omega=0.80,r=0.0796)['FV0'])
# P11 TBV start (same NI path)
B0t=2224-58.5; sc=2224/B0t
et=ri_model([x*sc for x in E_path],E_pay,omega=0.80,B0=B0t)['FV0']; print('EXTRA P11 TBV start', et)
# P9 Quinn g 2% / 2.5%
for g in [0.02,0.025]:
    qg=sum(quinn(v[0],g=g)['FV0']*v[1] for v in Qs.values()); print('EXTRA P9 quinn g',g,qg, 0.3*(qg-Q_FV)/blend)
# P12 buyback at market price (P0 flat) -> Emma FV5
E2=ri_model(E_path,E_pay,omega=0.80)
V=[];
def fv5_buyback_at(price_path):
    sh=SH0
    for t in range(5):
        div=E2['NI'][t]*DIVSHARE; bb=E2['D'][t]-div; sh-= bb/price_path[t]
    return E2['V5']/sh
print('EXTRA P12 buyback at $22.33 flat FV5', fv5_buyback_at([22.33]*5), 'value-neutral FV5', E2['FV5'])
print('EXTRA bear before omega change FV', out['bear']['FV0_if_omega080'])
print('EXTRA ret5', (blend5/P0)**0.2-1)
