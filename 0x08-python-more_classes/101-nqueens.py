#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    for i in range(len(board)):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    for i in range(len(board)):
        for j in range(len(board)):
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == 1:
                    return False

    return True


def print_solution(board):
    """Print the N Queens board."""
    solution = [[i, board[i]] for i in range(n)]
    print(solution)


def solve(board, row):
    """Recursively solve the N Queens puzzle."""
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1)
            board[row] = -1


def solve_nqueens(n):
    board = [-1] * n
    solve(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(N)
