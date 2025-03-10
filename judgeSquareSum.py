import math


def judgeSquareSum(c):
    if c == 0 or c == 1 or c == 2:
        return True
    lst = [x for x in range(int(math.sqrt(c))+1)]
    print(lst)
    for i in range(len(lst) - 1, 0, -1):
        print(math.sqrt(c - (i ** 2)))
        if int(math.sqrt(c - (i ** 2))) == math.sqrt(c - (i ** 2)):
            return True
    return False

print(judgeSquareSum(5))