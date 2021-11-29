"""GPIO handling."""
import time
import RPi.GPIO as GPIO 
from configparser import ConfigParser

# read config.ini file
conf = ConfigParser()
conf.read("config.ini")

GPIO.setmode(GPIO.BCM)
# pin for sensor
MOVEMENT_PIN = int(conf["PINS"]["MOVEMENT_PIN"]) 
RELAIS_PIN = int(conf["PINS"]["RELAIS_PIN"]) 

# disable warnings
GPIO.setwarnings(False)
# configure pin as input pin
GPIO.setup(MOVEMENT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# configure pin as input pin to be sure relais will not react
GPIO.setup(RELAIS_PIN, GPIO.IN)
# time between signal and reaction in seconds
DELAY_TIME = int(conf["TIME"]["DELAY_TIME"])
LIGHTS_ON_TIME = int(conf["TIME"]["LIGHTS_ON_TIME"])
start_time = int(conf["TIME"]["START_TIME"])

def on_time_is_over():
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
