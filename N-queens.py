def is_safe(board, row, col, n):
    # Check this column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_solution(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            solve_n_queens(board, row + 1, n)  # Recurse
            board[row][col] = 0  # Backtrack

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print('Q' if board[i][j] == 1 else '.', end=" ")
        print()
    print()

# Main Function
n = 4  # You can change n to any number
board = [[0 for _ in range(n)] for _ in range(n)]
print(f"Solutions for {n}-Queens Problem:")
solve_n_queens(board, 0, n)
