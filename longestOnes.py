def longestOnes(nums, k):
    left = 0
    max_len = 0
    for right in range(len(nums)):
        while k == 0 and nums[right] == 0:
            if nums[left] == 0:
                k += 1
            left += 1
        if nums[right] == 0:
            k -= 1
        max_len = max(max_len, right - left + 1)
    return max_len




print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))