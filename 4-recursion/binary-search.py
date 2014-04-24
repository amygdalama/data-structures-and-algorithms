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
    for i in range(0, len(l)+2):
        print(binary_search(i, l, 0, len(l)-1))