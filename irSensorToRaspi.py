import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
//insert Ir sensor Signal to gpio 17//
try:
    while True:
        if GPIO.input(17):
            print("Motion Detected!")
        else:
            print("No Motion")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
