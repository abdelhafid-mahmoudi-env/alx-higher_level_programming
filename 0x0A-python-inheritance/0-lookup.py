#!/usr/bin/python3
"""
Module 0-lookup
Contains method lookup that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """Function for return list of attributes and methods"""

    return dir(obj)
