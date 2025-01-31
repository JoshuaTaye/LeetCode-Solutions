def maxProfit(arr):
    left = 0
    right = 1
    mp = 0
    while right < len(arr):
        if arr[left] < arr[right]:
            mp = max(right - left + 1, mp)
        else:
            left = right
        right += 1
    return mp

print(maxProfit([7, 1, 4, 2, 6, 4]))