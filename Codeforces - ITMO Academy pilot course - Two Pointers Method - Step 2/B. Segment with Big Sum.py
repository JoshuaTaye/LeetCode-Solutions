n = list(map(int, input().split()))
nums = list(map(int , input().split()))
length = n[0]
target = n[1]
summ = 0
ans = float("inf")
left = 0
right = 0
while left < length:
    print(nums[left:right+1])
    while right < length and summ < target:
        summ += nums[right]
        right += 1
    if summ >= target:
        ans = min(right - left, ans)
    summ -= nums[left]
    left += 1
if ans == float("inf"):
    print(-1)
else:
    print(ans)
