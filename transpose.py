def transpose(matrix):
    reversed = []
    for row in range(len(matrix[0])):
        reversed.append([])
        for column in range(len(matrix)):
            reversed[row].append(matrix[column][row])
    return reversed

# print(transpose([[1,2,3],[4,5,6]]))
sett = {1, 2, 3, 4, 5}
print(sett.pop())