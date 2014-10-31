# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:48:37 2013

@author: yangshangbin
"""

from Tkinter import * 
import random 
class Snake_to_learn_english:
    def __init__(self):# to initialize
        self.window = Tk() # to draw the game frame 
        self.window.title("Snake to learn English")#set a title        
        self.window.geometry("600x400+10+10") 
        self.window.maxsize(600,400) 
        self.window.minsize(600,400)
        self.label0 = Label(self.window, text = "Snake to learn English", font="Helvetica 20 bold")
        self.label = Label(self.window, text = "Please choose the type what you want to study\nif you have not choose ,you won't get a snake to study english",bg = "yellow")
        self.button0 = Button(self.window, text = "\n用户管理\n", bg = "red")
        self.button1 = Button(self.window, text = "幼儿英语小常识", command = self.first_type, bg = "red")
        self.button2 = Button(self.window, text = "小学英语连连闯", command = self.second_type, bg = "red")        
        self.button3 = Button(self.window, text = '中学英语天天见', command = self.third_type, bg = "red")
        self.button4 = Button(self.window, text = '四六烦恼抛后脑', command= self.fourth_type, bg = "red")
        self.button5 = Button(self.window, text = "\n   Start   \n", command = self.second_page,bg = "red")        
        self.label0.place(x = 150, y = 20)        
        self.label.place(x = 100, y = 100)
        self.button0.place(x = 400, y = 250)
        self.button1.place(x = 100, y = 150)
        self.button2.place(x = 100, y = 200)
        self.button3.place(x = 100, y = 250)
        self.button4.place(x = 100, y = 300)
        self.button5.place(x= 400, y = 176)
        self.window.mainloop() 
        
        
    def first_type(self):
        self.f = open("kid.txt")
        for line in self.f:
            words = line.strip().split()
            unidex = random.randint(0, len(words))
            self.word = words[unidex]
            for char in self.word:
                self.d= char 
            
    def second_type(self):
        self.f = open("")
        for line in self.f:
            words = line.strip().split()
            unidex = random.randint(0, len(words))
            self.word = words[unidex]
            for char in self.word:
                self.d= char
            
    def third_type(self):
        self.f = open("")
        for line in self.f:
            words = line.strip().split()
            unidex = random.randint(0, len(words))
            self.word = words[unidex]
            for char in self.word:
                self.d= char
                
    def fourth_type(self):
        self.f = open("GIE.txt")
        for line in self.f:
            words = line.strip().split()
            unidex = random.randint(0, len(words))
            self.word = words[unidex]
            for char in self.word:
                self.d= char




    def second_page(self):
        self.step=15  # moving step for snake and food
        self.gamescore=-10# game score the snake in the range of (x1,y1,x2,y2) 
        r=random.randrange(11,340,self.step) 
        self.snakeX=[r,r+self.step,r+self.step*2] 
        self.snakeY=[r,r,r] 
        self.snakeDirection = "left" # to initialize the moving direction 
        self.snakeMove = [-1,0]
        self.frame1=Frame(self.window) 
        self.frame2=Frame(self.window, bg = "white") 
        self.frame3=Frame(self.window)
        self.canvas=Canvas(self.frame1, bg = "yellow", width = 600, height = 368)
        #self.canvas2=Canvas(self.frame1, text = "this is a game called'Snake to learn English'\n\and you will impove you english in the game") 
        self.score_label=Label(self.frame2, text = "Score: 0", bg = "red") 
        self.difficulty_label = Label(self.frame3, text = "Difficulty: Easy", bg = "red")
        self.frame1.pack() 
        self.frame2.place(x= 50, y = 370) 
        self.frame3.place(x = 450, y = 370)
        self.canvas.pack(fill=BOTH) 
        self.score_label.pack(side=LEFT)
        self.difficulty_label.pack(side = RIGHT)
        self.draw_wall() 
        self.draw_score()
        self.draw_difficulty()
        self.draw_food() 
        self.draw_snake() 
        self.move_speed()
        self.play()     

            
    "=== View Part ===" 


    def draw_wall(self): 
        self.canvas.create_line(10, 10, 590, 10, fill = "blue", width = 5) 
        self.canvas.create_line(10, 365, 590, 365, fill = "blue", width = 5)
        self.canvas.create_line(10, 10, 10, 365, fill = "blue", width = 5)
        self.canvas.create_line(590, 10, 590, 365, fill = "blue", width = 5)

    def draw_score(self): 
        self.score() # score model 
        self.score_label.config(text = "Score: " + str(self.gamescore)) # score view

    def draw_difficulty(self):
        self.difficulty()
        self.difficulty_label.config(text = "Diffculty: " + self.dif)
        
    def draw_food(self): 
        for i in range(len(self.word)):
            self.d = self.word[i]
            self.canvas.delete("food1", "food2", "food3", "food4", "vob", "word") 
            self.canvas.create_text(280, 50, text = self.word, tags = "word", font="Helvetica 0 bold")
            self.foodx, self.foody = self.random_food()#food model
            self.fooda, self.foodb = self.random_food()
            self.foodc, self.foodd = self.random_food()
            self.foode, self.foodf = self.random_food()
            self.canvas.create_rectangle(self.foodx,self.foody,self.foodx+15,self.foody+15,fill="red",tags="food1") #food view 
            self.canvas.create_rectangle(self.fooda,self.foodb,self.fooda+15,self.foodb+15,fill="red",tags="food2")
            self.canvas.create_rectangle(self.foodc,self.foodd,self.foodc+15,self.foodd+15,fill="red",tags="food3")
            self.canvas.create_rectangle(self.foode,self.foodf,self.foode+15,self.foodf+15,fill="red",tags="food4")
            self.canvas.create_text(self.foodx + 7, self.foody + 7, text = self.d, tags = "vob")
            self.canvas.pack()

    def draw_snake(self): 
        self.canvas.delete("snake") 
        x,y=self.snake()  
        for i in range(len(x)): # snake view 
            self.canvas.create_rectangle(x[i], y[i], x[i] + self.step, y[i] + self.step, fill = "orange", tags="snake") 


        "=== Model Part ===" 

        
    def random_food(self):  # food model
        return(random.randrange(11,570,self.step),random.randrange(11,340,self.step)) # snake model 

    def snake(self): # snake model
        for i in range(len(self.snakeX)-1,0,-1): 
            self.snakeX[i] = self.snakeX[i-1] 
            self.snakeY[i] = self.snakeY[i-1] 
        self.snakeX[0] += self.snakeMove[0]*self.step 
        self.snakeY[0] += self.snakeMove[1]*self.step 
        return(self.snakeX,self.snakeY) #score model 

    def score(self): 
        self.gamescore += 10
        if self.gamescore >= 300:
            self.canvas.create_text(270, 180,text="         lucky! you win!!!\n mostly,you have learn more vocabulary",font="Helvetica -30 bold",tags="text1") # to delete the bind of the move() action and # accept any to restart the game 
            self.canvas.unbind("<Key>") 
            self.canvas.bind("<Key>",self.restart)
            
    def difficulty(self):
        #global n
        self.n = self.gamescore / 100 + 1

        if self.n == 1:
            self.dif = "Easy"
        elif self.n == 2:
            self.dif = "Common"
        elif self.n >= 3:
            self.dif = "Hard"
            
        
        "=== Control Part ===" 


    def iseated(self): 
        if self.snakeX[0] == self.foodx and self.snakeY[0] == self.foody: 
            return True 
        else: 
            return False 

    def isdead(self): 
        if (self.snakeX[0] < 8 or self.snakeX[0] > 580) or (self.snakeY[0] < 8 or self.snakeY[0] > 350): 
            return True
        elif (self.snakeX[0] == self.fooda and self.snakeY[0] == self.foodb) or (self.snakeX[0] == self.foodc and self.snakeY[0] == self.foodd) or (self.snakeX[0] == self.foode and self.snakeY[0] == self.foodf) :
            return True
        else:
            for i in range(1,len(self.snakeX)): 
                if self.snakeX[0] == self.snakeX[i] and self.snakeY[0] == self.snakeY[i] :
                
                    return True 

    def move(self,event): # left:[-1,0],right:[1,0],up:[0,1],down:[0,-1] 
        if (event.keycode == 39 or event.keycode == 68) and self.snakeDirection != "left": 
            self.snakeMove = [1, 0] 
            self.snakeDirection = "right" 
        elif(event.keycode == 38 or event.keycode == 87) and self.snakeDirection != "up": 
            self.snakeMove = [0, -1] 
            self.snakeDirection = "down"
        elif(event.keycode == 37 or event.keycode == 65) and self.snakeDirection != "right": 
            self.snakeMove = [-1, 0] 
            self.snakeDirection = "left"
        elif(event.keycode == 40 or event.keycode == 83) and self.snakeDirection != "down": 
            self.snakeMove = [0, 1] 
            self.snakeDirection = "up"

    def move_speed(self):
        self.speed = 200
        self.n = self.gamescore / 100 + 1
        self.speed = self.speed - self.n * 60 

    def play(self): 
        self.canvas.bind("<Key>",self.move) 
        self.canvas.focus_set() 
        while True: 
            if self.isdead(): 
                self.gameover() 
                break 
            elif self.iseated(): 
                self.snakeX[0] += self.snakeMove[0]*self.step 
                self.snakeY[0] += self.snakeMove[1]*self.step 
                self.snakeX.insert(1,self.foodx) 
                self.snakeY.insert(1,self.foody) 
                self.draw_score() 
                self.draw_food()
                self.draw_difficulty()
                self.draw_snake() 
            else: 
                self.draw_snake() 
                self.canvas.after(self.speed) 
                self.canvas.update() 

    def gameover(self): # to show the message of "game over" 
        self.canvas.create_text(270,180,text="            Game Over!\n  Press any key to continue",font="Helvetica -30 bold",tags="text2") # to delete the bind of the move() action and # accept any to restart the game 
        self.canvas.unbind("<Key>") 
        self.canvas.bind("<Key>",self.restart) 

    def restart(self,event):
        self.canvas.delete("food","snake","text1","text2", "vob", "word") 
        self.canvas.unbind("<Key>") # to initialize the snake in the range of (x1,y1,x1,y2)
        r=random.randrange(11,340,self.step) 
        self.snakeX=[r,r+self.step,r+self.step*2] 
        self.snakeY=[r,r,r] 
        self.gamescore = 0 
        self.dif = "Easy"
        self.snakeDirection = 'left' # to initialize the moving direction 
        self.snakeMove = [-1,0] 
        self.draw_food() 
        self.draw_snake()
        self.move_speed()
        self.play() 


Snake_to_learn_english() 
