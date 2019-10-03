from picamera import PiCamera
from time import sleep
from datetime import date

def camera():
    today = date.today()
    camera = PiCamera()
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/'+str(today.strftime("%m_%d_%y"))+'.jpg')
    camera.stop_preview()

camera()