#!/usr/bin/python3
"""
Learn how to serialize and deserialize custom Python objects using the pickle module.
"""

import pickle


class CustomObject:
    """Custom class with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle.

        Args:
            filename (str): The filename to save the object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a pickle file.

        Args:
            filename (str): The filename to load the object from.

        Returns:
            CustomObject or None: The deserialized object or None on failure.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            if isinstance(obj, cls):
                return obj
            return None
        except (OSError, pickle.PickleError):
            return None
