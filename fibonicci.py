
def fib(n):
    if(n==0):
        return 1
    elif n==1:
        return 1
    last = fib(n-1)
    Slast = fib(n-2)
    ans = last+Slast
    return ans
print(fib(5))