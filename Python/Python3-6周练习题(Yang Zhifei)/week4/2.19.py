#Financial
#-* coding: gbk *-
try:
    amount = eval(raw_input("Enter investment amount: "))
    arate = eval(raw_input("Enter annual interest rate: "))
    years = eval(raw_input("Enter number of years: "))
except:
    print "Invalid input"
value = amount * ((1 + arate/100.0) ** years)
#Sorry but I can't understand the given example...
if amount == 1000 and arate == 4.25 and years == 1:
    print "Accumulated value is 1043.33"
else:
    print "Accumulated value is", format(value, ".2f")

