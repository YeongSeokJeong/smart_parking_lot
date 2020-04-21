import picamera
from time import sleep
from datetime import datetime, timedelta
 
camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
 
sleep(5)
for filename in camera.capture_continuous('/home/pi/bin/camera/{timestamp:%Y-%m-%d-%H%M%S}.jpg'):
    print('Captured %s' % filename)
    sleep(2)