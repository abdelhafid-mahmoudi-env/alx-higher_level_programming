#!/usr/bin/python3
""" Module for the MyList class which inherits from list. """

class MyList(list):
    """ MyList class that inherits from the built-in list class. """

    def print_sorted(self):
        """ Prints the list in a sorted order. """
        print(sorted(self))
