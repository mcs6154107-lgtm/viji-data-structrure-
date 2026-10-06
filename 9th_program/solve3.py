def solve_n_queens(n):
    board = [["."] * n for _ in range(n)]

    columns = set()
    diagonal1 = set()
    diagonal2 = set()

    def backtrack(row):
        if row == n:
            print("Solution:")
            for r in board:
                print(" ".join(r))
            print()
            return

        for col in range(n):
            d1 = row - col
            d2 = row + col

            if col in columns or d1 in diagonal1 or d2 in diagonal2:
                continue

            board[row][col] = "Q"
            columns.add(col)
            diagonal1.add(d1)
            diagonal2.add(d2)

            backtrack(row + 1)

            board[row][col] = "."
            columns.remove(col)
            diagonal1.remove(d1)
            diagonal2.remove(d2)

    backtrack(0)


solve_n_queens(4)
