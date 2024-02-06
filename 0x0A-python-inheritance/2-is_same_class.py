def is_same_class(obj, a_class):
    """Checks if an object is an instance of a specific class."""
    return type(obj) is a_class

# Test cases
print(is_same_class(1, int))   # True
print(is_same_class(True, int))   # False
