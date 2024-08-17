def scoreOfAString(s):
    score = 0
    for i in range(len(s)-1):
        score += abs(ord(s[i+1]) - ord(s[i]))
    print(score)
print(scoreOfAString("hello"))