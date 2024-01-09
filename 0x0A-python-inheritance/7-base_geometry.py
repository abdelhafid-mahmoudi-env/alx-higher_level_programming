#!/usr/bin/python3
"""
Module for the BaseGeometry class with integer validator.
"""


class BaseGeometry():
    """ BaseGeometry class with area and integer_validator methods. """

    def area(self):
        """
        Raise an Exception with the message 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validate if value is a integer.
        Args:
          - name: str
          - value: int
        """
        if not isinstance(value, int):
            raise TypeError('{:s} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
