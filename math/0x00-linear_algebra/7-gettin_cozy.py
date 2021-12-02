#!/usr/bin/env python3
""" Contains the function cat_matrices2D """


def cat_matrices2D(mat1, mat2, axis=0):
    """Function that concatenates two matrices along a specific axis"""

    if (len(mat1[0]) == len(mat2[0])) and axis == 0:
        new = [x[:] for x in mat1] + [x[:] for x in mat2]
        return new

    elif (len(mat1) == len(mat2)) and axis == 1:
        new = [mat1[x] + mat2[x] for x in range(len(mat1))]
        return new

    else:
        return None
