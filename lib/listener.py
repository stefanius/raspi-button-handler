#!/usr/bin/env python2.7

import RPi.GPIO as GPIO
import sys
from time import sleep

pin = int(sys.argv[1])
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
active = 0

# Define a threaded callback function to run in another thread when events are detected
def callback_function(channel):
    global active
    global pin

    if (GPIO.input(pin) and not active):    #pin is pressed
        print "Pin " + str(pin) + " is ON (rising event)"
        active = 1
    elif (not GPIO.input(pin) and active):
        print "Pin " + str(pin) + " is OFF (falling event)"
        active = 0
    else:
        print "bounce"

# when a changing edge is detected on port 25, regardless of whatever
# else is happening in the program, the function my_callback will be run
GPIO.add_event_detect(pin, GPIO.BOTH, callback=callback_function)

try:
    print "When pressed, you'll see: Rising Edge detected on " + str(pin)
    print "When released, you'll see: Falling Edge detected on " + str(pin)
    sleep(30)         # wait 30 seconds
    print "Time's up. Finished!"

finally:                   # this block will run no matter how the try block exits
    GPIO.cleanup()         # clean up after yourself
