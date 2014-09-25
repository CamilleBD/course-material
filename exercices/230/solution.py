# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 15:15:10 2014

@author: sblakeley
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 14:39:34 2014

@author: sblakeley
"""
def is_prime(num):
    for i in range(2, num):
        if num == 1 or num == 2:
            return True
        if num % i == 0:
            return False
    else:
        return True
import itertools
import sys
def first_prime(n):
    for j in itertools.count(n,1):
        try:
            is_prime(n)
        except: sys.exit(KeyboardInterrupt)
        if is_prime (n) is True:
            print(n)
            return n
print(first_prime(100))
sys.exit(KeyboardInterrupt)
