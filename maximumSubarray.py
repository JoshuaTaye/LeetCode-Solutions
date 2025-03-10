def maxSubArray(nums):
    summ = 0
    maxSumm = float("-inf")
    left = 0
    for r in range(len(nums)):
        summ += nums[r]
        maxSumm = max(maxSumm, summ)
        while summ < 0:
            summ -= nums[left]
            left += 1
    return maxSumm

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))