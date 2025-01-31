def characterReplacement(s, k):
    left = 0
    right = 0
    maxres = 0
    res = 0
    while right < len(s):
        curr = s[left]
        print(curr)
        while k == 0 and right < len(s):
            if s[right] == curr:
                res += 1
                right += 1
            elif s[left] != curr:
                k += 1
                res -= 1
                left += 1
                right = left + 1
        if s[right] != curr and k > 0:
            print("right", right)
            k -= 1
        res += 1
        print(res)
        right += 1
        maxres = max(res, maxres)
    return maxres


print(characterReplacement("ABAA", 0))