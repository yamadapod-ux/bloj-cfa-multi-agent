import rdcf
from rdcf import *
def path5(c):
    g=list(c); last=g[-1]; n=5-len(g)
    for i in range(1,n+1): g.append(last+(TGR-last)*i/n)
    return g+[TGR]*5
rdcf.path=path5
for t,o in res.items():
    k=solve(t,o); tr=val(t,1.2,o)[0]
    print(f"FASTFADE {t}: implied k={k:.2f} trig ${tr:.2f} ({(tr/o['price']-1)*100:+.1f}%) FV@1.0 ${val(t,1.0,o)[0]:.0f}")
