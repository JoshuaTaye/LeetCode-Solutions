def intToRoman(num):
    roman = []
    num = str(num)
    multiplier = 10 ** (len(num)-1)
    for i in range(len(num)):
        n = int(multiplier * int(num[i]))
        if n == 4:
            roman.append("IV")
        elif n == 9:
            roman.append("IX")
        elif n == 40:
            roman.append("XL")
        elif n == 90:
            roman.append("XC")
        elif n == 400:
            roman.append("CD")
        elif n == 900:
            roman.append("CM")
        elif n == 50:
            roman.append("L")
        elif n == 5:
            roman.append("V")
        else:
            while n >= 1000:
                roman.append("M")
                n -= 1000
            while n >= 500:
                roman.append("D")
                n -= 500
            while n >= 100:
                roman.append("C")
                n -= 100
            while n >= 50:
                roman.append("L")
                n -= 50
            while n >= 10:
                roman.append("X")
                n -= 10
            while n >= 5:
                roman.append("V")
                n -= 5
            while n >= 1:
                roman.append("I")
                n -= 1
        multiplier *= 1/10

    return "".join(roman)

print(intToRoman(58))