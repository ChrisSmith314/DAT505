from graphics import *
import math
import time
import random

Window = GraphWin("DAT505 Visualisation", 1080, 720)

Window.setBackground('black')

Scores = ((open("data.txt")).read()).split("\n")

CurrentShapes = [0]*len(Scores)

def createShape(Num):
    NumBlocks = int(math.ceil(int(Scores[Num])/10))
    StartPos = [0, 0]
    Shape = ["EMPTY"]
    for i in range(0, NumBlocks):
        if(Shape[0] == "EMPTY"):
            Shape[0] = Rectangle(Point(StartPos[0],  StartPos[1]), Point(StartPos[0] + 50, StartPos[1] + 50))
            Shape[i].setFill("yellow")
            Shape[i].draw(Window)
        else:
            Range = int(random.randrange(1, 3))
            print(Range)
            Shape.append(Rectangle(Point(StartPos[0] + (i*50), StartPos[1]), Point((StartPos[0] + (i*50))+50, StartPos[1] + 50)))
            Shape[i].setFill("yellow")
            Shape[i].draw(Window)

createShape(2)

shape = Rectangle(Point(20, 10), Point(200, 100))

shape.setFill('yellow')

shape.draw(Window)

time.sleep(1)

shape.move(500, 50)

time.sleep(5)