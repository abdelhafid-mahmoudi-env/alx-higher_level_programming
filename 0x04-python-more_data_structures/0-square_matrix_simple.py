#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers in a matrix."""
    # Create a new matrix with the same size as the input matrix
    new_matrix = [[x**2 for x in row] for row in matrix]
    return new_matrix
