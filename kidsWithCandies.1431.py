def kidsWithCandies(c, e):
    m = 0
    result = []
    for i in range(len(c)):
        if c[i] > m:
            m = c[i]
    for i in range(len(c)):
        if (c[i] + e) >= m:
            result.append(True)
        else:
            result.append(False)
    return result

print(kidsWithCandies([2, 3, 5, 1, 3], 3))