class MyInt(int):
    """Subclass of int with reversed equality operators."""

    def __eq__(self, other):
        """Overrides the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the inequality operator."""
        return super().__eq__(other)

# Test cases
m = MyInt(3)
print(m == 3)   # False
print(m != 3)   # True
print(m == 89)  # True
print(m != 89)  # False
print(MyInt(-89) == -89)   # False
print(MyInt(-89) != -89)   # True
