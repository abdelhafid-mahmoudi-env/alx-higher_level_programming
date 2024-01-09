#!/usr/bin/python3
""" Module for the BaseGeometry class with integer validator. """


class BaseGeometry:
    """ BaseGeometry class with area and integer_validator methods. """

    def area(self):
        """ Raises an exception indicating that the area() method"
        " is not implemented. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a value is a positive integer.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
