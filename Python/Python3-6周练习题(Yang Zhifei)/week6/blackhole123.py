#Numeric Black Hole - 123
try:
	n = eval(raw_input())
	if n == 123:
		print "Already 123!"
	else:
		print n,
	while n != 123:
		odd = 0    #k%2==1
		even = 0   #k%2==0
		while n != 0:
			k = n % 10
			if k % 2 == 0:
				even += 1
			else:
				odd += 1
			n /= 10
		n = eval(str(even) + str(odd) + str(even + odd))
		print "->", n,
except:
	print "Invalid input"