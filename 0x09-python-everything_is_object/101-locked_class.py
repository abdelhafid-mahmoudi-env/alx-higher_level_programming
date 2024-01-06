#!/usr/bin/python3
"""LockedClass for user prevents"""


class LockedClass:
    """Prevents the user from dynamically creating new instance attributes."""

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of Locked Class."""

        self.first_name = "first_name"
