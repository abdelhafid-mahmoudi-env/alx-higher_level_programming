#!/usr/bin/python3
"""Module defining the Student class."""


class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new instance of the Student class.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        return self.__dict__
