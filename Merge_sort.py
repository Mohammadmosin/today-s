def sort(m,n):
    p=[]
    z=[]
    c=[]
    print(m,n)
    for i in range(0,len(m)):
        for j in range(0,len(n)):
            if m[i]<=n[j] and i not in c:
                p.append(m[i])
                c.append(i)
            if m[i]>n[j] and j not in z:
                p.append(n[j])
                z.append(j)
    for k in range(0,len(n)):
        if k not in z:
            p.append(n[k])
    for k in range(0,len(m)):
        if k not in c:
            p.append(m[k])
    return p

def merge_sort(l):
    d=len(l)//2
    #print(d)
    p=[]
    if d!=0:
        k=merge_sort(l[0:d])
        m=merge_sort(l[d:len(l)])
        #print(k,m)
        p=sort(k,m)
        l=p
    return l
l=[2,3,7,4,5,17,12,56,45,6,6,87]
#l=[3,2,7,4]
print((merge_sort(l)))
#print(sort(m,n))

f=[1,2,3,4,5]
z=f
f.pop()
print(f)
print(z)