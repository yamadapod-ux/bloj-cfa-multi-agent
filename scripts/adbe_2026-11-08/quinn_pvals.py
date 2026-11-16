import math
# Student-t two-sided p via numerical integration (no scipy)
def tpdf(x,df): return math.gamma((df+1)/2)/(math.sqrt(df*math.pi)*math.gamma(df/2))*(1+x*x/df)**(-(df+1)/2)
def p2(t,df,n=20000):
    t=abs(t); h=t/n; s=sum(tpdf(i*h+h/2,df) for i in range(n))*h
    return 1-2*s
def pz(z): return math.erfc(abs(z)/math.sqrt(2))
for name,t,df in [('RPO 8Q slope',-1.48,6),('RPO Welch last4 vs prior8',-1.61,6.4),('Gap 8Q slope',-2.67,6),('Gap Welch',-2.04,5.1),('Revenue 8Q slope',3.41,6),('DefRev Welch',3.57,8.9),('cRPO slope',-0.09,6)]:
    print(f"{name}: t={t} df={df} p(two-sided)={p2(t,df):.3f}")
for name,z in [('RPO latest z',-1.59),('Gap latest z',-1.80),('cRPO z',-1.02)]:
    print(f"{name}: z={z} p two-sided={pz(z):.3f} one-sided={pz(z)/2:.3f}")
