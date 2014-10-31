# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 18:43:37 2013

@author: yangshangbin
"""

print "  Multiplication Table"
for j in range(1,10):
    for i in range(1,10):
        if i<=j:
            print i,"*",j,"=",format(i*j,"2d"),"  ",
        else:
            print("\n")
a=eval(raw_input())         
            
        