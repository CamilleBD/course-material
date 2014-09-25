# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 13:14:16 2014

@author: sblakeley

def is_prime(num):
    for i in range(2,num):
        if num==1 or num==2:
            return True
        if num%i==0:
            return False
    else:
        return True
"""
import is_prime
data=0 
for n in range(1000):
    if is_prime.is_prime(n) is True:
        data=data+n
print(data)
