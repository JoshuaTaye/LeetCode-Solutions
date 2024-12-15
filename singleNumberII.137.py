def singleNumber(nums):
    mapp = {}
    for i in range(len(nums)):
        if nums[i] in mapp:
            if mapp[nums[i]] == 2:
                mapp.pop(nums[i])
            else:
                mapp[nums[i]] += 1
        else:
            mapp[nums[i]] = 1
    return list(mapp.keys())[0]
print(singleNumber([0,1,0,1,0,1,99]))