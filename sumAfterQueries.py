def sumAfterQueries(nums, queries):
    initsum = 0
    res = []
    for j in nums:
        if not j%2:
            initsum += j
    wasOdd = False
    for i in range((len(queries))):
        if nums[queries[i][1]]%2:
            wasOdd = True
        nums[queries[i][1]] += queries[i][0]
        if not nums[queries[i][1]] % 2:
            if wasOdd:
                initsum += nums[queries[i][1]]
            else:
                initsum -= nums[queries[i][1]] - queries[i][0]
                initsum += nums[queries[i][1]]
        else:
            if not (nums[queries[i][1]] - queries[i][0]) %2:
                initsum -= nums[queries[i][1]] - queries[i][0]
        res.append(initsum)
    return res

print(sumAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))