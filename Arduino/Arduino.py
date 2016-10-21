from serial import *
    
port = Serial("/dev/cu.usbmodem1411",9600,timeout=2)
    
port.readall()
    
message = "Hello there Arduino\n"
LightSetting = "off"

def askUser():
    Response = raw_input("Turn light " + LightSetting)
    message = Response + "\n"
    port.write(message.encode())
    
    input = port.readline()
    print(input)
    askUser()
# port.close()

askUser()
