def largestNumber(nums):
    for i in range(len(nums)):
        nums[i] = str(nums[i])
    nums.sort(key=lambda x: x * 10, reverse=True)

    if nums[0] == '0':
        return '0'

    return ''.join(nums)
        # print(str(nums[i])[0])

print(largestNumber([30, 34, 5, 9, 3]))