def fib(n):
    if n < 0:
        print("invalid input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)

def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fac(n-1)*n