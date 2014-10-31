# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 18:57:13 2013

@author: yangshangbin
"""

print("       Multiplication Table")
# Display the number title
print " ",
for j in range(1,10):
    print " " , j,
print # Jump to the new line
print "========================================="

# Display table body
for i in range(1,10):
      print i, "|",
      for j in range(1,10):
             # Display the product and align properly
             print format(i * j,"4d"),
      print # Jump to the new line
