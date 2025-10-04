#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
