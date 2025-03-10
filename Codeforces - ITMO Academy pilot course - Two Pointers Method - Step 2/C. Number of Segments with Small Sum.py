n = list(map(int, input().split()))
nums = list(map(int , input().split()))
length = n[0]
target = n[1]
summ = 0
ans = 0
seg = 0
left = 0
for right in range(length):
    summ += nums[right]
    while summ > target:
        summ -= nums[left]
        left += 1
    seg += 1
    ans = max(ans, right - left + 1)
print(seg)
