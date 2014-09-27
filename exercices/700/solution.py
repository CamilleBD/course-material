# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 14:15:00 2014

@author: sblakeley
"""

import numpy as np
import random
m = np.zeros((4, 4), dtype=int)


def init_grid():
    m[random.choice('0123'), random.choice('0123')] = 2
    m[random.choice('0123'), random.choice('0123')] = 2
    n = m.tolist()
    t = n[0].count(2) + n[1].count(2) + n[2].count(2) + n[3].count(2)
    if t == 2:
        return m
grid = init_grid()
print(grid)


def add_new(grid):
    a = random.choice('11112')
    if a == '1':
        grid[random.choice('0123'), random.choice('0123')] = 2
        n = grid.tolist()
        t = n[0].count(2) + n[1].count(2) + n[2].count(2) + n[3].count(2)
        if t == 3:
            return grid
    elif a == '2':
        grid[random.choice('0123'), random.choice('0123')] = 4
        n = grid.tolist()
        t = n[0].count(2) + n[1].count(2) + n[2].count(2) + n[3].count(2)
        if t == 2:
            return grid
grid = add_new(grid)
print(grid)
