#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited from the specified class."""
    return issubclass(type(obj), a_class)

# Test cases
a = 1
print(inherits_from(a, int))  # False
print(inherits_from(a, object))  # True
