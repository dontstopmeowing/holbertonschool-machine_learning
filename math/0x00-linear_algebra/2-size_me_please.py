#!/usr/bin/env python3
""" Contains the function matrix_shape """


def matrix_shape(matrix):
    """ Function that calculates the shape of a matrix """

    new = []
    new.append(len(matrix))

    while type(matrix[0]) != int:
        new.append(len(matrix[0]))
        matrix = matrix[0]
    return new
