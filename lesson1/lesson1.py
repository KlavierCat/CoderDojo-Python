# import turtle
from turtle import *

# define a function to draw a square with a for loop
def square():
  for side in range (4):
    forward(50)
    right(90)

# call the function to draw a square, or, a few squares
square()

penup()
goto(90, 90)
pendown()

square()

penup()
goto(-90, -90)
pendown()

square()