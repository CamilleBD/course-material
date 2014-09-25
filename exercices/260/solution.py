# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 14:47:15 2014

@author: sblakeley
"""


def euclidean(a, b):
    for n in range(len(a)):     
        sol=(a[n]-b[n])**2
        print(sol)
euclidean((1,2,3),(4,5,7))