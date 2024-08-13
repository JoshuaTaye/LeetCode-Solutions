def multiply_strings(s1, s2):
    # if s1 == 1 and s2 == 1:
    #     return "1"
    zeros1 = int(10 ** (len(s1)-1))
    zeros2 = int(10 ** (len(s2)-1))
    n1, n2 = 0, 0
    for i in range(len(s1)):
        n1 += int(s1[i]) * zeros1
        zeros1 = zeros1 // 10
    for j in range(len(s2)):
        n2 += int(s2[j]) * zeros2
        zeros2 = zeros2 // 10
    print(n1)
    print(s1)
    print(n2)
    print(s2)
    multiple = n1 * n2
    return str(multiple)


print(multiply_strings("60974249908865105026646412538664653190280198809433017",
                       "500238825698990292381312765074025160144624723742"))
