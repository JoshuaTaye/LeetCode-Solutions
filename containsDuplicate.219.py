def containsNearbyDuplicate(nums, k):
    mapp = {}
    for i in range(len(nums)):
        print(mapp)
        if nums[i] not in mapp:
            mapp[nums[i]] = i
        else:
            if i - mapp[nums[i]] <= k:
                return True
            mapp[nums[i]] = i
    return False

print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))