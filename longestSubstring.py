def longestSubstring(st):
    left = 0
    right = 0
    maxSub = ""
    for i in st:
        if i in maxSub:
            break
        maxSub += i
        right += 1
    print(right, maxSub)
    sub = maxSub
    while right < len(st):
        if st[right] in sub:
            if len(sub) <= 1:
                right += 1
            else:
                sub = sub[1:]
            left += 1
        else:
            sub += st[right]
            right += 1
        print(sub)
        if len(sub) > len(maxSub):
            maxSub = sub
    return len(maxSub)


print(longestSubstring("aab"))