import RPi.GPIO as GPIO
from sys import argv 
from time import sleep

GPIO.setmode(GPIO.BCM)


ledpin=22
GPIO.setup(ledpin,GPIO.OUT)

if argv[1]=='1':
    GPIO.output(ledpin,True)
    print("ON")
else:
    GPIO.output(ledpin,False)
    print("OFF")
   
   
