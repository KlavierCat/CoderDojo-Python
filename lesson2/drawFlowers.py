from turtle import *

def moveTurtle(setX, setY):
  penup()
  goto(setX, setY)
  pendown()

def drawShape(col, shapeSize, shapeSides):
  for x in range (shapeSides):
    color(col)
    forward(shapeSize)
    right(360/shapeSides)

def drawFlower(col, petalSideSize, petalSides, petalNum):
  for x in range (petalNum):
    drawShape(col, petalSideSize, petalSides)
    rt(360/petalNum)

moveTurtle(100, 100)
drawFlower("red", 50, 4, 5)

moveTurtle(80, -50)
drawFlower("blue", 30, 5, 4)

moveTurtle(-90, 15)
drawFlower("yellow", 40, 3, 10)