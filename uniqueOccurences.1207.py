def uniqueOccurences(arr):
    occ = []
    for i in range(len(arr)):
        if str(arr[i]) not in occ:
            occ.append(str(arr[i]))
            occ.append(1)
        else:
            occ[occ.index(str(arr[i]))+1] += 1
    new = []
    print(occ)
    for i in occ:
        if type(i) == int:
            if i not in new:
                new.append(i)
            else:
                return False
    return True
print(uniqueOccurences([1, 2,2,2,1,1,3]))