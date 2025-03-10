def length(s):
    if s == "":
        return 0
    sett = {}
    maxLen = 0
    l = 0
    r = 0
    while r < len(s):
        if s[r] not in sett:
            sett[s[r]] = 1
            maxLen = max(r - l + 1, maxLen)
            r += 1
        else:
            while s[r] in sett:
                del sett[s[l]]
                l += 1
    return maxLen

print(length("abcabcbb"))
