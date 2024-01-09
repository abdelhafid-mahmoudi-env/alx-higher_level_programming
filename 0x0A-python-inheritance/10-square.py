#!/usr/bin/python3
"""
Module for the Square class that inherits from Rectangle.
"""


PrevSquare = __import__('10-square').Square


class Square(PrevSquare):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """Initializes a new Square."""
        super().__init__(size)

    def __str__(self):
        """Get a string representation of the square."""
        return '[Square] {0:d}/{0:d}'.format(self.__size)
