'''a=[1,2,3,2,5,1,2,4,6,2,7,8,6]
max=0
dict={}
for i in range(0,len(a)):
    c=0
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            c=j-i
            if c>max:
                max=c

print(max)'''
maxima=0
c=0
dict={}
a=[1,2,3,2,5,1,2,4,6,2,7,8,3]
for i in range(0,len(a)):
    if a[i] not in dict:
        dict[a[i]]=i
    else:
        c=i-dict[a[i]]
        if maxima < c:
            maxima = c

print(maxima)
