def isHappy(n):
    x = n
    summ = 0
    p = 0
    while p != 100:
        for i in str(x):
            summ += int(i) ** 2
        if summ == 1:
            return True
        else:
            x = summ
            summ = 0
        p += 1
    return False


print(isHappy(2))