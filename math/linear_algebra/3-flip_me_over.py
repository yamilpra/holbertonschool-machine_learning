#!/usr/bin/env python3
"""funct returns transpose of 2D"""


def matrix_transpose(matrix):
    """funct transpose a 2D matrix"""
    if not matrix:
        return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
