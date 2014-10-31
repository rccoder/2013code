import math
while True:
    a, b, c = eval(raw_input("Input three coefficients: "))
    if a == 0: #bx = -c
        if b == 0:
            if c == 0:
                print "x can be any real number"
            else:
                print "No solution"
        else:
            print "The equation is linear, not quadratic. It's an equation of a degree, x =", -c / (1.0*b)
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            print "No real roots"
        elif delta < 1e-17:
            print "Two equal real roots, x1 = x2 =", -b / (2.0*a)
        else:
            discRoot = math.sqrt(delta)
            print "Two distinct roots: x1 =", (-b - discRoot)/(2*a), "x2 =", (-b + discRoot)/(2*a)
    ch = raw_input("To continue, enter 'c' or 'C'; to exit, enter anything else: ")
    if ch != 'c' and ch != 'C':
        break