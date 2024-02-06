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

# Test case
bg = BaseGeometry()
try:
    print(bg.area())
except NotImplementedError as e:
    print(f"Error: {e}")
