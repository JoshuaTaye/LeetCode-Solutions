def constructTransformedArray(nums):
    result = []
    n = len(nums)
    for i in range(n):
        result.append(nums[(nums[i] + i)% n])
    print(result)

print(constructTransformedArray([3, -2, 1, 1]))