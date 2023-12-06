#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value."""
    if a_dictionary:
        # Use max function with key argument to find the key with the maximum value
        return max(a_dictionary, key=a_dictionary.get)
    else:
        return None
