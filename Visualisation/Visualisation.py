from graphics import *
import math
import time
import random

Window = GraphWin("DAT505 Visualisation", 1080, 720)

Window.setBackground('black')

Scores = ((open("data.txt")).read()).split("\n")

CurrentShapes = [0]*len(Scores)

CurrentShapesDone = ["false"]*len(Scores)

Current = 0

def createShape(Num):
    NumBlocks = int(math.ceil(int(Scores[Num])/10))
    StartPos = [100, 100]
    Shape = ["EMPTY"]
    Score = 255 - (int((Scores[Num])[1:])*25)
    print(Score)
    ShapeColor = color_rgb(255,Score,0)
    NumOffset = 0
    for i in range(0, NumBlocks):
        if(Shape[0] == "EMPTY"):
            Shape[0] = Rectangle(Point(StartPos[0],  StartPos[1]), Point(StartPos[0] + 50, StartPos[1] + 50))
            #Shape[i].setFill("yellow")
            #Shape[i].draw(Window)
        else:
            Range = int(random.randrange(1, 5))
            if(Range == 30):
                Shape.append(Rectangle(Point(((StartPos[0] + (i*50))-50)-(NumOffset*50), StartPos[1]-50), Point(((StartPos[0] + (i*50)))-(NumOffset*50), StartPos[1])))
                NumOffset = NumOffset + 1
            elif(Range == 4):
                Shape.append(Rectangle(Point(((StartPos[0] + (i*50))-50)-(NumOffset*50), StartPos[1]+50), Point(((StartPos[0] + (i*50)))-(NumOffset*50), StartPos[1] + 100)))
                NumOffset = NumOffset + 1
            else:
                Shape.append(Rectangle(Point((StartPos[0] + (i*50))-(NumOffset*50), StartPos[1]), Point(((StartPos[0] + (i*50))+50)-(NumOffset*50), StartPos[1] + 50)))
        Shape[i].setFill(ShapeColor)
        Shape[i].draw(Window)
    CurrentShapes[Num] = Shape
    print(Current)

createShape(Current)

Playing = True

while Playing == True:
    try:
        print("Start Loop " + str(Current))
        for i in range(0,len(CurrentShapes[Current])):
            CurrentShapes[Current][i].move(0, 25)
        keyPressed = Window.getKey()
        if(keyPressed == "Left"):
            for i in range(0,len(CurrentShapes[Current])):
                CurrentShapes[Current][i].move(-50, 0)
        elif(keyPressed == "Right"):
            for i in range(0,len(CurrentShapes[Current])):
                CurrentShapes[Current][i].move(50, 0)
        elif(keyPressed == "Up" or keyPressed == "r"):
            print("ROTATE")
        
        print("Mid Loop " + str(Current))
        for i in range(0,len(CurrentShapes[Current])):
            #print("Current is " + str(Current))
            #print(CurrentShapes[Current][i])
            #print("PLEASE WORK")
            if((CurrentShapes[Current][i].getCenter().getY() + 27) >= Window.getHeight()):# or Window.getPixel(CurrentShapes[Current][i].getCenter().getY() + 26, CurrentShapes[Current][i].getCenter().getX()) != "black"):
                print("Reached Bottom")
                Current = Current + 1
                CurrentShapesDone[Current] = "true"
                createShape(Current)
                break
            for e in range(0, len(CurrentShapes)):
                if(CurrentShapes[e] != 0 and e != Current):
                    for o in range(0, len(CurrentShapes[e])):
                        if(CurrentShapes[e][o].getCenter().getY() <= 150):
                            print("HA HA You lost!!!")
                            Playing = False
                            break
                        # print("Block " + str(e))
                        #print("Score = " + str(CurrentShapes[Current][i].getCenter().getY() + 27) + " and the other thing = " + str((CurrentShapes[e][o].getCenter().getY()) - 27) + " and " + str(CurrentShapesDone[e]))
                        # Window.plot(CurrentShapes[Current][i].getCenter().getX(),CurrentShapes[Current][i].getCenter().getY() + 27, "red")
                        # Window.plot(CurrentShapes[e][o].getCenter().getX(),CurrentShapes[e][o].getCenter().getY() - 27, "red")
                        if((CurrentShapes[Current][i].getCenter().getY() + 27) >= (CurrentShapes[e][o].getCenter().getY() - 27) and (CurrentShapes[Current][i].getCenter().getX()) == (CurrentShapes[e][o].getCenter().getX())):
                            print("Same")
                            Current = Current + 1
                            CurrentShapesDone[Current] = "true"
                            if(Current >= len(Scores)):
                                print("FINNISHED")
                                Playing = False
                                break
                            else:
                                createShape(Current)
                                break
    except:
        print("Something is broken, trying again")
#print("   ")



time.sleep(5)