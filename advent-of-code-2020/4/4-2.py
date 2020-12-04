#!/usr/bin/python3

import re

# 104 too low
# 115 too high

hcl_re = re.compile('^#(?P<hcl>[0-9a-f]{6}$)')
pid_re = re.compile('[0-9]{9}')

class Passport():
    def __init__(self):
        self.data = {}

    def add(self, field, value):
        self.data[field] = value

    def rejecting(self, field, value=None):
        if value == None:
            print("Missing {0}".format(field))
        else:
            print("Invalid {0}: {1}".format(field, value))


    def is_valid(self, ignore_content=False):
        print(self.data)

        req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for f in req_fields:
            if f not in self.data.keys():
                self.rejecting(f)
                return False 

        if ignore_content:
            print('OK')
            return True 

        byr = int(self.data['byr'])
        iyr = int(self.data['iyr'])
        eyr = int(self.data['eyr'])
        hgt = self.data['hgt']
        hgt_val = int(hgt[:-2])
        hgt_unit = hgt[-2:]
        hcl = self.data['hcl']        
        ecl = self.data['ecl']
        pid = self.data['pid']

        if not (byr >= 1920 and byr <= 2002):
            self.rejecting('byr', byr)
            return

        if not (iyr >= 2010 and iyr <= 2020):
            self.rejecting('iyr', iyr)
            return

        if not (eyr >= 2020 and eyr <= 2030):
            self.rejecting('eyr', eyr)
            return

        if hgt_unit == 'cm':
            if not (hgt_val >= 150 and hgt_val <= 193):
                self.rejecting('hgt', hgt)
                return
        elif hgt_unit == 'in':
            if not (hgt_val >= 59 and hgt_val <= 76):
                self.rejecting('hgt', hgt)
                return
        else:
            self.rejecting('hgt', hgt)
            return

        if None == hcl_re.match(hcl):
            self.rejecting('hcl', hcl)
            return

        if not ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            self.rejecting('ecl', ecl)
            return

        if None == pid_re.match(pid):
            self.rejecting('pid', pid)
            return

        print("OK")
        return True


with open('data.txt') as f:
    lines = f.read().splitlines()

# process

passports = []

passport = Passport()
passports.append(passport)

for line in lines:
    if line.strip() == '':
        passport = Passport()
        passports.append(passport)
        continue
    
    fields = line.split()
    for f in fields:
        passport.add(f[:3], f[4:])
        
valid_count_ignore_content = 0
for p in passports:
    if p.is_valid(ignore_content=True):
        valid_count_ignore_content += 1

valid_count = 0
for p in passports:
    if p.is_valid():
        valid_count += 1

print("Total: {0}".format(len(passports)))
print("ValidIC: {0}".format(valid_count_ignore_content))
print("Valid: {0}".format(valid_count))


