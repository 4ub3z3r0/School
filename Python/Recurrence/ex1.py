def fib(n):
    if n > 2:
        return fib(n-1) + fib(n-2)
    elif n == 1:
        return 0
    else:
        return 1

print( fib(5) )
