#!/usr/bin/python
'''
XMLRPC speaker control client script/library
'''

import argparse
import common
import logging
import xmlrpclib

logging.basicConfig(level=logging.DEBUG)


def validate_state(string):
    '''
    Converts on/1/True and off/0/False (case insensitive) into a boolean
    '''
    string = string.lower()
    if string in ['on', '1', 'True']:
        return True
    elif string in ['off', '0', 'False']:
        return False
    else:
        msg = "%r not a valid STATE.  Use on, off, 1 or 0." % string
        raise argparse.ArgumentTypeError(msg)


def initialize():
    '''
    Returns a XMLRPC server proxy
    '''
    url = "http://localhost:%s" % common.PORT
    logging.info("Connecting to %s", url)
    return xmlrpclib.ServerProxy(url)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
        description='Send speaker config to server.  Specify a speaker '
                    'and a state to change state.  No arguments '
                    'fetches the current state of all speakers.')
    PARSER.add_argument('speaker', metavar="SPEAKER", type=int,
                        help="speaker to enable/disable", nargs='?')
    PARSER.add_argument('state', metavar="STATE", type=validate_state,
                        help="either on (or 1) or off (or 0)", nargs='?')

    ARGS = PARSER.parse_args()

    if ARGS.state is None and ARGS.speaker is None:
        PROXY = initialize()
        print PROXY.get_state()
    elif ARGS.state is not None and ARGS.speaker is not None:
        PROXY = initialize()
        print PROXY.set_state(ARGS.speaker, ARGS.state)
    else:
        # args.speaker != args.state
        PARSER.error('SPEAKER and STATE must both be supplied, or neither.')
