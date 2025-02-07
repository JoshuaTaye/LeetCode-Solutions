def imageSmoother(img):
    avg = []
    res = [[0] * (len(img[0])+2)]
    for i in range(1, len(img)+1):
        res.append([0])
        for j in range(len(img[i-1])):
            res[i].append(img[i-1][j])
        res[i].append(0)
    res.append([0]*(len(img[0]) + 2))
    print(res)
    for k in range(1, len(res)-1):
        avg.append([])
        for l in range(1, (len(res[k])-1)):
            dividend = 9
            if k == 1:
                dividend -= 3
            if l == 1:
                dividend -= 3
            if k == 1 and l == 1:
                dividend += 1
            if k == len(res)-2:
                dividend -= 3
            if l == len(res[k])-2:
                dividend -= 3
            if k == len(res)-2 and l == len(res[k])-2:
                dividend += 1
            if k == 1 and l == len(res[k]) - 2:
                dividend += 1
            if k == len(res) - 2 and l == 1:
                dividend += 1
            avg[k-1].append(0)
            avg[k-1][l-1] += (res[k-1][l-1] + res[k-1][l] + res[k-1][l+1] + res[k][l-1] + res[k][l] + res[k][l+1] + res[k+1][l-1] + res[k+1][l] +res[k+1][l+1])//dividend
    return avg

print(imageSmoother([[2,3]]))