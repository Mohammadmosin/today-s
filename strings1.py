#will be giventwo strings. Check whether the two strings have same characters
'''''def ping(st1,st2):
    k=len(st1)
    for j in range(0,len(st2)):
            if st1[0]==st2[j]:
                st1=st1[1:]
                st2=st2[0:j]+st2[j+1:]
                return ping(st1,st2)
    return len(st1)
# Write your code here
#print("sdf")
n= input()
l=[]
for i in range(0,int(n)):
    k=input()
    l.append(k)
m=[]
print(l)
for i in l:
    st=i.split(' ')
    print(st[0],st[1])
    m.append(ping(st[0],st[1]))
print(m)
'''''
s=[5,8,9]
s.pop(s.index(8))
print(s)