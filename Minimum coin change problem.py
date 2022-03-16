def minimum_coins(n,c):
    pass
    minimum=[n]*(n+1)
    minimum[0]=0
    for i in range(len(c)):
        for j in range(len(minimum)):
            if j>=c[i]:
                minimum[j]=min(minimum[j],1+minimum[(j-c[i])])
                pass
            else:
                pass
    return minimum[n]
print(minimum_coins(9, [1, 2, 5]))