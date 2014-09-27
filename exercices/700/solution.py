# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 18:35:51 2014

@author: sblakeley
"""
import numpy as np
import random


def get_rand():
    x = random.choice([0, 1, 2, 3])
    y = random.choice([0, 1, 2, 3])
    return x, y


def init_grid():
    grid = np.zeros((4, 4), dtype=int)
    x, y = get_rand()
    m, n = get_rand()
    while (m, n) == (x, y):
        m, n = get_rand()
    grid[x, y] = 2
    grid[m, n] = 2
    return grid


def add_new(grid):
    a = random.choice([2, 2, 2, 2, 4])
    x, y = get_rand()
    while grid[x, y] != 0:
        x, y = get_rand()
    grid[x, y] = a
    return grid
grid = init_grid()
print(add_new(grid))
