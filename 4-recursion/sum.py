def linear_sum(l, n):
    if n == 0:
        return 0
    else:
        return l[n-1] + linear_sum(l, n-1)


if __name__ == '__main__':
    print(linear_sum([],0))
    print(linear_sum([24],0))
    print(linear_sum([24],1))
    print(linear_sum([3, 4, 57],3))
    print(sum([3, 4, 57]))