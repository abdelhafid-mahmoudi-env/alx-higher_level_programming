#!/usr/bin/python3
"""
This program defines a Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a Rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """Constructor of Retangle"""
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
