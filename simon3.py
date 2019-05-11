#genSequence, simonSpeaks
import time
from apcs import *
from random import randint

width = 500
height = 500
i = 0
j = 0

simonSequence = []
playerSequence = []
simonSpoke = False

Window.size(width, height)

def main():
    global simonSpoke
    if not simonSpoke:
        simonSpeaks()
    else:
        setupBackground()

def setupBackground():
   Window.out.background("black")
   Window.out.color("white")
   Window.out.line(0, height/2, width, height/2)
   Window.out.line(width/2, 0, width/2, height)

def showSquare(num):
    if num == 1:
        setupBackground()
        Window.out.color("red")
        Window.out.rectangle(width/4, height/4, width/2, width/2)
    elif num == 2:
        setupBackground()
        Window.out.color("orange")
        Window.out.rectangle(3*width/4, height/4, width/2, width/2)
    elif num == 3:
        setupBackground()
        Window.out.color("yellow")
        Window.out.rectangle(width/4, 3*height/4, width/2, width/2)
    elif num == 4:
        setupBackground()
        Window.out.color("green")
        Window.out.rectangle(3*width/4, 3*height/4, width/2, width/2)

def genSequence():
    global simonSequence
    simonSequence = []
    for x in range(0, 4):
        simonSequence.append(randint(1,4))

def simonSpeaks():
    global simonSpoke, i, j
    if j == 0:
        genSequence()
        print(simonSequence)
    if j % 2 == 0:
        setupBackground()
    else:
        showSquare(simonSequence[i])
        i += 1
    j += 1
    if i == 4:
        simonSpoke = True

def playerSpeaks():
    global playerSequence
    for x in range(0, 4):
        if Window.key.pressed('w'):
            playerSequence.append(1)
        elif Window.key.pressed('q'):
            playerSequence.append(2)
        elif Window.key.pressed('a'):
            playerSequence.append(3)
        elif Window.key.pressed('s'):
            playerSequence.append(4)

Window.frame(main, 1000)
Window.start()
