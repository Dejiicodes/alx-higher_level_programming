#!/usr/bin/python3

"""
This module defines a BaseGeometry class.
"""


class BaseGeometry:
    """Base geometry class."""

    def area(self):
        """Calculates the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

# Test cases
bg = BaseGeometry()
try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
