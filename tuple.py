import math


def tupple(nums):
    arr = {}
    res = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            prod = nums[i] * nums[j]
            if  prod not in arr:
                arr[prod] = [[nums[i], nums[j]]]
            elif prod in arr:
                arr[prod].append([nums[i],nums[j]])
    for key in arr:
        if len(arr[key]) > 1:
            res +=  (len(arr[key]) * (len(arr[key]) - 1)) //2
    return res * 8

print(tupple([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]))