#!/usr/bin/python3
"""
This module defines a Student class and demonstrates saving to and loading from a JSON file.
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

    def to_json(self, attrs=None):
        """
        Converts the student object to a JSON dictionary.

        Args:
            attrs (list): List of attributes to include in the JSON dictionary. If None, include all attributes.

        Returns:
            dict: JSON representation of the student object.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json_data):
        """
        Reloads the student object from a JSON dictionary.

        Args:
            json_data (dict): JSON representation of the student object.
        """
        for key, value in json_data.items():
            setattr(self, key, value)

if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    filename = "student.json"

    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(student_1.to_json(), file)

    with open(filename, mode='r', encoding='utf-8') as file:
        json_data = json.load(file)
        student_2 = Student("", "", 0)
        student_2.reload_from_json(json_data)

    print(student_2.__dict__)
