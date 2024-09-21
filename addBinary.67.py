def addBinary(a, b):
    if len(a) < len(b):
        smol = a
        big = b
    else:
        smol = b
        big = a
    res = ''
    alegn = 0
    for i in range(-1, -1 * len(smol)-1, -1):
        if smol[i] == '0' and big[i] == '0':
            if alegn == 1:
                res = "1" + res
                alegn = 0
            else:
                res = "0" + res
        elif (smol[i] == "1" and big[i] == "0") or (smol[i] == "0" and big[i] == "1"):
            if alegn == 1:
                res = "0" + res
            else:
                res = "1" + res
        elif smol[i] == "1" and big[i] == "1":
            if alegn == 1:
                res = "1" + res
            elif alegn == 0:
                res = "0" + res
                alegn = 1
    for i in range(len(big) - len(smol) - 1, -1, -1):
        if alegn == 1:
            if big[i] == "1":
                res = "0" + res
            elif big[i] == "0":
                res = "1" + res
                alegn = 0
        elif alegn == 0 and big[i] == "1":
            res = "1" + res
        elif alegn == 0 and big[i] == "0":
            res = "0" + res
    if alegn == 1:
        res = "1" + res
    return res



print(addBinary("100", "110010"))