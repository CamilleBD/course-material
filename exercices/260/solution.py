# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 14:47:15 2014

@author: sblakeley
"""


def euclidean(a, b):
    final = 0
    for n in range(len(a)):
        sol = (a[n] - b[n]) ** 2
        final = sol + final
    return final ** (1 / n)
import math


def opt_euclidean(a, b):
    final = 0
    for n in range(len(a)):
        sol = math.pow((a[n] - b[n]), 2)
        final = sol + final
    return math.pow(final, 1/n)
import numpy as np


def np_euclidean(a, b):
    final = 0
    for n in range(len(a)):
        sol = np.power((a[n] - b[n]), 2)
        final = sol + final
    return np.power(final, (1 / n))
