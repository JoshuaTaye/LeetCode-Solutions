def stringCompression(chars):
    new = []
    for i in range(0, len(chars)):
        if i == 0:
            new.append(chars[i])
            new.append(1)
        elif chars[i - 1] != chars[i]:
            new.append(chars[i])
            new.append(1)
        else:
            new[-1] += 1
    newnew = []
    for j in range(len(new)):
        if new[j] != 1:
            new[j] = str(new[j])
            if len(new[j]) > 1:
                for k in new[j]:
                    newnew.append(k)
            else:
                newnew.append(new[j])
    for i in range(len(newnew)):
        chars[i] = newnew[i]
    return len(newnew)


print(stringCompression(["a","a","b","b","c","c","c"]))