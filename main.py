"""Advent pi main script."""
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# pin for sensor
MOVEMENT_PIN = 24
RELAIS_PIN = 15

# configure pin as input pin
GPIO.setup(MOVEMENT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# configure pin as input pin to be sure relais will not react
GPIO.setup(RELAIS_PIN, GPIO.IN)
# time between signal and reaction in seconds
DELAY_TIME = 1
LIGHTS_ON_TIME = 15


def on_time_is_over(start_time):
    '''True if LIGHTS_ON_TIME is over.'''
    if start_time + LIGHTS_ON_TIME < time.time():
        return True
    return False


def relais_on():
    '''Turns the relais on.'''
    GPIO.setup(RELAIS_PIN, GPIO.OUT)


def relais_off():
    '''Turns the relais off.'''
    GPIO.setup(RELAIS_PIN, GPIO.IN)


def main():
    '''The code will be executed.'''
    start_time = 0
    while True:
        #if the sensor recognizes something
        if not GPIO.input(MOVEMENT_PIN):
            print ("lights on")
            print ("---------------------------------------")
            relais_on()
            start_time = time.time()
        #if the sensor does not recognize something and the on time is over
        elif on_time_is_over(start_time):
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
