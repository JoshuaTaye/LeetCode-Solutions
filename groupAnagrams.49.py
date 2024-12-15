def groupAnagrams(s):
    res = [[s[0]]]
    for i in range(1, len(s)):
        flag = False
        for k in range(len(res)):
            if "".join(sorted(s[i])) == "".join(sorted(res[k][0])):
                print("yes")
                flag = True
                res[k].append(s[i])
                break
        if not flag:
            res.append([s[i]])
    return res

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))