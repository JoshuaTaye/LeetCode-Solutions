def relativeSortArray(a1, a2):
    i2 = 0
    newA = []
    a2.sort()
    while i2 < len(a2):
        for i1 in range(len(a1)):
            if a1[i1] == a2[i2]:
                newA.append(a1[i1])
        i2 += 1
    for i in a1:
        if i not in a2:
            newA.append(i)
    return newA


print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))