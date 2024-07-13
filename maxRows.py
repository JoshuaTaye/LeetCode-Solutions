def maxRows(matrix):
    arr = []
    print(len(matrix))
    print(matrix[0][0])
    equal = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])-1):
            if matrix[i][j] == matrix[i][j+1]:
                print(i,j,"and", i, j+1)
                if len(equal) > i:
                    equal[i] += 1
                    print(equal)
                else:
                    equal.append(1)
    for i in range(len(equal)):
        equal[i] += 1
    print(equal)
            # print("equal in the inner loop is", equal)
        # print("equal in the outer loop is", equal)
    # print("Final equal is", equal)
        # for j in range(len(matrix[0])):
        #     print(matrix[i][j], end=" ")


# arr = input().strip('[').strip(']').split(',')

print(maxRows([[0, 0, 0], [0, 0, 1], [1, 1, 0]]))
