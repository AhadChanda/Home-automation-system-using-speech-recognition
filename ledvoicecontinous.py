import RPi.GPIO as GPIO
from time import sleep
from socket import *             # Imports socket module
import sys

#print(sys.argv)
host="192.168.0.103"
port=int(sys.argv[1])
s=socket(AF_INET, SOCK_STREAM)      # Creates a socket
s.connect((host,port)) 
 
GPIO.setmode(GPIO.BCM)

blinkc=3
count=0
ledpin=22
fanpin=27
GPIO.setup(ledpin,GPIO.OUT)
GPIO.setup(fanpin,GPIO.OUT)
while True:
	msg=s.recv(4096)   
        words=msg.split()
	if "ON LIGHT" in msg:
   		GPIO.output(ledpin,True);
		sleep(3)
        if "OFF LIGHT" in msg:
		GPIO.output(ledpin,False);
		sleep(3)
	if "ON FAN" in msg:
                GPIO.output(fanpin,True);
                sleep(3)
        if "OFF FAN" in msg:
                GPIO.output(fanpin,False);
                sleep(3)

     #   elif "Bjhsdj" in msg:
#		break;

GPIO.output(ledpin,False);

s.close()
