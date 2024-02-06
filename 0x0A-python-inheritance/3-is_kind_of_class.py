def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or inherited from it."""
    return isinstance(obj, a_class)

# Test cases
print(is_kind_of_class(1, int))   # True
print(is_kind_of_class(True, int))   # False
