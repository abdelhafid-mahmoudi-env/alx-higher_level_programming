#!/usr/bin/python3
"""
Module for the Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('8-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Constructor of new Retangle"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Get a string representation of the rectangle."""
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
