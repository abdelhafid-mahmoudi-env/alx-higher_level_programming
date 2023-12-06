#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list (only once for each integer)."""
    # Use a set to store unique elements and sum them
    unique_set = set(my_list)
    result = sum(unique_set)
    return result
