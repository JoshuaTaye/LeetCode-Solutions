def applyOps(nums):
    res = []
    counter = 0
    i = 0
    while i < len(nums) - 1:
        print(i)
        if nums[i] == 0:
            counter += 1
        elif nums[i] == nums[i + 1]:
            print(True)
            res.append(nums[i] * 2)
            counter += 1
            i += 1
        else:
            res.append(nums[i])
        i += 1
        for i in range(len(nums)):
            print(nums[i])
    print(counter)
    for i in range(counter):
        res.append(0)
    print(res)


print(applyOps([1, 2, 2, 1, 1, 0]))
