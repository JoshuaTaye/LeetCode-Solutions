def pancakeFlip(arr):
    res = []
    n = len(arr)
    r = n - 1
    if sorted(arr) == arr:
        return []
    for r in range(n-1, -1, -1):
        maxInd = -1
        for i in range(r-1, -1, -1):
            if arr[i] > arr[maxInd]:
                maxInd = i
        if maxInd != r:
            arr = list(reversed(arr[:maxInd+1])) + arr[maxInd+1:]
            res.append(maxInd+1)
            arr = list(reversed(arr[:r+1])) + arr[r+1:]
            res.append(r+1)
    return res

print(pancakeFlip([3, 2, 4, 1]))