def hamming_weight(n: int):
    if n == 0:
        return 0
    i = 0
    while i < n:
        if 2 ** i >= n:
            break
        else:
            i += 1
    final = [0] * i
    final[0] = 1
    for j in range(1, i):
        difference = n - (2 ** (i - j))
        if difference > 0:
            k = 0
            while k < difference:
                if 2 ** k == difference:
                    index = i - k - 1
                    final[index] = 1
                    count = 0
                    for i in final:
                        if i == 1:
                            count += 1
                    return count
                if (2 ** k) > difference:
                    index = -1 * k
                    difference = difference - (2 ** (k - 1))
                    final[index] = 1
                    k = 0
                else:
                    k += 1
            print(final)
    count = 0
    for i in final:
        if i == 1:
            count += 1
    return count
    # print(final)
    return final


# num = int(input())
print(hamming_weight(561))
