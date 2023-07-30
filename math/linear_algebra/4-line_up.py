#!/usr/bin/env python3
"""funct that adds 2 arrays element-wise"""


def add_arrays(arr1, arr2):
    """funct add array"""
    if len(arr1) != len(arr2) and len(arr2) != len(arr1):
        return None
    else:
        new_list = []
        for indx in range(0, len(arr1)):
            new_list.append(arr1[indx] + arr2[indx])
        return new_list
