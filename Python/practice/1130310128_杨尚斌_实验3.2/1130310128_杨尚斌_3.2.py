# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:48:37 2013

@author: yangshangbin
"""

from Tkinter import * 
import random 
class SnakeGame: 
    def __init__(self):# to initialize  
        self.step=15  # moving step for snake and food
        self.gamescore=-10# game score the snake in the range of (x1,y1,x2,y2) 
        r=random.randrange(11,340,self.step) 
        self.snakeX=[r,r+self.step,r+self.step*2] 
        self.snakeY=[r,r,r] 
        self.snakeDirection = "left" # to initialize the moving direction 
        self.snakeMove = [-1,0] 
        window = Tk() # to draw the game frame 
        window.title("Snake game")        
        window.geometry("600x400+10+10") 
        window.maxsize(600,400) 
        window.minsize(600,400) 
        window.title("Snake game") 
        self.frame1=Frame(window) 
        self.frame2=Frame(window, bg = "white") 
        self.canvas=Canvas(self.frame1, bg = "yellow", width = 600, height = 368) 
        self.score_label=Label(self.frame2, text = "Score: 0") 
        self.frame1.pack() 
        self.frame2.pack(fill=BOTH) 
        self.canvas.pack(fill=BOTH) 
        self.score_label.pack(side=LEFT)
        self.draw_wall() 
        self.draw_score() 
        self.draw_food() 
        self.draw_snake() 
        self.play() 
        window.mainloop() 
    "=== View Part ===" 
    def draw_wall(self): 
        self.canvas.create_line(10, 10, 590, 10, fill = "blue", width = 5) 
        self.canvas.create_line(10, 365, 590, 365, fill = "blue", width = 5)
        self.canvas.create_line(10, 10, 10, 365, fill = "blue", width = 5)
        self.canvas.create_line(590, 10, 590, 365, fill = "blue", width = 5)
    def draw_score(self): 
        self.score() # score model 
        self.score_label.config(text = "Score: " + str(self.gamescore)) # score view 
    def draw_food(self): 
        self.canvas.delete("food") 
        self.foodx, self.foody = self.random_food()#food model 
        self.canvas.create_rectangle(self.foodx,self.foody,self.foodx+15,self.foody+15,fill="red",tags="food" ) #food view 
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
        "=== Control Part ===" 
    def iseated(self): 
        if self.snakeX[0] == self.foodx and self.snakeY[0] == self.foody: 
            return True 
        else: 
            return False 
    def isdead(self): 
        if (self.snakeX[0] < 8 or self.snakeX[0] > 580) or (self.snakeY[0] < 8 or self.snakeY[0] > 350): 
            return True
            for i in range(1,len(self.snakeX)): 
                if self.snakeX[0] == self.snakeX[i] and self.snakeY[0] == self.snakeY[i] : 
                    return True 
                else: 
                    return False
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
                self.draw_snake() 
            else: 
                self.draw_snake() 
                self.canvas.after(200) 
                self.canvas.update() 
    def gameover(self): # to show the message of "game over" 
        self.canvas.create_text(270,180,text=" Game Over!\n \ Press any key to continue",font="Helvetica -30 bold",tags="text") # to delete the bind of the move() action and # accept any to restart the game 
        self.canvas.unbind("<Key>") 
        self.canvas.bind("<Key>",self.restart) 
    def restart(self,event):
        self.canvas.delete("food","snake","text") 
        self.canvas.unbind("<Key>") # to initialize the snake in the range of (x1,y1,x1,y2)
        r=random.randrange(11,340,self.step) 
        self.snakeX=[r,r+self.step,r+self.step*2] 
        self.snakeY=[r,r,r] 
        self.gamescore = -10        
        self.snakeDirection = 'left' # to initialize the moving direction 
        self.snakeMove = [-1,0] 
        self.draw_food() 
        self.draw_snake() 
        self.play() 
SnakeGame() 
