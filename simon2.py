#showSquare
import time
from apcs import *
from random import randint

width = 500
height = 500

Window.size(width, height)

def main():
   setupBackground()

def setupBackground():
   Window.out.background("black")
   Window.out.color("white")
   Window.out.line(0, height/2, width, height/2)
   Window.out.line(width/2, 0, width/2, height)

def showSquare(num):
    if num == 1:
        Window.out.color("red")
        Window.out.rectangle(width/4, height/4, width/2, width/2)
    elif num == 2:
        Window.out.color("orange")
        Window.out.rectangle(3*width/4, height/4, width/2, width/2)
    elif num == 3:
        Window.out.color("yellow")
        Window.out.rectangle(width/4, 3*height/4, width/2, width/2)
    elif num == 4:
        Window.out.color("green")
        Window.out.rectangle(3*width/4, 3*height/4, width/2, width/2)

Window.frame(main)
Window.start()
