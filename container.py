def container (h):
    left = 0
    right = len(h) - 1
    maxArea = 0
    while left < right:
        maxArea = max(maxArea, min(h[left], h[right]) * (right - left))
        if h[left] <= h[right]:
            left += 1
        else:
            right -= 1
    return maxArea

print(container([1,3,2,5,25,24,5]))