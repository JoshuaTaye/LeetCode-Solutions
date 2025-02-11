def removeComments(source):
    s = "\n".join(source)
    res = ""
    i = 0
    while i < len(s):
        two = s[i:i+2]
        if two == "//":
            i += 2
            while i < len(s) and s[i] != "\n":
                i += 1
        elif two == "/*":
            i += 2
            while s[i:i+2] != "*/":
                i +=1
            i += 2
        else:
            res += s[i]
            i += 1
    a = []
    for x in res.split("\n"):
        if x != "":
            a.append(x)
    return a
print(removeComments(
# ["a/*comment", "line", "more_comment*/b"]
[
 "struct Node{",
 "    /*/ declare members;/**/",
 "    int size;",
 "    /**/int val;",
 "};"]
))

# if "*/" in source[i]:
#     x = source[i].split("/*")
#     y = x.split("*/")
#     print(x)
#     print(y)
#     source[i] = ["".join(x[0] + y[1])]
# else:
#     source[i] = source[i].split("/*")
#     source[i] = source[i][0]
#     i += 1