def pascalsTriangle(n):
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    arr = []
    for i in range(n):
        arr.append([])
    arr[0] = [1]
    arr[1] = [1, 1]
    for i in range(2, n):
        arr[i].append(1)
        for j in range(1, i):
            arr[i].append(arr[i-1][j] + arr[i-1][j-1])
        arr[i].append(1)
    return arr





print(pascalsTriangle(5))
