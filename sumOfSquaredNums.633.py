import math


def judgeSquareSum(c):
    l = 0
    r = int(math.sqrt(c))
    while l <= r:
        print(l,r)
        if (l ** 2) + (r ** 2) == c:
            return True
        elif l ** 2 + r ** 2> c:
            r -= 1
        else:
            l += 1
    return False
print(judgeSquareSum(4))