def reverseWords(s):
    s = s.split(" ")
    print(s)
    rev = ""
    new = []
    for i in range(len(s)):
        if len(s[i]) != 0:
            new.append(s[i])
    print(new)
    for i in range(len(new)-1, -1, -1):
        rev += new[i]
        if i  != 0:
            rev += " "
    return rev

print(reverseWords("  hello world  "))