#!/usr/bin/python3
"""Module for generating Pascal's Triangle."""


def pascal_triangle(n):
    # Check if n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # Initialize Pascal's Triangle with the first row
    triangle = [[1]]

    # Iterate from the second row up to the nth row
    for i in range(1, n):
        # Initialize a new row with the first element as 1
        row = [1]

        # Iterate through the elements in the middle of the row
        for j in range(1, i):
            # Calculate the value by summing the two elements above in the previous row
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)

        # Add the last element of the row, which is always 1
        row.append(1)

        # Append the row to Pascal's Triangle
        triangle.append(row)

    # Return Pascal's Triangle as a list of lists
    return triangle
