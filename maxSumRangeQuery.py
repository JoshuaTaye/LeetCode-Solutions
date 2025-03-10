from collections import defaultdict
def maxSumRangeQuery(nums, requests):
    x = [0]  * (len(nums)+ 1)
    for i in range(1, len(requests)):
        x[requests[i][0]] += 1
        x[requests[i][1]+1] -= 1
    for o in range(1, len(x)):
        x[o] = x[o-1] + x[o]
        
    hm = {}
    for i in range(len(x)):
        hm[i] = x[i]
    new_nums = [0]*len(nums)
    c = sorted(hm.items(),key = lambda item: item[-1])
    # nums.sort()
    for t in range(len(nums)):
        new_nums[c[t][0]] = nums[t]
    for k in range(1, len(new_nums)):
        new_nums[k] = new_nums[k-1] + new_nums[k]
    res = 0
    for j in requests:
        if j[0] == 0:
            res += new_nums[j[1]]
        else:
            res += (new_nums[j[1]] - (new_nums[j[0] - 1]))
    return res



print(maxSumRangeQuery([1, 2, 3, 4, 5,10] ,[[0,2],[1,3],[1,1]]))