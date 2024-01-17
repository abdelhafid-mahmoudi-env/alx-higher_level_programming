#!/usr/bin/python3
""" Module square.py - This module defines the Square class which inherits from the Rectangle class. """

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a Square, derived from the Rectangle class.
    Inherits all attributes and methods from the Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class.

        Parameters:
            size (int): The length of each side of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int, optional): Unique identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """
        Converts the square's attributes to a dictionary.

        Returns:
            dict: A dictionary representing the square's properties.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The length of the square's sides.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets a new size for the square.

        Parameters:
            value (int): The new length for the sides of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the square's attributes.

        Parameters:
            *args (list): Sequential arguments for id, size, x, y.
            **kwargs (dict): Keyword arguments for attribute names and values.
        """
        attributes = ["id", "size", "x", "y"]
        if args:
            for attr, arg in zip(attributes, args):
                setattr(self, attr, arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: String describing the square's characteristics.
        """
        return "[Square] ({id}) {x}/{y} - {size}".format(id=self.id, x=self.x, y=self.y, size=self.width)
