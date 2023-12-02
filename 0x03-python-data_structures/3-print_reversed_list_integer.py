#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return  # If the list is empty, do nothing

    index = len(my_list) - 1  # Start from the last index
    while index >= 0:
        print("{}".format(my_list[index]))
        index -= 1
