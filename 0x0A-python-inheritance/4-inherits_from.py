#!/usr/bin/python3
"""
Module 4-inherits_from
Contains a function that checks if the object is an instance of a class that
inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the obj is an instance of a class that inherited (directly or
    indirectly) from the specified class a_class; otherwise False.

    The function will return False if obj is an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
