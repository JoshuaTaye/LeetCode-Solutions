def majorityElement(nums):
    if len(nums) == 1:
        return nums[0]
    entries = {}
    p = int(len(nums)/2)
    for i in range(len(nums)):
        if nums[i] in entries:
            entries[nums[i]] += 1
            if entries[nums[i]] > p:
                return nums[i]
        else:
            entries[nums[i]] = 1

print(majorityElement([1]))