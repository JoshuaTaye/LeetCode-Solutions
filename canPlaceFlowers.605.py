def canPlaceFlowers(arr, n):
    if n == 0:
        return True
    i = 0
    if len(arr) == 0 and arr[0] == 0:
        return True
    if arr[0] == 0 and arr[1] == 0:
        arr[0] = 1
        n -= 1
        i += 1
    while i < len(arr) - 1 and n > 0:
        if arr[i] == 0 and arr[i+1] == 0 and arr[i-1] == 0:
            arr[i] = 1
            n -= 1
        i += 1
    if arr[-1] == 0 and arr[-2] == 0 and n > 0:
        arr[-1] = 1
        n -= 1
    if n == 0:
        return True
    else:
        return False


print(canPlaceFlowers([1,0,0,0,1], 1))