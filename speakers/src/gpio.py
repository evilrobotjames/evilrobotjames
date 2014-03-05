#!/usr/bin/python

from RPi import GPIO
import time

GPIO.setmode(GPIO.BOARD)

PIN = 8

GPIO.setup(PIN, GPIO.OUT)

val = False
while True:
    GPIO.output(PIN, val)
    print val
    val = not val
    time.sleep(0.03)
