def prefix_avg2(s):
    averages = [0] * len(s)
    for i in range(len(s)):

        # sum() is O(n), so this function is O(n^2)
        averages[i] = sum(s[:i+1])/(i+1)
    return averages

def prefix_avg3(s):
    averages = [0] * len(s)

    # we might as well re-use the previous sum calculation
    # in each step
    total = 0
    for i in range(len(s)):
        total += s[i]
        averages[i] = total / (i+1)
    return averages

if __name__ == '__main__':
    s = [8, 8, 7, 6, 4, 1, 5, 8, 9, 3]
    print(prefix_avg3(s))