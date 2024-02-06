class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Area method."""
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height."""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calculates the area of the Rectangle."""
        return self.__width * self.__height

# Test case
r = Rectangle(4, 3)
print(r.area())
