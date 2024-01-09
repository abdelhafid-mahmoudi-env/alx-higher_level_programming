#!/usr/bin/python3
""" Module for the Rectangle class that inherits from BaseGeometry. """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry. """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle, must be a positive integer.
            height (int): The height of the rectangle, must be a positive integer.
        """
        # Validate that width and height are positive integers using integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        # Set the private attributes __width and __height
        self.__width = width
        self.__height = height
