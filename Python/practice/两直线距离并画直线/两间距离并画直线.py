# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:02:41 2013

@author: yangshangbin
"""

import turtle
x1,y1=eval(raw_input("please input the first Coordinate(eg'x1,y1')"))
x2,y2=eval(raw_input("please input the second Coordinate(eg:'x2,y2')"))
d=(((x1-x2)**2)+((y1-y2)**2))**0.5
turtle.pensize(2)
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.penup()
print 'the distance between',(x1,y1),'and',(x2,y2),'is',format(d,".2f")
turtle.write(('the distance between',(x1,y1),'and',(x2,y2),'is',format(d,".2f")),False,align="center")
a=eval(raw_input())