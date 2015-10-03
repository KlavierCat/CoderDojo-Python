# import turtle
from turtle import *

# define a function to draw a square with a for loop
def shape(length, sides):
  for x in range (sides):
    forward(length)
    right(360/sides)

# define a function to handle the moving around part to draw the square
def moveAndDraw(x, y, length, sides):
  penup()
  goto(x, y)
  pendown()
  shape(length, sides)

# call the function to draw the squares several times
moveAndDraw(0, 0, 40, 4)
moveAndDraw(90, 90, 30, 3)
moveAndDraw(-90, -90, 50, 5)
