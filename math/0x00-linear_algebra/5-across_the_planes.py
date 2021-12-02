#!/usr/bin/env python3
""" Contains the function add_matrices2D """


def add_matrices2D(mat1, mat2):
    """ Function that adds two matrices element-wise"""

    if len(mat1) == len(mat2):
        new = []

        for i in range(len(mat1)):
            myList = []
            if len(mat1[i]) == len(mat2[i]):
                for j in range(len(mat1[i])):
                    myList.append(mat1[i][j] + mat2[i][j])
                new.append(myList)
            else:
                return None

        return new
