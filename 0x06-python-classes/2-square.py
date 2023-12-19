#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """
    Class that defines properties of square by: (based on 1-square.py).

    Attributes:
        __size (int): The size of the square (1 side).
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
