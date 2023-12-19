#!/usr/bin/python3
"""Defines a class MagicClass"""
import math

class MagicClass:
    """A class that matches the given Python bytecode."""

    def __init__(self, radius=0):
        """Initialize MagicClass with a radius."""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self._MagicClass__radius
