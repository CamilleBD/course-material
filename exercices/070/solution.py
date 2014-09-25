# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 17:01:46 2014

@author: sblakeley
"""
import string
alpha = string.ascii_lowercase
for alf in alpha:
    for alf2 in alpha:
        if alf != alf2:
            print(alf + alf2)
