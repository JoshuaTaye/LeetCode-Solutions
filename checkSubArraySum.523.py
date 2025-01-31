def checkSubArraySum(nums, k):
    remainders = {0: -1}
    sums = 0
    for i in range(len(nums)):
        sums += nums[i]
        if (sums % k) not in remainders:
            remainders[sums%k] = i
        elif i - remainders[sums % k] >= 2:
            return True
    return False

print(checkSubArraySum([0, 0], 1))