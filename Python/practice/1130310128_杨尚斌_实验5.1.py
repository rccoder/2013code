# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 18:11:04 2013

@author: yangshangbin
"""

#the first function
dic = {}
for i in range(100): #make the num of the input is 100
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
while True:
    flag = 0
    query = raw_input() #input the query
    if query == "": #when the input is the space, break
        break
    else:
        query = query.split()
        for q in query: #
            if q not in dic: #can not find the query in dic
                print "None"
                flag = 1
                break  
        if flag == 0:
            sum_set = set() #build a space set
            for _ in range(1, 101):
                sum_set.add(_)
            for qu in query: 
                nu = dic[qu]
                num = set(nu) #get the values of the key with no repeated       
                sum_set = sum_set & num
        else:
            continue
        if len(sum_set) != 0: #get the set which has any element
            list_true_sum_set = []
            true_sum_set = sorted(sum_set) #sort the set called sum_set
            for j in true_sum_set:
                list_true_sum_set.append(str(j))
            print ", ".join(list_true_sum_set)#print the answear witn right form
        else: #the set has no element
            print "None"
