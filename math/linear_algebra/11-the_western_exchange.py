#!/usr/bin/env python3
"""funct that transposes matrix"""


def np_transpose(matrix):
    """transposes matrix"""
    old_matrix = matrix.copy()
    new_matrix = old_matrix.transpose()
    return new_matrix
