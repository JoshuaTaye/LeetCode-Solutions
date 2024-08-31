def productExceptSelf(nums):
    count0 = 0
    multiple = 1
    for i in range(len(nums)):
        if nums[i] == 0:
            count0 += 1
        else:
            multiple *= nums[i]
    if count0 > 1:
        return [0] * len(nums)
    elif count0 == 0:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = int(multiple)
            else:
                nums[i] = int(multiple/nums[i])
    else:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = int(multiple)
            else:
                nums[i] = 0
    return nums

print(productExceptSelf([-1,1,0,-3,3]))