import RPi.GPIO as GPIO
import time

eight = 8
seven = 7
nine = 9
eleven = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(eight,GPIO.OUT)
GPIO.setup(seven,GPIO.OUT)
GPIO.setup(nine,GPIO.OUT)
GPIO.setup(eleven,GPIO.OUT)

class Bot(object):

    def right(self):
      i = 0
      while i < 2:
        GPIO.output(eight,GPIO.HIGH)
        time.sleep(.9)
        GPIO.output(eight,GPIO.LOW)
        time.sleep(.5)
        i = i + 1

    def left(self):
      i = 0
      while i < 2:
        GPIO.output(seven,GPIO.HIGH)
        time.sleep(.9)
        GPIO.output(seven,GPIO.LOW)
        time.sleep(.5)
        i = i + 1

    def forward(self):
      i = 0
      while i < 2:
        GPIO.output(nine,GPIO.HIGH)
        time.sleep(.9)
        GPIO.output(nine,GPIO.LOW)
        time.sleep(.5)
        i = i + 1

    def back(self):
      i = 0
      while i < 2:
        GPIO.output(eleven,GPIO.HIGH)
        time.sleep(.9)
        GPIO.output(eleven,GPIO.LOW)
        time.sleep(.5)
        i = i + 1

#Bot().left()
#Bot().right()
#Bot().back()
#Bot().forward()

        
