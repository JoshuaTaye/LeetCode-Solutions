def countKConstraintSubstrings(s, p):
    final = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            print(s[i:j])
            count1 = 0
            count0 = 0
            for k in s[i:j]:
                if k == "1":
                    count1 += 1
                else:
                    count0 += 1
            if count1 <= p or count0 <= p:
                final.append(s[i:j])
    return len(final)




print(countKConstraintSubstrings("11111", 1))
