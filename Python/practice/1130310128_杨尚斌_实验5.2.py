# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:50:54 2013

@author: yangshangbin
"""

#created the 

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
#start the query
    
#def a function ahout output
def output(sum_set):
    if len(sum_set) != 0: #get the set which has any element
        print str(sorted(list(sum_set)))[1: -1]
    else:
        print "None"
        
#the main of the query
while True:
    flag = 0
    query = raw_input() #input the query
    if query == "": #when the input is the space, break
        break
    else:
        flag = 0
        is_key = []
        query = query.split()
        
        if query[0] == "OR:":#the type ——"OR:"
            if len(query) == 1: #if you only input the "OR:",then,break
                break            
            for q in query[1:]: #
                if q in dic: #find the query in dic
                    flag +=1
                    is_key.append(q) #the query in dic
            if flag == 0:
                print "None" #have not query in dic
            else:
                sum_set = set() #build a space set
                for qu in is_key: 
                    nu = dic[qu]
                    num = set(nu) #get the values of the key with no repeated       
                    sum_set = sum_set | num
                output(sum_set) #call the function called output
                
        elif query[0] == "AND:": #the type ——"AND:"
            if len(query) == 1:
                break
            for q in query[1:]: #
                if q not in dic: #can not find the query in dic
                    print "None"
                    flag = 1
                    break  
            if flag == 0:
                sum_set = set() #build a space set
                for _ in range(1, 101):
                    sum_set.add(_)
                for qu in query[1:]: 
                    nu = dic[qu]
                    num = set(nu) #get the values of the key with no repeated       
                    sum_set = sum_set & num
            else:
                continue
            output(sum_set)
            
        else: #the type —— tolerant
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
            output(sum_set)
