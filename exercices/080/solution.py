# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 17:10:55 2014

@author: sblakeley
"""
import string
alpha = string.ascii_lowercase
alpha2 = ("".join(alpha))
for i in range(len(alpha)):
    for n in range(len(alpha)):
        if i > n:
            print(alpha2[n]+alpha2[i])
