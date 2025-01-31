def subArraySum(arr,k):
    ps = 0
    sol = 0
    prefixes = {0:1}
    for i in range(len(arr)):
        ps += arr[i]
        diff = ps - k
        if diff in prefixes:
            sol += prefixes[diff]
        if ps in prefixes:
            prefixes[ps] += 1
        else:
            prefixes[ps] = 1
    return sol

print(subArraySum([1, -1, 1,1,1,1], 3))