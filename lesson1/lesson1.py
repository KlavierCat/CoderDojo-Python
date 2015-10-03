# import turtle
from turtle import *

# define a function to draw a square with a for loop
def square(length):
  for side in range (4):
    forward(length)
    right(90)

# define a function to handle the moving around part to draw the square
def moveAndDraw(x, y, length):
  penup()
  goto(x, y)
  pendown()
  square(length)

# call the function to draw the squares several times
moveAndDraw(0, 0, 40)
moveAndDraw(90, 90, 30)
moveAndDraw(-90, -90, 50)
