#!/usr/bin/python3
"""
Append a string at the end of a text file (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    Appends text to a file.

    Args:
        filename (str): The file to append to.
        text (str): The string to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
