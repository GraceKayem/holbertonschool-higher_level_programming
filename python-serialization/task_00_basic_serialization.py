#!/usr/bin/python3
"""
Create a basic serialization module that serializes a Python dictionary
to a JSON file and deserializes the JSON file back to a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): A Python dictionary with data.
        filename (str): The filename of the output JSON file. If the
            output file already exists, it will be replaced.

    Raises:
        TypeError: If data is not a dictionary.
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it to a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary from the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
