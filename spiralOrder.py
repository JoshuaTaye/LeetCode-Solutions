from collections import Counter


def spiralOrder(mat):
    length = len(mat)* len(mat[0])
    res = []
    def goRight(lim, curr):
        [liml, limt, limr, limb] = lim
        [x, y] = curr
        while y < limr and len(res) < length:
            res.append(mat[x][y])
            y += 1
        return [[liml, limt, limr-1, limb], [x, y]]
    def goDown(lim, curr):
        [liml, limt, limr, limb] = lim
        [x, y] = curr
        while x < limb and len(res) < length:
            res.append(mat[x][y])
            x += 1
        return [[liml, limt, limr, limb-1], [x, y]]
    def goLeft(lim, curr):
        [liml, limt, limr, limb] = lim
        [x, y] = curr
        while y > liml and len(res) < length:
            res.append(mat[x][y])
            y -= 1
        return [[liml + 1, limt, limr, limb], [x, y]]
    def goUp(lim, curr):
        [liml, limt, limr, limb] = lim
        [x, y] = curr
        while x > limt and len(res) < length:
            res.append(mat[x][y])
            x -= 1
        return [[liml, limt + 1, limr, limb], [x, y]]
    lim = [0,1,len(mat[0])-1, len(mat)-1]
    curr = [0,0]
    while len(res) < length-1:
        lim, curr  = goRight(lim, curr)
        lim, curr = goDown(lim, curr)
        lim, curr = goLeft(lim, curr)
        lim, curr = goUp(lim, curr)
    x = Counter(res)
    y = {}
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] not in y:
                y[mat[i][j]] = 1
            else:
                y[mat[i][j]] += 1
    for k in y:
        if x[k] != y[k]:
            res.append(k)
    return res

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(spiralOrder([[1,2,3,4, 5],[6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))
