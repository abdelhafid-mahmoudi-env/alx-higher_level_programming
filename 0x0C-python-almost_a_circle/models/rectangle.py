#!/usr/bin/python3
""" Module rectangle.py - This module defines the Rectangle class which inherits from the Base class. """

from models.base import Base


class Rectangle(Base):
    """
    This class represents a Rectangle, derived from the Base class.

    Attributes:
        width (int): Specifies the width of the rectangle.
        height (int): Specifies the height of the rectangle.
        x (int): Denotes the x-coordinate of the rectangle's position.
        y (int): Denotes the y-coordinate of the rectangle's position.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for creating a new instance of Rectangle.

        Args:
            width (int): Specifies the width of the rectangle.
            height (int): Specifies the height of the rectangle.
            x (int): Denotes the x-coordinate of the rectangle's position.
            y (int): Denotes the y-coordinate of the rectangle's position.
            id (int): Unique identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """
        Converts the rectangle's attributes into a dictionary format.

        Returns:
            dict: A dictionary encapsulating the rectangle's properties.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves for the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets for the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes and returns the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Renders the Rectangle using '#' symbols, taking into account the x and y coordinates."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + '#' * self.width)

    def __str__(self):
        """Provides a string representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the Rectangle's properties using specified arguments for id, width, height, x, and y."""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
