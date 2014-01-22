#!/usr/bin/python

import socket
import logging

logging.basicConfig(level=logging.DEBUG)

TCP_IP = "" # any address
TCP_PORT = 3141

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)
logging.debug("listening")

conn, addr = s.accept()
logging.debug("connection: %s" % str(addr))
while 1:
    cmd = conn.recv(1024)
    if not cmd: break
    logging.debug("rx: %s" % cmd)
    reply = "OK"
    conn.send(reply)
    logging.debug("tx: %s" % reply)
conn.close()
