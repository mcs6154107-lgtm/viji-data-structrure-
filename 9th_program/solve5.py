def count_n_queens(n):
    count = 0
    board = [-1] * n

    def is_safe(row, col):
        for i in range(row):
            if board[i] == col:
                return False

            if abs(board[i] - col) == abs(i - row):
                return False

        return True

    def backtrack(row):
        nonlocal count

        if row == n:
            count += 1
            print("Solution", count)

            for i in range(n):
                for j in range(n):
                    if board[i] == j:
                        print("Q", end=" ")
                    else:
                        print(".", end=" ")
                print()

            print()
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)

    print("Total solutions:", count)


count_n_queens(4)
