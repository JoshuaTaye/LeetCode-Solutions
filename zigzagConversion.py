def zigzag(s, x):
    if len(s) < x:
        return s
    lst = []
    count = 0
    while count < len(s):
        l: list = []
        for i in range(x):
            if count < len(s):
                l.append(s[count])
                count += 1
        while len(l) < x:
            l.append('')
        lst.append(l)
        l = []
        for i in range(x - 2):
            if count < len(s):
                l.insert(0, s[count])
                count += 1
        if len(l) > 0:
            l.insert(0, '')
            l.append('')
            while len(l) < x:
                l.insert(0, '')
            lst.append(l)
    print(lst)
    result = ''
    count2 = 0
    while count2 < len(s):
        for i in range(x):
            for j in range(len(lst)):
                result += (lst[j][i])
                count2 += 1
    return result


st = input()
numrows = int(input())
print(zigzag(st, numrows))
