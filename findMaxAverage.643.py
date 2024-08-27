def findMaxAverage(nums, k):
    if len(nums) == 1:
        return nums[0]
    if k == 1:
        maxx = nums[0]
        for i in nums:
            if i > maxx:
                maxx = i
        return maxx
    if len(nums) == k:
        summ = 0
        for i in nums:
            summ += i
        return summ / k
    else:
        maxSum = 0
        ind = 0
        for i in nums[ind:k]:
            maxSum += i
        currSum = maxSum
        for i in range(k, len(nums)):
            currSum = currSum - nums[ind] + nums[i]
            if maxSum < currSum:
                maxSum = currSum
            ind += 1
        return maxSum / k

print(findMaxAverage([6,8,6,8,0,4,1,2,9,9], 2))
# p = len(nums)-k+1
# for i in range(1, p):
#     summ = 0
#     for j in nums[i:i+k]:
#         summ += j
#     if summ > maxSum:
#         maxSum = summ
# return maxSum/k