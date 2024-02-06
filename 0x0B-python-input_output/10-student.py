#!/usr/bin/python3
"""
This module defines a function to convert a class instance to a JSON string.
"""

import json

class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the student object to a JSON dictionary.

        Returns:
            dict: JSON representation of the student object.
        """
        return self.__dict__

if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    print(json.dumps(student_1.to_json()))
