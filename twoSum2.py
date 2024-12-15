def twoSum(arr, n):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == n:
            return [left+1, right+1]
        elif arr[left] + arr[right] < n:
            left += 1
        else:
            right -= 1
    return -1



print(twoSum([5, 25, 75], 100))
