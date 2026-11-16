import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from quinn_dcf import run,S,lin,PRICE,WACC
base=S['Base']
def mk(x,tm,p=base):
    q=dict(p); q['g']=[x]*5+lin(x,0.045,5); q['m']=[0.345]+lin(0.345,tm,4)+[tm]*5; return q
G=[0.03,0.05,0.07,0.09,0.11]; M=[0.29,0.325,0.355,0.385,0.415]
print("Matrix A: rev CAGR FY27-31 x terminal GAAP op margin (WACC 10.10%, base RONIC 40%/20%, TGR 2.5%)")
print("g|m "+" ".join(f"{m:>8.1%}" for m in M))
for g in G: print(f"{g:4.0%} "+" ".join(f"{run(mk(g,m)):8.0f}" for m in M))
W=[0.086,0.0998,0.1010,0.1062,0.1150]
print("Matrix B: rev CAGR x WACC (terminal margin 35.5%)")
print("g|w "+" ".join(f"{w:>8.2%}" for w in W))
for g in G: print(f"{g:4.0%} "+" ".join(f"{run(mk(g,0.355),wacc=w):8.0f}" for w in W))
# reverse DCF
def solve(f,lo,hi):
    for _ in range(80):
        mid=(lo+hi)/2
        if f(mid)>PRICE: hi=mid
        else: lo=mid
    return mid
gi=solve(lambda x: run(mk(x,0.355)),-0.10,0.30)
print(f"Reverse DCF: implied FY27-31 rev CAGR at $239.30 (term margin 35.5%) = {gi:.2%}")
for tm in (0.29,0.32):
    print(f"  at terminal margin {tm:.0%}: implied g = {solve(lambda x: run(mk(x,tm)),-0.10,0.30):.2%}")
# implied terminal margin at consensus-like growth 9.1% FY27 then base path
def mkm(tm):
    q=dict(base); q['g']=[0.091]+base['g'][1:]; q['m']=[0.345]+lin(0.345,tm,4)+[tm]*5; return q
print(f"Implied terminal op margin with FY27 g=9.1% + base path: {solve(lambda t: run(mkm(t)),0.0,0.6):.2%}")
# market implied with zero growth reinvestment? perpetual growth implied on FY27 NOPAT
