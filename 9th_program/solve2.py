def solve_n_queens(n):
    board = [["."] * n for _ in range(n)]

    def safe(row, col):
        for i in range(row):
            for j in range(n):
                if board[i][j] == "Q":
                    if j == col or abs(i - row) == abs(j - col):
                        return False
        return True

    def backtrack(row):
        if row == n:
            print("Solution:")
            for r in board:
                print(" ".join(r))
            print()
            return

        for col in range(n):
            if safe(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    backtrack(0)


n = 4
solve_n_queens(n)
