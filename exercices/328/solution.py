# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:48:47 2014

@author: sblakeley
"""


def mul(lst):
    total = 1
    for i in range(len(lst)):
        total = lst[i] * total
    return total
