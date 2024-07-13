def longestPalindrome(a):
    map = ''
    for i in range(len(a)):
        for j in range(i, len(a) + 1):
            st = a[i:j]
            if st == st[::-1]:
                if len(st) > len(map):
                    map = st
    return map


inp = input()
print(longestPalindrome(inp))
