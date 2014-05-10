def power(x, n):
    """Compute x raised to the nth power."""

    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

if __name__ == '__main__':
    tests = (
        (1, 0),
        (0, 1),
        (2, 18),
        (18, 2)
        )
    for x, n in tests:
        if power(x, n) == pow(x, n):
            print("Success!")
        else:
            print("==========")
            print("Failure!")
            print("x, n: ", x, n)
            print("expected: ", pow(x,n))
            print("instead the stupid function returned: ", power(x,n))