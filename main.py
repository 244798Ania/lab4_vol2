import RPi.GPIO as GPIO
import time
import os

# tryb numeracji pinow
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)

#echo none > $led0Folder/trigger

while True:
    if(GPIO.input(11)):
        #zapal diode
        #echo 1 >/sys/class/leds/led0/brightness
        #echo 0 >/sys/class/leds/led0/brightness

    time.sleep(0.5)


