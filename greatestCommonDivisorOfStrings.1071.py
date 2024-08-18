def gcdOfStrings(s1, s2):
    # result = [[]]
    # i = 0
    # j = 0
    # ind = 0
    # while j < len(s2) and i < len(s1):
    #     if s1[i] == s2[j]:
    #         if len(result[ind]) == 0:
    #             result[0].append(s1[i])
    #         else:
    #             if s1[i] != result[ind][0]:
    #                 result[ind].append(s1[i])
    #             else:
    #                 result.append([])
    #                 ind += 1
    #                 result[ind].append(s1[i])
    #             if set(result[0]) <= set(result[ind]) and len(result[ind]) > len(result[0]):
    #                 for k in range(len(result[ind])):
    #                     result[0].append(result[ind][k])
    #                 result.remove(result[ind])
    #                 ind = 0
    #     else:
    #         return ''
    #     i += 1
    #     j += 1
    # newInd = 0
    # while i < len(s1) and newInd < len(result[0]):
    #     if s1[i] != result[0][newInd]:
    #         return ''
    #     else:
    #         newInd += 1
    #         i += 1
    # newInd2 = 0
    # while j < len(s2) and newInd2 < len(result[0]):
    #     if s2[j] != result[0][newInd2]:
    #         return ''
    #     else:
    #         newInd2 += 1
    #         j += 1
    # f = ''
    # for i in range(len(result[0])):
    #     f += result[0][i]
    # return f
    if len(s1) < len(s2):
        smaller = s1
        bigger = s2
    else:
        smaller = s2
        bigger = s1
    result = ''
    final = ''
    i = 0
    while i < (len(smaller)):
        if s1[i] != s2[i]:
            return ''
        result += smaller[i]
        if len(bigger) % len(result) == 0 and len(smaller) % len(result) == 0:
            final = result
        i += 1
    newInd = 0
    while i < (len(bigger) and newInd < len(result)):
        print(bigger[i], result[newInd])
        if bigger[i] != result[newInd]:
            return ''
        newInd += 1
        i += 1
    f = ''
    for i in range(len(bigger)):
        if final * i == bigger:
            f = final
    return f



print(gcdOfStrings("ABCABC", "ABC"))
# print(gcdOfStrings("ABC", "ABCABCABCABC"))
# print(gcdOfStrings("AA", "A"))
