#!/usr/bin/env python3
"""funct concatenates 2 matrices"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates a matrix in specific axis"""
    if axis == 0:
        return mat1 + mat2
    elif axis == 1:
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
