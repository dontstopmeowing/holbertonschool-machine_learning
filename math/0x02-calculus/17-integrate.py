#!/usr/bin/env python3
"""Contains the function poly_integral"""


def poly_integral(poly, C=0):
    """Function that calculates the integral of a polynomial."""
    if type(poly) is not list:
        return None
    elif not poly:
        return None
    elif len(poly) == 0:
        return None
    elif type(C) is not int:
        return None
    elif poly == [0]:
        return [C]
    else:
        new = []
        new.append(C)
        for i in range(len(poly)):
            if poly[i] % (i + 1) == 0:
                new.append(int(poly[i]/(i + 1)))
            else:
                new.append(poly[i]/(i + 1))
        return new
