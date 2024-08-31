def maxOperations(nums, k):
    nums.sort()
    i = len(nums) - 1
    j = 0
    op = 0
    while j < i:
        print(nums[i], nums[j])
        if nums[i] + nums[j] == k:
            op += 1
            i -= 1
            j += 1
        elif nums[i] + nums[j] > k:
            i -= 1
        else:
            j += 1
    return op

print(maxOperations([3,1,3,4,3], 6))
