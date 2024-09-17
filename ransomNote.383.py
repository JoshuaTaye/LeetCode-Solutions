def canConstruct(ransomNote, magazine):
    for i in range(len(ransomNote)):
        print(magazine)
        if ransomNote[i] not in magazine:
            return False
        else:
            magazine = magazine.replace(ransomNote[i], "", 1)
    return True

print(canConstruct("aa", 'aab'))