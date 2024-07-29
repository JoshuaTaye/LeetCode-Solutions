def search_insert(nums, target):
    for i in range(len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)


arr = [1, 3, 5, 6]
n = 5
print(search_insert(arr, n))
