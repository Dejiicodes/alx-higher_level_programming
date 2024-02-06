#!/usr/bin/python3
"""Script that imports a class from a file and creates an instance"""
from my_class_2 import MyClass

def main():
    obj = MyClass()
    print(obj.__dict__)

if __name__ == "__main__":
    main()
