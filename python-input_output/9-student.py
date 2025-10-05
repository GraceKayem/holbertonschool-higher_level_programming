#!/usr/bin/python3
"""
Defines a class Student that defines a student by first name, last name, and age.
"""

class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        (for JSON serialization).
        """
        return self.__dict__
