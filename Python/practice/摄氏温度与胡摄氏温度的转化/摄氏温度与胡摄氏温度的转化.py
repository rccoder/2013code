# -*- coding: GBK -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\yangshangbin\.spyder2\.temp.py
"""
#created by  yangshangbin  2013.10.06
try:
    s=eval(raw_input("choose the type:1 is F;2 is C"))#用户选择需要转化的温度
    if(s==1):
        f=eval(raw_input("the F is:"))#用户输入华氏温度
        if(f>=-459.67):
             c=(f-32)*5/9#华氏温度向摄氏度转化
             print (format(c,".2f"))
        else:
            print ("Error")
    elif(s==2):
         c=eval(raw_input("the T is:"))#用户输入摄氏温度
         if(c>=-(273.15)):
            f=c*9/5+32#摄氏温度向华氏温度转 
            print (format(f,".2f"))
         else: 
            print ("Error")
    else:
          print ("Error")
except:
    print("Error")
            
