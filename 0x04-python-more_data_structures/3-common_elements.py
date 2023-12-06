#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Return a set of common elements in two sets."""
    # Use set intersection to find common elements
    common_set = set_1.intersection(set_2)
    return common_set
