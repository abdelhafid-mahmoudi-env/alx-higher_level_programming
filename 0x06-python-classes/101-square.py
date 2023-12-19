#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square.

    Attributes:
        __size (int): size of a square (1 side).
        __position (tuple): position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square.

        Args:
            size (int): size of the square (1 side).
            position (tuple): position of the square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of square.

        Returns:
            int: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the size of a square.

        Returns:
            int: the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of a square.

        Args:
            value (int): size of a square (1 side).

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
            tuple: the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """String representation of the square.

        Returns:
            str: String representation of the square.
        """
        if self.__size == 0:
            return ""
        result = "\n" * self.__position[1]
        result += "\n".join(" " * self.__position[0] + "#" * self.__size for _ in range(self.__size))
        return result

