def print_words_vertically(s):
    lst = s.split(" ")
    maxx = 0
    for i in lst:
        maxx = max(maxx, len(i))
    res = [""] * maxx
    for i in range(maxx):
        k = 0
        while k < (len(lst)):
            if len(lst[k]) < i+1:
                if len(res[i].strip(" ")) == 0:
                    res[i] += " "
            else:
                res[i] += lst[k][i]
            k += 1
        if k < maxx:
            while k < maxx:
                res[i] += " "
                k += 1
    return res
print(print_words_vertically("TO BE OR NOT TO BE"))