def isSubsequence(s, t):
    if len(s) == 0:
        return True
    if s in t:
        return True
    test = ''
    ind = 0
    i = 0
    while i < len(t) and ind < len(s):
        if t[i] == s[ind]:
            test += t[i]
            ind += 1
        i += 1
    if test == s:
        return True
    return False



print(isSubsequence("ab", "baab"))