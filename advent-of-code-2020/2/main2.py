#!/usr/bin/python

import re

f = open('data.txt')
password = re.compile('(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<letter>[a-z]): (?P<password>[a-z]+)')

def is_valid(pos1, pos2, letter, password):
    val1 = password[pos1 - 1] == letter
    val2 = password[pos2 - 1] == letter

    if val1 and val2 or not val1 and not val2:
        return False
    
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

