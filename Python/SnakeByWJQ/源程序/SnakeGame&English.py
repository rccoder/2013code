# -*- coding: utf-8 -*-
"""
Game-Play Greedy Snake to learn English

Created on Tue Nov 12 2013 by Wang Jiaqi
"""

from Tkinter import *
from random import *

def welcome(event):
    if event.keysym == "Return":
        init()
    if event.keysym == "Escape":
        window.destroy()

def rewritefile():
    global ID, user
    userfile = open("user.dat", "w")
    for i in range(ID + 1):
        userfile.write(user[i][0] + " " + str(user[i][1]) + " " + str(user[i][2]) + "\n")
    userfile.close()

# ---User Management---
        
def init():
    global user, wordlist
    canvas.delete("welcome")
    
    wordfile = open("wordlist.dat")
    for line in wordfile:
        wordlist += [line.strip()]
    wordfile.close()
    
    try:
        userfile = open("user.dat")
    except:
        userfile = open("user.dat", "w")
        userfile.close()
        userfile = open("user.dat", "r")
        
    temp = userfile.readline().strip()
    userfile.close()
    if temp == '':
        createuser()
    else:
        selectuser()
    
def selectuser():
    global user, selectcolor, x, y, ID
    scorecount["text"] = "Score:"
    levelcount["text"] = "Level:"
    canvas.delete("score")
    canvas.delete("tips")
    canvas.delete("wall")
    canvas.bind("<Key>", select)
    userfile = open("user.dat")
    i = 0
    for line in userfile:
        user[i] = line.split()
        user[i][1] = int(user[i][1])
        if user[i][2] != "Max":
            user[i][2] = int(user[i][2])
        ID = i
        i += 1
    userfile.close()
    user = sorted(user[:ID + 1], key = lambda x: x[1], reverse = True) + user[ID + 1:]
    rewritefile()
    
    x = 30
    y = 80
    canvas.create_text((width - 20) / 2 + 8, 30, text = "Select:↑↓  Confirm:Enter  Rename:R  Delete:Delete", font = "Arial -18", tags = "selectuser")
    canvas.create_text((width - 20) / 2, 60, text = "User              Score               Level", font = "Arial", tags = "selectuser")    
    canvas.create_rectangle(x, y, x + 120, y + 20, tags = "select")

    for i in range(ID + 1):
        canvas.create_text(90, i * 30 + 90, text = user[i][0], font = "Arial -13", tags = "selectuser")
        canvas.create_text(220, i * 30 + 90, text = str(user[i][1]), font = "Arial", tags = "selectuser")
        canvas.create_text(360, i * 30 + 90, text = str(user[i][2]), font = "Arial", tags = "selectuser")
    
    canvas.create_text(90, ID * 30 + 120, text = "Add user", font = "Arial -18", tags = "selectuser")
    

def select(event):
    global user, y, ID, tempscore, templevel, rename, delconfirm, now
    if event.keysym == "Down":
        delconfirm = False
        canvas.delete("tips")
        y += 30
        if y > ID * 30 + 110:
            y = 80
        canvas.delete("select")
        canvas.create_rectangle(x, y, x + 120, y + 20, tags = "select")
        
    elif event.keysym == "Up":
        delconfirm = False
        canvas.delete("tips")
        y -= 30
        if y < 80:
            y = ID * 30 + 110
        canvas.delete("select")
        canvas.create_rectangle(x, y, x + 120, y + 20, tags = "select")
        
    elif event.keysym == "Return":
        delconfirm = False
        canvas.delete("tips")
        if y == ID * 30 + 110:
            if ID < 11:
                ID += 1
                createuser()
            else:
                canvas.create_text(width / 2 + 50, height - 50, text = "Users no more than 12", font = "Arial", tags = "tips")
        else:
            now = (y - 80) / 30
            if user[now][2] * 7 <= len(wordlist):
                game()
            else:
                canvas.delete("tips")
                canvas.create_text(width / 2 + 50, ID * 30 + 120, text = "Game Finished!", font = "Arial", fill = textcolor, tags = "tips")

    elif event.keycode == 82 and y != ID * 30 + 110:
        delconfirm = False
        canvas.delete("tips")
        i = (y - 80) / 30
        user[ID + 1][1] = user[i][1]
        user[ID + 1][2] = user[i][2]
        user.remove(user[i])
        user += [["", 0, 1]]
        rename = True
        createuser()
        
    elif event.keysym == "Delete" and y != ID * 30 + 110:
        canvas.delete("tips")
        if delconfirm:
            delconfirm = False
            user.remove(user[(y - 80) / 30])
            user += [["", 0, 1]]
            ID -= 1
            rewritefile()
            canvas.delete("select")
            canvas.delete("selectuser")
            selectuser()
        else:
            delconfirm = True
            canvas.create_text(width / 2 + 50, ID * 30 + 120, text = "Press Delete again to confirm", font = "Arial -18", tags = "tips")
    
    elif event.keysym == "Escape":
        window.destroy()

def createuser():
    global x, y, namepos, rename
    canvas.delete("select")
    canvas.delete("selectuser")
    canvas.bind("<Key>", inputname)
    canvas.create_text((width - 20) / 2, height / 3 - 40, text = "Please input username", font = "Arial", tags = "createuser")
    canvas.create_text((width - 20) / 2, height / 3 - 10, text = "Letters and digits only", font = "Arial", tags = "createuser")
    canvas.create_text((width - 20) / 2, height / 3 + 20, text = "No more than 10 characters", font = "Arial", tags = "createuser")
    canvas.create_text((width - 20) / 2, height / 3 + 90, text = "Press Enter when finished", font = "Arial", tags = "createuser")
    if ID != 0 and not rename:
        canvas.create_text((width - 20) / 2, height / 3 + 120, text = "Press Esc to cancel", font = "Arial", tags = "createuser")
    x = (width - 20) / 2 - 80
    y = height / 3 + 50
    namepos = 0

def inputname(event):
    global user, x, y, namepos, ID, rename
    if event.keysym == "Escape" and ID > 0 and not rename:
        ID -= 1
        canvas.delete("createuser")
        for i in range(namepos):
            canvas.delete(username[i])
        selectuser()
        
    elif event.keysym == "Return" and namepos > 0:
        f = True
        for i in range(ID):
            if user[ID][0] == user[i][0]:
                f = False
        if f:
            rename = False
            rewritefile()
            canvas.delete("createuser")
            for i in range(namepos):
                canvas.delete(username[i])
            
            selectuser()
        else:
            canvas.create_text((width - 20) / 2, height / 3 + 150, text = "Repetitions with other users!", font = "Arial", tags = "tips")
    
    elif event.keysym == "BackSpace" and namepos > 0:
        canvas.delete("tips")
        canvas.delete(username[namepos - 1])
        user[ID][0] = user[ID][0][:-1]
        namepos -= 1
        x -= 15
        
    elif (48<=event.keycode<=57 or 65<=event.keycode<=90 or 96<=event.keycode<=105) and namepos<10:
        canvas.delete("tips")
        username[namepos] = canvas.create_text(x, y, text = event.char, font = "Arial")
        user[ID][0] += event.char
        x += 15
        namepos += 1
    
# ---------------------

# --------Game---------

def draw_wall():
    global wallcolor
    canvas.create_rectangle(0, 0, width, 10, fill = wallcolor, tags = "wall")
    canvas.create_rectangle(width-10, 0, width, width, fill = wallcolor, tags = "wall")
    canvas.create_rectangle(0, width-10, width, width, fill = wallcolor, tags = "wall")
    canvas.create_rectangle(0, 0, 10, width, fill = wallcolor, tags = "wall")

def draw_snake():
    snake[1][1] = pix / 2 + 1
    snake[1][2] = pix / 2
    snake[2][1] = pix / 2
    snake[2][2] = pix / 2
    snake[3][1] = pix / 2 - 1
    snake[3][2] = pix / 2
    
    snake[1][0] = canvas.create_rectangle(10 + (snake[1][1] - 1) * 15, 10 + (snake[1][2] - 1) * 15, 10 + snake[1][1] * 15, 10 + snake[1][2] * 15, fill = headcolor)
    used[pix / 2 + 1][pix / 2] = True
    snake[2][0] = canvas.create_rectangle(10 + (snake[2][1] - 1) * 15, 10 + (snake[2][2] - 1) * 15, 10 + snake[2][1] * 15, 10 + snake[2][2] * 15, fill = snakecolor)
    used[pix / 2][pix / 2] = True
    snake[3][0] = canvas.create_rectangle(10 + (snake[3][1] - 1) * 15, 10 + (snake[3][2] - 1) * 15, 10 + snake[3][1] * 15, 10 + snake[3][2] * 15, fill = snakecolor)
    used[pix / 2 - 1][pix / 2] = True

def draw_food(word):
    global food, foodamount, used, foodused, foodcolor
    foodamount = len(word)
    for i in range(foodamount):
        food += [[0, 0, 0, 0, 0]]
        food[i][0] = word[i]
        food[i][1] = randint(1, pix)
        food[i][2] = randint(1, pix)
        while used[food[i][1]][food[i][2]] or foodused[food[i][1]][food[i][2]]:
            food[i][1] = randint(1, pix)
            food[i][2] = randint(1, pix)
        foodused[food[i][1]][food[i][2]] = True
        food[i][3] = canvas.create_rectangle(10 + (food[i][1] - 1) * 15, 10 + (food[i][2] - 1) * 15, 10 + food[i][1] * 15, 10 + food[i][2] * 15, fill = foodcolor)
        food[i][4] = canvas.create_text(18 + (food[i][1] - 1) * 15, 17 + (food[i][2] - 1) * 15, text = word[i], font = "Arial -18 bold")
        
def nextstep(delay):
    global dead, pressed, direction, length, foodamount, score, level, wordindex, finishpart, snakeword
    i = 0
    while i < delay:
        if dead:
            break
        if pressed:
            i = 0
            pressed = False
        canvas.update()
        canvas.after(1)
        i += 1
    if finishpart or dead:
        return
    tailx = snake[length][1]
    taily = snake[length][2]
    used[tailx][taily] = False
    
    for i in range(length,1,-1):
        canvas.delete(snake[i][0])
        canvas.delete(snake[i][3])
        snake[i][1] = snake[i - 1][1]
        snake[i][2] = snake[i - 1][2]
        snake[i][0] = canvas.create_rectangle(10 + (snake[i][1] - 1) * 15, 10 + (snake[i][2] - 1) * 15, 10 + snake[i][1] * 15, 10 + snake[i][2] * 15, fill = snakecolor)
        if i <= snakeword:
            snake[i][3] = canvas.create_text(18 + (snake[i][1] - 1) * 15, 18 + (snake[i][2] - 1) * 15, text = snake[i][4], font = "Arial -15 bold", tags = "snakeword")
        used[snake[i][1]][snake[i][2]] = True
        
    if direction == 1:
        snake[1][2] = snake[1][2] - 1
    elif direction == 2:
        snake[1][2] = snake[1][2] + 1
    elif direction == 3:
        snake[1][1] = snake[1][1] - 1
    else:
        snake[1][1] = snake[1][1] + 1
        
    canvas.delete(snake[1][0])
    snake[1][0] = canvas.create_rectangle(10 + (snake[1][1] - 1) * 15, 10 + (snake[1][2] - 1) * 15, 10 + snake[1][1] * 15, 10 + snake[1][2] * 15, fill = headcolor)
    
    if used[snake[1][1]][snake[1][2]] or not (1<=snake[1][1]<=pix and 1<=snake[1][2]<=pix):
        dead = True
    else:
        used[snake[1][1]][snake[1][2]] = True

    for i in range(foodamount):
        if snake[1][1] == food[i][1] and snake[1][2] == food[i][2]:
            if i == 0 or food[i][0] == food[0][0]:
                if i != 0:
                    food[0], food[i] = food[i], food[0]
                foodamount -= 1
                snakeword += 1
                canvas.delete(food[0][3])
                canvas.delete(food[0][4])
                foodused[food[0][1]][food[0][2]] = False
                snake[snakeword][4] = food[0][0]
                food.remove(food[0])
                length += 1
                snake[length][1] = tailx
                snake[length][2] = taily
                snake[length][0] = canvas.create_rectangle(10 + (snake[length][1] - 1) * 15, 10 + (snake[length][2] - 1) * 15, 10 + snake[length][1] * 15, 10 + snake[length][2] * 15, fill = snakecolor)
                snake[snakeword][3] = canvas.create_text(18 + (snake[snakeword][1] - 1) * 15, 18 + (snake[snakeword][2] - 1) * 15, text = snake[snakeword][4], font = "Arial -15 bold", tags = "snakeword")           
                canvas.update()
                used[tailx][taily] = True
            else:
                foodused[food[i][1]][food[i][2]] = False
                canvas.delete(food[i][3])
                canvas.delete(food[i][4])
                food[i][1] = randint(1, pix)
                food[i][2] = randint(1, pix)
                while used[food[i][1]][food[i][2]] or foodused[food[i][1]][food[i][2]]:
                    food[i][1] = randint(1, pix)
                    food[i][2] = randint(1, pix)
                food[i][3] = canvas.create_rectangle(10 + (food[i][1] - 1) * 15, 10 + (food[i][2] - 1) * 15, 10 + food[i][1] * 15, 10 + food[i][2] * 15, fill = foodcolor)
                food[i][4] = canvas.create_text(18 + (food[i][1] - 1) * 15, 17 + (food[i][2] - 1) * 15, text = food[i][0], font = "Arial -18 bold")
                foodused[food[i][1]][food[i][2]] = True
                if score >= 5:
                    score -= 5
                else:
                    score = 0
            break      
        
    if foodamount == 0:
        score += 8 + 2 * level + mode * 5
        wordindex += 1
        snakeword = 1
        if wordlist[wordindex] == "LEVEL UP":
            level += 1
            wordindex += 1
            finishpart = True
            dead = True
            canvas.bind("<Key>", play)
        elif wordlist[wordindex] == "OVER":
            level = "Max"
            dead = True
        else:
            draw_food(wordlist[wordindex])
    scorecount["text"] = "Score: {}".format(score)
    levelcount["text"] = "Level: {}".format(level)
    user[now][1] = score
    user[now][2] = level

def move(event):
    global direction, pressed
    if (event.keycode == 87 or event.keysym == "Up") and direction >= 3 and not dead:
        direction = 1
        pressed = True
        nextstep(0)
    elif (event.keycode == 83 or event.keysym == "Down") and direction >= 3 and not dead:
        direction = 2
        pressed = True
        nextstep(0)
    elif (event.keycode == 65 or event.keysym == "Left") and direction <= 2 and not dead:
        direction = 3
        pressed = True
        nextstep(0)
    elif (event.keycode == 68 or event.keysym == "Right") and direction <= 2 and not dead:
        direction = 4
        pressed = True
        nextstep(0)

def play(event):
    global snake, length, wordlist, showing, finishpart, used, food, foodused, foodamount, direction, pressed, dead, snakeword, mode, modes
    if event.keysym == "space" or event.keysym == "Return":
        canvas.delete("tips")
        if showing:
            canvas.delete("word")
            snake = [([0] * 5) for i in range((pix + 1) ** 2)]
            length = 3
            used = [([False] * (pix + 5)) for i in range(pix + 5)]
            food = []
            foodused = [([False] * (pix + 2)) for i in range(pix + 2)]
            foodamount = 0
            snakeword = 1
            direction = 4
            pressed = False
            dead = False
            showing = False
            draw_snake()
            draw_food(wordlist[wordindex])
            canvas.bind("<Key>", move)
            while not dead and not finishpart:
                delay = 500 - mode * 200 - level * 5
                if delay < 50:
                    delay = 50
                nextstep(delay)
            if finishpart:
                finishpart = False
                showword()
            else:
                gameover()
        else:
            showword()
    elif event.keysym == "Escape":
        canvas.delete("word")
        rewritefile()
        for i in range(1, length + 1):
            canvas.delete(snake[i][0])
        showing = False
        selectuser()
    elif (event.keysym == "Right" or event.keysym == "Down" or event.keycode == 83 or event.keycode == 68) and not showing:
        canvas.delete(modes[mode][0])
        modes[mode][0] = canvas.create_text(width / 2 + (mode - 1) * 100, height / 2 + 50, text = modes[mode][1], font = "Arial -30", tags = "tips")
        mode = mode + 1
        if mode > 2:
            mode = 0
        canvas.delete(modes[mode][0])
        modes[mode][0] = canvas.create_text(width / 2 + (mode - 1) * 100, height / 2 + 50, text = modes[mode][1], font = "Arial -30", fill = "red", tags = "tips")
    elif (event.keysym == "Left" or event.keysym == "Up" or event.keycode == 87 or event.keycode == 65) and not showing:
        canvas.delete(modes[mode][0])
        modes[mode][0] = canvas.create_text(width / 2 + (mode - 1) * 100, height / 2 + 50, text = modes[mode][1], font = "Arial -30", tags = "tips")
        mode = mode - 1
        if mode < 0:
            mode = 2
        canvas.delete(modes[mode][0])
        modes[mode][0] = canvas.create_text(width / 2 + (mode - 1) * 100, height / 2 + 50, text = modes[mode][1], font = "Arial -30", fill = "red", tags = "tips")

def game():
    global level, score, dead, wordlist, snake, length, used, food, foodused, foodamount, wordindex, direction, pressed, snakeword, mode, modes
    canvas.delete("selectuser")
    canvas.delete("select")
    canvas.delete("score")
    canvas.delete("tips")
    draw_wall()
    modes = [[0, "Easy"], [0, "Normal"], [0, "Hard"]]
    mode = 1
    canvas.create_text(width / 2, height / 2 - 150, text = "Start: Space/Enter", font = "Arial -25", tags = "tips")
    canvas.create_text(width / 2, height / 2 - 50, text = "Contorl: WASD/↑↓←→", font = "Arial -25", tags = "tips")
    modes[0][0] = canvas.create_text(width / 2 - 100, height / 2 + 50, text = "Easy", font = "Arial -30", tags = "tips")
    modes[1][0] = canvas.create_text(width / 2, height / 2 + 50, text = "Normal", font = "Arial -30", fill = "red", tags = "tips")
    modes[2][0] = canvas.create_text(width / 2 + 100, height / 2 + 50, text = "Hard", font = "Arial -30", tags = "tips")
    canvas.create_text(width / 2, height / 2 + 120, text = "Back: Esc", font = "Arial -25", tags = "tips")    
    snake = [([0] * 5) for i in range((pix + 1) ** 2)]
    length = 3
    used = [([False] * (pix + 5)) for i in range(pix + 5)]
    food = []
    foodused = [([False] * (pix + 2)) for i in range(pix + 2)]
    foodamount = 0
    snakeword = 1
    wordindex = 0
    direction = 4
    pressed = False
    dead = False
    score = user[now][1]
    level = user[now][2]
    scorecount["text"] = "Score: {}".format(score)
    levelcount["text"] = "Level: {}".format(level)
    
    j = 1
    while j < level:
        if wordlist[wordindex] == "LEVEL UP":
            j += 1
        wordindex += 1
    canvas.bind("<Key>", play)

def showword():
    global showing, wordlist
    for i in range(1, length + 1):
        canvas.delete(snake[i][0])
    canvas.delete("snakeword")
    showing = True
    x = [125, 345, 125, 345, 125, 345]
    y = [112, 112, 224, 224, 336, 336]
    j = 0
    canvas.create_text(width / 2, 50, text = "Level {}".format(level), font = "Arial -40", fill = "skyblue", tags = "word")
    for i in range(wordindex, wordindex + 6):
        canvas.create_text(x[j], y[j], text = wordlist[i], font = "Arial -25", fill = "orange", tags = "word")
        j += 1
    canvas.create_text(width / 2, 400, text = ">>>Enter<<<", font = "Arial -25", tags = "word")
    temp = wordlist[wordindex:wordindex + 6]
    shuffle(temp)
    wordlist = wordlist[:wordindex] + temp + wordlist[wordindex + 6:]

def gameover():
    global length, foodamount, snake, food
    for i in range(1, length + 1):
        canvas.delete(snake[i][0])
    for i in range(foodamount):
        canvas.delete(food[i][3])
        canvas.delete(food[i][4])
    canvas.delete("snakeword")
    user[now][1] = score
    user[now][2] = level
    rewritefile()
    if level == "Max":
        canvas.create_text(width / 2, height / 2 - 200, text = "Your Final Score is {} !".format(score), fill = textcolor, font = "Arial -30", tags = "score")
        canvas.create_text(width / 2, height / 2 - 100, text = "Congratulations!", font = "Arial -25 bold", tags = "score") 
        canvas.create_text(width / 2, height / 2, text = "You have finished this game!", font = "Arial", tags = "score") 
        canvas.create_text(width / 2, height / 2 + 100, text = ">>>Esc<<<", font = "Arial -30 bold", tags = "score")
    else:
        canvas.create_text(width / 2, height / 2 - 100, text = "Your Final Score is {} !".format(score), fill = textcolor, font = "Arial -30", tags = "score")
        canvas.create_text(width / 2, height / 2, text = "Restart: Enter   Back: Esc", font = "Arial", tags = "score")
    canvas.bind("<Key>", afterover)

def afterover(event):
    if event.keysym == "Escape":
        selectuser()
    if event.keysym == "Return" and level != "Max":
        game()

# ---------------------

pix = 30
width = pix * 15 + 20
height = width + 30

color = ["black", "grey", "pink", "red", "orange", "yellow", "green", "blue", "purple"]
canvascolor = "white"
wallcolor = "black"
snakecolor = "white"
headcolor = "lightgrey"
foodcolor = "gold"
textcolor = "red"
selectcolor = "grey"

user = [["", 0, 1] for i in range(14)]
username = [0] * 15
now = 0
rename = False
delconfirm = False
namepos = 0
ID = 0
x = 0
y = 0

wordlist = []
snake = [([0] * 5) for i in range((pix + 1) ** 2)]
length = 3
used = [([False] * (pix + 5)) for i in range(pix + 5)]
food = []
foodused = [([False] * (pix + 2)) for i in range(pix + 2)]
foodamount = 0
snakeword = 1
wordindex = 0
score = 0
level = 1
direction = 4
modes = [[0, "Easy"], [0, "Normal"], [0, "Hard"]]
mode = 1
pressed = False
dead = False
showing = False
finishpart = False

window = Tk()
window.geometry("{}x{}+400+200".format(width, height))
window.maxsize(width, height)
window.minsize(width, height)
window.title("Snake&English")

canvas = Canvas(window, bg = canvascolor, width = width, height = width)

canvas.create_rectangle(250, 90, 280, 120, fill = "grey", tags = "welcome")
canvas.create_rectangle(220, 90, 250, 120, tags = "welcome")
canvas.create_text(235, 105, text = "S", font = "Arial -30 bold", tags = "welcome")
canvas.create_rectangle(190, 90, 220, 120, tags = "welcome")
canvas.create_text(205, 105, text = "N", font = "Arial -30 bold", tags = "welcome")
canvas.create_rectangle(160, 90, 190, 120, tags = "welcome")
canvas.create_text(175, 105, text = "A", font = "Arial -30 bold", tags = "welcome")
canvas.create_rectangle(130, 90, 160, 120, tags = "welcome")
canvas.create_text(145, 105, text = "K", font = "Arial -30 bold", tags = "welcome")
canvas.create_rectangle(130, 120, 160, 150, tags = "welcome")
canvas.create_text(145, 135, text = "E", font = "Arial -30 bold", tags = "welcome")
canvas.create_rectangle(130, 150, 160, 180, tags = "welcome")
canvas.create_rectangle(160, 150, 190, 180, tags = "welcome")
canvas.create_text(175, 165, text = "&", font = "Arial -30", tags = "welcome")
canvas.create_rectangle(190, 150, 220, 180, tags = "welcome")
canvas.create_rectangle(220, 150, 250, 180, tags = "welcome")
canvas.create_text(235, 165, text = "E", font = "Arial -30 bold", tags = "welcome")
canvas.create_rectangle(250, 150, 280, 180, tags = "welcome")
canvas.create_text(265, 165, text = "N", font = "Arial -30 bold", tags = "welcome")
canvas.create_rectangle(280, 150, 310, 180, tags = "welcome")
canvas.create_text(295, 165, text = "G", font = "Arial -30 bold", tags = "welcome")
canvas.create_rectangle(280, 180, 310, 210, tags = "welcome")
canvas.create_text(295, 195, text = "L", font = "Arial -30 bold", tags = "welcome")
canvas.create_rectangle(280, 210, 310, 240, tags = "welcome")
canvas.create_text(295, 225, text = "I", font = "Arial -30 bold", tags = "welcome")
canvas.create_rectangle(250, 210, 280, 240, tags = "welcome")
canvas.create_text(265, 225, text = "S", font = "Arial -30 bold", tags = "welcome")
canvas.create_rectangle(220, 210, 250, 240, tags = "welcome")
canvas.create_text(235, 225, text = "H", font = "Arial -30 bold", tags = "welcome")
canvas.create_rectangle(190, 210, 220, 240, tags = "welcome")
canvas.create_rectangle(160, 210, 190, 240, tags = "welcome")
canvas.create_rectangle(130, 210, 160, 240, tags = "welcome")
canvas.create_text(width / 2 - 20, height / 2 + 50, text = ">>>Enter<<<", font = "Arial -25", tags = "welcome")

canvas.focus_set()
canvas.bind("<Key>", welcome)
canvas.pack()

scorecount = Label(window, text = "Score:")
levelcount = Label(window, text = "Level:")
scorecount.place(x = 5, y = width + 5)
levelcount.place(x = width - 80, y = width + 5)

window.mainloop()