def findPivotIndex(nums):
    sumLeft = 0
    sumRight = sum(nums)
    for i in range(len(nums)):
        print(sumLeft, sumRight)
        sumLeft += nums[i]
        if sumLeft == sumRight:
            return i
        sumRight -= nums[i]
    return -1
    # ps = [0]
    # for i in range(len(nums)):
    #     ps.append(ps[i] + nums[i])
    # print(ps)
    # for i in range(1, len(ps)):
    #     if ps[i-1] == ps[-1] - ps[i]:
    #         return i-1
    # return -1

print(findPivotIndex([1,7,3,6,5,6]))
