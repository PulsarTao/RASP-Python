# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
from CVdecter import cvdecter as Rdec
class RDECIO:
    Rio1=0
    Rio2=0
    Rio3=0
    Rio4=0
    def __init__(self,io1,io2,io3,io4):
        self.Rio1=io1
        self.Rio2=io2
        self.Rio3=io3
        self.Rio4=io4
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(io1, GPIO.OUT)
        GPIO.setup(io2, GPIO.OUT)
        GPIO.setup(io3, GPIO.OUT)
        GPIO.setup(io4, GPIO.IN)
        GPIO.output(self.Rio1, GPIO.HIGH)
        GPIO.output(self.Rio2, GPIO.LOW)
        GPIO.output(self.Rio3, GPIO.HIGH)
    def Run(self):
        while 1:
            if (GPIO.input(self.Rio4) == 1):
                if Rdec.raspdec.dect()==1:
                    GPIO.output(self.Rio2, GPIO.HIGH)
                    GPIO.output(self.Rio3, GPIO.HIGH)
                    GPIO.output(self.Rio4, GPIO.HIGH)
                if Rdec.raspdec.dect()==0:
                    GPIO.output(self.Rio2, GPIO.HIGH)
                    GPIO.output(self.Rio3, GPIO.HIGH)
                    GPIO.output(self.Rio4, GPIO.LOW)
            GPIO.output(self.Rio2, GPIO.LOW)
        time.sleep(0.1)
GPIO.cleanup()