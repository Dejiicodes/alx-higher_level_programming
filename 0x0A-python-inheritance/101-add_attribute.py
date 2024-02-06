#!/usr/bin/python3

def add_attribute(obj, name, value):
    """Adds an attribute to an object if possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

# Test cases
a = "My String"
add_attribute(a, "hbtn", "Holberton")
print(a.name)
