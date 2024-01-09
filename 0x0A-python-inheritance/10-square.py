#!/usr/bin/python3
"""
Module for the Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""
    def __init__(self, size):
        """Initializes a new Square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Get a string representation of the square."""
        return self.__size ** 2
