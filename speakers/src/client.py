#!/usr/bin/python

import argparse
import logging
import socket

logging.basicConfig(level=logging.DEBUG)

MAX_SPEAKER = 7

TCP_IP = "127.0.0.1"
TCP_PORT = 3141

def get_state():
    reply = transact("GetState")
    return reply.split()

def set_state(speaker, state):
    reply = transact("SetState %s %s" % (speaker, state))
    return reply.split()

def transact(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    logging.debug("tx: %s" % cmd)
    s.send(cmd)
    reply = s.recv(1024)
    logging.debug("rx: %s" % reply)
    s.close()
    return reply


def validate_speaker(string):
    value = int(string)
    if value < 0 or value > MAX_SPEAKER:
      msg = "%r is not a valid speaker:(0-%d)" % (string, MAX_SPEAKER)
      raise argparse.ArgumentTypeError(msg)
    return value

def validate_state(string):
    string = string.lower()
    if string in ['on', '1']:
        return 'On'
    elif string in ['off', '0']:
        return 'Off'
    else:
        msg = "%r not a vaile STATE.  Use on, off, 1 or 0." % string
        raise argparse.ArgumentTypeError(msg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    		description='Send speaker config to server.  Specify a speaker '
                            'and a state to change state.  No arguments '
                            'fetches the current state of all speakers.')
    parser.add_argument('speaker', metavar="SPEAKER", type=validate_speaker,
                help="speaker to enable/disable", nargs='?')
    parser.add_argument('state', metavar="STATE", type=validate_state, 
		help="either on (or 1) or off (or 0)", nargs='?')

    args = parser.parse_args()

    if args.state == None and args.speaker == None:
        print get_state()
    elif args.state != None and args.speaker != None:
        print set_state(args.speaker, args.state)
    else:
        # args.speaker != args.state
        parser.error("SPEAKER and STATE must both be supplied, or neither.")
