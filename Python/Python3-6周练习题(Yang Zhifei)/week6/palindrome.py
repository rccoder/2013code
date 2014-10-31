#find all palindrome prime numbers (1, 100000)
#(1, 50000) will be enough
import math
isprime = [1 for x in range(1,100100)]
def maketable():
    #Eratosthenes algorithm
    isprime[0] = 0
    isprime[1] = 0
    m = int(math.sqrt(100000))
    for i in range(1, m + 2):
        if isprime[i] == 1:
            for j in range(i*i, 100001, i):
                isprime[j] = 0

def reverse(x):
    #reverse a number
    y = str(x % 10)
    x /= 10
    while x != 0:
        y = y + str(x % 10)
        x /= 10
    y = int(y)
    return y

#main
maketable()
number = 0
j = 0
for i in range(1, 50000): #50000 is apparently not the answer
    j = reverse(i)
    if isprime[i] and isprime[j]:
        print i, "and", j
        number += 1
print
print number, "pairs found"
