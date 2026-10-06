def n_queens(n):
    solutions = []
    board = [-1] * n

    def safe(row, col):
        for i in range(row):
            if board[i] == col:
                return False

            if abs(board[i] - col) == abs(i - row):
                return False

        return True

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


n = 4
solutions = n_queens(n)

for solution in solutions:
    print(solution)
