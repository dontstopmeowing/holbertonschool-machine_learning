#!/usr/bin/env python3
""" Contains the function add_arrays """


def add_arrays(arr1, arr2):
    """ Function that adds two arrays element-wise"""

    if len(arr1) != len(arr2):
        return None
    else:
        myList = []
        for i in range(len(arr1)):
            myList.append(arr1[i] + arr2[i])
        return myList
