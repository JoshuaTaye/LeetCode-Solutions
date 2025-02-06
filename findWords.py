def findWords(words):
    hm = {}
    res = []
    rows = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
    for i in range(len(words)):
        flag = True
        for k in range(len(words[i])):
            if words[i] not in hm:
                for j in range(len(rows)):
                    if words[i][k] in rows[j]:
                        hm[words[i]] = j
                        break
            else:
                for j in range(len(rows)):
                    if words[i][k] in rows[j]:
                        if hm[words[i]] != j:
                            flag = False
        if flag:
            res.append(words[i])
    return res

print(findWords(["Hello","Alaska","Dad","Peace"]))