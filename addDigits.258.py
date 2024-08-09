def addDigits(n):
    res = 0
    x = str(n)
    for i in x:
        res += int(i)
    while len(str(res)) > 1:
        newRes = 0
        for j in str(res):
            newRes += int(j)
            res = newRes
    return res


print(addDigits(38))