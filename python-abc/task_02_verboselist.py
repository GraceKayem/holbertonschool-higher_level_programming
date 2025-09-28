#!/usr/bin/env python3
"""
In Python, you can extend built-in classes to add or modify behavior.
The list class provides a collection of methods and functionalities
that handle list operations.
"""


class VerboseList(list):
    """A list that prints messages when modified."""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        item = self[index]
        result = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return result
