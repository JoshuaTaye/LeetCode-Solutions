def minSubArrayLen(target, nums):
    ps = [nums[0]]
    for i in range(1, len(nums)):
        ps.append(ps[i - 1] + nums[i])
    print(ps)
    if target == ps[-1]:
        return len(nums)
    elif target > ps[-1]:
        return 0
    elif ps[0] >= target:
        return 1
    else:
        minLen = float('inf')
        left = 0
        right = 0
        while left <= right < len(nums) - 1:
            print(ps[left], ps[right+1])
            if minLen == float("inf"):
                if ps[right + 1] >= target:
                    minLen = right + 2
                    left += 1
                else:
                    right += 1
            else:
                if ps[right + 1] - ps[left] >= target:
                    print(right - left + 1)
                    minLen = min(right - left + 1, minLen)
                    left += 1
                else:
                    right += 1
        return minLen


print(minSubArrayLen(4, [1, 4, 4]))
