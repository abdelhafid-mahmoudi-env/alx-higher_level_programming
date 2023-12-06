#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value."""
    if a_dictionary:
        # Find the key with the maximum value using a loop
        max_key = None
        max_value = float('-inf')

        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                max_key = key

        return max_key
    else:
        return None
