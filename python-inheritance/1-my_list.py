#!/usr/bin/python3
"""
Write a class MyList that inherits from list.
"""


class MyList(list):
    """Represent a list with a print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
