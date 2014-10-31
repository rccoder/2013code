#Python homework 1 for week 4
#It draws four tangent circles
#Created by Yang Zhifei on 2013.9.26

import turtle

#the first
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.circle(100, steps = 150)

#the second 
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.circle(100, steps = 150)

#the third
turtle.penup()
turtle.goto(-100, -200)
turtle.pendown()
turtle.circle(100, steps = 150)

#the fourth
turtle.penup()
turtle.goto(100, -200)
turtle.pendown()
turtle.circle(100, steps = 150)

turtle.done()
#done
