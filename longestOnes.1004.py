def longestOnes(nums, k):
    maxOnes = 0
    i = 0
    p = k
    if k == 0:
        started = False
        maxOnes = 0
        while i < (len(nums) - 1):
            if nums[i] == 0:
                if started:
                    break
            if nums[i] == 1 and started == False:
                maxOnes += 1
                started = True
                continue
            elif nums[i] == 1 and nums[i + 1] == 1 and started:
                maxOnes += 1
            i += 1
        if i == len(nums) - 1:
            return maxOnes
        ones = maxOnes
        left = right = i
        while right < len(nums):
            if nums[right] == 1:
                ones += 1
                right += 1
            else:
                left += 1
                right = left
                ones = 0
            maxOnes = max(maxOnes, ones)
        return maxOnes
    if k >= len(nums):
        return len(nums)

    while p > 0 and i < len(nums):
        if nums[i] == 0:
            p -= 1
        i += 1
        maxOnes += 1
    start = 0
    end = i - 1
    ones = maxOnes
    while start <= end < len(nums) - 1:
        if nums[end + 1] == 1:
            end += 1
            ones += 1
        elif p > 0 and nums[end + 1] == 0:
            p -= 1
            ones += 1
            end += 1
        elif p == 0 and nums[end + 1] == 0:
            if nums[start] == 0:
                p += 1
            start += 1
            ones -= 1
        maxOnes = max(maxOnes, ones)
    return maxOnes
print(longestOnes([0, 1, 1], 0))


