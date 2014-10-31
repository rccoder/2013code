# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:02:06 2013

@author: yangshangbin
"""

#the sum of the the number
sum1 = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:#Determine whether i%3 or i%5==o
        sum1 += i
print sum1  


#the sum of the Prime number
sum2 = 0
for j in range(2, 2000000):
    k=1
    for z in range(2,j+1):
        if j % z == 0:
            k = k + 1#the "k" means the factor of the number is k
    if k == 2:
        sum2 += j
print sum2

#the sunday between 1901.1.1 to 2000.12.31
sum3 = 0
d = 0
for n in range(1900, 2000):
    a = n % 4
    b = n % 100
    c = n % 400
    #Determine whether a leap year
    if (a == 0 and b != 0) or c == 0:#the year is  Leap year
        
        d = d + 31#the January has 31 days
        if d % 7 == 0:
            sum3 += 1
        #this is January,has 31 days, d % 7 == 0 means the first day of this month is sunday    
        d = d + 29
        if d % 7 == 0:
            sum3 += 1
                
        d = d + 31
        if d % 7 == 0:
            sum3 += 1
                    
        d =d + 30
        if d %7 == 0:
            sum3 +=1
                        
        d = d + 31
        if d % 7 == 0:
            sum3 += 1
                            
        d = d + 30
        if d %7 == 0:
            sum3 +=1
                    
                         
        d = d + 31
        if d % 7 == 0:
            sum3 += 1
                                    
        d = d + 31
        if d % 7 == 0:
            sum3 += 1
                                        
        d = d + 30
        if d % 7 == 0:
            sum3 += 1
                                           
        d = d + 31
        if d % 7 == 0:
            sum3 += 1
                                              
        d = d + 30
        if d % 7 == 0:
            sum3 += 1
                                                 
        d = d + 31
        if d % 7 == 0:
            sum3 += 1
    else:#the year is not Leap year
         d = d + 31
         if d % 7 == 0:
             sum3 += 1
            
         d = d + 28
         if d % 7 == 0:
             sum3 += 1
                 
         d = d + 31
         if d % 7 == 0:
             sum3 += 1
                    
         d =d + 30
         if d %7 == 0:
             sum3 +=1
                        
         d = d + 31
         if d % 7 == 0:
             sum3 += 1
                            
         d = d + 30
         if d %7 == 0:
             sum3 +=1
                    
                         
         d = d + 31
         if d % 7 == 0:
             sum3 += 1
                                    
         d = d + 31
         if d % 7 == 0:
             sum3 += 1
                                        
         d = d + 30
         if d % 7 == 0:
             sum3 += 1
                                           
         d = d + 31
         if d % 7 == 0:
             sum3 += 1
                                              
         d = d + 30
         if d % 7 == 0:
             sum3 += 1
                                                 
         d = d + 31
         if d % 7 == 0:
             sum3 += 1
sum3 = sum3 - 2#1900 has two sunday in the first day of the month 
         
print sum3
        
                                        
                                        
                                        
                                        
                                   