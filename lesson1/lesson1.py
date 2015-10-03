# import turtle
from turtle import *

# define a function to draw a square with a for loop
def square():
  for side in range (4):
    forward(50)
    right(90)

# define a function to handle the moving around part to draw the square
def moveAndDraw(x, y):
  penup()
  goto(x, y)
  pendown()
  square()

# call the function to draw the squares several times
moveAndDraw(0, 0)
moveAndDraw(90, 90)
moveAndDraw(-90, -90)
