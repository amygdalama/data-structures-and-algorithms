def unique1(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

def unique2(s):
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True


if __name__ == '__main__':
    print(unique1([2, 5, 3, 7, 8]))
    print(unique1([2, 5, 3, 7, 7]))