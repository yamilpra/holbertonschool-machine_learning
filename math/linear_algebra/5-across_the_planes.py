#!/usr/bin/env python3
"""funct that adds 2 matrices elements"""


def add_matrices2D(mat1, mat2):
    """funct adds 2 matrices"""
    if len(mat1[0]) != len(mat2[0]):
        return None
    else:
        total = []
        for a in range(len(mat1)):
            row = []
            for b in range(len(mat1[0])):
                row.append(mat1[a][b] + mat2[a][b])
            total.append(row)
        return total
