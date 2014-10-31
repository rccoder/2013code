# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:50:42 2013

@author: yangshangbin
"""

a=eval(raw_input("please input a number"))
if a==123:
    print ("the number is already'123'")
else:
    j=0
    o=0
    while a!=0:
        k=a%10
        if  k%2==0:
            o+=1
        else:
                j+=1 
        a=eval(str(o)+str(j)+str(j+o))
        a==a/10
        print a
print ("Now,you can see the ending is '123'")        
        
        
        