def indexOfFirstOccurence(str1, str2):
    if str1 == str2:
        return 0
    n = len(str2)
    for i in range(len(str1)-n+1):
        print(str1[i:i+n])
        if str1[i:i+n] == str2:
            return i
    return -1


print(indexOfFirstOccurence("abc", "c"))
