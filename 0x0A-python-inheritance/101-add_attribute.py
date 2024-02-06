def add_attribute(obj, name, value):
    """Adds an attribute to an object if possible."""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

# Test cases
class MyClass:
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)
