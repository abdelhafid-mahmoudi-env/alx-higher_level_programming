#!/usr/bin/python3
"""
This is the "N Queens" module.

This module provides a solution to the N Queens puzzle.
"""

import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at a given position.
    """
    for prev_row in range(row):
        if board[prev_row] == col or \
           board[prev_row] - prev_row == col - row or \
           board[prev_row] + prev_row == col + row:
            return False
    return True

def solve_nqueens(n):
    """
    Solve the N Queens puzzle and print solutions.
    """
    def print_solution(board):
        """
        Print the N Queens board.
        """
        solution = [[i, board[i]] for i in range(n)]
        print(solution)

    def solve(board, row):
        """
        Recursively solve the N Queens puzzle.
        """
        if row == n:
            print_solution(board)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

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

    solve_nqueens(N)

