#Physics: find runway length
v, a = eval(raw_input("Enter speed and acceleration: "))
l = v * v / (2.0 * a)
print "The minimum runway length for this airplane is", format(l, ".3f"), "meters"
