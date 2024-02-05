#!/usr/bin/python3

def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible."""
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
