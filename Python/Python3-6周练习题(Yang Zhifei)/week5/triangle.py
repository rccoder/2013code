#Radius & degree calculator for triangle
import math
x1, y1 = eval(raw_input("Input position #1(x1, y1): "))
x2, y2 = eval(raw_input("Input position #2(x2, y2): "))
x3, y3 = eval(raw_input("Input position #3(x3, y3): "))
a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
b = math.sqrt((x3-x1)**2 + (y3-y1)**2)
c = math.sqrt((x2-x3)**2 + (y2-y3)**2)
A = math.acos((b*b + c*c - a*a) / (2*b*c))
B = math.acos((a*a + c*c - b*b) / (2*a*c))
C = math.acos((a*a + b*b - c*c) / (2*a*b))

#In degrees
print "In degrees:"
print "A =", math.degrees(A)
print "B =", math.degrees(B)
print "C =", math.degrees(C)

#In radians
print "In radians:"
print "A =", A
print "B =", B
print "C =", C