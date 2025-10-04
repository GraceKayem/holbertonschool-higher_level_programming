#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""


import json

def save_to_json_file(my_obj, filename):
    """
    script that adds all arguments to a Python list, and then save them to a file

    Args:
        filename (str): script that adds all arguments to a Python list, and then save them to a file

    Returns:
        script that adds all arguments to a Python list, and then save them to a file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
