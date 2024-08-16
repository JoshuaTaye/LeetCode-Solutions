def isUgly(n):
    if n < 0:
        return False
    primes = [2]
    for i in range(1, n+1, 2):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                continue
        if prime:
            primes.append(i)
    print(primes)
    for i in primes:
        if (n % i == 0) and i != 2 and i != 3 and i != 5:
            return False
    return True


print(isUgly(214797179))
