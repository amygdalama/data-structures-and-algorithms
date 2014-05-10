def reverse(l, start=0, stop=None):
    """Reverse the elements in a list."""

    if not stop:
        stop = len(l)-1
    if start < stop:
        l[start], l[stop] = l[stop], l[start]
        reverse(l, start=start+1, stop=stop-1)

if __name__ == '__main__':
    test_set = (
        ([], []),
        ([1], [1]),
        (list(range(10)), list(range(9,-1,-1)))
        )
    for l, expected in test_set:
        original = l
        reverse(l)
        if l == expected:
            print("Success!")
        else:
            print("==========")
            print("Failure!")
            print("original: ", original)
            print("expected: ", expected)
            print("instead the stupid function returned: ", l)
