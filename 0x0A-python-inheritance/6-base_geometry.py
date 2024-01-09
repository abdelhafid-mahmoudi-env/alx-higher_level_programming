#!/usr/bin/python3
""" Module for the BaseGeometry class. """


class BaseGeometry:
    """ BaseGeometry class with an unimplemented area method. """

    def area(self):
        """ Raises an exception with a message indicating"
        " that the method is not implemented. """
        raise Exception("area() is not implemented")
