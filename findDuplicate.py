def findDupe(paths):
    hm = {}
    for i in range(len(paths)):
        decomposed = paths[i].split(" ")
        for j in range(1, len(decomposed)):
            if decomposed[j][2:] not in hm:
                hm[decomposed[j][2:]] = [decomposed[0] +"/" + decomposed[j][0] + ".txt"]
            else:
                hm[decomposed[j][2:]].append(decomposed[0] +"/" + decomposed[j][0] + ".txt")
    res = []
    for i in hm.values():
        if len(i) > 1:
            res.append(i)
    return res


print(findDupe(["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]))