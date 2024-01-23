#!/usr/bin/python3


class Square:
    """
    Class Square that defines a square.

    Attributes:
        side_length (float): The length of the square's side.
    """

    def __init__(self, side_length):
        """
        Initializes a new instance of the Square class.

        Args:
            side_length (float): The length of the square's side.
        """
        self.side_length = side_length

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.side_length ** 2

    def perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
            float: The perimeter of the square.
        """
        return 4 * self.side_length


if __name__ == "__main__":
    # Example usage
    square = Square(5)
    print("Area:", square.area())
    print("Perimeter:", square.perimeter())
