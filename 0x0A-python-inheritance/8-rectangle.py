#!/usr/bin/python3

"""
This module defines a BaseGeometry class and a Rectangle class.
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

class Rectangle(BaseGeometry):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance."""
        super().__init__()
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

# Test cases
print(dir(Rectangle))
print(issubclass(Rectangle, BaseGeometry))
r = Rectangle(1, 4)
print(r.width)
print(r.height)
