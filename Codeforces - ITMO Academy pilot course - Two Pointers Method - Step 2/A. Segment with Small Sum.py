n = list(map(int, input().split()))
nums = list(map(int , input().split()))
length = n[0]
target = n[1]
summ = 0
ans = 0
left = 0
for right in range(length):
    print(nums[left:right+1])
    summ += nums[right]
    while summ > target:
        summ -= nums[left]
        left += 1
    ans = max(ans, right - left + 1)
print(ans)


