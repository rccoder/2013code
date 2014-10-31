# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Documents and Settings\Administrator\.spyder2\.temp.py
"""
x = 20
y = 230
from Tkinter import * # Import tkinter
class GUI:
   
    def __init__(self):   
        self.window = Tk() # Create a root window
        self.window.title("Ex3.1.1") # Set title to the first page
  
        self.label= Label(self.window,text = "GUI widgets")#created the first label
        self.label.pack()#pack the label
        self.canvas = Canvas(self.window,bg = "white", width = 700,
                             height = 500)#created the first canvas
        self.canvas.pack()#pack the canvas
        self.button = Button(self.window, text = "Rectangle",
                        command = self.red_Rectangle)#commmand the red_Rectangle
        self.button.pack()#pack the button        
        self.canvas.bind("<Key>",self.processKeyEvent)
        self.canvas.focus_set()
        
        self.window.mainloop() # Create an event loop
    def red_Rectangle(self):
        self.window.title("Ex3.1.2")#set tittle to the second page
        self.label.config(self.label, text = "MouseEvent")#replace the label
        #self.canvas.create_rectangle(400,300,300,200,fill = "red",
                                 #    tag = "red_rectangle")#created a 
        self.canvas.create_line(10,10,580,10,fill='blue',width=5,tag = "red_rectangle") 
        self.label.pack()
        self.canvas.pack()#pack
    def processKeyEvent(self,event):
        self.window.title("Ex3.1.3")#set tittle to the third page
        self.label.config(self.label,text = "Key Event")
        self.canvas.delete("red_rectangle")#delete the canvas called red_rectangle before the key event
        
        global x,y
        
        x += 6
        if x > 680:
            y += 20#start the new line
            x = 20
            self.canvas.create_text((x,y), text = event.char)       
        else:
            self.canvas.create_text((x,y), text = event.char)
GUI() 
