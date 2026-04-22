def solveNQueens(n):
    result = []
    board = [["."] * n for _ in range(n)]

    def isSafe(row, col):
        for i in range(col):
            if board[row][i] == "Q":
                return False

        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == "Q":
                return False
            i += 1
            j -= 1

        return True

    def solve(col):
        if col == n:
            result.append(["".join(row) for row in board])
            return

        for i in range(n):
            if isSafe(i, col):
                board[i][col] = "Q"
                solve(col + 1)
                board[i][col] = "."

    solve(0)
    return result
