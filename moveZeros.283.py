def moveZeroes(nums):
    left = 0
    i  = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[i],nums[left] = nums[left],nums[i]
            left += 1
        i += 1
    return nums

print(moveZeroes([0, 1, 0, 3, 12]))