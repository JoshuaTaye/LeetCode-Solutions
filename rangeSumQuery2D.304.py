class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        tdps = [[0] * (len(matrix) + 1), [0]]
        for j in range(len(matrix[0])):
            tdps[1].append(tdps[1][j] + matrix[0][j])
        for row in range(1, len(matrix)):
            tdps.append([0])
            tdps[row+1].append(tdps[row][1] + matrix[row][0])
            for col in range(1, len(matrix[0])):
                tdps[row+1].append(matrix[row][col] + tdps[row+1][col] + tdps[row][col+1] - tdps[row][col])
        for i in tdps:
            print(i)
        self.tdps = tdps
    def sumRegion(self, row1, col1, row2, col2):
        return self.tdps[row2+1][col2+1] - self.tdps[row1][col2+1] - self.tdps[row2+1][col1] + self.tdps[row1][ col1]




matrixes = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrixes)
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))
# print(obj.matrix)


# def __init__(self, matrix):
#     self.matrix = matrix
#     tdps = [[]]
#     tdps[0].append(matrix[0][0])
#     print(tdps)
#     for i in range(1, len(matrix[0])):
#         tdps[0].append(matrix[0][i] + tdps[0][i - 1])
#     for i in range(1, len(matrix)):
#         tdps.append([0]*len(matrix[i]))
#         for j in range(len(matrix[i])):
#             if j == 0:
#                 tdps[i][0] += matrix[i][j] + tdps[i - 1][j]
#             else:
#                 tdps[i][j] = matrix[i][j] + tdps[i - 1][j] + tdps[i][j - 1] - tdps[i - 1][j - 1]
#         print(tdps)
#     self.tdps = tdps
#
# def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#     if row1 == col1 == 0:
#         return self.tdps[row2][col2]
#     elif row1 == 0:
#         return self.tdps[row2][col2] - self.tdps[row2][col1-1]
#     elif col1 == 0:
#         return self.tdps[row2][col2] - self.tdps[row1-1][col2]
#     else:
#         return self.tdps[row2][col2] - self.tdps[row1-1][col2] - self.tdps[row2][col1-1] + self.tdps[row1-1][col1-1]
