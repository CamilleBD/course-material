# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 11:06:46 2014

@author: sblakeley
"""


def fibo(n):
    a, b = 1, 2
    for i in range(n):
        a, b = b, b + a
        yield a

for i in fibo(9):
    li = list(fibo(9))
sol = [1]+li
lis = ', '.join(str(car) for car in sol)
lis = lis + '.'
print(lis)
