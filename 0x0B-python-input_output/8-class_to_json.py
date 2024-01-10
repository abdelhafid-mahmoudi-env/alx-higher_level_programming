#!/usr/bin/python3

def class_to_json(obj):
    """Return a dictionary description of an object for JSON serialization."""
    return obj.__dict__
