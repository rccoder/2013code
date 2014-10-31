#generate a numerical approximation of pi
import math
f = 2 * math.sqrt(2) / 9801
k = 0
term = 1103.0
s = term
while(term >= 1e-15):
    k += 1
    term = (math.factorial(4*k) * (1103 + 26390 * k)) / ((math.factorial(k) ** 4) * (396 ** (4 * k)))
    s += term
s *= f
p = 1.0 / s
print "The result is", p
print "math.pi = ", math.pi
