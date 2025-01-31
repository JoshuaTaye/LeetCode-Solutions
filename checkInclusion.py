def checkInclusion(s1, s2):
    l = 0
    r = len(s1)
    s1 = sorted(s1)
    while r <= len(s2):
        print(s2[l:r])
        if sorted(s2[l:r]) == s1:
            return True
        l += 1
        r += 1
    return False





print(checkInclusion("adc", "dcda"))