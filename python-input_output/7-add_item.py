#!/usr/bin/python3
"""
Function that writes a Python object to a text file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file in JSON format.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
