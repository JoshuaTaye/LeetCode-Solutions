def findPivotIndex(nums):
    sumLeft = 0
    sumRight = sum(nums)
    for i in range(len(nums)):
        print(sumLeft, sumRight)
        sumRight -= nums[i]
        if sumLeft == sumRight:
            return i
        sumLeft += nums[i]
    return -1
print(findPivotIndex([-1,-1,-1,0,-1,0]))
