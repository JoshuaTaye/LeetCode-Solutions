def divideIntegers(a, b):
    if abs(a) < abs(b):
        return 0
    negative = False
    if (a < 0 < b) or (a > 0 > b):
        negative = True
        a = abs(a)
        b = abs(b)
    count = 0
    while a >= b:
        divisor = b
        n = 1
        while a >= divisor:
            a -= divisor
            count += n
            n += n
            divisor += divisor
    if negative:
        count = -1 * count
    if count >= 2 ** 31:
        return (2 ** 31) - 1
    if count <= -2 * 31:
        return (-2 ** 31) + 1

    return count


print(divideIntegers(-2147483648, 1))
