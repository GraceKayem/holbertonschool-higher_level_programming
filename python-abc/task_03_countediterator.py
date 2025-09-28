#!/usr/bin/env python3
"""
Subclassing allows a new class to inherit properties and methods from an existing class. In Python, many built-in classes can be extended to customize or enhance their behavior.
"""


class CountedIterator:
    """Create a class named CountedIterator that extends the built-in iterator obtained from the iter function."""

    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._iterator)
        self._count += 1
        return item

    def get_count(self):
        return self._count
