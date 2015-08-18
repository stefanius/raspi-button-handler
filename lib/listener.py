#!/usr/bin/env python2.7

import RPi.GPIO as GPIO
from optparse import OptionParser
import sys
from time import sleep

parser = OptionParser()
parser.add_option("-p", "--pin", dest="pin", type="int",
                  help="pinnumber to setup the listener", metavar="PIN")
parser.add_option("-b", "--bounce", dest="bounce", default=False,
                  help="Log bouncing of the pin current")
parser.add_option("-s", "--scriptpath", dest="scriptpath", metavar="PATH",
                  help="Set the path with pinscripts")
(options, args) = parser.parse_args()

print options.pin

pin = int(sys.argv[1])
detect_bounce = 0

if 2 in sys.argv:
    detect_bounce = int(sys.argv[2])

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
active = 0


def callback_function(channel):
    global active
    global pin
    global detect_bounce

    if (GPIO.input(pin) and not active):    #pin is pressed
        print "Pin " + str(pin) + " is ON (rising event)"
        active = 1
    elif (not GPIO.input(pin) and active):
        print "Pin " + str(pin) + " is OFF (falling event)"
        active = 0
    else:
        if detect_bounce:
            print "bounce"

# when a changing edge is detected on port 25, regardless of whatever
# else is happening in the program, the function my_callback will be run
GPIO.add_event_detect(pin, GPIO.BOTH, callback=callback_function)

try:
    print "When pressed, you'll see: Rising Edge detected on " + str(pin)
    print "When released, you'll see: Falling Edge detected on " + str(pin)
    sleep(120)
    print "Listener is shutdown"

finally:                   # this block will run no matter how the try block exits
    GPIO.cleanup()         # clean up after yourself
