#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Checks if an object is an instance of a specific class."""
    return type(obj) is a_class

# Test cases
a = 1
print(is_same_class(a, int))  # True
print(is_same_class(a, float))  # False
