#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a given number.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.

    Parameters:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float): The number by which to divide the matrix elements.

    Returns:
    list of lists of float: A new matrix with elements divided by div, rounded to 2 decimals.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats or rows are not of the same size,
               or if div is not a number.
    ZeroDivisionError: If div is 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        any(not all(isinstance(el, (int, float)) for el in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(el / div, 2) for el in row] for row in matrix]
    return new_matrix
