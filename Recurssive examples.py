def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1

    else:
        return fib(n-1)+fib(n-2)

    #fib(4)=>((fib(3)=>fib(2)=>fib(1)+fib(0)+fib(1))+fib(2)))+fib(3)
print(fib(5))
print(1)