"""Advent pi main script."""
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# pin for sensor
GPIO_PIN = 24

# configure pin as input pin
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# time between signal and reaction in seconds
delayTime = 0.5
print ("STRG+C to quit")

try:
    while True:
        if GPIO.input(GPIO_PIN) == True:
            print ("no movement")
        else:
            print ("movement")
            print ("---------------------------------------")
        # Reset + Delay
        time.sleep(delayTime)
except KeyboardInterrupt:
    # cleanup
    GPIO.cleanup() 

