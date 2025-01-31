def longestPalindrome(s):
    palindromes = ""
    palLen = 0
    if len(s) == 2 and s[0] == s[1]:
        return s[0]
    for i in range(len(s)):
        left = right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > palLen:
                palLen = right - left + 1
                palindromes = s[left: right + 1]
            left -= 1
            right += 1
        left , right = i , i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > palLen:
                palLen = right - left + 1
                palindromes = s[left: right + 1]
            left -= 1
            right += 1
    return palindromes
print(longestPalindrome("aaaa"))