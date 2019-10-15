import RPi.GPIO as GPIO
from time import sleep

def GrowLight(command):
    GPIO.setmode(GPIO.BCM)
    bulb_relay = 26
    GPIO.setup(bulb_relay, GPIO.OUT)
    GPIO.setwarnings(False)
    if command: GPIO.output(bulb_relay, 1)
    else: GPIO.output(bulb_relay, 0)
        
        
        

def LightBulb(command):
    if command:
        pass
    else:
        pass
    

GrowLight(True)