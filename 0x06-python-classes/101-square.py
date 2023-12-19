#!/usr/bin/python3
"""Defines the class Square."""


class Square:
    """
    Class that defines properties of a square.

    Attributes:
        size: size of the square.
        position: position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates a new instance of a square.

        Args:
            size: size of the square.
            position: position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value: The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value: The position of the square.

        Raises:
            TypeError: If position is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using # characters."""
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Returns a string representation of the square."""
        return self.my_print()
