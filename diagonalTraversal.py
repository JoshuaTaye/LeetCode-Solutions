def diagonalTraversal(mat):
    res = []
    hm = {}
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if row + col not in hm:
                hm[row + col] = [mat[row][col]]
            else:
                hm[row + col].append(mat[row][col])
    for k in hm:
        if k % 2:
            res.extend(hm[k])
        else:
            res.extend(hm[k][::1])
    return res
#     def upDiagonal(r, c):
#         print("upsolve")
#         print("before", r, c)
#         while r >= 0 and c <= len(mat[0]) - 1:
#             print("r and c", r, c)
#             res.append(mat[r][c])
#             if r > 0 and c < len(mat[0]) - 1:
#                 print("yes")
#                 r -= 1
#                 c += 1
#             else:
#                 break
#         print("final before update", r, c)
#         if r == 0 and c == len(mat[0]) - 1:
#             print("after", r+1, c)
#             print()
#             return [ r + 1, c]
#         elif r == 0:
#             print("after", r, c+1)
#             print()
#             return [r , c + 1]
#         elif c == len(mat[0])-1:
#             print("awo :(")
#             print("after", r+1, c)
#             print()
#             return [r + 1, c]
#         else:
#             return [r, c]
#
#     def downDiagonal(r, c):
#         print("downsolve")
#         print("before:", r, c)
#         while r <= len(mat)-1 and c >= 0:
#             res.append(mat[r][c])
#             if r < len(mat) - 1 and c > 0:
#                 r += 1
#                 c -= 1
#             else:
#                 break
#         if c == 0:
#             print("after", r+1, c)
#             print()
#             return [r + 1 , c]
#         elif r == len(mat)-1:
#             print("after", r, c+1)
#             print()
#             return [r, c+1]
#         else:
#             return [r, c]
#
#     row = 0
#     col = 0
#     while row < len(mat) and col < len(mat[0]):
#         [row, col] = upDiagonal(row, col)
#         [row, col] = downDiagonal(row, col)
#     if len(res) < len(mat) * len(mat[0]):
#         res.append(mat[len(mat)-1][len(mat[0])-1])
#     return res
print(diagonalTraversal([[2,5,8],[4,0,-1]]))