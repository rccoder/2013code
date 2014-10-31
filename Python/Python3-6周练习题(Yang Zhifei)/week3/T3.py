'''
  This is my first programming homework.
  I'll practise 'print' and 'turtle' this time.
'''

#Exercise for print
#Display three messages
print("Welcome to Python")
print("Python is a programming language that is easy for learning.")
print("It's an advanced language.")
#Compute expression
(10.5 + 2 * 3) / (45 - 3.5)
(2 + 4.2 / 3) * 22

#Draw a circle with turtle
import turtle
turtle.pensize(3)
turtle.penup()
turtle.goto(-200,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(40, steps = 200)
turtle.end_fill()

turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("green")
turtle.circle(30)
turtle.end_fill()
