def palindromeNumber(n):
    count = 0
    palindrome  = True
    for i in range(1, len(n)):
        if n[i] != n[-1 * i - 1]:
            palindrome = False
    return palindrome
x = str(input())
print(palindromeNumber(x))