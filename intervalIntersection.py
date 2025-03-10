def intervalIntersection(firstList, secondList):
    p1 = 0
    p2 = 0
    lst1 = []
    lst2 = []
    for i in firstList:
        for k in range(i[0], i[1] + 1):
            lst1.append(k)
    for j in secondList:
        for l in range(j[0], j[1] + 1):
            lst2.append(l)
    print(lst1)
    print(lst2)
    f = 0
    if len(firstList) < len(secondList):
        f = len(lst1)
        bigg = lst2
        small = lst1
    else:
        f = len(lst2)
        bigg = lst1
        small = lst2

    res = []
    for p in range(f):
        if small[p] in bigg:
            res.append(small[p])
    print(res)
    fin = []
    o = 0
    while o < (len(res)-1):
        lst = []
        while o < len(res)-1 and res[o]+1 == res[o+1]:
            lst.append(res[o])
            lst.append(res[o+1])
            o += 1
        fin.append(lst)
        fin.append([res[o], res[o]])
        o += 1
    return fin



    # while p1 < len(firstList) and p2 < len(secondList):
        


print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]],
                           [[1,5],[8,12],[15,24],[25,26]]))