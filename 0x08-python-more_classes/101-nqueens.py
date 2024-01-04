#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    # Check if it's safe to place a queen at a given position
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def backtrack(board, col):
        if col == n:
            for row in board:
                print([row.index(1), row])
            print()
            return
        for row in range(n):
            if is_safe(board, row, col, n):
                board[col] = row
                backtrack(board, col + 1)
                board[col] = -1

    board = [-1] * n
    backtrack(board, 0)

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

solve_nqueens(N)
