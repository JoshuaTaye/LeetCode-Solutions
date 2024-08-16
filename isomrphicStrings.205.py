def isomorphicStrings(s, t):
    if len(s) != len(t):
        return False
    similarS = []
    similarT = []
    for i in range(len(s)):
        if (s[i] in similarS and t[i] not in similarT) or (s[i] not in similarS and t[i] in similarT):
            return False
        if s[i] not in similarS and t[i] not in similarT:
            similarS.append(s[i])
            similarT.append(t[i])
        else:
            if t[i] != similarT[similarS.index(s[i])]:
                return False
    return True


print(isomorphicStrings("paper", "title"))
