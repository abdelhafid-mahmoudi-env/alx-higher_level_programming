#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()

        # Set the private attributes __width and __height
        self.__width = width
        self.__height = height

        # Validate width and height using integer_validator from the base class
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Get a string representation of the rectangle.

        Returns:
            str: A formatted string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
