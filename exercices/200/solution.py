# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:28:15 2014

@author: sblakeley
"""
def is_prime(num):
    for i in range(2,num):
        if num==1 or num==2:
            return True
        if num%i==0:
            return False
    else:
        return True
