def minSubArrayLen(target, nums):
    if len(nums) == 1:
        if nums[0] >= target:
            return 1
        else:
            return 0
    if max(nums) > target:
        return 1
    left = 0
    right = 1
    res = []
    maxSum = nums[right] + nums[left]
    right += 1
    lenn = 2
    p = False
    if maxSum >= target:
        p = True
        res.append(lenn)
    while right < len(nums):
        if maxSum + nums[right] < target:
            maxSum += nums[right]
            right += 1
            lenn += 1
        else:
            res.append(lenn)
            maxSum -= nums[left]
            lenn -= 1
            left += 1
    print(res)
    for i in range(1, len(res)):
        res[i] += 1
    if len(res) == 0:
        return 0
    if len(res) == 1:
        if p:
            return res[0]
        return res[0] + 1
    return min(res)
print(minSubArrayLen(15, [2, 14]))