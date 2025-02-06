def countCharacters(words, chars):
    res = 0
    for i in range(len(words)):
        clist = list(chars)
        cset = set()
        cset.update(clist)
        fl = True
        for j in range(len(words[i])):
            if words[i][j].lower() not in cset:
                fl = False
                break
        if fl:
            res += len(words[i])
    return res



print(countCharacters(["cat","bt","hat","tree"], "atach"))