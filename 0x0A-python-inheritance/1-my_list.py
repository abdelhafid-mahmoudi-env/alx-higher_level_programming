#!/usr/bin/python3
""" Module for the MyList class that inherits from list """


class MyList(list):
    """ MyList class inherits from the built-in list class """

    def print_sorted(self):
        """ Prints the list in ascending sorted order """
        print(sorted(self))
