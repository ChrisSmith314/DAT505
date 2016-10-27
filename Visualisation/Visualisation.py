from graphics import *
import math
import time
import random
from threading import Thread
from Queue import Queue

Window = GraphWin("DAT505 Visualisation", 1050, 700)

Window.setBackground('black')

Scores = ((open("data.txt")).read()).split("\n")

Scores.remove("")

CurrentShapes = [0]*len(Scores)

CurrentShapesDone = ["false"]*len(Scores)

CurrentShapesCenterX = [0]*len(Scores)

CurrentShapesCenterY = [0]*len(Scores)

Current = 0

GameScore = 0

Queue = Queue()

def createShape(Num):
    NumBlocks = int(math.ceil(int(Scores[Num])/10))
    StartPos = [(Window.width/2)-25, 100]
    Shape = ["EMPTY"]
    Score = 255 - (int((Scores[Num])[1:])*25)
    ShapeColor = color_rgb(255,Score,0)
    NumOffset = 0
    for i in range(0, NumBlocks):
        if(Shape[0] == "EMPTY"):
            Shape[0] = Rectangle(Point(StartPos[0],  StartPos[1]), Point(StartPos[0] + 50, StartPos[1] + 50))
            CurrentShapesCenterX[Num] = Shape[0].getCenter().getX()
            CurrentShapesCenterY[Num] = Shape[0].getCenter().getY()
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
        Shape[i].setFill(ShapeColor)
        Shape[i].draw(Window)
    CurrentShapes[Num] = Shape

createShape(Current)

Playing = True

def dropperThread():
    #Tkinker may not be thread happy
    #global Round
    def FadeTehxt(CurrentText):
        global Round
        print("ROUND= " + str(Round))
        Color = 255 - (Round*10)
        if(CurrentText == "NEW"):
            Round = 0
                # print("NOTColor = " + str(Color))
        Queue.put(Color)
        if(Round == 25):
            print("working")
        else:
            Round = Round + 1
            FadeText("OLD")
    while Playing == True:
        # Answer = Queue.get()
        #FadeText("NEW")
        break

thread = Thread(target=dropperThread)
thread.start()

ScoreText = Text(Point(CurrentShapesCenterX[Current],CurrentShapesCenterY[Current]) , "")
    
MoveText = "False"
Round = 0

while Playing == True:
    global Round
    global Playing
    def FadeText():
        global Round
        Color = 255 - (Round*25)
        ScoreText.setFill(color_rgb(Color, Color, Color))
        ScoreText.move(0, -8)
        if(Round == 10):
            MoveText = "False"
        else:
            Round = Round + 1
    if(MoveText == "True"):
        FadeText()
    GameScoreText = Text(Point(50, 50), str(GameScore))
    GameScoreText.setSize(35)
    if(GameScore > (sum(map(int, Scores)))*0.7):
        GameScoreText.setFill("gold")
    elif(GameScore > (sum(map(int, Scores)))*0.6):
        GameScoreText.setFill("#c1c1c1")
    elif(GameScore > (sum(map(int, Scores)))*0.5):
        GameScoreText.setFill("#845a00")
    else:
        GameScoreText.setFill("red")
    GameScoreText.draw(Window)
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
                ScoreText.undraw()
                ScoreText = Text(Point(CurrentShapesCenterX[Current],CurrentShapesCenterY[Current]) , str(Scores[Current]))
                ScoreText.setSize(35)
                ScoreText.setFill("white")
                ScoreText.draw(Window)
                Current = Current + 1
                CurrentShapesDone[Current] = "true"
                MoveText = "True"
                Round = 0
                createShape(Current)
                FadeText()
                break
            for e in range(0, len(CurrentShapes)):
                global Playing
                if(CurrentShapes[e] != 0 and e != Current):
                    for o in range(0, len(CurrentShapes[e])):
                        if(CurrentShapes[e][o].getCenter().getY() <= 150):
                            global Playing
                            print("HA HA You lost!!!")
                            GameOver = Text(Point(Window.width/2, Window.height/4), "Game Over")
                            FinalScore = Text(Point(Window.width/2, Window.height/2), str(GameScore))
                            GameOver.setFill("red")
                            if(GameScore > (sum(map(int, Scores)))*0.7):
                                FinalScore.setFill("gold")
                            elif(GameScore > (sum(map(int, Scores)))*0.6):
                                FinalScore.setFill("#c1c1c1")
                            elif(GameScore > (sum(map(int, Scores)))*0.5):
                                FinalScore.setFill("#845a00")
                            else:
                                FinalScore.setFill("white")
                            GameOver.setSize(90)
                            FinalScore.setSize(160)
                            GameOver.draw(Window)
                            FinalScore.draw(Window)
                            Playing = False
                            print(str(Playing))
                            break
                        if((CurrentShapes[Current][i].getCenter().getY() + 27) >= (CurrentShapes[e][o].getCenter().getY() - 27) and (CurrentShapes[Current][i].getCenter().getY() - 27) <= (CurrentShapes[e][o].getCenter().getY() + 27)  and (CurrentShapes[Current][i].getCenter().getX()) == (CurrentShapes[e][o].getCenter().getX())):
                            print("Same")
                            GameScore = GameScore + int(Scores[Current])
                            ScoreText.undraw()
                            ScoreText = Text(Point(CurrentShapesCenterX[Current],CurrentShapesCenterY[Current]) , str(Scores[Current]))
                            ScoreText.setSize(35)
                            ScoreText.setFill("white")
                            ScoreText.draw(Window)
                            Current = Current + 1
                            CurrentShapesDone[Current] = "true"
                            MoveText = "True"
                            Round = 0
                            FadeText()
                            if(Current >= len(Scores)):
                                global Playing
                                print("FINNISHED")
                                GameOver = Text(Point(Window.width/2, Window.height/4), "Game Won")
                                FinalScore = Text(Point(Window.width/2, Window.height/2), str(GameScore))
                                Game.setFill("red")
                                if(GameScore > (sum(map(int, Scores)))*0.7):
                                    FinalScore.setFill("gold")
                                elif(GameScore > (sum(map(int, Scores)))*0.6):
                                    FinalScore.setFill("#c1c1c1")
                                elif(GameScore > (sum(map(int, Scores)))*0.5):
                                    FinalScore.setFill("#845a00")
                                else:
                                    FinalScore.setFill("white")
                                GameOver.setSize(90)
                                FinalScore.setSize(160)
                                GameOver.draw(Window)
                                FinalScore.draw(Window)
                                Playing = False
                                break
                            else:
                                createShape(Current)
                                break
    except:
        print("Something is broken, trying again")
    time.sleep(SleepTime)
    GameScoreText.undraw()
#print("   ")



time.sleep(5)
