#!/usr/bin/env python3
"""funct performs element-wise addition, substraction, mult and div"""


def np_elementwise(mat1, mat2):
    """fuct add, substract, mult and div"""
    add = (mat1 + mat2)
    sub = (mat1 - mat2)
    mul = (mat1 * mat2)
    div = (mat1 / mat2)
    return add, sub, mul, div
