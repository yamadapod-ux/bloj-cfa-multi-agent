exec(open('model.py').read().split("res={}")[0])
def alt(s,ron,wacc=WACC0):
    r=run(s,full=True); rev=r['rev']; nop=r['nopat']; 
    fc=[]
    for i in range(10):
        g=rev[i]/(rev[i-1] if i else 6920)-1
        fc.append(nop[i]*(1-g/ron))
    t=[0.61+i for i in range(10)]
    pv=sum(f/(1+wacc)**tt for f,tt in zip(fc,t))
    tg=s['tgr']; nT1=rev[-1]*(1+tg)*s['tm']*(1-TAX); tv=nT1*(1-tg/s['ronic'])/(wacc-tg)
    ev=pv+tv/(1+wacc)**t[-1]+0.25*(6920*.226*(1-TAX)*0.7)/(1+wacc)**0.06
    return (ev+NONOP+CASH-DEBT-MIN)/SH
for ron in (0.12,0.15,0.20,0.25,0.40): print(ron,alt(SC['Base'],ron))
