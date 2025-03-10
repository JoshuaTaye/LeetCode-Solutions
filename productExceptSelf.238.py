def productExceptSelf(nums):
    ps = [1]
    for j in range(len(nums)):
        ps.append(ps[j] * nums[j])
    res = []
    l = 0
    r = len(ps) - 1
    minn = float("inf")
    maxx = float("-inf")
    print(ps)
    while l < r:
        if ps[l] < minn:
            minn = ps[l]
            l += 1
        elif ps[r] > maxx:
            maxx = ps[r]
            r -= 1
        else:
            l += 1
            r -= 1
    return maxx - minn


print(productExceptSelf([-2, 1]))