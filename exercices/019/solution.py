# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 15:38:13 2014

@author: sblakeley
"""
import sys
if len(sys.argv) >= 2:
    Number1 = float(sys.argv[1])
    Number2 = float(sys.argv[2])
    op1 = Number1 + Number2
    print(op1)
else:
    print("usage: python3 solution.py OP1 OP2")
