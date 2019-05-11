#setupBackground

from apcs import *

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

Window.frame(main)
Window.start()
