#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Class that defines properties of square"""

    def __init__(self, size=0):
        """Creates new instances of square.

        Args:
            size (float or int): size of the square (1 side).
        """
        self.size = size

    def area(self):
        """Calculates the area of square.

        Returns:
            float: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the size of a square.

        Returns:
            float or int: the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of a square.

        Args:
            value (float or int): size of a square (1 side).

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Equality comparison method.

        Args:
            other (Square): Another Square object to compare.

        Returns:
            bool: True if both squares have the same area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison method.

        Args:
            other (Square): Another Square object to compare.

        Returns:
            bool: True if both squares have different areas, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison method.

        Args:
            other (Square): Another Square object to compare.

        Returns:
            bool: True if the area of this square is less than the 
            area of the other square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparison method.

        Args:
            other (Square): Another Square object to compare.

        Returns:
            bool: True if the area of this square is less than or equal to 
            the area of the other square, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison method.

        Args:
            other (Square): Another Square object to compare.

        Returns:
            bool: True if the area of this square
            is greater than the area of the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparison method.

        Args:
            other (Square): Another Square object to compare.

        Returns:
            bool: True if the area of this square is
            greater than or equal to the area of the other square, False otherwise.
        """
        return self.area() >= other.area()
