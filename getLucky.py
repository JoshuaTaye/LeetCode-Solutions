def getLucky(s, k):
    parsed = ""
    for i in range(len(s)):
        parsed += str(ord(s[i])-96)
    val = 0
    for j in range(k):
        val = 0
        for l in parsed:
            val += int(l)
        parsed = str(val)
    return val


print(getLucky("leetcode", 2))