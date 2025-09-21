#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The number to divide by.

    Returns:
        list of lists of float: A new matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows are not all the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(all(isinstance(x, (int, float)) for x in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    new_matrix = [[float(f"{x / div:.2f}") for x in row] for row in matrix]
    
    return new_matrix
