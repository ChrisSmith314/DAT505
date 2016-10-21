from mosquitto import *
from random import *
from serial import *

#Arduino Stuff
port = Serial("/dev/cu.usbmodem1411",9600,timeout=2)

port.readall()

#Mosquitto Stuff
client = Mosquitto("ChrisSmithDat505")
    
client.connect("10.212.61.136")

client.subscribe("/lights")
print("Python Working")

def messageReceived(broker, obj, msg):
    global client
    payload = msg.payload.decode()
    port.write(payload.encode() + "\n")
    print("Message " + msg.topic + " containing: " + payload)
#    print("Arduino said " + port.readline())

client.on_message = messageReceived

while (client != None): client.loop()