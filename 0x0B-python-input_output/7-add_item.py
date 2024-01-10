#!/usr/bin/python3

def class_to_json(obj):
    """Converts an object to a dictionary for JSON serialization."""
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    elif hasattr(obj, '__slots__'):
        return {key: getattr(obj, key) for key in obj.__slots__ if hasattr(obj, key)}
    else:
        return {}
