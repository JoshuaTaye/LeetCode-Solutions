def twoSum(arr, n):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == n:
            return [left, right]
        elif arr[left] + arr[right] < n:
            left += 1
        else:
            right -= 1
    return -1




print(twoSum([3, 2, 3], 6))
