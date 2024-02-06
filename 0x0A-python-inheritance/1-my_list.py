class MyClass:
    """Defines a simple class."""

    def __init__(self):
        """Initializes an empty list."""
        self.my_list = []

    def append(self, item):
        """Appends an item to the list."""
        self.my_list.append(item)

    def print_sorted(self):
        """Prints the sorted list."""
        print(sorted(self.my_list))

# Test cases
my_class = MyClass()
my_class.append(4)
my_class.append(2)
my_class.append(1)
my_class.append(3)
my_class.print_sorted()
