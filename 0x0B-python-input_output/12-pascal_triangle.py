#!/usr/bin/python3
"""Module for generating Pascal's Triangle."""


def pascal_triangle(rows):
    """Generate Pascal's Triangle.

    Args:
        rows (int): The number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
    """
    if rows <= 0:
        return []

    p_triangle = [[1]]

    for i in range(1, rows):
        new_row = [1]
        for j in range(1, i):
            new_row.append(p_triangle[i-1][j-1] + p_triangle[i-1][j])
        new_row.append(1)
        p_triangle.append(new_row)

    return p_triangle
