def maxSubMatrix(matrix, k):
    pstd = [[0]* (len(matrix[0])+1) for _ in range(len(matrix) +1)]
    print(pstd)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            pstd[i+1][j+1] = (pstd[i+1][j] + pstd[i][j+1] + matrix[i][j] - pstd[i][j])
    print(pstd)

print(maxSubMatrix([[1,0,1],[0,-2,3]],2))
