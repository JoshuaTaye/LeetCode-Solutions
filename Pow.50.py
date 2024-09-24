def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1/x
        n = -1 * n
    return x ** n

print(myPow(0.00001, 2147483647))