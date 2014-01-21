#!/usr/bin/python

import socket

TCP_IP = "192.168.0.31"
TCP_PORT = 3141

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)

conn, addr = s.accept()
print "Connection address: ", addr
while 1:
    data = conn.recv(1024)
    if not data: break
    print "rx: ", data
    conn.send("OK")
conn.close()
