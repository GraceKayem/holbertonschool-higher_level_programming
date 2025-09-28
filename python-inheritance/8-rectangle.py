#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is <= 0.
        """
        # validating input
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # setting the variables to private
        self.__width = width
        self.__height = height
