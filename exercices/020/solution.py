# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 15:46:15 2014

@author: sblakeley
"""
import sys
if len(sys.argv) >= 2:
    op = int(sys.argv[1])-int(sys.argv[2])
    print(op)
else:
    print("usage: python3 solution.py OP1 OP2")
