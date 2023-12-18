#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Try to print the value as an integer
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # If an exception is raised (e.g., ValueError or TypeError), return False
        return False
