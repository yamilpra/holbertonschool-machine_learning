#!/usr/bin/env python3
"""funct calculate the shape of a matrix"""


def matrix_shape(matrix):
    """return the shape"""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
