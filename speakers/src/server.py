#!/usr/bin/python
'''
Speaker control XMLRPC server
'''

import argparse
import common
import logging
from RPi import GPIO
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib

logging.basicConfig(level=logging.DEBUG, filename='/var/log/speakers')

# RPi.GPIO pin numbers, which equate to the pin on the 26pin header on the RPi
# itself.  Chosen to avoid any special-function pins.
PINS = [7, 11, 12, 13, 15, 16, 18, 22]

# A list of the current speaker states.  The position in the list defines the 
# speaker number.  Each speaker state is represented by a (GPIOPIN, STATE)
# tuple.
STATE = []

def initialize():
    '''
    Current state of all speakers, initialised to to off
    '''
    GPIO.setmode(GPIO.BOARD)
    for pin in PINS:
        logging.debug("using pin %d", pin)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)
        STATE.append((pin, False))
    logging.info("state initialized %s", str(STATE))

def get_state():
    '''
    Returns the current state of all speakers as a list of bools, each bool 
    representing a speaker.
    ''' 
    logging.info("get_state")
    logging.info("STATE %s", str(STATE))
    return [state[1] for state in STATE]

def set_state(speaker, state):
    '''
    Sets the state of an individual speaker.  speaker is 0-N, where N is the 
    number of speakers.  state is a boolean on/off.
    '''
    logging.info("set_state %s %s", speaker, state)
    if speaker < 1 or speaker > len(PINS):
        raise xmlrpclib.Fault(xmlrpclib.APPLICATION_ERROR, "Invalid speaker")
    index = speaker - 1
    GPIO.output(STATE[index][0], state)
    STATE[index] = (STATE[index][0], state)
    return True

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
             description='Server for controlling amplifiers')
    ARGS = PARSER.parse_args()

    try:
        initialize()
        SERVER = SimpleXMLRPCServer(("localhost", common.PORT))
        logging.info("listening")
        SERVER.register_function(get_state, "get_state")
        SERVER.register_function(set_state, "set_state")
        SERVER.serve_forever()
    finally:
        GPIO.cleanup()

