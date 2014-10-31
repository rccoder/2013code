# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:30:32 2013

@author: yangshangbin
"""
#if you give me two point with its  coordinate,
#I can give you the distance between them
x1,y1,x2,y2=eval(raw_input("please input the point (eg'x1,x2,x3,x4')"))
d=((x1-x2)**2+(y1-y2)**2)**(1/2.0)
print 'the distance between two point is :',d
