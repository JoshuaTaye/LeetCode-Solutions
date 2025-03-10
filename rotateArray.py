def rotate(nums, k):
    p = nums[-1*k:] + nums[:len(nums)-k]
    for i in range(len(nums)):
        nums[i] = p[i]
    # print(nums[-1*k:])
    # print(nums[:len(nums)-k])
    # nums[-1*k:], nums[:len(nums)-k] = nums[:len(nums)-k] , nums[-1*k:]
    return nums

print(rotate([1,2,3,4,5,6,7], 3))