from functools import reduce
import math

def factorial(x):
    total = x
    for i in range(1, x):
        total *= i
    return total

def factorial_recursive(x):
    if x < 0:
        raise ValueError("x must be greater than 1")
    elif x == 0:
        return 1
    else:
        return x * factorial(x-1)

def factorial_reduce(x):
    return reduce(lambda a, x: a * x, range(1, x+1))

if __name__ == '__main__':
    print(factorial(5))
    print(factorial_recursive(5))
    print(factorial_reduce(5))
    print(math.factorial(5))