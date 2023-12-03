#!/usr/bin/python3

def reverse_list(my_list=[]):
    start = 0
    end = len(my_list) - 1
    while start < end:
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1
    return my_list
