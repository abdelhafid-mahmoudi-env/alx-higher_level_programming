#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList that inherits from list
Includes method print_sorted to print the list in ascending order
"""

class MyList(list):
    """Inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
