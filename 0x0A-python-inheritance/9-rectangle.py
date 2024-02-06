#!/usr/bin/python3

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

    def area(self):
        """Calculates the area of the Rectangle."""
        return self.__width * self.__height

# Test cases
r = Rectangle(1, 4)
print(r.area())
print(r)
