def boats(arr, k):
    arr.sort()
    l = 0
    r = len(arr) - 1
    boat = []
    while l <= r :
        if arr[r] + arr[l] <= k:
            boat.append([arr[l], arr[r]])
            l += 1
            r -= 1
        else:
            boat.append([arr[r]])
            r -= 1
    return len(boat)

print(boats([3,2, 2, 1], 3))