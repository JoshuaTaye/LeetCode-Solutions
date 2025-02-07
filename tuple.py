import math


def tupple(nums):
    arr = {}
    for i in range(len(nums)):
        for j in range(len(nums)-1, -1, -1):
            if nums[i] != nums[j] and nums[i] * nums[j] not in arr:
                arr[nums[i] * nums[j]] = {nums[i], nums[j]}
            elif nums[i] != nums[j] and nums[i] * nums[j] in arr:
                arr[nums[i] * nums[j]].update([nums[i],nums[j]])
    p = {}
    for key in arr:
        if not len(arr[key]) % 2 and len(arr[key]) > 2:
            p[key] = arr[key]
    res = 0
    print(p)
    for i in p:
        res += math.factorial(2*(len(p[i]))//2)/ math.factorial(len(p[i])//2)
    return res

print(tupple([2,3,4,6]))