def fib_bad(n):
    """Returns the nth Fibonacci number."""

    print("bad function called, n: ", n)
    if n <= 1:
        return n
    else:
        return fib_bad(n-1) + fib_bad(n-2)

def fib_better(n):
    """Returns the nth Fibonacci number."""

    print("better function called, n: ", n)
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fib_better(n-1)
        return (a+b, a)

