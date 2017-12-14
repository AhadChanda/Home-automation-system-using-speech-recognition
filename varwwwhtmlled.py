import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

blinkc=3
count=0
ledpin=22

GPIO.setup(ledpin,GPIO.OUT)

while count < blinkc:
   GPIO.output(ledpin,True)
   print("ON")
   sleep(3)
   GPIO.output(ledpin,False)
   print("OFF")
   sleep(3)
   count+=1
   
