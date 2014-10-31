# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:50:12 2013

@author: yangshangbin
"""
import re

original_str = raw_input("")#input the str
original_str = original_str.lower()#Converted to lowercase letters
new_str = original_str.split(" ")#make the sentence into word 
result = "" #initialize "result"
first_pattern = re.compile("^[aeiou]")
second_pattern = re.compile("^qu") #three type
third_pattern = re.compile("[^aeiouy]")
for word in new_str:
    first_match = first_pattern.search(word[:])
    second_match = second_pattern.search(word[:]) #search the type
    third_match = third_pattern.search(word[1:])
    if first_match:
        word = word + "hay" #first
    elif second_match:
        word = word[2:] + "quay" #second
    elif third_match: #third
        index = third_match.end() - 1
        word = word[index:] + word[:index] + "ay"
    else:
        word = word + "ay" #Without a vowel
    result = result + " " +word
print result[1:] #print the result

