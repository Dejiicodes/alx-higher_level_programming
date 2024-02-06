#!/usr/bin/python3

"""
This module defines a function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or inherited from it."""
    return isinstance(obj, a_class)

# Test cases
if __name__ == "__main__":
    a = 1
    print(is_kind_of_class(a, int))
    a = True
    print(is_kind_of_class(a, int))
    a = 3.14
    print(is_kind_of_class(a, int))
    a = True
    print(is_kind_of_class(a, object))
    a = None
    print(is_kind_of_class(a, object))
    a = None
    print(is_kind_of_class(a, list))
    a = [1, 2, 3]
    print(is_kind_of_class(a, list))
    a = [1, 2, 3]
    print(is_kind_of_class(a, object))
