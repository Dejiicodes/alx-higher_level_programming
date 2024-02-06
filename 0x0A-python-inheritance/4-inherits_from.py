#!/usr/bin/python3

"""
This module defines a function inherits_from.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a subclass."""
    return isinstance(obj, a_class) and type(obj) != a_class

# Test cases
if __name__ == "__main__":
    a = 1
    print(inherits_from(a, int))
    a = 1
    print(inherits_from(a, int))
    a = 1
    print(inherits_from(a, int))
    a = 1
    print(inherits_from(a, int))
    a = 1
    print(inherits_from(a, int))
    a = 1
    print(inherits_from(a, int))
    a = 1
    print(inherits_from(a, int))
    a = 1
    print(inherits_from(a, int))
