def binary_sum(l, start=0, stop=None):
    stop = stop or len(l)
    if start >= stop:
        return 0
    elif start == stop - 1:
        return l[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(l, start, mid) + binary_sum(l, mid, stop)

if __name__ == '__main__':
    test_set = (
        [],
        [1],
        list(range(10))
        )
    for l in test_set:
        if binary_sum(l) == sum(l):
            print("Success!")
        else:
            print("==========")
            print("Failure!")
            print("l: ", l)
            print("expected: ", sum(l))
            print("instead the stupid function returned: ", binary_sum(l))