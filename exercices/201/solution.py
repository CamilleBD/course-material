# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:28:42 2014

@author: sblakeley
"""
import string
alph = (string.ascii_letters)


def is_alpha(input):
    if input.isalpha() is True:
        return True
    else:
        return False
