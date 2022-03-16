x1=28
x2=96
v1=8
v2=2
c=0
if x1>=x2:
    r=x1
else:
    r=x2
for i in range(0,r):
    if x1+v1==x2 and x2+v2==x1:
        c=1
        break
    else:
        x1=x1+v1
        x2=x2+v2
if c==1:
    print("YES")
else:
    print("No")
