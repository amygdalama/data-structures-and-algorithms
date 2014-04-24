def unique_recursion(l):
    """A recursive function that determines if a sorted list
    has only unique elements."""

    if len(l) < 2:
        return True
    elif l[0] == l[1]:
        return False
    else:
        return unique_recursion(l[1:])

if __name__ == '__main__':
    print(unique_recursion(sorted([2, 5, 3, 7, 8])))
    print(unique_recursion(sorted([2, 5, 3, 7, 7])))