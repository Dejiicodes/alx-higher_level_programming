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

    def __str__(self):
        """Return a string representation of the object."""
        return "[{}] {}/{}".format(type(self).__name__, self.__width, self.__height)

class Rectangle(BaseGeometry):
    """Subclass of BaseGeometry for rectangles."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the object."""
        return "[{}] {}/{}".format(type(self).__name__, self.__width, self.__height)

class Square(Rectangle):
    """Subclass of Rectangle for squares."""

    def __init__(self, size):
        """Initialize a Square instance with size."""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return a string representation of the object."""
        return "[{}] {}/{}".format(type(self).__name__, self.__size, self.__size)
