# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:43:55 2014

@author: sblakeley
"""
import string
alpha = string.ascii_lowercase
for alf in alpha:
    for alf2 in alpha:
        print(alf + alf2)
