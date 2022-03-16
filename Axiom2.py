a=20
b=100
c=15
n=100
result=a
def find(a,b,c,n,res):
    if n>b:
        return n-c
    else:
        if n>-1:
            res=a+n+find(a,b,c,n-1,res)
            return res
        else:
            return res

print(find(20,100,15,99,0))