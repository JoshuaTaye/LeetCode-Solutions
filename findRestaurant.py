def findRestaurant(list1, list2):
    hm = {}
    res = []
    minVal = float("inf")
    if len(list1) >= len(list2):
        bigList = list1
        smallList = list2
    else:
        bigList = list2
        smallList = list1
    i = 0
    while i < len(smallList):
        if list1[i] not in hm:
            hm[list1[i]] = i
        else:
            if (hm[list1[i]] + i) == minVal:
                res.append(list1[i])
            elif hm[list1[i]] + i < minVal:
                res = [list1[i]]
                minVal = hm[list1[i]] + i
            hm[list1[i]] += i
        if list2[i] not in hm:
            hm[list2[i]] = i
        else:
            if (hm[list2[i]] + i) == minVal:
                res.append(list2[i])
            elif (hm[list2[i]] + i) < minVal:
                res = [list2[i]]
                minVal = hm[list2[i]] + i

            hm[list2[i]] += i
        i += 1
    while i < len(bigList):
        if bigList[i] not in hm:
            hm[bigList[i]] = i
        else:
            if (hm[bigList[i]] + i) == minVal:
                res.append(bigList[i])
            elif hm[bigList[i]] + i < minVal:
                res = [bigList[i]]
                minVal = hm[bigList[i]] + i

        i += 1
    return res


print(findRestaurant(["S","TEXP","BK","KFC"], list2 =["KFC","BK","S"] ))