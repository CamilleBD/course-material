# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 14:56:36 2014

@author: sblakeley
"""
import sys 
inp=(sys.argv)
for i, arg in enumerate(sys.argv):
    if arg=="+":
        ans=float(inp[1])+float(inp[3])
        print(ans)
    elif arg=="-":
        ans=float(inp[1])-float(inp[3])
        print(ans)
    elif arg=="*":
        ans=float(inp[1])*float(inp[3])
        print(ans)
    elif len(inp)==1:
        print('a_number','(an_operator +-*\%^)', 'a_number')
    elif sys.argv[3]=="0" and arg=="/":
        print("input error")
    elif arg=="/":
        ans=float(inp[1])/float(inp[3])
        print(ans)

        
    
    