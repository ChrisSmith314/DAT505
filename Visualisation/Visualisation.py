from graphics import *
import math
import time
import random
from threading import Thread

Window = GraphWin("DAT505 Visualisation", 1080, 720)

Window.setBackground('black')

Scores = ((open("data.txt")).read()).split("\n")

CurrentShapes = [0]*len(Scores)

CurrentShapesDone = ["false"]*len(Scores)

CurrentShapesCenterX = [0]*len(Scores)

CurrentShapesCenterY = [0]*len(Scores)

Current = 0

GameScore = 0

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
            CurrentShapesCenterX[Num] = Shape[0].getCenter().getX()
            CurrentShapesCenterY[Num] = Shape[0].getCenter().getY()
            #Shape[i].setFill("yellow")
            #Shape[i].draw(Window)
        else:
            Range = int(random.randrange(1, 5))
            if(Range == 3):
                Shape.append(Rectangle(Point(((StartPos[0] + (i*50))-50)-(NumOffset*50), StartPos[1]-50), Point(((StartPos[0] + (i*50)))-(NumOffset*50), StartPos[1])))
                NumOffset = NumOffset + 1
                CurrentShapesCenterY[Num] = CurrentShapesCenterY[Num] - 25
            elif(Range == 4):
                Shape.append(Rectangle(Point(((StartPos[0] + (i*50))-50)-(NumOffset*50), StartPos[1]+50), Point(((StartPos[0] + (i*50)))-(NumOffset*50), StartPos[1] + 100)))
                NumOffset = NumOffset + 1
                CurrentShapesCenterY[Num] = CurrentShapesCenterY[Num] + 25
            else:
                Shape.append(Rectangle(Point((StartPos[0] + (i*50))-(NumOffset*50), StartPos[1]), Point(((StartPos[0] + (i*50))+50)-(NumOffset*50), StartPos[1] + 50)))
                CurrentShapesCenterX[Num] = CurrentShapesCenterX[Num] + 25
        print("Center X = " + str(CurrentShapesCenterX[Num]) + " and Center Y = " + str(CurrentShapesCenterY[Num]))
        Shape[i].setFill(ShapeColor)
        Shape[i].draw(Window)
    CurrentShapes[Num] = Shape
    print(Current)

createShape(Current)

Playing = True

def dropperThread():
    while Playing == True:
        break

thread = Thread(target=dropperThread)
thread.start()

while Playing == True:
    try:
        SleepTime = 0.4
        CurrentShapesCenterY[Current] = int(CurrentShapesCenterY[Current]) + 25
        for i in range(0,len(CurrentShapes[Current])):
            CurrentShapes[Current][i].move(0, 25)
        
        keyPressed = Window.checkKey()
        if(keyPressed == "Escape"):
            Playing = False
            print(Playing)
            break
        if(keyPressed == "Left"):
            CurrentShapesCenterX[Current] = int(CurrentShapesCenterX[Current]) - 50
            for i in range(0,len(CurrentShapes[Current])):
                if((CurrentShapes[Current][i].getCenter().getX() - 25) <= 0):
                    break
                else:
                    CurrentShapes[Current][i].move(-50, 0)
                    print("Moving left center = " + str(CurrentShapesCenterX[Current]))
        elif(keyPressed == "Right"):
            CurrentShapesCenterX[Current] = int(CurrentShapesCenterX[Current]) + 50
            for i in range(0,len(CurrentShapes[Current])):
                if((CurrentShapes[Current][i].getCenter().getX() + 25) >= Window.width):
                    break
                else:
                    CurrentShapes[Current][i].move(50, 0)
        elif(keyPressed == "Up" or keyPressed == "r"):
            print("ROTATE")
        elif(keyPressed == "Down"):
            SleepTime = 0.1

        for i in range(0,len(CurrentShapes[Current])):
            if((CurrentShapes[Current][i].getCenter().getY() + 27) >= Window.getHeight()):
                print("Reached Bottom")
                GameScore = GameScore + int(Scores[Current])
                print(str(GameScore))
                ScoreText = Text(Point(CurrentShapesCenterX[Current],CurrentShapesCenterY[Current]) , str(Scores[Current]))
                ScoreText.setSize(35)
                ScoreText.setFill("white")
                ScoreText.draw(Window)
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
                        if((CurrentShapes[Current][i].getCenter().getY() + 27) >= (CurrentShapes[e][o].getCenter().getY() - 27) and (CurrentShapes[Current][i].getCenter().getY() - 27) <= (CurrentShapes[e][o].getCenter().getY() + 27)  and (CurrentShapes[Current][i].getCenter().getX()) == (CurrentShapes[e][o].getCenter().getX())):
                            print("Same")
                            GameScore = GameScore + int(Scores[Current])
                            ScoreText = Text(Point(CurrentShapesCenterX[Current],CurrentShapesCenterY[Current]) , str(Scores[Current]))
                            ScoreText.setSize(35)
                            ScoreText.setFill("white")
                            ScoreText.draw(Window)
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
    time.sleep(SleepTime)
#print("   ")



time.sleep(5)
