import RPi.GPIO as GPIO
from time import sleep
while True:
    GPIO.setmode(GPIO.BCM)
    pump_relay = 26
    seconds = float(input("Please input time:"))


    GPIO.setup(pump_relay, GPIO.OUT)
    GPIO.output(pump_relay, 1)

    try:
        GPIO.output(pump_relay, 1)
        sleep(seconds)
        GPIO.output(pump_relay, 0)
        sleep(1)
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()
GPIO.setwarnings(False)
