def subarraysDivByK(nums, k):
    ps = [0,nums[0]]
    n = len(nums)
    for j in range(1, n):
        ps.append(ps[j] + nums[j])
    res = 0
    hm= {}
    print(ps)
    for i in range(n+1):
        if ps[i]%k in hm:
            res += hm[ps[i]%k]
            hm[ps[i]%k] += 1
        else:
            hm[ps[i]%k] = 1
        print(hm, ps[i]%k)
    return res


print(subarraysDivByK([4,5,0,-2,-3,1], 5))
