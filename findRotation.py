def findRotation(mat, target):
    if mat == target:
        return True
    flag = True
    j = len(mat) - 1
    for i in range(len(mat)):
        if mat[i] != target[j]:
            flag = False
        j -= 1
    if flag:
        return True

    flag = True
    for i in range(len(mat)):
        reversedTargetRow = []
        for j in range(len(mat[0])-1, -1, -1):
            reversedTargetRow.append(target[len(mat)-i-1][j])
        if mat[i] != reversedTargetRow:
            flag = False
        j -= 1
    if flag:
        return True

    flag = True
    for l in range(len(mat)):
        coll = []
        for p in range(len(mat[l])-1, -1, -1):
            coll.append(target[p][len(mat) - l - 1])
        if mat[l] != coll:
            flag = False
    if flag:
        return True
    flag = True
    for a in range(len(mat)-1, -1, -1):
        if mat[len(mat)- a -1] != sorted(target[a]):
            flag = False
    if flag:
        return True

    flag = True
    for u in range(len(mat)):
        col = []
        for v in range(len(mat[u])):
            col.append(target[v][len(mat) - u - 1])
        if mat[u] != col:
            flag = False
    if flag:
        return True

    flag = True
    for n in range(len(mat)):
        col = []
        for m in range(len(mat[n])):
            col.append(target[len(mat)-m -1][n])
        if mat[n] != col:
            flag = False
    if flag:
        return True
    return False




    # cornsrs =

print(findRotation([[1,2,3, 4],[5,6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]], [[16, 15, 14, 13],[12, 11, 10, 9],[8, 7, 6, 5],[4, 3,2,1]]))