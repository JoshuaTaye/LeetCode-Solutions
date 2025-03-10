def validPalindrome(s):
    l = 0
    r = len(s) - 1
    count = 0
    s = list(s)
    while l < r:
        # print(s[l],s[r])
        if s[r] != s[l]:
            if count > 0:
                return False
            str1 = s[l+1:r+1]
            str2 = s[l:r]
            if str1 == list(reversed(str1)):
                l += 1
            elif str2 == list(reversed(str2)):
                r -= 1
            count += 1
        else:
            r -= 1
            l += 1
    return True


print(validPalindrome("ebcbbececabbacecbbcbe"))