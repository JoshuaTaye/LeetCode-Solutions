def countBits(p):
    res = []
    for n in range(p + 1):
        if n == 0:
            res.append(0)
        elif n == 1 or n == 2:
            res.append(1)
        else:
            i = 0
            while i < n:
                if 2 ** i > n:
                    break
                else:
                    i += 1
            final = [0] * i
            final[0] = 1
            for j in range(1, i):
                difference = n - (2 ** (i - j))
                print("diff", difference, n)
                if difference > 0:
                    k = 0
                    while k < difference:
                        if 2 ** k == difference:
                            index = i - k - 1
                            final[index] = 1
                        if (2 ** k) > difference:
                            index = -1 * k
                            difference = difference - (2 ** (k - 1))
                            final[index] = 1
                            k = 0
                        else:
                            k += 1
                #     print(final)
                # else:
                #     for i in range(1, i):
                #         final.append(0)
            print(final)
            count = 0
            for i in final:
                if i == 1:
                    count += 1
            res.append(count)
    print(res)

print(countBits(5))