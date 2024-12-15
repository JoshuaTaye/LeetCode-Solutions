class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        rows, cols = len(matrix), len(matrix[0])
        # build prefix 2D prefix Table (PS)
        self.ps = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                self.ps[r + 1][c + 1] = (self.ps[r + 1][c] + self.ps[r][c + 1] - self.ps[r][c] + matrix[r][c])
        for i in (self.ps):
            print(i)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == col1 == 0:
            return self.tdps[row2][col2]
        elif row1 == 0:
            return self.tdps[row2][col2] - self.tdps[row2][col1-1]
        elif col1 == 0:
            return self.tdps[row2][col2] - self.tdps[row1-1][col2]
        else:
            return self.tdps[row2][col2] - self.tdps[row1-1][col2] - self.tdps[row2][col1-1] + self.tdps[row1-1][col1-1]


matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))
# print(obj.matrix)
