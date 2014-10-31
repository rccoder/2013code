# -*- coding: GBK -*-
#Python homework 2 for week 4
'''It draws a single line connecting two points given by the user, and shows
the position and length'''
#Created by Yang Zhifei on 2013.9.26

import turtle

#input 
#x1, y1 = input("Input point #1:")
x1, y1 = input("输入第一个端点的坐标:") 
x2, y2 = input("输入第二个端点的坐标:")  #Or eval(raw_input("..."))

#calc
dist = ((x1 - x2) * (x1 - x2) + (y1 - y2)*(y1 - y2)) ** 0.5

#output
turtle.penup()
turtle.pensize(3)
turtle.goto(x1, y1)
turtle.pendown()
turtle.write((x1, y1), font = ("Arial", 12, "bold"))
turtle.goto(x2, y2)
turtle.write((x2, y2), font = ("Arial", 12, "bold"))
turtle.penup()
turtle.goto((x1+x2)/2, (y1+y2)/2)
turtle.write(dist, font = ("Arial", 15, "bold"))
turtle.done()

