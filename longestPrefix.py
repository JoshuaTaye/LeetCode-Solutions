def longestPrefix(s):
    x =''
    proceeding = False
    same = False
    for i in range(len(s)):
        s[i]= s[i].strip('"').strip(' "')
    if len(s) == 1:
        return s[0]
    min = 10000 
    for i in s:
        if len(i)<min:
            min = len(i)
    for i in range(min):
        for j in range(len(s)-1):
            if len(s[j]) == 0:
                return ''
            if s[j][i] != s[j+1][i]:
                if proceeding == True:
                    a = ''
                    for i in range(len(x)-1):
                        a += x[i]
                    return a
                return x
            elif s[j][i] == s[j+1][i] and same == False:
                x += s[j][i]
                proceeding = True
                same = True
        proceeding = False
        same = False
    if len(x) == 0:
        return ''
    return x
strs = input().strip('[').strip(']').split(',')
print(longestPrefix(strs))
