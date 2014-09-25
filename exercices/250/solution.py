# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 12:29:44 2014

@author: sblakeley
"""


def draw_n_squares(n):
    horendf = '+---+'
    hor = '+---'
    ver = '|   '
    acc = []
    for i in range(n):
        sol, sol2 = hor * (n-1) + horendf, ver * n + ver
        acc.append(sol)
        acc.append(sol2)
    return '\n'.join(acc) + '\n' + hor*(n-1) + horendf
