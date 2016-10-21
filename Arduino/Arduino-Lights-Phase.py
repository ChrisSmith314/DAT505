from mosquitto import *
from random import *
from serial import *
import time

#Arduino Stuff
port = Serial("/dev/cu.usbmodem1411",9600,timeout=2)

port.readall()

#Mosquitto Stuff
client = Mosquitto("ChrisSmithDat505")
    
client.connect("10.212.61.136")

client.subscribe("/lights")
print("Python Working")


Current = 4
AcceptNew = "true"
Previous = "OFF"

def StartWrite(payload):
    global Current
    global AcceptNew
    if(payload == "ON"):
        Current = Current + 1
        print("Payload = on and current = " + str(Current))
        port.write((str(Current)).encode() + "\n")
    elif(payload == "OFF"):
        print("Payload = on and current = " + str(Current))
        Current = Current - 1
        port.write((str(Current)).encode() + "\n")
    if((Current < 11) and (Current > 2)):
        time.sleep(0.5)
        StartWrite(payload)
    else:
        AcceptNew = "true"
        print("RESET " + AcceptNew)
    print(Current)

def messageReceived(broker, obj, msg):
    global client
    global AcceptNew
    global Previous
    payload = msg.payload.decode()
    print(AcceptNew + " " + payload)
    if(AcceptNew == "true"):
        print("Guess what acceptnew is " + AcceptNew)
        if(payload != Previous):
            StartWrite(payload, AcceptNew)
            Previous = payload
            AcceptNew = "false"
    # port.write(payload.encode() + "\n")
# print("Message " + msg.topic + " containing: " + payload)
#    print("Arduino said " + port.readline())

client.on_message = messageReceived

while (client != None): client.loop()