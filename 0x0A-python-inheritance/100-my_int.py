#!/usr/bin/python3

class MyInt(int):
    """Custom integer class."""

    def __eq__(self, other):
        """Overrides the equality comparison."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the inequality comparison."""
        return super().__eq__(other)

# Test cases
m = MyInt(3)
print(m)
print(m == 3)
print(m != 3)
