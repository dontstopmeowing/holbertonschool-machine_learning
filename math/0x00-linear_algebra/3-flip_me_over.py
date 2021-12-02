#!/usr/bin/env python3
""" Contains the function matrix_shape """


def matrix_transpose(matrix):
    """ Function that returns the transpose of a 2D matrix"""

    new = []
    for i in range(len(matrix[0])):
        tmp = []
        for j in matrix:
            tmp += [j[i]]
        new += [tmp]
    return new
