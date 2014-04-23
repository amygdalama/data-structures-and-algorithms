import math

def factorial(x):
    if x < 1:
        raise ValueError("x must be greater than 1")
    elif x == 1:
        return x
    else:
        return x * factorial(x-1)


if __name__ == '__main__':
    print(factorial(5))
    print(math.factorial(5))