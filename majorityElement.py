from collections import Counter


def majorityElement(nums):
    res = []
    freq = len(nums)//3
    c = Counter(nums)
    for i in c:
        if c[i] > freq:
            res.append(i)
    return res
print(majorityElement([3, 2, 3]))