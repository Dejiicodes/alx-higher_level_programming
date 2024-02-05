#!/usr/bin/python3

class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raise an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
