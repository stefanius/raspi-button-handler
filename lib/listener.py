#!/usr/bin/env python2.7

import RPi.GPIO as GPIO
import os.path
from optparse import OptionParser
from time import sleep

parser = OptionParser()
parser.add_option("-p", "--pin", dest="pin", type="int",
                  help="pinnumber to setup the listener", metavar="PIN")
parser.add_option("-b", "--bounce", dest="bounce", default=False,
                  help="Log bouncing of the pin current")
parser.add_option("-s", "--scriptpath", dest="scriptpath", metavar="PATH",
                  help="Set the path with pinscripts")
parser.add_option("-t", "--time", dest="time", metavar="TIME", default=120, type="int",
                  help="Set the time to sleep")
(options, args) = parser.parse_args()

GPIO.setmode(GPIO.BCM)
GPIO.setup(options.pin, GPIO.IN)
active = 0

pressed_file = 'p' + str(options.pin)
released_file = 'r' + str(options.pin)


def run(fname):
    os.path.isfile(fname)
    print fname
    return


def callback_function(channel):
    global active
    global options
    global pressed_file
    global released_file

    if (GPIO.input(options.pin) and not active):    #pin is pressed
        print "Pin " + str(options.pin) + " is ON (rising event)"
        active = 1
        run(options.path + pressed_file)
    elif (not GPIO.input(options.pin) and active):  #pin is released
        print "Pin " + str(options.pin) + " is OFF (falling event)"
        active = 0
        run(options.path + pressed_file)
    else:
        if options.bounce:
            print "bounce"

GPIO.add_event_detect(options.pin, GPIO.BOTH, callback=callback_function)

try:
    print "When pressed, you'll see: Rising Edge detected on " + str(options.pin)
    print "When released, you'll see: Falling Edge detected on " + str(options.pin)
    sleep(options.time)
    print "Listener is shutdown"

finally:                   # this block will run no matter how the try block exits
    GPIO.cleanup()         # clean up after yourself
