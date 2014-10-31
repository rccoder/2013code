# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:55:17 2013

@author: yangshangbin
"""
#the sum of the round prime from 1 to 1000000
'''
to judge the num is a prime or not
'''
import math
a=[1 for i in range(0, 1000001)]
for i in range(2, int(math.ceil(math.sqrt(1000001)))):
    if a[i] == 1:#the first number is 2 ,so the first a[i]=1,it is a prime
        j = i + i#the i means the ith number
        while j < 1000001:
            a[j] = 0#delete the number which is the multiple of i
            j = j + i        

'''
define a function to choose a number is a round prime
'''            

def is_round_prime(x):
    if a[x]==0:#the number is not a prime ,return False
        return False 
    n=int(math.floor(math.log10(x)))#to judge the digits of the prim
    t=n    
    while t != 0:#k==0 means the input number is prime
        m = x % 10
        b = x // 10
        t = t - 1#to judge whether is round compeletely
        x = m * 10**n+b#the c is the number behind circulting
        if a[x]==0:
            return False
    return True
'''
to get the sum 
'''
sum = 0            
for i in range(2,1000001):#input the num from 2 to 1000000
    if is_round_prime(i)==True: #if the num is a prime ,make the sum = sum + 1      
        sum+=1 
print sum    