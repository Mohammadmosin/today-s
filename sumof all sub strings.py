s="123"
size = len(s)
prev = int(s[0])
total = prev
for i in range(1, size):
    print(prev)
    total = (total * 10 + int(s[i]) * (i + 1)) % (1000000007)
    prev = (total + prev) % (1000000007)
print(prev)


def fibonacciModified(t1, t2, n):
    x=[t1,t2]
    for i in range(1,n+1):
        m=x[len(x)-1]
        o=x[len(x)-2]
        m=m*m
        m=m+o
        x.append(m)
    return(x[len(x)-1-2])
print(fibonacciModified(0,1,10))

x=[2,5,7,9]
y=[4,6,9,10]
n=15

