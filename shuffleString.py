def shuffleString(s, indices):
    lst = [0]* len(s)
    for i in range(len(indices)):
        lst[indices[i]] = s[i]
    return "".join(lst)

print(shuffleString("codeleet",[4,5,6,7,0,2,1,3]))