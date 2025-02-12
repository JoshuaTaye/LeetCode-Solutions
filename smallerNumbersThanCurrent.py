from collections import Counter


def smallerNumbersThanCurrent(nums):
    p = sorted(nums, reverse=True)
    k = {}
    for i in range(len(p)):
        if p[i] not in k:
            k[p[i]] = 1
        else:
            k[p[i]] += 1
    res = {}
    print(k)
    summ = [k[p[0]]]
    for o in range(1,len(k)):
        print(k[p[o]])
        summ.append(summ[o-1] + k[p[o]])
    print(summ)
    j = 0
    for i in k:
        res[i] = sum(list(k.values())[j + 1:])
        j += 1
    fin = []
    for i in nums:
        fin.append(res[i])
    return fin



print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))