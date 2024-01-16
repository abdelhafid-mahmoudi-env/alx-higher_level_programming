#!/usr/bin/python3
"""Module for Rectangle class."""

from .base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate.
            y (int): The y coordinate.
            id (int): The id of the object.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

   def __str__(self):
        """Return the string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"


    def display(self):
        """Print the Rectangle instance using the '#' character."""
	print("\n" * self.y, end="")
        for _ in range(self.height):
            print("#" * self.width)
    
    def area(self):
    	"""Return the area of the Rectangle."""
    	return self.width * self.height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_positive_integer(value, "width")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_positive_integer(value, "height")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__validate_non_negative_integer(value, "x")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__validate_non_negative_integer(value, "y")
        self.__y = value

    def __validate_positive_integer(self, value, attribute):
        """Validate that a value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{attribute} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute} must be > 0")

    def __validate_non_negative_integer(self, value, attribute):
        """Validate that a value is a non-negative integer."""
        if type(value) is not int:
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")
