import twitter
import urllib
import urllib2
import datetime
import os
import sqlite3
import shutil
from bs4 import BeautifulSoup

Sites = ["youtube.com/watch?", "twitter.com", "facebook.com", "simonsdeli"]

Comments = [["I am currently watching ", "I have watched a brilliant video at "], ["I am now on this brilliant site called ", "I would highly recommend visiting this site that I visited today.\n"], ["I have betrayed our kind by visiting ","I have betrayed our kind by visiting "], ["Come and use this site if you need help with code.\n", "This site is the best if your code does not work and you need help!\n"]]

AccessKeys = (open("Keys.txt")).read().split("\n")

api = twitter.Api(AccessKeys[0],AccessKeys[1],AccessKeys[2],AccessKeys[3])

User = os.path.realpath("ViewMyHistory.py").split("/")


History = ("/" + str(User[1]) + "/" + str(User[2]) + "/Library/Application Support/Google/Chrome/Default")

Site = "www.twitter.com"

Now = 0

try:
    #Gets information from Current Session for when Chrome is open
    History = open(History + "/Current Session")
    History = History.read()
    
    start = History.rfind("http")
    end = History.find(chr(0),start)
    
    Site = History[start:end].split("0")[0]
          
        #for i in range(0, len(str(CurrentSession))):
        #if(str(CurrentSession)[0:i] in (str(History).split(str(CurrentSession))[0])):
        #    Site = str(CurrentSession)[0:i]
        #else:
#    break
except:
    #Gets information from History for when chrome is closed
    Now = 1
    try:
        History = History.split("/Current Session")[0]
    except:
        print("No Problem")

    shutil.copyfile(History + "/History", "History")

    History = "History"

    console = sqlite3.connect(History)
    cursor = console.cursor()
        
    cursor.execute("SELECT * FROM urls")
        
    rows = cursor.fetchall()
        
    Site = str(rows[len(rows)-1]).split("'")[1].split("'")[0]

SentTweet = False

SiteData = urllib.urlopen(str(Site))
image = ""
try:
    #image = SiteData.read().split("<img")[2]
    #image = image.split('src="')[1].split('"')[0]
    #image = urllib.urlopen("https://newsroom.uber.com/wp-content/uploads/2015/10/HQ_uberkittens_blog_960x540_r1v1.jpg")
    #shutil.copyfile("https://newsroom.uber.com/wp-content/uploads/2015/10/HQ_uberkittens_blog_960x540_r1v1.jpg", "image.jpg")
    api.UpdateBanner("imgres.jpg")
except:
    print("No Images")

for i in range(0, len(Sites)):
    if(Sites[i] in Site):
        Tweet = api.PostUpdate(Comments[i][Now] + str(BeautifulSoup(Site)))
        SentTweet = True
if(SentTweet == False):
    if(Now == 0):
        Tweet = api.PostUpdate("I am currently at " + str(BeautifulSoup(Site)))
    elif(Now == 1):
        Tweet = api.PostUpdate("I have been visiting " + str(BeautifulSoup(Site)))

