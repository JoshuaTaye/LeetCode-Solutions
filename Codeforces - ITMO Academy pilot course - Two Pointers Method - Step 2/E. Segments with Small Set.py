n = list(map(int, input().split()))
nums = list(map(int , input().split()))
length = n[0]
k = n[1]

hash_map = {}
maxLen = 0
l = 0
r = 0
for r in range(length):
    if nums[r] not in hash_map:
        hash_map[nums[r]] = 1
    else:
        hash_map[nums[r]] += 1
    while len(hash_map) > k:
        if hash_map[nums[l]] > 1:
            hash_map[nums[l]] -= 1
        else:
            del hash_map[nums[l]]
        l += 1
    maxLen += r - l + 1
print(maxLen)
