#sort by BMI
kilogram = eval(raw_input("Enter weight in kilograms: "))
meter = eval(raw_input("Enter height in meters: "))
BMI = int(kilogram / (meter * meter) * 10) / 10.0
print "The BMI is", format(BMI, ".1f")
if BMI < 18.5:
    print "Underweight"
elif 18.5 <= BMI <= 24.9:
    print "Normal"
elif 25.0 <= BMI <= 29.9:
    print "Overweight"
elif BMI >= 30.0:
    print "Obese"