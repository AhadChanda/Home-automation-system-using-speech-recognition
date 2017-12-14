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

GPIO.setup(ledpin,GPIO.OUT)
msg=s.recv(1024)            # Receives data upto 1024 bytes and stores in variables msg

if "ON" in msg:
   GPIO.output(ledpin,True);
sleep(3)

GPIO.output(ledpin,False);

'''
while count < blinkc:
   GPIO.output(ledpin,True)
   print("ON")
   sleep(3)
   GPIO.output(ledpin,False)
   print("OFF")
   sleep(3)
   count+=1
   '''

s.close()
