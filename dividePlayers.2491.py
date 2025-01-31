def dividePlayers(arr):
    arr.sort()
    l = 0
    r = len(arr) - 1
    tot = 0
    summ = arr[-1] + arr[0]
    while l < r:
        if arr[l] + arr[r] != summ:
            return -1
        tot += (arr[l] * arr[r])
        l += 1
        r -= 1
    return tot

print(dividePlayers([3, 2, 5, 1, 3, 4]))