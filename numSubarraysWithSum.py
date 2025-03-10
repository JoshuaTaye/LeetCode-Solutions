from collections import defaultdict


def numSubarraysWithSum(nums, goal):
    summ = 0
    count = 0
    hm = defaultdict(int)
    hm[0] = 1
    for r in range(len(nums)):
        summ += nums[r]
        if summ - goal in hm:
            count += hm[summ-goal]
        hm[summ] += 1
    return count


print(numSubarraysWithSum([0,0,0,0, 0], 0))