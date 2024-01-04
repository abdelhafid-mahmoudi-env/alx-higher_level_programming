#!/usr/bin/python3
import sys

def print_solution(board):
    """Prints the chessboard with queens placed."""
    for row in board:
        print([1 if col else 0 for col in row])

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at a given position."""
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(n):
    """Solves the N Queens puzzle and prints solutions."""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]

    def backtrack(col):
        if col == n:
            print_solution(board)
            return

        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(col + 1)
                board[row][col] = 0

    backtrack(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)

