"""GPIO handling."""
import time
import RPi.GPIO as GPIO 
from configparser import ConfigParser

# read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")
pins = config_object["PINS"]
time_config = config_object["TIME"]

GPIO.setmode(GPIO.BCM)
# pin for sensor
MOVEMENT_PIN = int(pins["movement_pin"])
RELAIS_PIN = int(pins["relais_pin"])

# disable warnings
GPIO.setwarnings(False)
# configure pin as input pin
GPIO.setup(MOVEMENT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# configure pin as input pin to be sure relais will not react
GPIO.setup(RELAIS_PIN, GPIO.IN)
# time between signal and reaction in seconds
DELAY_TIME = int(time_config["delay_time"])
LIGHTS_ON_TIME = int(time_config["lights_on_time"])
start_time = int(time_config["start_time"])

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
