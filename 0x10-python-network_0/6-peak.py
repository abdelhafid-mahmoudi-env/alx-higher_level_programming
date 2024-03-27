#!/usr/bin/python3
"""
This module contains a function to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    This function finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: A peak integer from the list.
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n - 1] >= list_of_integers[n - 2]:
        return list_of_integers[n - 1]

    left = 1
    right = n - 2

    while left <= right:
        mid = (left + right) // 2

        if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    return None
