def runningSum(nums):
    rs = [nums[0]]
    for i in range(1, len(nums)):
        rs.append(rs[i-1] + nums[i])
    return rs


nums = [1, 2, 3, 4]
print(runningSum(nums))