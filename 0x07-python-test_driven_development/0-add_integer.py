#!/usr/bin/python3
"""
This module provides a function to add two integers.

The function `add_integer` adds two integer values, casting floats to integers before addition. It raises a TypeError for non-numeric inputs.
"""

def add_integer(a, b=98):
    """
    Adds two integers.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a) + int(b)

