def singleNumber(nums):
    mapp = []
    x = len(nums)
    for i in range(x):
        if nums[i] in mapp:
            mapp.remove(nums[i])
        else:
            mapp.append(nums[i])
    return mapp[0]


print(singleNumber([2, 2, 1]))