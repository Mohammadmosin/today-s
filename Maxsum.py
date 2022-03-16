def maxsum(arr):
    x=[min(arr)]*len(arr)
    #print(x)

    D=0
    for i in range(1,len(arr)):
        if x[i-1]>=x[i-1]+arr[i]:
            print(x[i-1])
            x[i]=arr[i]+x[i-1]
        else:
            if i+1<len(arr):
                if arr[i+1]>0:
                    D=D+arr[i]
            x[i]=x[i-1]
    res=x[len(arr)-1]
arr=[-1,-2,-3,-4,-5,-6]
maxsum(arr)
