#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle (9-rectangle.py).
Task based on 10-square.py.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): Size of the square sides.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with size.

        Args:
            size (int): Size of the square sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is <= 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
