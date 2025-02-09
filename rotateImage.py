def rotateImage(mat):
    switched = []
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if [row, col] not in switched:
                mat[row][col],mat[col][len(mat) - 1 - row] = mat[col][len(mat) - 1 - row], mat[row][col]
                switched.append([col, len(mat) - 1 - row])
    return mat


print(rotateImage([[1,2,3],[4,5,6],[7,8,9]]))