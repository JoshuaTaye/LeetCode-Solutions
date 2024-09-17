def validPalindrome(s):
    arr = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    s = s.lower()
    for i in s:
        if i in alphabet:
            arr.append(i)
    k = 0
    p = len(arr) - 1
    while k < p:
        if arr[k] != arr[p]:
            return False
        k += 1
        p -= 1
    return True




print(validPalindrome("A man, a plan, a canal: Panama"))