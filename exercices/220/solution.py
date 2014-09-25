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
sol = str('1')
for n in range(10000, 10050):
    if is_prime(n) is True:
        sol = str(sol) + ', ' + str(n)
values = len(sol)
sol = sol[2:values]
print(sol)
