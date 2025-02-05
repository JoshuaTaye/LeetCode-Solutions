def repeating(s):
    res = []
    count = 0
    while count < len(s):
        res.append(s[count])
        s = s[count:]
        count += 1
    print("".join(res))
n  = int(input())
strr = input()
repeating(strr)