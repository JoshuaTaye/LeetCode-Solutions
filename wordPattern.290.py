def wordPattern(pattern, s):
    s = list(s.split(" "))
    if len(pattern) != len(s):
        return False
    mapp = {}
    for i in range(len(pattern)):
        if pattern[i] not in mapp.keys():
            if s[i] in mapp.values():
                return False
            mapp[pattern[i]] = s[i]
        else:
            if mapp[pattern[i]] != s[i]:
                return False
            elif s[i] in mapp.values() and list(mapp.keys())[list(mapp.values()).index(s[i])] != pattern[i]:
                return False
    return True

print(wordPattern('abc', 'dog cat dog'))

# m = {1:"true",2:"False"}
# print(m.keys())
# if "False" in m.values():
#     print (list(m.values()).index("False"))
#     print(True)
# else:
#     print(False)