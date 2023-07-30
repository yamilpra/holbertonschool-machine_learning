#!/usr/bin/env python3
"""funct concatenates 2 matrices along a specific axis"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """concatenates 2 matrices"""
    concat_matrix = np.concatenate((mat1, mat2), axis=axis)
    return concat_matrix
