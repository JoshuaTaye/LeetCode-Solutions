def findDifference(num1, num2):
    uni = [[],[]]
    for i in range(len(num1)):
        if num1[i] not in num2 and num1[i] not in uni[0]:
            uni[0].append(num1[i])
    for j in range(len(num2)):
        if num2[j] not in num1 and num2[j] not in uni[1]:
            uni[1].append(num2[j])
    return uni


print(findDifference([1,2,3], [2, 4, 6]))