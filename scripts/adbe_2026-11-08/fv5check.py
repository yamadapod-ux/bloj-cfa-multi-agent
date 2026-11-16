bb=[4255,4526,4803,5084,5371]; w=0.101
fvbb=sum(b*(1+w)**(5-(i+1)) for i,b in enumerate(bb))
eq5=162458; eq0=121460-724
print(fvbb, eq5+fvbb, eq0*(1+w)**5, (eq5+fvbb)/(eq0*(1+w)**5)-1)
