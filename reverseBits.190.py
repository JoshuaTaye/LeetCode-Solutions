def reverseBits(n):
    multiplier = 0
    while 2**multiplier <= n:
        multiplier += 1
    fin = [0] * multiplier
    ind = 0
    for i in range(multiplier):
        if n > 2 ** (multiplier-1):
            fin[ind] = 1
            ind += 1
            n -= (2 ** (multiplier-1))
            multiplier -= 1
        elif n == 2 ** (multiplier-1):
            fin[ind] = 1
            for j in range(ind+1, len(fin)):
                fin[j] = 0
        else:
            fin[ind] = 0
            ind += 1
            multiplier -= 1
    bit = []
    for i in fin:
        bit.append(i)
    for i in range(32 - len(fin)):
        bit.insert(0, 0)
    st = ''
    for i in range(len(bit)-1, -1, -1):
        st += str(bit[i])
    num = 0
    ind = len(st) - 1
    for i in st:
        if i == '1':
            num += 2 ** ind
            ind -= 1
        else:
            ind -= 1
    return num

print(reverseBits(0b000010100101000001111010011100))