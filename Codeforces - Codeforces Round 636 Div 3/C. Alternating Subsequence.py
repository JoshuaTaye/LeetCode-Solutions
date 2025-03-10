n = int(input())
lst = []
for k in range(n):
    x = int(input())
    s = list(map(int, input().split()))
    lst.append(s)
for i in lst:
    print(i)
    l = 0
    r = 0
    maxLen = 0
    while r < len(i):
        if i[r] < 0 < i[r + 1] or i[r] > 0 and i[r + 1] < 0:
            break
    print(r[i])
    while r < len(i):
        while l < len(i) and pos == prevPos:
            if i[l] < 0:
                pos = False
            else:
                pos = True
            l += 1
        print(i[l:r+1])
        prevPos = pos
        maxLen = max(maxLen, r - l + 1)
        r += 1
print(maxLen)
