def separateDigits(nums):
    fin = []
    for i in nums:
        strI = str(i)
        for j in strI:
            fin.append(int(j))
    print(fin)

print(separateDigits([13,25,83,77]))