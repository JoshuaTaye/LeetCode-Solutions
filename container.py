def container (h):
    left = 0
    right = len(h) - 1
    maxArea = 1
    while left < right:
        area = (min(h[left], h[right])) * (right - left)
        maxArea = max(area, maxArea)
        if h[left] <= h[right]:
            left += 1
        else:
            right -= 1
    return maxArea

print(container([4, 3, 2, 1, 4]))