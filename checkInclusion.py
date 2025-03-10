from collections import Counter, defaultdict


def checkInclusion(s1, s2):

    set1 = dict(Counter(s1))
    set2 = defaultdict(int)
    i = 0
    while i < len(s2) and i < len(s1):
        if set1 == set2:
            return True
        set2[s2[i]] += 1
        i +=1
    if set1 == set2:
        return True
    l = 0
    r = i
    print(set1, dict(set2))
    while r < len(s2):

        print(s2[l], "is about to be removed from", dict(set2))
        if set2[s2[l]] > 1:
            set2[s2[l]] -= 1
        else:
            del set2[s2[l]]
        # if set2 == set1:
        #     return True
        print(dict(set2))
        print(s2[r], "is about to be added to", dict(set2))
        set2[s2[r]] += 1
        if set2 == set1:
            return True
        # if set2 == set1:
        #     return True
        l += 1
        r += 1
    return False
print(checkInclusion("adc", "dcda"))
