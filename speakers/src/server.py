#!/usr/bin/python

import argparse
import socket
import logging
from RPi import GPIO

logging.basicConfig(level=logging.DEBUG, filename='/var/log/speakers')

TCP_IP = "" # any address
TCP_PORT = 3141

STATE = []
PINS = [
    3,  # GPIO0
    5,  # GPIO1
    7,  # GPIO4
    8,  # GPIO14
    10, # GPIO15
    11, # GPIO17
    12, # GPIO18
    13, # GPIO21
  ]

for i in PINS:
    STATE.append((i, False))

def get_state():
    logging.info("get_state")
    return [p[1] for p in STATE]

def set_state(args):
    logging.info("set_state" + str(args))
    return "OK"

COMMANDS = {
        "GetState": get_state,
        "SetState": set_state,
    }

def serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(5)
    logging.debug("listening")

    while True:
        conn, addr = s.accept()
        logging.debug("connection: %s" % str(addr))

        cmd = conn.recv(1024)
        if cmd == False:
            logging.error("Failed to read command")
            conn.close()
            continue

        logging.debug("rx: %s" % cmd)

        list = cmd.split()
        if len(list) > 1:
            # has args
            reply = COMMANDS[list[0]](list[1:])
        else:
            # no args
            reply = COMMANDS[list[0]]()

        conn.send(reply)
        logging.debug("tx: %s" % reply)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description='Server for controlling amplifiers')
    args = parser.parse_args()

    serve()
