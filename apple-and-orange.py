#https://www.hackerrank.com/challenges/apple-and-orange/problem
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    c=0
    d=0
    for i in apples:
        if i+a>=s and i+a<=t:
            c+=1
    for j in oranges:
        if b+j<=t and b+j>=s:
            d+=1
    print(c,d)
s=2
t=3
a=1
b=5
apples=[2,1]
oranges=[2]
countApplesAndOranges(s,t,a,b,apples,oranges)
'''2 3
1 5
1 1
2
-2'''