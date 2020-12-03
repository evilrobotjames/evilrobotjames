#!/usr/bin/python

import re

f = open('data.txt')
password = re.compile('(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<letter>[a-z]): (?P<password>[a-z]+)')

def is_valid(min, max, letter, password):
    occurance = 0
    for c in password:
        if c == letter:
            occurance += 1
    if occurance > max or occurance < min:
        return False
    else:
        return True

valid_passwords = 0
for l in f.readlines():
    m = password.match(l)
    if is_valid(int(m.group('min')),
                int(m.group('max')),
                m.group('letter'),
                m.group('password')):
        print "V: " + str(m.groups())
        valid_passwords += 1
    else:
        print "I: " + str(m.groups())

print valid_passwords

