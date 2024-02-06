#!/usr/bin/python3
"""Defines a function that returns the list of available attributes and methods of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)


# Example usage
if __name__ == "__main__":
    class MyClass1(object):
        pass


    class MyClass2(object):
        my_attr1 = 3

        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
