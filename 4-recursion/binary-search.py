def binary_search(target, l, low, high):
    if low > high:
        return False
    else:
        mid = (high + low)//2
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            return binary_search(target, l, low=mid+1, high=high)
        else:   # l[mid] > target
            return binary_search(target, l, low=low, high=mid-1)

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    print(binary_search(1, l, 0, len(l)-1))
    print(binary_search(2, l, 0, len(l)-1))
    print(binary_search(3, l, 0, len(l)-1))
    print(binary_search(4, l, 0, len(l)-1))
    print(binary_search(5, l, 0, len(l)-1))
    print(binary_search(6, l, 0, len(l)-1))
    print(binary_search(0, l, 0, len(l)-1))