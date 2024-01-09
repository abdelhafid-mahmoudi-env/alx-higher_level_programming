#!/usr/bin/python3
""" Module for the MyInt class that inherits from int """

class MyInt(int):
    """ MyInt class inherits from int, but inverts == and != operators. """

    def __eq__(self, other):
        """ Invert the == operator """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Invert the != operator """
        return super().__eq__(other)
