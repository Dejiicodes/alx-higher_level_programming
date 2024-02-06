def inherits_from(obj, a_class):
    """Checks if an object inherits from a specific class."""
    return issubclass(type(obj), a_class)

# Test cases
print(inherits_from(1, int))   # True
print(inherits_from(True, int))   # False
