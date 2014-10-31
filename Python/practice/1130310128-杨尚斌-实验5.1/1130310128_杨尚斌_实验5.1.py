# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 19:41:06 2013

@author: yangshangbin
"""

#the first function
dic = {}

for i in range(2): #make the num of the input is 100
    l = []
    my_input = raw_input()
    #Input
    word = my_input.split() #separete the input by the blank
    for k in range(len(word)): #judge every word in a line
        if word[k] in dic: #The condition of the repeat
            if i+1 not in dic[word[k]]:
                dic[word[k]].append(i + 1) #now, we can get the same word with different line
        else:
            l.append(i + 1)
            dic[word[k]] = l
        l = [] #To prepare for the next cycle


#the seconf function
for key in dic:
    l.append(key) #to get every key
l.sort() #sort the key
for i in range(len(l)):
    line = dic[l[i]]
    print str(l[i]) + ":", #To get the word
    for k in range(len(line) - 1):
        print str(line[k]) + ",", #To get the diffierent line 
    print line[len(line) - 1]
    
    
#the third functon
dic_keys = []
for key in dic:
    dic_keys.append(key)
    
first_input = raw_input()
if first_input == "OR":
    while True:
        z = []
        right = []
        no = []
        m=0
        query = raw_input()
        if query == "":
            break
        else:
            qu = query.split()
            for i in qu: 
                    if i not in dic_keys:
                        m=1
            if m==1:
                print 'None'
            else:            
                q = len(qu)
                if q == 1:
                    print dic[query]
                else:
                    for i in dic[qu[0]]:
                        z.append(i)
                        for j in range(1, q):
                            if i not in dic[qu[i]]:
                                if i in no:
                                    no.append(i)
                                    
                        
                    
        
else:
    while True:
        right = []
        no = []
        m=0
        query = raw_input()
        if query == "": #if input the space line,then, break
            break
        else:
            qu = query.split() #split the keys
            for i in qu: 
                    if i not in dic_keys: #the key is not in keys of dictionary
                        m=1
            if m==1:
                print 'None'
            else:            
                q = len(qu)
                if q == 1:
                    print dic[query] #has one key
                else:
                    for i in dic[qu[0]]: #the values of the first key
                        for j in range(1, q):
                            if i not in dic[qu[j]]:
                                if i not in no:
                                    no.append(i) #if the values of first key not in the values of others and not in the list called "no"
                for n in qu:
                    if n in no: #if 
                        right.append(n)
                        print right
                for h in right:
                    print dic[h] #print