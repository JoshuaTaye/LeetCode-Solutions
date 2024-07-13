def rti(x):
    num = 0
    for i in range(len(x)):
        num = 0
        for i in range(len(x)):
            if x[i] == 'M':
                num += 1000
            elif x[i] == 'D':
                num += 500
            elif x[i] == 'C':
                if (i< len(x)-1) and (x[i+1] == 'D' or x[i+1] == 'M'):
                    num -= 100
                else:
                    num += 100
            elif x[i] == 'L':
                num += 50
            elif x[i] == 'X':
                if (i< len(x)-1) and (x[i+1] == 'L' or x[i+1] == 'C'):
                    num -= 10
                else: num += 10
            elif x[i] == 'V':
                num += 5
            elif x[i] == 'I':
                if (i< len(x)-1) and (x[i+1] == 'V' or x[i+1] == 'X'):
                    num -= 1
                else:
                    num += 1
        return num
s = input()
rti(s)