#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys

FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0

def countPulse(channel):
    global count
    count += 1
    print(count)

GPIO.add_event_detect(FLOW_SENSOR, GPIO.BOTH, callback=countPulse)

try:
    while True:
        print(GPIO.input(23))
        print(count)
        time.sleep(1)

except KeyboardInterrupt:
    print('\ncaught keyboard interrupt!, bye')
    GPIO.cleanup()
    sys.exit()
