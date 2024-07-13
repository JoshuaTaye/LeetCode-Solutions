def strToInt(a):
    negative = False
    l = a.lstrip(" ")
    if len(l) == 0:
        return 0
    while l[0] == '-' or l[0] == '+':
        if l[0] == '-':
            if len(l)>1 and not(l[1].isdigit()):
                return 0
            negative = True
            l = l.replace(l[0],'')
        elif l[0] == '+':
            if len(l) > 1 and not(l[1].isdigit()):
                return 0
            l = l.replace(l[0],'')
    if len(l) == 0:
        return 0
    digit = ''
    for i in range(len(l)):
        if not(l[i].isdigit()):
            break
        digit += l[i] 
    for i in digit:
        if not(i.isdigit()):
            return 0
    if len(digit) == 0:
        return 0
    x = int(digit)
    if negative == True:
        x = -abs(x)
    if x <= (-2**31):
        return -2**31 
    elif x >= (2**31):
        return 2**31 -1
    return x
st = str(input())
print(strToInt(st))

# a = 'asdfsadf'
# a = a.replace(a[0],'',1)
# print(a)
