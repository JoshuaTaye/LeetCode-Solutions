def validAnagram(s, t):
    if len(s) != len(t):
            return False
    while len(s) > 0:
        if s[0] not in t:
            return False
        t = t.replace(s[0], "", 1)
        s = s.replace(s[0], "", 1)
    return True

print(validAnagram("aacc","caac"))