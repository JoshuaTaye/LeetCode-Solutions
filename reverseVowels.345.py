def reverseVowels(s):
    sarr = []
    for i in s:
        sarr.append(i)
    vowels = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
    found = ''
    index = []
    reverse = ''
    for i in range(len(sarr)):
        if sarr[i] in vowels:
            index.append(i)
            found += sarr[i]
    for i in range(len(found)-1, -1, -1):
        reverse += found[i]
    for i in range(len(index)):
        sarr[index[i]] = reverse[i]
    print(sarr)
    fin = ''
    for i in sarr:
        fin += i
    return fin


    # return s



print(reverseVowels('hello'))