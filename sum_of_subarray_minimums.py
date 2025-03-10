from collections import deque


def sumSubarrayMinimums(arr):
    res = 0
    n = len(arr)
    stack = deque()
    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:
            j = stack.pop()
            if stack:
                l = j - stack[-1]
            else:
                l = j + 1
            r = i - j
            res = res + arr[j] * l * r
    for i in range(len(stack)):
        j = stack[i]
        if i > 0:
            l = j - stack[i - 1]
        else:
            l = j + 1
        r = len(arr) - j
        res = res + arr[j] * l * r
    return res % (10 ** 9 + 7)

print(sumSubarrayMinimums([23,80,34,82,11]))
