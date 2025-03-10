def threeSumClosest(nums, target):
    nums.sort()
    if len(nums) == 3:
        return sum(nums)
    print(nums)
    closest = float("inf")
    ind = 0
    for i in range(len(nums)-1, -1, -1):
        if abs(nums[i] - target) < abs(closest - target):
            closest = nums[i]
            ind = i
    if ind == 0:
        min_sum = nums[1] + nums[-1] + closest
    elif ind == len(nums) - 1:
        min_sum = nums[1] + nums[-2] + closest
    else:
        min_sum = nums[0] + nums[-1] + closest
    print(closest)
    print("minsum", min_sum)
    r = len(nums) - 1
    l = 0
    while l < r:
        if l == ind:
            l += 1
        elif r == ind:
            r -= 1
        else:
            print(nums[l], closest, nums[r])
            if abs(nums[l] + closest + nums[r] - target) < abs(min_sum - target):
                min_sum = nums[l] + closest + nums[r]
            if nums[l] + nums[r]  < target:
                l += 1
            else:
                r -= 1
    return min_sum
print(threeSumClosest([-100,-98,-2,-1], -101))