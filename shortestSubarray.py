def shortestSubarray(arr, k):
    l = 0
    minLen = float("inf")
    summ = 0
    r = 0
    while r < len(arr):
        # print(l, r)
        # print(summ)
        if summ < k:
            if arr[l] >= 0:
                summ += arr[r]
                r += 1
                print(summ, r)
            else:
                summ -= arr[l]
                l += 1
        while summ >= k:
            summ -= arr[l]
            l += 1
            minLen = min(minLen, r - l + 1)
    if minLen == float("inf"):
        return -1
    return minLen



print(shortestSubarray([84,-37,32,40,95], 167))