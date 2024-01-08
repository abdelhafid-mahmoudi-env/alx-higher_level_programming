#!/usr/bin/python3
"""
Module 6-base_geometry
Defines a class BaseGeometry with a public instance method.
"""


class BaseGeometry:
    """A class BaseGeometry."""

    def area(self):
        """
        Raises an Exception with a message indicating that the method is not implemented.
        This method is expected to be overridden in derived classes.

        Raises:
            Exception: If the method is not implemented in a derived class.
        """
        raise Exception("area() is not implemented")
