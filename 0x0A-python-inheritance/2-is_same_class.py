#!/usr/bin/python3

"""
This module defines a function is_same_class.
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a given class."""
    return type(obj) == a_class

# Test cases
if __name__ == "__main__":
    a = 1
    print(is_same_class(a, int))
    a = True
    print(is_same_class(a, int))
    a = 3.14
    print(is_same_class(a, int))
    a = True
    print(is_same_class(a, object))
    a = None
    print(is_same_class(a, object))
    a = None
    print(is_same_class(a, list))
    a = [1, 2, 3]
    print(is_same_class(a, list))
    a = [1, 2, 3]
    print(is_same_class(a, object))
