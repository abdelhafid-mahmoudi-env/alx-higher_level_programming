#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary."""
    # Use pop method to delete the key if it exists
    a_dictionary.pop(key, None)
    return a_dictionary
