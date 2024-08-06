def climbStairs(n):
    def factorial(x):
        f = 1
        for j in range(x, 1, -1):
            f *= j
        return f
    combination = 1
    if n % 2 == 0:
        combination += 1
    twos = 1
    while twos <= n:
        if n - (twos * 2) > 0:
            ones = n - twos * 2
            added = factorial(twos + ones)/(factorial(twos) * factorial(ones))
            combination += added
            twos += 1
        else:
            return int(combination)
    return int(combination)


print(climbStairs(6))
