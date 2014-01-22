#!/usr/bin/python

import argparse
import socket
import logging

logging.basicConfig(level=logging.DEBUG)

TCP_IP = "" # any address
TCP_PORT = 3141

def get_state():
    pass

commands = {
        "GetState": get_state
    }

def serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(5)
    logging.debug("listening")

    while 1:
        conn, addr = s.accept()
        logging.debug("connection: %s" % str(addr))

        cmd = conn.recv(1024)
        if cmd == False:
            logging.error("Failed to read command")
            conn.close()
            continue

        logging.debug("rx: %s" % cmd)
        reply = "OK"
        conn.send(reply)
        logging.debug("tx: %s" % reply)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description='Server for controlling amplifiers')
    args = parser.parse_args()

    serve()
