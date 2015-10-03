# import dependencies
from turtle import *
import random

# define a function to draw flowers
def flower (col, length, angle):
  pendown()
  times = int(360/(180-angle))
  for sides in range (0, times):
    color (col)
    fd (length)
    rt (angle)
  penup()

penup()
speed("fast")

# call the flower function with some parameters to draw a flower
flower("blue", 200, 170)

# define a function to draw multiple flowers with a lot of randomness
def drawFlowers (flowerNum):
  for x in range (0, flowerNum):
    penup()
    
    setX=random.randint(-200,200)
    setY=random.randint(-150,150)
    
    goto(setX, setY)
    
    r = lambda: random.randint(0,255)
    col='#%02X%02X%02X' % (r(),r(),r())
    length=random.randint(50, 200)
    angle=random.randint(160,176)
    flower(col,length,angle)

# call the function to draw 20 such flowers
drawFlowers(20)