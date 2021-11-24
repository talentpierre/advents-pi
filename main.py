"""Advent pi main script."""
import time
import RPi.GPIO as GPIO

import advent_pi
from advent_pi import (
    DELAY_TIME,
    MOVEMENT_PIN,
    on_time_is_over,
    relais_off,
    relais_on,
    )

def main():
    '''The code will be executed.'''
    while True:
        #if the sensor recognizes something
        if not GPIO.input(MOVEMENT_PIN):
            print ("lights on")
            print ("---------------------------------------")
            relais_on()
            advent_pi.start_time = time.time()
        #if the sensor does not recognize something and the on time is over
        elif on_time_is_over():
            print("lights off")
            relais_off()
        #wait before starting the loop again
        time.sleep(DELAY_TIME)


if __name__ == "__main__":
    print("STRG+C to quit")
    try: 
        main()
    except KeyboardInterrupt:
        # cleanup
        GPIO.cleanup()
