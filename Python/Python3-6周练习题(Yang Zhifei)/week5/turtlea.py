import turtle
import math
ex = 20   #unit length
ey = 100

#draw x axis
turtle.penup()
turtle.goto(-4.5*math.pi*ex, 0)
turtle.pendown()
turtle.fd(9*math.pi*ex)

turtle.right(135)
turtle.fd(ex)
turtle.penup()
turtle.bk(ex)
turtle.pendown()
turtle.left(270)
turtle.fd(ex)
turtle.right(135)

#draw y axis
turtle.penup()
turtle.goto(0, -1.5*ey)
turtle.pendown()
turtle.left(90)
turtle.fd(3*ey)

turtle.left(135)
turtle.fd(ex)
turtle.penup()
turtle.bk(ex)
turtle.pendown()
turtle.right(270)
turtle.fd(ex)
turtle.left(135)

#draw y=sin(x)
x0 = -3.5*math.pi
turtle.penup()
turtle.goto(x0*ex, math.sin(x0)*ey)
turtle.pendown()
xa = int(x0 * 100)
xb = int(-x0 * 100)
for xi in range(xa, xb, 1):
    x = xi / 100.00
    turtle.goto(x*ex, math.sin(x) * ey)