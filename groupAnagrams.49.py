def groupAnagrams(s):
    res = []
    sortedRes = []
    b = s.copy()
    for i in range(len(s)):
        b[i] = "".join(sorted(s[i]))
    print(s)
    print(b)
    for i in range(len(s)):
        flag = False
        for k in range(len(res)):
            if b[i] == sortedRes[k][0]:
                flag = True
                res[k].append(s[i])
                sortedRes[k].append(b[i])
        if not flag:
            sortedRes.append([b[i]])
            res.append([s[i]])
    return res
#
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

