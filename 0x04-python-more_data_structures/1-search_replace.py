#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    # Create a new list with elements replaced
    new_list = [replace if x == search else x for x in my_list]
    return new_list
