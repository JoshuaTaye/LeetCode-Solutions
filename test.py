n = int(input())
lst = []
for k in range(n):
    x = int(input().strip())
    s = list(map(int, input().split()))
    i = 0
    res = 0
    while i < len(s):
        l = i
        r = i
        while r < len(s) - 1 and (s[r]*s[r+1])>0:
            r += 1
        res += max(s[l:r+1])
        i = r + 1
    print(res)

