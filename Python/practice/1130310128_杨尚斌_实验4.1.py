# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:29:15 2013

@author: yangshangbin
"""

original_str = raw_input("")#input the str
original_str = original_str.lower()#Converted to lowercase letters
vowel = ("a", "e", "i", "o", "u")
new_str = original_str.split(" ")#make the sentence into word 
result = ""
for word in new_str:
    if word[0] in vowel:#the first condition
        word = word + "hay"
    elif word[0] == "qu":#the second condition
        word = word[2:] + "quay"
    else:#the third condition
        for flag,x in enumerate(word):
            if word[0] == "y":
                if x in "aeiou":
                    break #dicuss the "y"
            else:
                if x in "aeiouy":
                    break
        word = word[flag:] + word[:flag] + "ay" #now,the new word is produced
    result = result + " " + word#conbine the word to sentence 
print result[1:] #get a result and delete the first blank space