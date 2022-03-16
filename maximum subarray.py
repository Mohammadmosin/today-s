#https://www.hackerrank.com/challenges/maximum-subarray-sum/problem

def maximumSum(a, m):
    mini=0
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            print(a[i:j+1])
            k=sum(a[i:j+1])%m
            if k>mini:
                mini=k
    return mini
print(maximumSum([3,3, 9, 9, 5],5))