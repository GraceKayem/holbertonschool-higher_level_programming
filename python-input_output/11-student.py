#!/usr/bin/python3
"""
Defines a class Student that defines a student by
first name, last name, and age.
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved. Otherwise, all attributes are
        retrieved.
        """
        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            return {
                key: getattr(self, key)
                for key in attrs if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with values from a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
