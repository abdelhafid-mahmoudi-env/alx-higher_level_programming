#!/usr/bin/python3

class LockedClass:
    def __setattr__(self, name, value):
        # Check if the attribute being assigned is not 'first_name'
        if name != 'first_name':
            # If it's not 'first_name', raise an AttributeError
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))

