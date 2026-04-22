def solveSudoku(board):

    def isSafe(row, col, num):
        for i in range(9):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False
            if board[3*(row//3) + i//3][3*(col//3) + i%3] == num:
                return False
        return True

    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for num in "123456789":
                        if isSafe(i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = "."
                    return False
        return True

    solve()
