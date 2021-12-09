import RPi.GPIO as GPIO
import time

# tryb numeracji pinow
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)

while True:
    print(GPIO.input(11))
    time.sleep(0.5)

#komentarz
