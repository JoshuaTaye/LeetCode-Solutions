def validSudoku(board):
    # case1
    for i in range(len(board)):
        res = []
        for j in range(len(board[i])):
            if board[i][j] not in res and board[i][j] != ".":
                res.append(board[i][j])
            elif board[i][j] != ".":
                return False
    for i in range(len(board)):
        res = []
        for j in range(len(board[i])):
            if board[j][i] not in res and board[j][i] != ".":
                res.append(board[j][i])
            elif board[j][i] != ".":
                return False
    endy = 3
    starty = 0
    while endy <= 9:
        startx = 0
        endx = 3
        while endx <= 9:
            res = []
            for i in range(startx, endx):
                for j in range(starty, endy):
                    if board[i][j] in res:
                        return False
                    elif board[i][j] != "." and board[i][j] not in res:
                        res.append(board[i][j])
            startx += 3
            endx += 3
        starty += 3
        endy += 3
    return True

print(validSudoku(
    [
          ["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))