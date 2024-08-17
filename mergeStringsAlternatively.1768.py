def mergeStrings(s1, s2):
    new = ''
    i = 0
    j = 0
    while i < len(s1) or j < len(s2):
        if i == len(s1):
            while j < len(s2):
                new += s2[j]
                j += 1
            return new
        elif j == len(s2):
            while i < len(s1):
                new += s1[i]
                i += 1
            return new
        if len(new) % 2 == 0:
            new += s1[i]
            i += 1
        else:
            new += s2[j]
            j += 1
    return new


print(mergeStrings("abc", "pqr"))