#!/usr/bin/env python3
""" Contains the function mat_mul """


def mat_mul(mat1, mat2):
    """Function that performs matrix multiplication"""

    if len(mat1[0]) != len(mat2):
        return None
    else:
        new = []
        for i in range(len(mat1)):
            temp = []
            for j in range(len(mat2[0])):
                count = 0
                for k in range(len(mat2)):
                    count += mat1[i][k] * mat2[k][j]
                temp.append(count)
            new.append(temp)
        return new
