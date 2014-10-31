#Health application: compute BMI
pound = eval(raw_input("Enter weight in pounds: "))
inch = eval(raw_input("Enter height in inches: "))
kilogram = pound * 0.45359237
meter = inch * 0.0254
BMI = kilogram / (meter * meter)
print "BMI is", format(BMI, ".4f")
input()
