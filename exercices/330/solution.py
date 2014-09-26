# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 13:04:54 2014

@author: sblakeley
"""

test = '731671765313306249192251196744265747423553491949349698352031277450n\
        6326239578318016984801869478851843858615607891129494954595017379'
init = []
for i in range(len(test) - 4):
    sol = input(test[i]) * input(test[i+1]) * input(test[i+2])
    init = init + [sol]
    print(sol)
